# Generated by Django 3.2 on 2021-05-01 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chess', '0005_board_stage'),
    ]

    operations = [
        migrations.AddField(
            model_name='user2figure',
            name='helth',
            field=models.IntegerField(default=100),
        ),
    ]