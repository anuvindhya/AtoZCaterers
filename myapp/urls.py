from django.urls import path

from myapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('service/', views.service, name='service'),
    path('event/', views.event, name='event'),
    path('menu/', views.menu, name='menu'),
    path('book/', views.book, name='book'),
    path('blog/', views.blog, name='blog'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('contact/', views.contact, name='contact'),
]