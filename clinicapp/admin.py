from django.contrib import admin
from .models import Owner, Pet, Doctor, Service, Appointment

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone")

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ("name", "species", "owner")

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "speciality")

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "price")

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("pet", "doctor", "date_time", "status")