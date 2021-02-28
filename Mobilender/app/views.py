"""
Definition of views.
"""
import traceback

from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from app.serializers import OrderSerializer, CustomerSerializer, OrderDetailSerializer, ArticleSerializer, CustomerSerializer
from app.models import *
from rest_framework import generics , viewsets, status
from rest_framework.response import Response
from django_filters import FilterSet, AllValuesFilter, DateTimeFilter, NumberFilter, BooleanFilter 
from rest_framework import routers, serializers, viewsets
from app.const import *

from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from app.serializers import MessageErrors
schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^$', schema_view)
]


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

class ArticleCreateViewSet(viewsets.ModelViewSet):
    model=Article
    queryset=Article.objects.all()
    serializer_class = ArticleSerializer

class CustomerCreateViewSet(viewsets.ModelViewSet):
    model=Customer
    queryset=Customer.objects.all()
    serializer_class = CustomerSerializer
class OrderCreateViewSet(viewsets.ModelViewSet):
    model = Order
    queryset = ''
    serializer_class = OrderSerializer
    def create(self, request):
        #save data before to save 
        order_serializer = OrderSerializer(data=request.data,many=False)
        try:
            order=Order()
            order.order_number    =request.data['order_number']
            order.customer_id     =request.data['customer']
            order.is_urgent       =request.data['is_urgent']        
            order.order_type      =request.data['order_type']
            order.cedis           =request.data['cedis']
            order.reference       =request.data['reference']
            order.brach_code      =request.data['brach_code']
            order.artner_code    =request.data['partner_code']
            order.is_supplied     =request.data['is_supplied']
        
            MessageErrors(order.order_type)
           
            order.save()
            order_details = request.data['order_details']
            for item in order_details:
            
                order_detail = OrderDetail()
                article=Article.objects.get(id=item['article'])
                order_detail.quantity = item['quantity']
                order_detail.order = order
                order_detail.article = article
                order_detail.save()
        except Exception as exception:
            print(type(exception), exception)
            raise serializers.ValidationError(str(exception))

        return order  
   


class OrderViewSet(viewsets.ModelViewSet):
    """!
    Vistas para registrar los Pedidos

    @author Alonso Lopez (luis.alonsoll89@gmail.com)
    @date 02-26-2020
    @version 1.0.0
    """
    
    model = Order
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def list(self, request):
        print("si estamos")
        queryset=Order.objects.select_related().filter(is_urgent=True,order_type=CEDIS,customer__customer_type=PLATINO,is_supplied=False)
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Order.objects.all()
        order = get_object_or_404(queryset, pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    def create(self, request):
        #save data before to save 
        order_serializer = OrderSerializer(data=request.data,many=False)
        try:
            order=Order()
            order.order_number    =request.data['order_number']
            order.customer_id     =request.data['customer']
            order.is_urgent       =request.data['is_urgent']        
            order.order_type      =request.data['order_type']
            order.cedis           =request.data['cedis']
            order.reference       =request.data['reference']
            order.brach_code      =request.data['brach_code']
            order.artner_code    =request.data['partner_code']
            order.is_supplied     =request.data['is_supplied']
        
            MessageErrors(order.order_type)
           
            order.save()
            order_details = request.data['order_details']
            for item in order_details:
            
                order_detail = OrderDetail()
                article=Article.objects.get(id=item['article'])
                order_detail.quantity = item['quantity']
                order_detail.order = order
                order_detail.article = article
                order_detail.save()
        except Exception as exception:
            print(type(exception), exception)
            raise serializers.ValidationError(str(exception))

        return order  
   

