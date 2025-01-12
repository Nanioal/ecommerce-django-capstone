# Generated by Django 4.0.10 on 2025-01-12 01:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_product_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='wishlist',
            old_name='added_date',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
