<template>
  <div class="vets-page container">
    <h1 class="page-title">Наши врачи</h1>
    <p class="page-subtitle">Профессиональные специалисты по терапевтическим и хирургическим профилям</p>

    <div v-if="loading" class="loading">Загрузка врачей...</div>
    
    <div v-else-if="vets.length === 0" class="empty-state">
      Врачи пока не добавлены в базу данных.
    </div>

    <div v-else class="doctors-grid">
      <div v-for="vet in vets" :key="vet.id" class="doctor-card">
        <div class="doctor-avatar">
          <span>{{ vet.first_name[0] }}{{ vet.last_name[0] }}</span>
        </div>
        <div class="doctor-info">
          <h3>{{ vet.first_name }} {{ vet.last_name }}</h3>
          <p class="speciality">{{ vet.speciality }}</p>
          <p class="description" v-if="vet.description">{{ vet.description }}</p>
          <p class="phone">📞 {{ vet.phone }}</p>
          <router-link to="/appointment" class="btn-book">Записаться</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import apiClient from '../api/index';

const vets = ref([]);
const loading = ref(true);

const fetchVets = async () => {
  try {
    const response = await apiClient.get('/doctors/');
    vets.value = response.data;
  } catch (error) {
    console.error("Ошибка при загрузке врачей:", error);
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  fetchVets();
});
</script>

<style scoped>
.vets-page { padding: 60px 20px; }
.page-title { font-size: 42px; font-weight: 900; color: #1a1a1a; margin-bottom: 10px; }
.page-subtitle { font-size: 18px; color: #666; margin-bottom: 40px; }

.doctors-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 30px;
}

.doctor-card {
  background: white;
  border-radius: 24px;
  padding: 30px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.05);
  display: flex;
  gap: 20px;
  align-items: flex-start;
  transition: transform 0.3s ease;
  border: 1px solid #f0f0f0;
}

.doctor-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 20px 40px rgba(255, 92, 138, 0.15);
}

.doctor-avatar {
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, #ff5c8a 0%, #ff8fa3 100%);
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 28px;
  font-weight: 800;
  flex-shrink: 0;
}

.doctor-info h3 { font-size: 22px; font-weight: 800; color: #1a1a1a; margin-bottom: 4px; }
.speciality { color: #ff5c8a; font-weight: 600; font-size: 15px; margin-bottom: 10px; }
.description { color: #666; font-size: 14px; line-height: 1.5; margin-bottom: 15px; }
.phone { color: #444; font-weight: 600; font-size: 15px; margin-bottom: 15px; }

.btn-book {
  display: inline-block;
  padding: 10px 24px;
  background: #fff0f5;
  color: #ff5c8a;
  text-decoration: none;
  border-radius: 50px;
  font-weight: 700;
  font-size: 14px;
  transition: all 0.3s ease;
}

.btn-book:hover { background: #ff5c8a; color: white; }
.loading, .empty-state { text-align: center; padding: 50px; color: #666; font-size: 18px; }
</style>