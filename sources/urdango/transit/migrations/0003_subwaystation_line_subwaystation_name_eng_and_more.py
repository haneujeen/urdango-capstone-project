# Generated by Django 4.2.1 on 2023-05-23 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transit', '0002_rename_location_subwaystation_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='subwaystation',
            name='line',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='stations', to='transit.subwayline'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subwaystation',
            name='name_eng',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='subwaystation',
            name='code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='subwaystation',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
