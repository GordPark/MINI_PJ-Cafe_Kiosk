# Generated by Django 4.2.9 on 2024-04-07 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0006_alter_order_wait_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='menu_order',
        ),
        migrations.AddField(
            model_name='order',
            name='menu_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu_order_set', to='cafe.shopping_cart'),
        ),
    ]
