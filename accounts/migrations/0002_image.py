# Generated by Django 4.1.5 on 2023-03-04 05:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('caption', models.CharField(max_length=255)),
                ('users', models.ManyToManyField(related_name='images', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]