# Generated by Django 3.0 on 2021-08-17 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20210817_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='prod',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Product'),
        ),
    ]
