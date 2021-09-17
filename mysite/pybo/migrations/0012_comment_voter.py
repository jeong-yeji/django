# Generated by Django 3.1.3 on 2021-09-16 16:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pybo', '0011_auto_20210912_0214'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='voter',
            field=models.ManyToManyField(related_name='voter_comment', to=settings.AUTH_USER_MODEL),
        ),
    ]
