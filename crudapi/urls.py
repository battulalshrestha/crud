from django.urls import path
from . import views
urlpatterns = [
path('',views.api_view,name = 'home'),
path('create/',views.item_list,name = "add-item"),
path('update/<int:pk>/',views.item_update,name = "item-detail"),
#path('delete/<int:pk>/',views.item_delete,name ="item-delete")
]