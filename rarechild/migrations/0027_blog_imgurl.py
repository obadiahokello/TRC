# Generated by Django 4.2.11 on 2024-04-08 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rarechild', '0026_alter_blog_options_alter_blogpictures_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='imgurl',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
