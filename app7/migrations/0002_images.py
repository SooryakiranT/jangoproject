# Generated by Django 4.1.2 on 2022-10-29 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app7', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Photo', models.ImageField(upload_to='')),
                ('Place', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]