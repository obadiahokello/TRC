# Generated by Django 4.2.4 on 2024-03-07 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rarechild', '0023_remove_cartorderitems_qty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(choices=[('process', 'Processing'), ('shipped', 'Shipped'), ('delivered', 'delivered')], default='active', max_length=50)),
                ('paid_status', models.BooleanField(default=False)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Cart Order',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rarechild.order')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rarechild.product')),
            ],
            options={
                'verbose_name_plural': 'Cart Order Items',
            },
        ),
        migrations.RemoveField(
            model_name='cartorderitems',
            name='order',
        ),
        migrations.RemoveField(
            model_name='cartorderitems',
            name='product',
        ),
        migrations.DeleteModel(
            name='CartOrder',
        ),
        migrations.DeleteModel(
            name='CartorderItems',
        ),
    ]
