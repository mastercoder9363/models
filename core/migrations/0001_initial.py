# Generated by Django 4.1.3 on 2022-12-16 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rang', models.CharField(max_length=31)),
            ],
        ),
        migrations.CreateModel(
            name='Moshina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField()),
                ('narx', models.IntegerField(default=100)),
                ('rasm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.rang')),
            ],
        ),
    ]
