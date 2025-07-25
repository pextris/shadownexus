# Generated by Django 5.2.1 on 2025-05-22 00:19

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_enemy_alter_customuser_options_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='default_username', error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enemy',
            name='critical_chance',
            field=models.FloatField(default=0.05),
        ),
        migrations.AddField(
            model_name='enemy',
            name='special_effect',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='enemy',
            name='dialogue',
            field=models.TextField(default='...incoming threat detected...'),
        ),
        migrations.AlterField(
            model_name='enemy',
            name='health',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='enemy',
            name='syscred_drop',
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='enemy',
            name='type',
            field=models.CharField(default='Malware', max_length=50),
        ),
        migrations.AlterField(
            model_name='enemy',
            name='xp_reward',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='player',
            name='achievements',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='faction',
            field=models.CharField(default='Independent', max_length=100),
        ),
        migrations.AlterField(
            model_name='player',
            name='handle',
            field=models.CharField(default='Anonymous', max_length=30),
        ),
        migrations.AlterField(
            model_name='player',
            name='syscred',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.player'),
        ),
    ]
