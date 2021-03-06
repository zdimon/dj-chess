from django.contrib import admin
from chess.models import SocialAuth, UserProfile, Figure, Board, User2Figure, Cell
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

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['owner','agressor', 'uuid', 'stage', 'owner_position_done', 'agressor_position_done']

@admin.register(Cell)
class CelldAdmin(admin.ModelAdmin):
    list_display = ['board', 'figure', 'row', 'col']

@admin.register(User2Figure)
class User2FigureAdmin(admin.ModelAdmin):
    list_display = ['user', 'figure', 'on_board', 'cellid']

