from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils.timezone import now
from .models import Player, Enemy, Post, Location
from .forms import CustomRegisterForm, EmailLoginForm
from .services.combat import hack_battle

def index(request):
    return HttpResponse("""
        <html>
        <head><title>ShadowNexus</title></head>
        <body style="font-family: monospace; background-color: black; color: lime; padding: 2rem;">
            <h1>Welcome to ShadowNexus</h1>
            <p>A web-based hacking RPG inspired by BBS culture and modern cybersecurity threats.</p>
            <p><a href="/accounts/login/" style="color: cyan;">Log in</a> to begin your journey.</p>
        </body>
        </html>
    """)

@login_required
def mainframe(request):
    player, created = Player.objects.get_or_create(user=request.user)

    if player.last_turn_reset < now().date():
        player.turns_remaining = 10
        player.last_turn_reset = now().date()
        player.save()

    if player.turns_remaining <= 0:
        return render(request, "game/mainframe.html", {
            "log": ["You’re out of turns for today. Come back tomorrow."],
            "player": player,
        })

    enemy = Enemy.objects.order_by('?').first()
    if not enemy:
        return render(request, "game/mainframe.html", {
            "log": ["No threats detected. Network is quiet..."],
            "player": player,
        })

    log = hack_battle(player, enemy)
    player.turns_remaining -= 1
    player.save()

    log.insert(0, f"> You have {player.turns_remaining} turns left today.")
    return render(request, "game/mainframe.html", {"log": log, "player": player, "enemy": enemy})

@login_required
def dialtone_den(request):
    player = Player.objects.get(user=request.user)

    if player.last_turn_reset < now().date():
        player.turns_remaining = 10
        player.last_turn_reset = now().date()
        player.save()

    message = ""
    if request.GET.get("action") == "heal":
        if player.syscred >= 10 and player.health < player.max_health:
            player.syscred -= 10
            player.health = player.max_health
            player.save()
            message = "You sip coffee and feel better. Full health restored."
        elif player.health >= player.max_health:
            message = "You're already fully healed."
        else:
            message = "Not enough credits to buy a coffee."

    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Post.objects.create(player=player, message=content)
            return redirect('dialtone_den')

    posts = Post.objects.all().order_by('-created_at')[:20]

    return render(request, "game/dialtone_den.html", {
        "player": player,
        "message": message,
        "posts": posts
    })

def register(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Player.objects.create(user=user)
            auth_login(request, user)
            return redirect('mainframe')
    else:
        form = CustomRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    form = EmailLoginForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        auth_login(request, user)
        return redirect('mainframe')

    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return render(request, 'registration/logout.html')

@login_required
def player_stats(request):
    player = Player.objects.get(user=request.user)
    return render(request, "game/stats.html", {"player": player})

@login_required
def explore(request):
    player = Player.objects.get(user=request.user)
    current_location = player.current_location

    if request.method == "POST":
        new_location_id = request.POST.get("move_to")
        if new_location_id:
            new_location = get_object_or_404(Location, id=new_location_id)
            if new_location in current_location.connections.all():
                player.current_location = new_location
                player.save()
                current_location = new_location

    connections = current_location.connections.all() if current_location else []

    return render(request, "game/explore.html", {
        "player": player,
        "current_location": current_location,
        "connections": connections
    })
