# Generated by Django 4.0.4 on 2022-07-04 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('sigla', models.CharField(blank=True, max_length=25, null=True, unique=True)),
                ('descricao', models.TextField()),
            ],
        ),
    ]
