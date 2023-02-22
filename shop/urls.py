from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='Home'),
    path('connect',views.connect,name="connect"),
    path('dashboard',views.dashboard,name="dashboard"),
    # path('signup',views.handelsignup,name="signup"),
    # path('login',views.handellogin,name="login"),
    path('logout',views.handellogout,name="logout"),
    path('solve',views.solve,name="solve"),
    # path('demo',views.demo,name="demo"),
    # path('')
]
# handler404 = "django_404_project.views.page_not_found_view"