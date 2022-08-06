from django.urls import path, include
from rest_framework import routers

from studentapp import views
from studentapp.views import *

router = routers.DefaultRouter()
# router.register("student",StudentViewSet)
router.register("student",StudentViewSet)
router.register("school",SchoolViewSet)
router.register("course",CourseViewSet)
router.register("filter",StudentListView)
router.register('student1', views.StudentListView)


urlpatterns = [
    path("",include(router.urls)),
    # path('api/student/', views.StudentListView.as_view(), name="student"),
    # path("school/",include(router.urls)),
    path("test",views.Register.as_view(),name="test")
]