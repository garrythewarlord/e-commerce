# Generated by Django 4.2.4 on 2023-10-03 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0002_remove_createorder_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='createorder',
            name='items',
            field=models.ManyToManyField(to='purchase.cartitem'),
        ),
    ]