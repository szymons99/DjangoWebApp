from django.urls import path
from . import views
from .views import form_f, edycja_f, usun_f, update_, comment_, champion_, item_

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('formularz/', form_f, name='form'),
    path('edycja/<int:id>/', edycja_f, name='edycja'),
    path('usun/<int:id>/', usun_f, name='usun'),
    path('updates/', update_, name='updates'),
    path('komentarz/', comment_, name='komentarz'),
    path('champion/', champion_, name='champions'),
    path('item/<int:id>/', item_, name='item')

]
