# Generated by Django 4.0.4 on 2022-05-24 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('blog', '0004_remove_blogpage_shortcut_image_blogpagegalleryimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='bg_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
