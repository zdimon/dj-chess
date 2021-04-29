from django.contrib import admin
from chess.models import SocialAuth, UserProfile, Figure
# Register your models here.

@admin.register(SocialAuth)
class SocialAuthAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'email', 'user', 'secret']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'publicname', 'sids', 'is_online']

@admin.register(Figure)
class FigureAdmin(admin.ModelAdmin):
    list_display = ['name', 'color','image_tag']