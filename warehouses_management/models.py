from django.db import models

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Box(models.Model):
    id = models.BigAutoField(primary_key=True)
    weight = models.BigIntegerField(verbose_name='Вага')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')
    amount = models.BigIntegerField(verbose_name='Кількість')
    rack = models.ForeignKey('Rack', models.CASCADE, verbose_name='Полиця')
    weapon = models.ForeignKey('Weapon', models.CASCADE, verbose_name='Зброя')

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

    def __str__(self):
        return f'полиця {self.id}'

    class Meta:
        get_latest_by = 'id'
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

def validate_address_unique(address):
    if Warehouse.objects.filter(address=address).exists():
        raise ValidationError(_('Склад з такою адресою вже існує'))

class Warehouse(models.Model):
    id = models.BigAutoField(primary_key=True)
    area = models.BigIntegerField(verbose_name='Площа')
    address = models.CharField(max_length=100, verbose_name='Адреса', validators=[validate_address_unique])

    def __str__(self):
        return f'cклад {str(self.id)} за адресою {str(self.address)}'

    class Meta:
        get_latest_by = 'id'
        managed=False
        db_table = 'warehouses'


def validate_weapon_unique(weapon):
    if Weapon.objects.filter(name=weapon).exists():
        raise ValidationError(_('Зброя з такою назвою вже існує'))

class Weapon(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Назва', validators=[validate_weapon_unique])

    def __str__(self):
        return f'зброя {str(self.name)}'
    class Meta:
        managed=False
        db_table = 'weapons'


def validate_phone_unique(phone):
    if Worker.objects.filter(phone=phone).exists():
        raise ValidationError(_('Робітник з таким номером вже існує'))

class Worker(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Прізвище')
    phone = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Телефон', validators=[validate_phone_unique])
    warehouse = models.ForeignKey(Warehouse, models.CASCADE, verbose_name='Склад')
    wage = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='З/П')

    def __str__(self):
        return f'робітник {str(self.name)} під кодом {str(self.id)}'

    class Meta:
        get_latest_by = 'id'
        managed=False
        db_table = 'workers'
