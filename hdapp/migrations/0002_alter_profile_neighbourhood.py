# Generated by Django 3.2.4 on 2021-06-08 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hdapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='neighbourhood',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hdapp.neighbourhood'),
        ),
    ]