# Generated by Django 4.0.6 on 2022-07-31 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0003_adversarialattack_attack_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='adversarialattack',
            name='image_class',
            field=models.CharField(default='candle', max_length=60),
        ),
    ]
