# Generated by Django 3.2.5 on 2021-11-16 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estimate', '0002_remove_activitypreset_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitypreset',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ActivityPresets'),
        ),
    ]