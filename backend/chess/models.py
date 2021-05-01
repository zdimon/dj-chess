from django.db import models
from django.contrib.auth.models import User
from .tasks import update_users_online
import uuid
from django.utils.html import mark_safe
from django.conf import settings

class UserProfile(User):
    publicname = models.CharField(default='', max_length=250)
    is_online = models.BooleanField(default=False)
    sids = models.TextField(default='')

    def get_sids(self):
        sids = []
        tmp = self.sids.split(';')
        for t in tmp:
            if len(t)>3:
                sids.append(t)
        return sids

    def add_sid(self,sid):
        sids = self.sids.split(';')
        if sid not in sids:
            sids.append(sid)
        self.sids = ';'.join(sids)
        self.save()
        self.check_online()

    @staticmethod
    def remove_sid(sid):
        user = UserProfile.objects.get(sids__contains=sid)
        sids = user.sids.split(';')
        if sid in sids:
            sids.remove(sid)
        user.sids = ';'.join(sids)
        user.save() 
        user.check_online() 

    def set_online(self,value):
        if self.is_online != value:
            self.is_online = value
            self.save()
            update_users_online.delay()

    def check_online(self):
        if(len(self.sids)>5):
            self.set_online(True)
        else:
            self.set_online(False)

class SocialAuth(models.Model):
    type = models.CharField(max_length=50)
    email =  models.CharField(max_length=50)
    secret =  models.CharField(max_length=250)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE) 

COLOR = (
    ("black", "Black"),
    ("white", "White")
)

STAGE = (
    ("setting", "setting"),
    ("play", "play")
)


class Figure(models.Model):
    name = models.CharField(max_length=90)
    image = models.ImageField(upload_to='figures')
    color = models.CharField(max_length=90, choices=COLOR,
                  default="white")

    def __str__(self):
        return f'{self.name}({self.color})'

    @property
    def get_image_absolute_url(self):
        return f'{settings.BASE_URL}{self.image.url}'

    @property
    def image_tag(self):
        try:
            return mark_safe(f'<img width="100" src="{self.image.url}" />')
        except:
            return 'No image'




class Board(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(UserProfile,on_delete=models.SET_NULL, null=True, blank=True, related_name='owner')
    agressor = models.ForeignKey(UserProfile,on_delete=models.SET_NULL, null=True, blank=True, related_name='agressor')
    stage = models.CharField(max_length=90, choices=STAGE,
                  default="setting")
    def __str__(self):
        return str(self.uuid)

class User2Figure(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    figure = models.ForeignKey(Figure,on_delete=models.CASCADE)
    board = models.ForeignKey(Board,on_delete=models.CASCADE)
    on_board = models.BooleanField(default=False)
    helth = models.IntegerField(default=100)
    cellid = models.IntegerField(default=0)

class Cell(models.Model):
    board = models.ForeignKey(Board,on_delete=models.CASCADE)
    figure = models.ForeignKey(User2Figure,on_delete=models.SET_NULL, null=True, blank=True)
    color = models.CharField(max_length=90, choices=COLOR,
                  default="white")
    row = models.IntegerField(default=0)
    col = models.IntegerField(default=0)
