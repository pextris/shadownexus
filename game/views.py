from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.timezone import now
from .models import Player, Enemy, Post
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
    player = Player.objects.get(user=request.user)

    # Reset daily turns
    if player.last_turn_reset < now().date():
        player.turns_remaining = 10
        player.last_turn_reset = now().date()
        player.save()

    if player.turns_remaining <= 0:
        return render(request, "mainframe.html", {
            "log": ["You’re out of turns for today. Come back tomorrow."]
        })

    enemy = Enemy.objects.order_by('?').first()
    if not enemy:
        return render(request, "mainframe.html", {
            "log": ["No threats detected. Network is quiet..."]
        })

    log = hack_battle(player, enemy)
    player.turns_remaining -= 1
    player.save()

    log.insert(0, f"> You have {player.turns_remaining} turns left today.")
    return render(request, "mainframe.html", {"log": log})

@login_required
def dialtone_den(request):
    player = Player.objects.get(user=request.user)

    # Reset daily turns
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
            message = "Not enough gold to buy a coffee."

    # Handle message board post
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Post.objects.create(player=player, content=content)
            return redirect('dialtone_den')

    posts = Post.objects.all().order_by('-timestamp')[:20]

    return render(request, "dialtone_den.html", {
        "player": player,
        "message": message,
        "posts": posts
    })
