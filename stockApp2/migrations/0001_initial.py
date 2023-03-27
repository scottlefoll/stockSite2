# Generated by Django 4.1.7 on 2023-03-26 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_symbol', models.CharField(max_length=10, null=True, unique=True)),
                ('symbol', models.CharField(max_length=10)),
                ('name', models.CharField(default='', max_length=50)),
                ('date', models.DateField(default=None, null=True)),
                ('close', models.DecimalField(decimal_places=2, default=None, max_digits=6, null=True)),
                ('volume', models.IntegerField(default=0)),
                ('exchange', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='UserStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockApp2.stock')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StockPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField(default=0)),
                ('user_stock_date', models.CharField(max_length=10, null=True, unique=True)),
                ('date', models.DateField(default=None, null=True)),
                ('open', models.DecimalField(decimal_places=2, default=None, max_digits=6, null=True)),
                ('high', models.DecimalField(decimal_places=2, default=None, max_digits=6, null=True)),
                ('low', models.DecimalField(decimal_places=2, default=None, max_digits=6, null=True)),
                ('close', models.DecimalField(decimal_places=2, default=None, max_digits=6, null=True)),
                ('volume', models.IntegerField(default=0, null=True)),
                ('adj_high', models.DecimalField(decimal_places=2, default=None, max_digits=6, null=True)),
                ('adj_low', models.DecimalField(decimal_places=2, default=None, max_digits=6, null=True)),
                ('adj_close', models.DecimalField(decimal_places=2, default=None, max_digits=6, null=True)),
                ('adj_open', models.DecimalField(decimal_places=2, default=None, max_digits=6, null=True)),
                ('adj_volume', models.IntegerField(default=0, null=True)),
                ('split_factor', models.DecimalField(decimal_places=2, default=None, max_digits=4, null=True)),
                ('dividend', models.DecimalField(decimal_places=2, default=None, max_digits=5, null=True)),
                ('symbol', models.CharField(max_length=10)),
                ('exchange', models.CharField(max_length=6)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockApp2.stock')),
            ],
        ),
    ]