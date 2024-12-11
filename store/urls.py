from django.urls import include, path
from rest_framework_nested import routers
from rest_framework.routers import SimpleRouter, DefaultRouter
from . import views

# this is the instance of the nested routers[The base for creating  nested routers]:
router = routers.DefaultRouter()
#Creating Parents [ordinary way ]
router.register("products",views.ProducViewset,basename="products")
router.register("collections",views.CollectionViewset,basename="collections")

#2.Create the Nested
product_router = routers.NestedDefaultRouter(router,'products',lookup = 'product')

#3. Register the Child
product_router.register('reviews',views.ReviewViewset,basename='product-reviews')

urlpatterns= [
    # #class_Based:
    # path('products_class/',views.ProductList.as_view()),
    # path('product_class/<int:id>',views.ProductDetail.as_view()),
    # #Function_Based
    # path('products/',views.product_list),
    # path('product/<int:id>',views.product_detail),
    # path('collection/',views.collection_list),
    # path('collection/<int:id>',views.collection_detail,name='collection-detail'),
    # #ViewSets
    path(r'',include(router.urls)),
    path(r"",include(product_router.urls))

]