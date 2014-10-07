# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('url', models.URLField(max_length=50)),
                ('number', models.DecimalField(max_digits=5, decimal_places=4)),
                ('referenced_by', models.ManyToManyField(related_name=b'+', to='engine1.Website')),
                ('references', models.ManyToManyField(related_name=b'+', to='engine1.Website')),
                ('words', models.ManyToManyField(to='engine1.Keyword')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
