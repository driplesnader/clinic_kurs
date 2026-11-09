<template>
  <div class="profile-page container">
    <h1>Личный кабинет</h1>
    <button @click="logout" class="btn-logout">Выйти</button>

    <div v-if="loading">Загрузка...</div>
    
    <div v-else class="profile-content">
      <!-- Блок питомцев -->
      <div class="my-pets-section">
        <h2>Мои питомцы</h2>
        <div class="pets-grid">
          <div v-for="pet in myPets" :key="pet.id" class="pet-card">
            <span class="pet-emoji">{{ pet.species === 'Кошка' ? '🐱' : '🐶' }}</span>
            <div>
              <strong>{{ pet.name }}</strong>
              <small>{{ pet.species }}, {{ pet.age }} г.</small>
            </div>
          </div>
          <div class="pet-card empty-pet">
            <router-link to="/appointment" class="add-pet-link">+ Записать нового питомца</router-link>
          </div>
        </div>
      </div>

      <!-- Блок записей -->
      <div class="appointments-section">
        <h2>Мои записи</h2>
        
        <div v-if="appointments.length === 0" class="empty">
          <p>У вас пока нет записей. <router-link to="/appointment">Записаться</router-link></p>
        </div>

        <div v-else class="appointments-list">
          <div v-for="app in appointments" :key="app.id" class="appointment-card">
            <div class="app-header">
              <h3>Запись #{{ app.id }}</h3>
              <span class="status" :class="app.status">{{ app.status }}</span>
            </div>
            <p><strong>Дата:</strong> {{ new Date(app.date_time).toLocaleString() }}</p>
            <!-- Используем новые поля для отображения -->
            <p><strong>Врач:</strong> {{ app.doctor_info || 'Не назначен' }}</p>
            <p><strong>Питомец:</strong> {{ app.pet_info }}</p>
            <p v-if="app.services_info && app.services_info.length > 0">
              <strong>Услуги:</strong> 
              <span v-for="srv in app.services_info" :key="srv.id" class="service-tag">{{ srv.title }}</span>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import apiClient from '../api/index';

const appointments = ref([]);
const myPets = ref([]);
const loading = ref(true);
const router = useRouter();

const fetchData = async () => {
  const token = localStorage.getItem('access_token');
  if (!token) {
    router.push('/login');
    return;
  }

  try {
    // Загружаем записи и питомцев
    const [appRes, petsRes] = await Promise.all([
      apiClient.get('/appointments/', { headers: { Authorization: `Bearer ${token}` } }),
      apiClient.get('/pets/', { headers: { Authorization: `Bearer ${token}` } })
    ]);
    
    appointments.value = appRes.data; 
    myPets.value = petsRes.data;
  } catch (err) {
    console.error(err);
    if (err.response?.status === 401) {
      logout();
    }
  } finally {
    loading.value = false;
  }
};

const logout = () => {
  localStorage.removeItem('access_token');
  localStorage.removeItem('refresh_token');
  router.push('/');
};

onMounted(fetchData);
</script>

<style scoped>
.profile-page { padding: 40px 20px; }
h1 { margin-bottom: 20px; }
h2 { font-size: 24px; margin-bottom: 20px; color: #1a1a1a; }
.btn-logout { margin-bottom: 30px; padding: 10px 20px; background: #ff5c8a; color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: 600; }

.profile-content { display: flex; flex-direction: column; gap: 50px; }

/* Мои питомцы */
.my-pets-section { background: white; padding: 30px; border-radius: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.03); }
.pets-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 20px; }
.pet-card { display: flex; align-items: center; gap: 15px; background: #faf5f7; padding: 15px; border-radius: 12px; }
.pet-emoji { font-size: 32px; }
.pet-card strong { display: block; font-size: 16px; color: #1a1a1a; }
.pet-card small { color: #666; font-size: 13px; }
.empty-pet { justify-content: center; border: 2px dashed #ffb6c1; background: transparent; }
.add-pet-link { color: #ff5c8a; font-weight: 600; text-decoration: none; font-size: 14px; }

/* Записи */
.appointments-section { background: white; padding: 30px; border-radius: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.03); }
.appointments-list { display: flex; flex-direction: column; gap: 15px; }
.appointment-card { background: #f9f9f9; padding: 20px; border-radius: 12px; }
.app-header { display: flex; justify-content: space-between; margin-bottom: 10px; }
.app-header h3 { font-size: 18px; margin: 0; }
.status { padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: bold; background: #eee; }
.status.new { background: #e0f7fa; color: #006064; }
.status.confirmed { background: #e8f5e9; color: #1b5e20; }
.appointment-card p { margin: 5px 0; color: #555; font-size: 15px; }

.service-tag {
  display: inline-block;
  background: #e0f7fa;
  color: #006064;
  padding: 2px 8px;
  border-radius: 10px;
  font-size: 12px;
  margin-right: 5px;
}
</style>