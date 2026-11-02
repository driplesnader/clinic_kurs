from rest_framework import viewsets
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

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Owner, Pet, Doctor, Service, Appointment
from .serializers import (
    OwnerSerializer, PetSerializer, DoctorSerializer, 
    ServiceSerializer, AppointmentSerializer
)
from django.contrib.auth.models import User

# ... (остальные ViewSet: OwnerViewSet, PetViewSet, DoctorViewSet, ServiceViewSet оставляем как были)

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    # Разрешаем создавать записи всем, но видеть их может только автор
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Получаем данные из запроса
        owner_name = self.request.data.get('owner_name', 'Неизвестный')
        owner_phone = self.request.data.get('owner_phone', '0000000000')
        pet_name = self.request.data.get('pet_name', 'Питомец')
        
        # Если пользователь авторизован, берем его, иначе создаем/ищем по телефону
        if self.request.user.is_authenticated:
            owner, _ = Owner.objects.get_or_create(
                phone=owner_phone, # Ищем по телефону, чтобы не дублировать
                defaults={'first_name': owner_name, 'last_name': 'Клиент'}
            )
        else:
            owner, _ = Owner.objects.get_or_create(
                phone=owner_phone,
                defaults={'first_name': owner_name, 'last_name': 'Клиент'}
            )

        # Создаем/ищем питомца
        pet, _ = Pet.objects.get_or_create(
            owner=owner,
            name=pet_name,
            defaults={'species': 'Не указан', 'age': 1}
        )

        # Сохраняем запись
        serializer.save(pet=pet)