from rest_framework import viewsets, permissions
from .models import Owner, Pet, Doctor, Service, Appointment
from .serializers import (
    OwnerSerializer, PetSerializer, DoctorSerializer, 
    ServiceSerializer, AppointmentSerializer
)

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [permissions.AllowAny]

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    # Вернули queryset, чтобы роутер не ругался
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.AllowAny]

    # Метод get_queryset тоже оставляем (он пригодится для фильтрации в будущем)
    def get_queryset(self):
        return Appointment.objects.all()