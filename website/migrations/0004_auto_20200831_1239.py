# Generated by Django 2.2.12 on 2020-08-31 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20200830_2204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_icone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(choices=[('icon-1 paroller', 'paroller-1'), ('icon-2 paroller', 'paroller-2')], max_length=250)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Contact_icone',
                'verbose_name_plural': 'Contact_icones',
            },
        ),
        migrations.RemoveField(
            model_name='contact',
            name='lieu',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='nom',
        ),
        migrations.AlterField(
            model_name='contact',
            name='description',
            field=models.TextField(),
        ),
    ]
