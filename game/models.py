from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
import random

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    syscred = models.IntegerField(default=50)  # Custom currency
    health = models.IntegerField(default=100)
    max_health = models.IntegerField(default=100)
    turns_remaining = models.IntegerField(default=10)
    last_turn_reset = models.DateField(default=now)

    def __str__(self):
        return f"{self.user.username} (Level {self.level})"

    def reset_turns_if_new_day(self):
        if self.last_turn_reset < now().date():
            self.turns_remaining = 10
            self.last_turn_reset = now().date()
            self.save()

    def gain_experience(self, amount):
        self.experience += amount
        while self.experience >= self.xp_needed_for_next_level():
            self.level_up()
        self.save()

    def xp_needed_for_next_level(self):
        return self.level * 100  # Level 1: 100 XP, Level 2: 200 XP, etc.

    def level_up(self):
        self.level += 1
        self.max_health += 10
        self.health = self.max_health  # Fully heal on level up

class Enemy(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField()
    health = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    syscred_drop = models.IntegerField()
    xp_drop = models.IntegerField()

    def __str__(self):
        return f"{self.name} (Lv {self.level})"

class Post(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.player.user.username} at {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
