# Generated by Django 2.2.10 on 2020-05-04 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190630_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Water Purifier Class-A '), ('SW', 'WP-class B'), ('OW', 'WP-class C')], max_length=2),
        ),
    ]
