# Generated by Django 2.1.4 on 2018-12-04 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comentarios',
        ),
        migrations.AddField(
            model_name='comentario',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Post'),
            preserve_default=False,
        ),
    ]
