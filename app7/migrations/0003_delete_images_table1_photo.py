# Generated by Django 4.1.2 on 2022-10-30 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app7', '0002_images'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Images',
        ),
        migrations.AddField(
            model_name='table1',
            name='Photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
