from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

FACTION_CHOICES = [
    ("white_hat", "White Hat"),
    ("black_hat", "Black Hat"),
    ("grey_hat", "Grey Hat"),
    ("nullsec", "NullSec"),
    ("init6", "Init6"),
    ("obfuscated", "The Obfuscated"),
    ("keepers", "The Keepers"),
]

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    handle = models.CharField(max_length=30, unique=True)
    faction = models.CharField(max_length=20, choices=FACTION_CHOICES, default="grey_hat")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class Location(models.Model):
    name = models.CharField(max_length=100)
    code = models.SlugField(unique=True)
    description = models.TextField()
    connections = models.ManyToManyField("self", symmetrical=False, blank=True)
    is_safe_zone = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Player(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    health = models.IntegerField(default=100)
    max_health = models.IntegerField(default=100)
    syscred = models.IntegerField(default=50)
    turns_remaining = models.IntegerField(default=10)
    last_turn_reset = models.DateField(default=timezone.now)
    level = models.IntegerField(default=1)
    xp = models.IntegerField(default=0)
    current_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.handle

class Enemy(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=1)
    health = models.IntegerField(default=100)
    damage = models.IntegerField(default=10)

    def __str__(self):
        return self.name

class Post(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player.user.handle}: {self.message[:30]}..."
