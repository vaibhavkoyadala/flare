# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-14 14:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='others')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('size', models.BigIntegerField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Flare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ImageMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('thumbnail', models.ImageField(editable=False, upload_to='thumbnails')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('size', models.BigIntegerField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Joker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('joined_on', models.DateTimeField(auto_now_add=True)),
                ('last_active', models.DateTimeField(auto_now_add=True)),
                ('flare', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flare.Flare')),
            ],
        ),
        migrations.CreateModel(
            name='TextMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=140)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('joker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flare.Joker')),
            ],
        ),
        migrations.AddField(
            model_name='imagemessage',
            name='joker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flare.Joker'),
        ),
        migrations.AddField(
            model_name='filemessage',
            name='joker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flare.Joker'),
        ),
    ]