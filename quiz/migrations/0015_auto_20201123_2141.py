# Generated by Django 3.1.2 on 2020-11-23 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0014_chatbox_chatter_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='marks',
            field=models.FloatField(default=0),
        ),
    ]
