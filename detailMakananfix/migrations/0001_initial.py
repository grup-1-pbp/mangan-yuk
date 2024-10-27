# Generated by Django 5.1.2 on 2024-10-23 07:04

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('restaurant', models.CharField(max_length=255)),
                ('deskripsi', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('preference', models.CharField(choices=[('Indo', 'Indonesia'), ('Chin', 'Chinese'), ('West', 'Western'), ('Jap', 'Japanese'), ('India,', 'Indian')], max_length=255)),
                ('image_url', models.URLField(blank=True, max_length=500, null=True)),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]