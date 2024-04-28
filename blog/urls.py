from django.urls import path
from .views import home_page, about_page, blog_page, article_detail
from moose.contact.views import contact_view

urlpatterns = [
    path('', home_page),
    path('about/', about_page, name='about'),
    path('blog/', blog_page, name='blog'),
    path('detail/<int:pk>/', article_detail, name='detail'),
    path('contact/', contact_view, name='contact')
]
