# Generated by Django 3.2.7 on 2022-02-27 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_remove_order_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='order.order'),
        ),
    ]
