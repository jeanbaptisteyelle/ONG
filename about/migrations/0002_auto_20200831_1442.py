# Generated by Django 2.2.12 on 2020-08-31 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domaine_don',
            name='icones',
            field=models.CharField(choices=[('flaticon-first-aid-kit', 'first-aid-kit'), ('flaticon-book', 'book'), ('flaticon-shelter', 'shelter')], max_length=50),
        ),
    ]
