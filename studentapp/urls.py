from django.urls import path

from studentapp import views

urlpatterns = [
   path('',views.home,name="home"),
   path('panel',views.panel,name='panel'),
   path('studentpanel',views.studentpanel,name="studentpanel")
]
