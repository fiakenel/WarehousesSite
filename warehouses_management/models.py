from django.db import models


class Boxes(models.Model):
    id = models.BigAutoField(primary_key=True)
    weight = models.BigIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.BigIntegerField()
    rack = models.ForeignKey('Racks', models.CASCADE)
    weapon = models.ForeignKey('Weapons', models.CASCADE)

    class Meta:
        managed=False;
        db_table = 'boxes'


class Countries(models.Model):
    id = models.BigAutoField(primary_key=True)
    country = models.CharField(max_length=50)

    class Meta:
        managed=False;
        db_table = 'countries'


class Racks(models.Model):
    id = models.BigAutoField(primary_key=True)
    max_weight = models.BigIntegerField()
    warehouse = models.ForeignKey('Warehouses', models.CASCADE)

    class Meta:
        managed=False;
        db_table = 'racks'


class Suppliers(models.Model):
    id = models.BigAutoField(primary_key=True)
    country = models.ForeignKey(Countries, models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        managed=False;
        db_table = 'suppliers'


class WarehouseSupplierRelationships(models.Model):
    id = models.BigAutoField(primary_key=True)
    warehouse = models.ForeignKey('Warehouses', models.CASCADE)
    supplier = models.ForeignKey(Suppliers, models.CASCADE)

    class Meta:
        managed=False;
        db_table = 'warehouse_supplier_relationships'


class Warehouses(models.Model):
    id = models.BigAutoField(primary_key=True)
    area = models.BigIntegerField()
    address = models.CharField(max_length=100)

    class Meta:
        managed=False;
        db_table = 'warehouses'


class Weapons(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed=False;
        db_table = 'weapons'


class Workers(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.DecimalField(max_digits=10, decimal_places=0)
    warehouse = models.ForeignKey(Warehouses, models.CASCADE)
    wage = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed=False;
        db_table = 'workers'
