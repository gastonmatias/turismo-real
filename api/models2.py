from django.db import models
from django.conf import settings

# Create your models here.
class Region(models.Model):
    id = models.BigAutoField(primary_key=True) 
    region = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.region

class Commune(models.Model):
    id = models.BigAutoField(primary_key=True) 
    id_region = models.ForeignKey('Region', models.DO_NOTHING) #, db_column='id_region')
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class DepartmentType(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class Department(models.Model):

    id = models.BigAutoField(primary_key=True)
    commune = models.ForeignKey(Commune, models.DO_NOTHING)
    department_type = models.ForeignKey('DepartmentType', models.DO_NOTHING)
    internet = models.BooleanField(blank=True, null=True)
    tv_cable = models.BooleanField(blank=True, null=True)
    heating = models.BooleanField(blank=True, null=True)
    address = models.CharField(max_length=100)
    on_maintenance = models.BooleanField(blank=True, null=True)
    qty_rooms = models.IntegerField()
    price = models.BigIntegerField()

    def __str__(self):
        return self.commune.name

class Services(models.Model):

    SERVICES_CATEGORIES = (
        #1er parametro = key value
        #2do parametro = value neto
        ('NA','Sin servicio extra'),
        ('TOUR','Tour'),
        ('TRANSPORTE','Transporte'),
        ('PACK','Tour + Transporte'),
    )
    id = models.BigAutoField(primary_key=True)
    price = models.BigIntegerField()
    description = models.CharField(max_length=100,choices=SERVICES_CATEGORIES,default='Sin servicio extra') # nada/tour/transporte/tour + transporte

    def __str__(self):
        return self.description


class Reservation(models.Model):
    
    STATUS_CATEGORIES = (
        ('R','Reservado'),
        ('P','Pagado'),
        ('C','Cancelado')
    )
    
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING)
    id_services = models.ForeignKey(Services, models.DO_NOTHING)
    id_department = models.ForeignKey(Department, models.DO_NOTHING)
    status = models.CharField(max_length=50,choices=STATUS_CATEGORIES,default='Reservado')
    total_amount = models.IntegerField() # sumatoria de costo depto + servicios extra
    reservation_amount = models.IntegerField() # $ a pagar al reservar (10% del total amount)
    difference_amount = models.IntegerField() # monto a pagar al momento de check in (90% del total amount)
    qty_customers = models.IntegerField(blank=True)
    reservation_date = models.DateTimeField()
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'Cliente: {self.user}, depto:{self.id_department}, desde {self.check_in} hasta {self.check_out}'
        #return f'{self.user} ha reservado depto en {self.depto}, desde {self.check_in} hasta {self.check_out}'


