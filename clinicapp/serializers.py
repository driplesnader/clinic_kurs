from rest_framework import serializers
from .models import Owner, Pet, Doctor, Service, Appointment

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'

class PetSerializer(serializers.ModelSerializer):
    owner_name = serializers.ReadOnlyField(source='owner.first_name')
    class Meta:
        model = Pet
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    pet_name = serializers.ReadOnlyField(source='pet.name')
    doctor_name = serializers.ReadOnlyField(source='doctor.last_name')
    service_title = serializers.ReadOnlyField(source='service.title')

    class Meta:
        model = Appointment
        fields = '__all__'