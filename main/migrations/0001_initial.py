# Generated by Django 4.0.2 on 2022-02-07 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('master_password', models.CharField(max_length=500)),
                ('key', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
    ]
