# Generated by Django 2.1.3 on 2018-11-27 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flag',
            name='name',
            field=models.CharField(max_length=100),
            preserve_default=False,
        ),
    ]
