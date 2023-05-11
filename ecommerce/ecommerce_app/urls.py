from django.urls import path
from ecommerce_app import views
app_name='ecommerce_app'
urlpatterns = [
    path('',views.allprodcat,name='allprodcat'),
    path('<slug:c_slug>/',views.allprodcat,name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.prodetails,name='prodetails')

]








