from django.urls import path
from . import views

urlpatterns = [
    # get list methods
    path('titles-list/' , views.get_titles, name='get-titles'),
    path('items-list/' , views.get_items, name='get-items'),
    path('subItems-list/' , views.get_subItems, name='get-subItems'),
    # PUT methods
    path('update-title/<str:id>/' , views.update_title, name='update-title'),
    path('update-item/<str:id>/' , views.update_item, name='update-item'),
    path('update-subItem/<str:id>/' , views.update_subItem, name='update-subItem'),
    # DELETE methods 
    path('delete-title/<str:id>/' , views.delete_title, name='delete-title'),
    path('delete-item/<str:id>/' , views.delete_item, name='delete-item'),
    path('delete-subItem/<str:id>/' , views.delete_subItem, name='delete-sub-item'),
    # POST methods 
    path('create-title/' , views.create_title, name='create-title'),
    path('create-item/' , views.create_item,name='create-item'),




]