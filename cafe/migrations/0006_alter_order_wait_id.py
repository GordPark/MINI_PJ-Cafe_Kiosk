# Generated by Django 4.2.9 on 2024-04-07 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0005_shopping_cart_price_shopping_cart_total_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='wait_id',
            field=models.IntegerField(null=True),
        ),
    ]
