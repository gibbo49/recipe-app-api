# Generated by Django 3.2.23 on 2023-12-17 02:34

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20231216_0624'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(null=True, upload_to=core.models.recipe_image_file_path),
        ),
    ]
