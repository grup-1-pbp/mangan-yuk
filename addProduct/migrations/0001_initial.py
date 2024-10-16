# Generated by Django 5.1.2 on 2024-10-15 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('restaurant', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('preference', models.CharField(choices=[('Veg', 'Vegetarian'), ('Non-Veg', 'Non-Vegetarian')], max_length=255)),
                ('image_url', models.URLField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
