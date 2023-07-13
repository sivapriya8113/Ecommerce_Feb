# Generated by Django 4.2.3 on 2023-07-05 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Cloths',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('price', models.FloatField(blank=True, null=True)),
                ('image_url', models.URLField(max_length=2083)),
                ('cloths_available', models.BooleanField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cloths', to='api.category')),
            ],
        ),
    ]
