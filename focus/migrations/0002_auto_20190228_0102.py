# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-28 01:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('focus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('put_date', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
                ('num_comments', models.IntegerField(default=0)),
                ('num_polls', models.IntegerField(default=0)),
                ('num_favotites', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=256)),
                ('register_date', models.DateTimeField()),
                ('profile', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('put_date', models.DateTimeField()),
                ('poll_num', models.IntegerField(default=0)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='focus.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='focus.Article')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='focus.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='focus.Article')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='focus.Comment')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='poll',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='focus.User'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='focus.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='polls',
            field=models.ManyToManyField(related_name='poll_user', through='focus.Poll', to='focus.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='focus.User'),
        ),
        migrations.AddField(
            model_name='author',
            name='favorites',
            field=models.ManyToManyField(through='focus.Favorite', to='focus.User'),
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='focus.Author'),
        ),
        migrations.AddField(
            model_name='article',
            name='favorites',
            field=models.ManyToManyField(related_name='favorite_users', through='focus.Favorite', to='focus.User'),
        ),
        migrations.AddField(
            model_name='article',
            name='polls',
            field=models.ManyToManyField(related_name='poll_users', through='focus.Poll', to='focus.User'),
        ),
    ]
