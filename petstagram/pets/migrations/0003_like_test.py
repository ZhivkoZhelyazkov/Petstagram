# Generated by Django 3.1.1 on 2020-10-11 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_auto_20201011_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='test',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]
