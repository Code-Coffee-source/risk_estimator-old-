# Generated by Django 3.2.5 on 2021-11-18 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estimate', '0007_auto_20211116_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitylevels',
            name='Activity',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='estimate.activitypreset'),
        ),
    ]