# Generated by Django 4.2.2 on 2023-06-19 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_remove_customuser_phone_number_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='verification_code',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
