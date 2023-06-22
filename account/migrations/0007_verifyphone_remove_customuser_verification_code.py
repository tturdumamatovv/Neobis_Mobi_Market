# Generated by Django 4.2.2 on 2023-06-19 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_customuser_verification_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerifyPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='verification_code',
        ),
    ]