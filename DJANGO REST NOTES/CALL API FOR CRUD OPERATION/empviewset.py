from rest_framework import viewsets
from .empserializer import EmpSerializer
from .models import Emp
class EmpViewSet(viewsets.ModelViewSet):
    queryset=Emp.objects.all()
    serializer_class=EmpSerializer