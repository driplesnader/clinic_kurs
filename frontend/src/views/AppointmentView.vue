<template>
  <div class="appointment-page">
    <div class="appointment-container">
      
      <div class="info-side">
        <h1 class="page-title">Запись на приём</h1>
        <p class="page-subtitle">Заполните форму ниже, и мы свяжемся с вами для подтверждения времени.</p>
        
        <div class="contact-info">
          <div class="contact-item"><span class="icon">📍</span><div><strong>Адрес</strong><p>г. Сургут, ул. Пушкина, 1</p></div></div>
          <div class="contact-item"><span class="icon">📞</span><div><strong>Телефон</strong><p>8 (800) 000-00-00</p></div></div>
          <div class="contact-item"><span class="icon">🕒</span><div><strong>Режим работы</strong><p>Пн–Вс: 09:00–20:00</p></div></div>
        </div>
      </div>

      <div class="form-side">
        <div v-if="isSuccess" class="success-message fade-in">
          <div class="success-icon">🎉</div>
          <h2>Заявка отправлена!</h2>
          <p>Администратор свяжется с вами в ближайшее время.</p>
          <router-link to="/" class="btn btn-primary" style="margin-top: 20px;">На главную</router-link>
        </div>

        <form v-else @submit.prevent="submitForm" class="appointment-form">
          <div class="form-group">
            <label>Ваше имя</label>
            <input type="text" v-model="formData.owner_name" required placeholder="Иван Иванов" />
          </div>

          <div class="form-group">
            <label>Телефон</label>
            <input type="tel" v-model="formData.owner_phone" required placeholder="+7 (___) ___-__-__" />
          </div>

          <!-- БЛОК ПИТОМЦА -->
          <div class="form-group">
            <label>Питомец</label>
            
            <template v-if="isAuthenticated">
              <select v-model="formData.pet_id" required>
                <option value="" disabled>Выберите питомца из списка</option>
                <option v-for="pet in myPets" :key="pet.id" :value="pet.id">
                  {{ pet.name }} ({{ pet.species }})
                </option>
                <option value="new">+ Добавить нового питомца</option>
              </select>
              
              <div v-if="formData.pet_id === 'new'" class="new-pet-fields">
                <input type="text" v-model="formData.pet_name" placeholder="Кличка" required />
                <input type="text" v-model="formData.pet_species" placeholder="Вид (кошка, собака)" required />
                <input type="number" v-model="formData.pet_age" placeholder="Возраст (лет)" min="0" required />
              </div>
            </template>

            <template v-else>
              <div class="new-pet-fields">
                <input type="text" v-model="formData.pet_name" required placeholder="Кличка питомца" />
                <input type="text" v-model="formData.pet_species" placeholder="Вид (кошка, собака)" required />
                <input type="number" v-model="formData.pet_age" placeholder="Возраст (лет)" min="0" required />
              </div>
            </template>
          </div>

          <!-- БЛОК УСЛУГ -->
          <div class="form-group">
            <label>Выберите услуги (можно несколько)</label>
            <div class="services-checkbox-list">
              <label v-for="service in services" :key="service.id" class="checkbox-item">
                <input type="checkbox" :value="service.id" v-model="formData.services" />
                <span>{{ service.title }} ({{ service.price }} ₽)</span>
              </label>
            </div>
          </div>

          <!-- ВЫБОР ВРАЧА -->
          <div class="form-group">
            <label>Выберите врача</label>
            <select v-model="formData.doctor" required>
              <option value="" disabled>Выберите специалиста</option>
              <option v-for="vet in filteredVets" :key="vet.id" :value="vet.id">
                {{ vet.first_name }} {{ vet.last_name }} ({{ vet.speciality }})
              </option>
            </select>
            <small v-if="formData.services.length > 0 && filteredVets.length === 0" class="no-vets-warning">
              ⚠️ Нет врачей, оказывающих выбранные услуги.
            </small>
          </div>

          <div class="form-group">
            <label>Дата и время</label>
            <input type="datetime-local" v-model="formData.appointment_date" required />
          </div>

          <div class="form-group">
            <label>Описание проблемы (необязательно)</label>
            <textarea v-model="formData.description" rows="3" placeholder="Что беспокоит вашего питомца?"></textarea>
          </div>

          <button type="submit" class="btn-submit" :disabled="isLoading">
            {{ isLoading ? 'Отправка...' : 'Отправить заявку' }}
          </button>
          
          <p v-if="errorMessage" class="error-msg">{{ errorMessage }}</p>
        </form>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed, watch } from 'vue';
import apiClient from '../api/index';

const vets = ref([]);
const services = ref([]);
const myPets = ref([]);
const isAuthenticated = ref(false);

const isLoading = ref(false);
const isSuccess = ref(false);
const errorMessage = ref('');

const formData = ref({
  owner_name: '',
  owner_phone: '',
  pet_name: '',
  pet_species: 'Кошка',
  pet_age: 1,
  pet_id: '',
  doctor: '',
  services: [],
  appointment_date: '',
  description: ''
});

const checkAuthAndLoadData = async () => {
  const token = localStorage.getItem('access_token');
  isAuthenticated.value = !!token;

  try {
    const [vetsRes, servicesRes] = await Promise.all([
      apiClient.get('/doctors/'),
      apiClient.get('/services/')
    ]);
    vets.value = vetsRes.data;
    services.value = servicesRes.data;

    if (isAuthenticated.value) {
      const petsRes = await apiClient.get('/pets/', {
        headers: { Authorization: `Bearer ${token}` }
      });
      myPets.value = petsRes.data;
    }
  } catch (err) {
    console.error("Ошибка загрузки данных", err);
  }
};

const filteredVets = computed(() => {
  if (formData.value.services.length === 0) {
    return vets.value;
  }
  return vets.value.filter(vet => {
    const vetServices = vet.services || []; 
    return formData.value.services.some(selectedId => 
      vetServices.includes(selectedId)
    );
  });
});

watch(() => formData.value.services, () => {
  const isValid = filteredVets.value.some(v => v.id === formData.value.doctor);
  if (!isValid) formData.value.doctor = '';
}, { deep: true });

onMounted(() => {
  checkAuthAndLoadData();
});

const submitForm = async () => {
  isLoading.value = true;
  errorMessage.value = '';
  
  try {
    const payload = {
      owner_name: formData.value.owner_name,
      owner_phone: formData.value.owner_phone,
      doctor: formData.value.doctor,
      services: formData.value.services,
      date_time: formData.value.appointment_date,
      description: formData.value.description
    };

    if (isAuthenticated.value && formData.value.pet_id && formData.value.pet_id !== 'new') {
      payload.pet = formData.value.pet_id;
    } else {
      payload.pet_name = formData.value.pet_name;
      payload.pet_species = formData.value.pet_species;
      payload.pet_age = formData.value.pet_age;
    }

    await apiClient.post('/appointments/', payload);
    isSuccess.value = true;
  } catch (err) {
    console.error(err.response?.data || err);
    errorMessage.value = "Ошибка при отправке. Проверьте соединение.";
  } finally {
    isLoading.value = false;
  }
};
</script>

<style scoped>
.appointment-page { padding: 60px 20px; background: #faf5f7; min-height: 80vh; display: flex; justify-content: center; align-items: center; }
.appointment-container { max-width: 1000px; width: 100%; background: white; border-radius: 32px; box-shadow: 0 20px 50px rgba(0,0,0,0.05); display: flex; overflow: hidden; }

.info-side { background: linear-gradient(135deg, #fff0f5 0%, #ffe4ec 100%); padding: 60px 40px; flex: 0 0 40%; display: flex; flex-direction: column; }
.page-title { font-size: 36px; font-weight: 900; color: #1a1a1a; margin-bottom: 16px; line-height: 1.1; }
.page-subtitle { font-size: 16px; color: #555; line-height: 1.6; margin-bottom: 40px; }
.contact-info { display: flex; flex-direction: column; gap: 20px; margin-top: auto; }
.contact-item { display: flex; align-items: flex-start; gap: 16px; background: rgba(255, 255, 255, 0.6); padding: 16px; border-radius: 16px; }
.contact-item .icon { font-size: 24px; }
.contact-item strong { display: block; font-size: 16px; color: #1a1a1a; margin-bottom: 4px; }
.contact-item p { font-size: 14px; color: #666; margin: 0; }

.form-side { padding: 60px 50px; flex: 1; }
.appointment-form { display: flex; flex-direction: column; gap: 20px; }
.form-group { display: flex; flex-direction: column; gap: 8px; }
.form-group label { font-size: 14px; font-weight: 600; color: #333; }

.form-group input,
.form-group select,
.form-group textarea {
  padding: 14px 16px;
  border-radius: 12px;
  border: 1px solid #e5e5e5;
  font-size: 15px;
  font-family: inherit;
  transition: all 0.3s ease;
  background: #fafafa;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: #ff5c8a;
  background: white;
  box-shadow: 0 0 0 4px rgba(255, 92, 138, 0.1);
}

.new-pet-fields {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-top: 10px;
  padding: 15px;
  background: #fdf2f6;
  border-radius: 12px;
  border: 1px dashed #ffb6c1;
}

.services-checkbox-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
  background: #fafafa;
  padding: 15px;
  border-radius: 12px;
  border: 1px solid #e5e5e5;
  max-height: 200px;
  overflow-y: auto;
}

.checkbox-item { display: flex; align-items: center; gap: 10px; font-size: 14px; cursor: pointer; color: #333; }
.checkbox-item input[type="checkbox"] { width: 18px; height: 18px; accent-color: #ff5c8a; cursor: pointer; }
.no-vets-warning { color: #d9534f; font-size: 13px; margin-top: 5px; }

.btn-submit { background: #ff5c8a; color: white; border: none; padding: 16px; border-radius: 12px; font-size: 16px; font-weight: 700; cursor: pointer; transition: all 0.3s ease; margin-top: 10px; }
.btn-submit:hover:not(:disabled) { background: #ff4074; transform: translateY(-2px); box-shadow: 0 10px 20px rgba(255, 92, 138, 0.3); }
.btn-submit:disabled { background: #ffb6c1; cursor: not-allowed; }

.error-msg { color: #ff4074; font-size: 14px; text-align: center; margin-top: 10px; }
.success-message { text-align: center; padding: 40px 20px; }
.success-icon { font-size: 60px; margin-bottom: 20px; }
.success-message h2 { font-size: 28px; color: #1a1a1a; margin-bottom: 12px; }
.success-message p { color: #666; font-size: 16px; }
.btn { display: inline-block; padding: 14px 28px; border-radius: 50px; text-decoration: none; font-weight: 700; }
.btn-primary { background: #ff5c8a; color: white; }

@media (max-width: 900px) {
  .appointment-container { flex-direction: column; }
  .info-side { padding: 40px 20px; }
  .form-side { padding: 40px 20px; }
}
</style>