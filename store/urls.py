from django.urls import include, path
from rest_framework.routers import SimpleRouter, DefaultRouter
from . import views

router = DefaultRouter()
router.register("products",views.ProducViewset,basename="products")
router.register("collections",views.CollectionViewset,basename="collections")


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
    path(r'',include(router.urls))

]