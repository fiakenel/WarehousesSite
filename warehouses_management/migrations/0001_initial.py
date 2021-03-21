# Generated by Django 3.1.7 on 2021-03-21 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boxes',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('weight', models.BigIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount', models.BigIntegerField()),
            ],
            options={
                'db_table': 'boxes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'countries',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Racks',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('max_weight', models.BigIntegerField()),
            ],
            options={
                'db_table': 'racks',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'suppliers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Warehouses',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('area', models.BigIntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'warehouses',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WarehouseSupplierRelationships',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'warehouse_supplier_relationships',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Weapons',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'weapons',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.DecimalField(decimal_places=0, max_digits=10)),
                ('wage', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'workers',
                'managed': False,
            },
        ),
    ]
