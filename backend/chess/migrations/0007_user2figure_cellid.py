# Generated by Django 3.2 on 2021-05-01 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chess', '0006_user2figure_helth'),
    ]

    operations = [
        migrations.AddField(
            model_name='user2figure',
            name='cellid',
            field=models.IntegerField(default=0),
        ),
    ]
