# Generated by Django 3.2.9 on 2021-12-06 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estimate', '0017_auto_20211206_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitylevels',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='ActivityPresets'),
        ),
    ]