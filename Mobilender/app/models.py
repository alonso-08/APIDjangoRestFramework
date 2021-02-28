"""
Definition of models.
"""

from django.db import models
from app.const import NORMAL, PLATA, ORO, PLATINO, CEDIS, SUCURSAL, EMPRESA


#Modelo de Cliente, customer_type se define con las CONSTANTES definidas en el archivo const.py 
class Customer(models.Model):
    def url(self,filename):
        ruta="MultimediaData/Customer/%s/%s"%(self.code,str(filename))
        return ruta
    #Los valores de este Choice estan en const.py, Se definen como constantes ya que son valores que no cambiaran
    CUSTOMER_TYPE_CHOICES = (
        (NORMAL,    'Normal'),
        (PLATA,     'Plata'),
        (ORO,       'Oro'),
        (PLATINO,   'Platino'),
        )

    name            = models.CharField(max_length=100)
    code            = models.CharField(max_length=10)
    picture         = models.FileField(upload_to=url,null=True,blank=True)
    addres          = models.CharField(max_length=100)
    customer_type   = models.CharField(max_length=10,choices=CUSTOMER_TYPE_CHOICES,default=NORMAL)


    def __str__(self):
        return '%s' %(self.code)

#Modelo Articulos
class Article(models.Model): 
    code            = models.IntegerField()
    description     = models.CharField(max_length=10)
    price           = models.DecimalField(decimal_places=2,max_digits=10,null=True,blank=True)
    
#Modelo Pedidos 
class Order(models.Model):
    order_number        =models.IntegerField(null=True,blank=True,unique=True)
    customer            =models.ForeignKey(Customer,on_delete=models.CASCADE,)
    create_date         =models.DateTimeField(auto_now_add=True)
    supplied_date       =models.DateTimeField(auto_now_add=True)
    is_urgent           =models.BooleanField()
    ORDER_TYPE_CHOICES = (
        (CEDIS,    'CEDIS'),
        (SUCURSAL,     'SUCURSAL'),
        (EMPRESA,       'EMPRESA'),
        
        )
    order_type          = models.CharField(max_length=10,choices=ORDER_TYPE_CHOICES,default=CEDIS)
    #Almacen donde se debe surtir
    cedis               =models.CharField(max_length=50)
    #El campo reference se reutiliza para cuando el type_order sea para una empresa o una sucursal.
    reference           =models.CharField(max_length=50)
    brach_code          =models.IntegerField(null=True,blank=True)
    partner_code        =models.IntegerField(null=True,blank=True)
    is_supplied         =models.BooleanField()
    order_details       =models.ManyToManyField(Article , through='OrderDetail')

    def __str__(self):
        return str(self.order_number)


    #def __str__(self):
     #   return '%s' %s(self.code)
#Detalle del Pedido con una o más entradas (Uno o más Articulos)
class OrderDetail(models.Model):    
    article     =models.ForeignKey(Article,on_delete=models.CASCADE, related_name='article_to_order')
    quantity    =models.IntegerField(null=True,blank=True)
    order       =models.ForeignKey(Order,on_delete=models.CASCADE, related_name='order_to_article' , blank=True , null=True)
    


#Modelo de Proveedores
class Supplier(models.Model):
    name            = models.CharField(max_length=100)
    addres          = models.CharField(max_length=100)
    #Articulos que surte un proveedor
    articles        =models.ManyToManyField(Article)

    def __str__(self):
        return '%s' %s(self.name)