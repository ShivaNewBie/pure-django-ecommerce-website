# Generated by Django 3.0 on 2021-08-17 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_comment_prod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='prod',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='product.Product'),
        ),
    ]
