from django.db import models

class Owner(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")

    class Meta:
        verbose_name = "Владелец"
        verbose_name_plural = "Владельцы"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Pet(models.Model):
    name = models.CharField(max_length=100, verbose_name="Кличка")
    species = models.CharField(max_length=50, verbose_name="Вид (собака/кошка)")
    breed = models.CharField(max_length=100, blank=True, null=True, verbose_name="Порода")
    age = models.IntegerField(verbose_name="Возраст (лет)")
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="pets", verbose_name="Владелец")

    class Meta:
        verbose_name = "Питомец"
        verbose_name_plural = "Питомцы"

    def __str__(self):
        return f"{self.name} ({self.species})"

class Doctor(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    speciality = models.CharField(max_length=100, verbose_name="Специальность")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    description = models.TextField(blank=True, verbose_name="Описание")  

    class Meta:
        verbose_name = "Врач"
        verbose_name_plural = "Врачи"

    def __str__(self):
        return f"Доктор {self.first_name} {self.last_name}"

class Service(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название услуги")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена (руб.)")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.title

class Appointment(models.Model):
    STATUS_CHOICES = (
        ('new', 'Новая'),
        ('confirmed', 'Подтверждена'),
        ('completed', 'Завершена'),
        ('cancelled', 'Отменена'),
    )
    
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="appointments", verbose_name="Питомец")
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, related_name="appointments", verbose_name="Врач")
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, verbose_name="Услуга")
    date_time = models.DateTimeField(verbose_name="Дата и время приёма")
    description = models.TextField(blank=True, null=True, verbose_name="Описание проблемы")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="Статус")

    class Meta:
        verbose_name = "Запись на прием"
        verbose_name_plural = "Записи на прием"
        ordering = ['-date_time']

    def __str__(self):
        return f"{self.pet.name} к {self.doctor.last_name if self.doctor else 'Врач не назначен'}"