from django.urls import path
from . import views

urlpatterns= [
    #class_Based:
    path('products_class/',views.ProductList.as_view()),
    path('product_class/<int:id>',views.ProductDetail.as_view()),
    #Function_Based
    path('products/',views.product_list),
    path('product/<int:id>',views.product_detail),
    path('collection/',views.collection_list),
    path('collection/<int:id>',views.collection_detail,name='collection-detail'),

]