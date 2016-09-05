# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-04 19:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actas', '0007_auto_20160903_1929'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='encuentro',
            name='rut_encargado',
        ),
        migrations.AddField(
            model_name='encuentro',
            name='encargado',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='actas.Participante'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participa',
            name='encuentro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actas.Encuentro'),
        ),
        migrations.AddField(
            model_name='participa',
            name='ocupacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actas.Ocupacion'),
        ),
        migrations.AddField(
            model_name='participa',
            name='origen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actas.Origen'),
        ),
        migrations.AddField(
            model_name='participa',
            name='participante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actas.Participante'),
        ),
    ]