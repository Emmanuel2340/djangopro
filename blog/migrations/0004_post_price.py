# Generated by Django 4.1.7 on 2023-04-28 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]