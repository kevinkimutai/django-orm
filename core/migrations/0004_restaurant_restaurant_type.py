# Generated by Django 5.1.6 on 2025-02-25 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='restaurant_type',
            field=models.CharField(choices=[('IN', 'INDIAN'), ('CH', 'CHINESE'), ('MX', 'MEXICAN'), ('JP', 'JAPANESE'), ('AR', 'ARABIC'), ('SM', 'SOMALI'), ('NA', 'OTHER')], default='NA', max_length=2),
        ),
    ]
