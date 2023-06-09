# Generated by Django 4.2.1 on 2023-07-01 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transit', '0007_pushsubscription'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bus',
        ),
        migrations.AddField(
            model_name='pushsubscription',
            name='expiration_time',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='pushsubscription',
            name='endpoint',
            field=models.URLField(max_length=255, unique=True),
        ),
    ]
