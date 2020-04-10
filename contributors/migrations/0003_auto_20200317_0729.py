# Generated by Django 2.2.11 on 2020-03-17 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contributors', '0002_issueinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issueinfo',
            name='issue',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='info', to='contributors.Contribution', verbose_name='issue'),
        ),
    ]