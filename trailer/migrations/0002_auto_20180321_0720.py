# Generated by Django 2.0.3 on 2018-03-21 07:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trailer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trailer',
            name='highlighted',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trailer',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='trailer', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]