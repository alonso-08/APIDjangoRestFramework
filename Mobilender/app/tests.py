"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
from django.test import TestCase
from rest_framework.test import APITestCase 

from django.utils.http import urlencode 
from django.urls import reverse 
from rest_framework import status 

from app.models import Order 
from app import views,serializers
from Mobilender.urls import router

from rest_framework.authtoken.models import Token 
from django.contrib.auth.models import User
from app.const import NORMAL, PLATA, ORO, PLATINO, CEDIS, SUCURSAL, EMPRESA

# TODO: Configure your database in settings.py and sync before running tests.


#La clase OrderCreateTests es una subclase de la superclase rest_framework.test.APITestCase 
# y declara el método post_order_create que recibe el nombre deseado para la nueva categoría de drones como argumento.

#Este método crea la URL y el diccionario de datos para redactar y enviar una solicitud HTTP POST a la vista asociada 
# con el nombre views.DroneCategoryList.name (dronecategory-list) y devuelve la respuesta generada por esta solicitud.

#El código usa el atributo self.client para acceder a la instancia APIClient que nos permite componer y enviar fácilmente 
# solicitudes HTTP para probar nuestro servicio web RESTful que usa el marco REST de Django. Para esta prueba, el código 
# llama al método de publicación con la URL construida, el diccionario de datos(data) y el formato deseado para los datos: 'json'.
class OrderCreateTests(APITestCase):     
    def post_order_create(self, order_number,customer,create_date,supplied_date,is_urgent,order_type,cedis,reference,brach_code,partner_code,is_supplied):         
        print(router.get_urls())
        url = reverse('order-list')         
        data = {
                'order_number':order_number,
                'customer':customer,
                'create_date':create_date,
                'supplied_date':supplied_date,
                'is_urgent':is_urgent,
                'order_type':order_type,
                'cedis':cedis,
                'reference':reference,
                'brach_code':brach_code,
                'partner_code':partner_code,
                'is_supplied':is_supplied,
               }         
        response = self.client.post(url, data, format='json')         
        return response

    def test_post_order_create(self):         
              
        new_order_number = 23
        new_customer = 1
        new_create_date =  '2021-12-12 12:30:00-06'
        new_supplied_date = '2021-12-12 10:30:00-06' 
        new_is_urgent = True 
        new_order_type = NORMAL
        new_cedis = 'GERM' 
        new_reference = '14XEG' 
        new_branch_code = '1235678' 
        new_partner_code = '235' 
        new_is_supplied = False 

        response = self.post_order_create(
            new_order_number,
            new_customer,
            new_create_date,
            new_supplied_date,
            new_is_urgent,
            new_order_type,
            new_cedis,
            new_reference,
            new_branch_code,
            new_partner_code,
            new_is_supplied)

              
    
   
