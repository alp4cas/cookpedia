# Generated by Django 5.0.6 on 2024-05-23 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_recipe_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(blank=True, null=True)),
                ('password', models.TextField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('role', models.TextField(blank=True, null=True)),
            ],
        ),
    ]