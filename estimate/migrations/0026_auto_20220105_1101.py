# Generated by Django 3.2.9 on 2022-01-05 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estimate', '0025_auto_20220103_0542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitylevels',
            name='Image',
            field=models.FileField(blank=True, null=True, upload_to='ActivityLevls'),
        ),
        migrations.AlterField(
            model_name='result_formula',
            name='Name',
            field=models.CharField(default='', max_length=300),
        ),
    ]
