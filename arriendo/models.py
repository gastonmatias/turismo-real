# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Commune(models.Model):
    id = models.BigIntegerField(primary_key=True) # SIN BigAutoField !
    id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='id_region')
    commune = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commune'


class Company(models.Model):
    id = models.BigIntegerField(primary_key=True) # SIN BigAutoField !
    commune = models.ForeignKey(Commune, models.DO_NOTHING)
    rut = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    mail_address = models.CharField(max_length=100)
    legal_representative = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'company'


class Customer(models.Model):
    id = models.BigAutoField(primary_key=True) 
    rut = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mail_address = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'customer'


class CustomerAccount(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(Customer, models.DO_NOTHING)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    regular_customer = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_account'


class Department(models.Model):
    id = models.BigAutoField(primary_key=True)
    commune = models.ForeignKey(Commune, models.DO_NOTHING)
    department_maintenance = models.ForeignKey('DepartmentMaintenance', models.DO_NOTHING)
    department_type = models.ForeignKey('DepartmentType', models.DO_NOTHING)
    internet = models.BooleanField(blank=True, null=True)
    tv_cable = models.BooleanField(blank=True, null=True)
    heating = models.BooleanField(blank=True, null=True)
    address = models.CharField(max_length=100)
    status = models.CharField(max_length=1)
    qty_rooms = models.BigIntegerField()
    price = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'department'


class DepartmentInventory(models.Model):
    id = models.BigAutoField(primary_key=True)
    department = models.ForeignKey(Department, models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    date_time = models.DateTimeField(blank=True, null=True)
    qty = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'department_inventory'


class DepartmentMaintenance(models.Model):
    id = models.BigAutoField(primary_key=True)
    maintenance_date = models.DateField(blank=True, null=True)
    last_maintenance = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department_maintenance'


class DepartmentType(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'department_type'


class Employee(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee_type = models.ForeignKey('EmployeeType', models.DO_NOTHING)
    rut = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mail_address = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'employee'


class EmployeeAccount(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(Employee, models.DO_NOTHING)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'employee_account'


class EmployeeType(models.Model):
    id = models.BigAutoField(primary_key=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    work_area = models.ForeignKey('WorkArea', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'employee_type'


class Finance(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(Employee, models.DO_NOTHING)
    income = models.BigIntegerField()
    egress = models.BigIntegerField()
    total = models.BigIntegerField()
    date_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'finance'


class Payment(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    guarantee_payment = models.BigIntegerField()
    amount = models.BigIntegerField()
    total_payment = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'payment'


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_type = models.ForeignKey('ProductType', models.DO_NOTHING, db_column='product_type')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'product'


class ProductType(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'product_type'


class Region(models.Model):
    id = models.BigIntegerField(primary_key=True) # SIN BigAutoField !
    region = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'region'


class Rent(models.Model):
    id = models.BigAutoField(primary_key=True)
    tariff = models.BigIntegerField(blank=True, null=True)
    rental_date = models.DateField(blank=True, null=True)
    payment = models.ForeignKey(Payment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rent'


class Reservation(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='id_customer')
    id_services = models.ForeignKey('Service', models.DO_NOTHING, db_column='id_services')
    id_payment = models.ForeignKey(Payment, models.DO_NOTHING, db_column='id_payment')
    id_employee = models.ForeignKey(Employee, models.DO_NOTHING, db_column='id_employee')
    id_vehicle = models.ForeignKey('Vehicle', models.DO_NOTHING, db_column='id_vehicle')
    id_tour = models.ForeignKey('Tour', models.DO_NOTHING, db_column='id_tour')
    id_department = models.ForeignKey(Department, models.DO_NOTHING, db_column='id_department')
    id_reservation_status = models.ForeignKey('ReservationStatus', models.DO_NOTHING, db_column='id_reservation_status')
    qty_customer = models.BigIntegerField()
    tour = models.BooleanField(blank=True, null=True)
    reservation_date = models.DateField(blank=True, null=True)
    check_in = models.DateField(blank=True, null=True)
    check_out = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reservation'


class ReservationStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reservation_status'


class Service(models.Model):
    id = models.BigAutoField(primary_key=True)
    service_type = models.ForeignKey('ServiceType', models.DO_NOTHING, db_column='service_type')
    hire_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service'


class ServiceType(models.Model):
    id = models.BigAutoField(primary_key=True)
    available = models.BooleanField(blank=True, null=True)
    description = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'service_type'


class Tour(models.Model):
    id = models.BigAutoField(primary_key=True)
    destination = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    hire_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tour'


class Vehicle(models.Model):
    id = models.BigAutoField(primary_key=True)
    color = models.CharField(max_length=100)
    id_vehicle = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'vehicle'


class WorkArea(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'work_area'
