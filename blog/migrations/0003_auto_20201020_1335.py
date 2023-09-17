# Generated by Django 2.2.6 on 2020-10-20 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_product_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=200)),
                ('product', models.CharField(blank=True, max_length=200)),
                ('price', models.CharField(blank=True, max_length=200)),
                ('user', models.CharField(max_length=100)),
                ('address', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Product_Order',
        ),
    ]