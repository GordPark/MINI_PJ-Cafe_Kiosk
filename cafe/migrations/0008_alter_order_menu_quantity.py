# Generated by Django 4.2.9 on 2024-04-07 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0007_remove_order_menu_order_order_menu_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='menu_quantity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu_quantity_set', to='cafe.shopping_cart'),
        ),
    ]
