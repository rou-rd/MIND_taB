# Generated by Django 2.2.2 on 2020-06-04 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200604_0838'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_product', models.CharField(max_length=200)),
                ('product', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='product',
        ),
    ]
