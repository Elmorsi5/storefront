from django.urls import path
from . import views

urlpatterns= [
    path('products/',views.product_list),
    path('product/<int:id>',views.product_detail),
    path('collection/',views.collection_list),
    path('collection/<int:id>',views.collection_detail,name='collection-detail'),

]