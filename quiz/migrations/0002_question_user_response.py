# Generated by Django 3.1.2 on 2020-10-25 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='user_response',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]