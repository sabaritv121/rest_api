from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, filters
from rest_framework.pagination import PageNumberPagination

from studentapp.forms import LoginRegister, StudentRegister
from studentapp.models import Student, School, Course, Login
from studentapp.serializers import StudentSerializer, SchoolSerializer, CourseSerializer, RegisterSerializer


def home(request):
    return render(request, 'home.html')


def panel(request):
    return render(request, 'panel.html')


#
def login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get("pass")
        user = authenticate(username=username, passsword=password)
        if user is not None:
            login(request, user)

            if user.is_student:
                return render(request, '')


def user_add(request):
    form1 = LoginRegister()
    form2 = StudentRegister()
    if request.method == 'POST':
        form1 = LoginRegister(request.POST)
        form2 = StudentRegister(request.POST)

        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.is_user = True
            user.save()
            user1 = form2.save(commit=False)
            user1.user = user
            user1.save()
            return redirect('home')

    return render(request, 'user_register.html', {'form1': form1, 'form2': form2})


def studentpanel(request):
    return render(request, "studenttemp/studentpanel.html")


## serializer
class StudentPagination(PageNumberPagination):
    page_size = 1


class DjangoSearchBackend:
    pass


class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = PageNumberPagination
    # pagination_class = StudentPagination
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['school', 'course']
    filters_backends = [filters.SearchFilter]
    search_fields = ['=^name', '=^course']

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentListView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['school', 'course']

class Register(generics.ListCreateAPIView):
    queryset = Login.objects.all()
    serializer_class = RegisterSerializer



