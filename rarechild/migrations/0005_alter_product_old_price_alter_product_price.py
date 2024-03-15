# Generated by Django 4.2.4 on 2024-02-29 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rarechild', '0004_remove_product_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.DecimalField(decimal_places=2, default='2.99', max_digits=99),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default='1.99', max_digits=99),
        ),
    ]
