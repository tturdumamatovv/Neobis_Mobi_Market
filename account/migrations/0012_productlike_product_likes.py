# Generated by Django 4.2.2 on 2023-06-22 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_likes', to='account.product')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('product', 'username')},
            },
        ),
        migrations.AddField(
            model_name='product',
            name='likes',
            field=models.ManyToManyField(related_name='liked_product', through='account.ProductLike', to=settings.AUTH_USER_MODEL),
        ),
    ]
