from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from app.models import Order, Customer, OrderDetail , Article
from app.const import *

#Clase para Serializar el modelo Cliente
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','name', 'code', 'picture','addres','customer_type']


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields=['id','code','description','price']

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields=['id','quantity','article','order']

#Clase para Serializar el modelo Pedido
class OrderSerializer(serializers.ModelSerializer):
    name='create-order'
    order_details = OrderDetailSerializer(source='order_to_article',many=True)
    customer = CustomerSerializer(many=False)
    class Meta:
        model = Order
        fields = ['id','order_number',
                 'customer','create_date',
                 'supplied_date','is_urgent',
                 'order_type','cedis',
                 'reference','brach_code',
                 'partner_code','is_supplied','order_details']

    

    def create(self, validated_data):
        #save data before to save 
        
        order_details = validated_data['order_to_article']
        validated_data.pop('order_to_article')
        order = Order(**validated_data)
           
        order.save()
          
        for item in order_details:
            order_detail = OrderDetail()
            order_detail.quantity = item['quantity']
            order_detail.order = order
            order_detail.article = item['article']
            order_detail.save()

        return order   





def MessageErrors(order_type):
        if order_type not in (CEDIS, SUCURSAL, EMPRESA):
            raise serializers.ValidationError("El campo order_type no es valido")