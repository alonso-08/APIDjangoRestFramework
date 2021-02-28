"""
Definition of urls for Mobilender.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from app.views import  *
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Pastebin API')
router = routers.DefaultRouter()

router.register(r'^order/(P<pk>\d+)/$', OrderViewSet) #order detail
router.register(r'order', OrderViewSet,basename='order') #order list 
router.register(r'order-create', OrderCreateViewSet,basename='order-create') #order list 
router.register(r'article', ArticleCreateViewSet,basename='article') #order list 
router.register(r'customer', CustomerCreateViewSet,basename='customer') #order list 


urlpatterns = [
    #path(r'^swagger$', schema_view),
    path('', schema_view, name='swagger'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('order',OrderViewSet,name='order'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    #path('v1/customer', CustomerList.as_view()), 
    
    #path('v1/order', OrderList.as_view(),name=views.OrderList.name), 
    #path('v1/order-detail', OrderDetailList.as_view(),name=views.OrderDetailList.name), 
    path('api/', include(router.urls)),
    #path('v1/order', OrderList.as_view()), 
    path('admin/', admin.site.urls),
]
