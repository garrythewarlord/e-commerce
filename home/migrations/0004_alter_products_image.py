# Generated by Django 4.2.4 on 2023-09-21 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='files/media'),
        ),
    ]