from django.db import models

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_price(price):
    if price <= 0:
        raise ValidationError(_("Ціна не може бути від'ємна"))
def validate_amount(amount):
    if price <= 0:
        raise ValidationError(_("Кількість не може бути від'ємна"))

class Box(models.Model):
    id = models.BigAutoField(primary_key=True)
    price = models.DecimalField(max_digits=10,
                                validators=[validate_price],
                                decimal_places=2,
                                verbose_name='ціна')
    amount = models.BigIntegerField(verbose_name='кількість'
                                    ,validators=[validate_amount])
    warehouse = models.ForeignKey('Warehouse',
                                  models.CASCADE,
                                  verbose_name='склад')
    weapon = models.ForeignKey('Weapon',
                               models.CASCADE,
                               verbose_name='зброя')

    def __str__(self):
        return '{} {}'.format(self.id, self.weapon)

    class Meta:
        managed=False
        db_table = 'boxes'


def validate_country(country):
    if not name.isalpha():
        raise ValidationError(_("Каїна повинна складатись з літер"))

class Country(models.Model):
    id = models.BigAutoField(primary_key=True)
    country = models.CharField(max_length=50,
                               validators=[validate_country],
                               unique=True,
                               error_messages={
                                   'unique': 'Така країна вже існує'},
                               verbose_name='назва')

    def __str__(self):
        return self.country

    class Meta:
        managed=False
        db_table = 'countries'


#class Rack(models.Model):
#    id = models.BigAutoField(primary_key=True)
#    max_weight = models.BigIntegerField()
#    warehouse = models.ForeignKey('Warehouse', models.CASCADE)
#
#    def __str__(self):
#        return f'полиця {self.id}'
#
#    class Meta:
#        get_latest_by = 'id'
#        managed=False
#        db_table = 'racks'

class Warehouse(models.Model):
    id = models.BigAutoField(primary_key=True)
    area = models.BigIntegerField(verbose_name='площа')
    address = models.CharField(max_length=100,
                               verbose_name='адреса',
                               error_messages={
                                   'unique': 'Склад з такою адресою вже існує'},
                               unique=True)
    supplier = models.ManyToManyField('Supplier',
                                      through='WarehouseSupplierM2M')

    def __str__(self):
        return str(self.address)

    class Meta:
        get_latest_by = 'id'
        managed=False
        db_table = 'warehouses'


class Supplier(models.Model):
    id = models.BigAutoField(primary_key=True)
    country = models.ForeignKey(Country,
                                models.CASCADE,
                                verbose_name='країна')
    name = models.CharField(max_length=100,
                            unique=True,
                            error_messages={
                                'unique': 'Постачальник вже існує'},
                            verbose_name='назва')

    def __str__(self):
        return '{}. {}'.format(self.name, self.country)

    class Meta:
        managed=False
        db_table = 'suppliers'

class WarehouseSupplierM2M(models.Model):
    id = models.BigAutoField(primary_key=True)
    warehouse = models.ForeignKey('Warehouse', models.CASCADE)
    supplier = models.ForeignKey(Supplier, models.CASCADE)

    class Meta:
        managed=False
        db_table = 'warehouse_supplier_relationships'

class Weapon(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100,
                            verbose_name='Назва',
                            error_messages={
                                'unique': 'Така зброя вже є'},
                            unique=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        managed=False
        db_table = 'weapons'

def validate_name(name):
    if not name.isalpha():
        raise ValidationError(_("Ім'я повинно складатись з літер"))

class Worker(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100,
                            validators=[validate_name],
                            verbose_name='прізвище')
    phone = models.DecimalField(max_digits=10,
                                decimal_places=0,
                                verbose_name='телефон',
                                error_messages={
                                    'unique': 'робітник з таким номером вже існує'},
                                unique=True)
    warehouse = models.ForeignKey(Warehouse,
                                  models.CASCADE,
                                  verbose_name='cклад')
    wage = models.DecimalField(max_digits=10,
                               decimal_places=2,
                               verbose_name='З/П')

    def __str__(self):
        return '{} {}'.format(self.name, self.phone)

    class Meta:
        get_latest_by = 'id'
        managed=False
        db_table = 'workers'
