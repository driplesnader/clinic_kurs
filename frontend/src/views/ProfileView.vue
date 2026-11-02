<template>
  <div class="profile-page container">
    <h1>Личный кабинет</h1>
    <button @click="logout" class="btn-logout">Выйти</button>

    <div v-if="loading">Загрузка...</div>
    
    <div v-else-if="appointments.length === 0" class="empty">
      <p>У вас пока нет записей. <router-link to="/appointment">Записаться</router-link></p>
    </div>

    <div v-else class="appointments-list">
      <div v-for="app in appointments" :key="app.id" class="appointment-card">
        <div class="app-header">
          <h3>Запись #{{ app.id }}</h3>
          <span class="status" :class="app.status">{{ app.status }}</span>
        </div>
        <p><strong>Дата:</strong> {{ new Date(app.date_time).toLocaleString() }}</p>
        <p><strong>Врач:</strong> {{ app.doctor_name || 'Не назначен' }}</p>
        <p><strong>Питомец:</strong> {{ app.pet_name }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import apiClient from '../api/index';

const appointments = ref([]);
const loading = ref(true);
const router = useRouter();

const fetchAppointments = async () => {
  const token = localStorage.getItem('access_token');
  if (!token) {
    router.push('/login');
    return;
  }

  try {
    // Отправляем токен в заголовке
    const response = await apiClient.get('/appointments/', {
      headers: { Authorization: `Bearer ${token}` }
    });
    appointments.value = response.data;
  } catch (err) {
    console.error(err);
    router.push('/login');
  } finally {
    loading.value = false;
  }
};

const logout = () => {
  localStorage.removeItem('access_token');
  localStorage.removeItem('refresh_token');
  router.push('/');
};

onMounted(fetchAppointments);
</script>

<style scoped>
.profile-page { padding: 40px 20px; }
.btn-logout { margin-bottom: 20px; padding: 10px 20px; background: #ff5c8a; color: white; border: none; border-radius: 8px; cursor: pointer; }
.appointments-list { display: grid; gap: 20px; }
.appointment-card { background: white; padding: 20px; border-radius: 16px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
.app-header { display: flex; justify-content: space-between; margin-bottom: 15px; }
.status { padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: bold; background: #eee; }
.status.new { background: #e0f7fa; color: #006064; }
.status.confirmed { background: #e8f5e9; color: #1b5e20; }
</style>