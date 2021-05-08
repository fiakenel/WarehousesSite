from django.db import models


class Box(models.Model):
    id = models.BigAutoField(primary_key=True)
    weight = models.BigIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.BigIntegerField()
    rack = models.ForeignKey('Rack', models.CASCADE)
    weapon = models.ForeignKey('Weapon', models.CASCADE)

#    def __str__(self):
#        return 

    class Meta:
        managed=False
        db_table = 'boxes'


class Country(models.Model):
    id = models.BigAutoField(primary_key=True)
    country = models.CharField(max_length=50)

    class Meta:
        managed=False
        db_table = 'countries'


class Rack(models.Model):
    id = models.BigAutoField(primary_key=True)
    max_weight = models.BigIntegerField()
    warehouse = models.ForeignKey('Warehouse', models.CASCADE)

    class Meta:
        managed=False
        db_table = 'racks'


class Supplier(models.Model):
    id = models.BigAutoField(primary_key=True)
    country = models.ForeignKey(Country, models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        managed=False
        db_table = 'suppliers'


class WarehouseSupplierRelationship(models.Model):
    id = models.BigAutoField(primary_key=True)
    warehouse = models.ForeignKey('Warehouse', models.CASCADE)
    supplier = models.ForeignKey(Supplier, models.CASCADE)

    class Meta:
        managed=False
        db_table = 'warehouse_supplier_relationships'


class Warehouse(models.Model):
    id = models.BigAutoField(primary_key=True)
    area = models.BigIntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id) + ' ' + str(self.address)

    class Meta:
        get_latest_by = 'id'
        managed=False
        db_table = 'warehouses'


class Weapon(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed=False
        db_table = 'weapons'


class Worker(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.DecimalField(max_digits=10, decimal_places=0)
    warehouse = models.ForeignKey(Warehouse, models.CASCADE)
    wage = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.id) + ' ' + str(self.name)

    class Meta:
        get_latest_by = 'id'
        managed=False
        db_table = 'workers'
