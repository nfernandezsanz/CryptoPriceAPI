# Generated by Django 3.2.11 on 2022-05-28 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0003_rename_felling_sentiment'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentiment',
            name='price',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='crypto.pricerecord'),
        ),
    ]
