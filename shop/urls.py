from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='ShopHome'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('tracker',views.tracker,name='tracker'),
    path('search',views.search,name='search'),
    path('productview',views.productview,name='productview'),
    path('checkout/',views.checkout,name='checkout'),
    path('base/',views.base,name="base"),
    path('base/submit',views.submit,name="submit"),
    path('base/submit/show',views.show,name="show"),
    path('signup',views.handelsignup,name="signup"),
    path('login',views.handellogin,name="login"),
    path('logout',views.handellogout,name="logout"),
    path('orderdetail/<int:id>/<str:username>',views.orderdetail,name="orderdetail"),
    path('orderhistory/<str:username>',views.orderhistory,name="orderhistory"),
    path('demo',views.demo,name="demo")
]
# handler404 = "django_404_project.views.page_not_found_view"