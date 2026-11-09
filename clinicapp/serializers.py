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

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    services = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    # Поля для записи (создания)
    owner_name = serializers.CharField(write_only=True, required=False)
    owner_phone = serializers.CharField(write_only=True, required=False)
    pet_name = serializers.CharField(write_only=True, required=False)
    pet_species = serializers.CharField(write_only=True, required=False)
    pet_age = serializers.IntegerField(write_only=True, required=False)
    
    # Поля для чтения (отображения на фронтенде)
    pet_info = serializers.CharField(source='pet.name', read_only=True)
    doctor_info = serializers.CharField(source='doctor.last_name', read_only=True)
    services_info = ServiceSerializer(source='services', many=True, read_only=True)

    class Meta:
        model = Appointment
        fields = '__all__'
        extra_kwargs = {
            'pet': {'required': False, 'allow_null': True}
        }

    def create(self, validated_data):
        owner_name = validated_data.pop('owner_name', 'Неизвестный')
        owner_phone = validated_data.pop('owner_phone', '0000000000')
        pet_name = validated_data.pop('pet_name', 'Питомец')
        pet_species = validated_data.pop('pet_species', 'Не указан')
        pet_age = validated_data.pop('pet_age', 1)
        services = validated_data.pop('services', [])
        
        pet_id = validated_data.pop('pet', None)
        
        if pet_id:
            pet = Pet.objects.get(id=pet_id)
            owner = pet.owner
        else:
            owner, _ = Owner.objects.get_or_create(
                phone=owner_phone,
                defaults={'first_name': owner_name, 'last_name': 'Клиент'}
            )
            pet, _ = Pet.objects.get_or_create(
                owner=owner,
                name=pet_name,
                defaults={'species': pet_species, 'age': pet_age}
            )

        appointment = Appointment.objects.create(pet=pet, **validated_data)
        
        if services:
            appointment.services.set(services)
            
        return appointment