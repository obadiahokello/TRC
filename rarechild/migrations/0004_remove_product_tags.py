# Generated by Django 4.2.4 on 2024-02-29 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rarechild', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
    ]