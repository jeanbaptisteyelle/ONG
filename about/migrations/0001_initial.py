# Generated by Django 2.2.12 on 2020-08-29 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=150)),
                ('publicite', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='image/about')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'Abouts',
            },
        ),
        migrations.CreateModel(
            name='Icones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(choices=[('flaticon-donation-2', 'donation'), ('flaticon-world-1', 'world'), ('flaticon-blood-2', 'blood')], max_length=50)),
                ('titre', models.CharField(max_length=150)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Icones',
                'verbose_name_plural': 'Icones',
            },
        ),
        migrations.CreateModel(
            name='Objectif',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Objectif',
                'verbose_name_plural': 'Objectifs',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('icones', models.CharField(choices=[('flaticon-care', 'Care'), ('flaticon-pigeon', 'pigeon'), ('flaticon-harvest', 'harvest')], max_length=50)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Domaine_don',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('icones', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='icones_domaine_don', to='about.Icones')),
            ],
            options={
                'verbose_name': 'Domaine_don',
                'verbose_name_plural': 'Domaine_dons',
            },
        ),
    ]
