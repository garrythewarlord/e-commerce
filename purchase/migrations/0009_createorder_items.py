# Generated by Django 4.2.4 on 2023-10-04 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0008_cart_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='createorder',
            name='items',
            field=models.ManyToManyField(to='purchase.cartitem'),
        ),
    ]
