# Generated by Django 2.1 on 2018-08-23 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CLASS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]