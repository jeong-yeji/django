# Generated by Django 3.1.3 on 2021-09-11 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0007_answer_view_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='view_count',
        ),
        migrations.AddField(
            model_name='question',
            name='view_count',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
