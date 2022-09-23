""" from django.db import models

class Region(models.Model):
    id = models.BigAutoField(primary_key=True) 
    region = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'Región: {self.region}'

class Commune(models.Model):
    id = models.BigAutoField(primary_key=True) 
    id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='id_region')
    commune = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'Comuna: {self.commune}'

class DepartmentType(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f'Tipo Depto: {self.description}'

class Department(models.Model):
    id = models.BigAutoField(primary_key=True)
    commune = models.ForeignKey(Commune, models.DO_NOTHING)
    department_type = models.ForeignKey('DepartmentType', models.DO_NOTHING)
    internet = models.BooleanField(blank=True, null=True)
    tv_cable = models.BooleanField(blank=True, null=True)
    heating = models.BooleanField(blank=True, null=True)
    address = models.CharField(max_length=100)
    status = models.CharField(max_length=1)
    qty_rooms = models.BigIntegerField()
    price = models.BigIntegerField()

    def __str__(self):
        return f'Depto: {self.commune}, Precio: {self.price}' """

""" class User(AbstractBaseUser):
    id = models.BigAutoField('Id usuario',primary_key=True)
    email = models.CharField('Email',max_length=100,null=False, blank=False,unique=True)
    rut = models.CharField('Rut',max_length=100,null=False, blank=False)
    name = models.CharField('Nombre',max_length=100,null=False, blank=False)
    last_name = models.CharField('Apellido',max_length=100,null=False, blank=False)
    password = models.CharField(max_length=100,null=False, blank=False)
    regular_customer = models.BooleanField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email','name','last_name','rut']

    def __str__(self):
        return f'{self.name}, {self.last_name}'
    
    # para determinar si puede acceder o no al admin de django
    def has_perm(self,perm,obj = None):
        return True
    
    def has_module_perms(self,app_label):
        return True

 """


  