# game/admin.py

from django.contrib import admin
from .models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('user', 'level', 'experience', 'syscred', 'health', 'turns_remaining')
