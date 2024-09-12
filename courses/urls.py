from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    #path('courses/',views.courses,name='courses'),
    path('products/', views.products, name='products'),
    path('add-to-cart/<int:course_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('contact-us/', views.contact_us, name='contact_us'),
]
