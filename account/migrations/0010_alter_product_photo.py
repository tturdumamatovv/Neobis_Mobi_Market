# Generated by Django 4.2.2 on 2023-06-21 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
    ]
