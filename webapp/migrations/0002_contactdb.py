# Generated by Django 4.1.7 on 2023-05-23 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=30, null=True)),
                ('Number', models.IntegerField(blank=True, null=True)),
                ('Email', models.IntegerField(blank=True, max_length=40, null=True)),
                ('Subject', models.CharField(blank=True, max_length=40, null=True)),
                ('Message', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
    ]
