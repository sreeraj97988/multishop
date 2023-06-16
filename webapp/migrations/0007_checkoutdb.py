# Generated by Django 4.1.7 on 2023-06-14 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_alter_cartdb_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkoutdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fist_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Last_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Email', models.EmailField(blank=True, max_length=50, null=True)),
                ('Mobile', models.IntegerField(blank=True, null=True)),
                ('AdressoOne', models.CharField(blank=True, max_length=50, null=True)),
                ('AddressTwo', models.CharField(blank=True, max_length=50, null=True)),
                ('Country', models.CharField(blank=True, max_length=50, null=True)),
                ('City', models.CharField(blank=True, max_length=50, null=True)),
                ('State', models.CharField(blank=True, max_length=50, null=True)),
                ('Zipcode', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
