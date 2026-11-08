<template>
  <div class="service-page container">
    <!-- Если идет загрузка -->
    <div v-if="loading" class="loading-state">
      <div class="spinner"></div>
      <p>Загрузка информации об услуге...</p>
    </div>

    <!-- Если произошла ошибка -->
    <div v-else-if="error" class="error-state">
      <p>{{ error }}</p>
      <router-link to="/" class="btn-back">Вернуться на главную</router-link>
    </div>

    <!-- Страница услуги -->
    <div v-else-if="service" class="service-detail">
      <router-link to="/" class="back-link">← Назад ко всем услугам</router-link>
      
      <div class="service-header">
        <div class="service-icon-large">💉</div>
        <h1 class="service-title">{{ service.title }}</h1>
        <div class="service-price-large">{{ service.price }} ₽</div>
      </div>

      <div class="service-body">
        <div class="service-description">
          <h2>Описание услуги</h2>
          <p>{{ service.description || 'Подробное описание появится позже.' }}</p>
          
          <h3>Что входит в услугу:</h3>
          <ul>
            <li>Осмотр квалифицированным специалистом</li>
            <li>Индивидуальный подход к вашему питомцу</li>
            <li>Консультация по уходу и профилактике</li>
            <li>Рекомендации по дальнейшему лечению (при необходимости)</li>
          </ul>
        </div>

        <div class="service-sidebar">
          <div class="action-card">
            <h3>Записаться на эту услугу</h3>
            <p>Выберите удобное время, и мы вас примем.</p>
            <router-link to="/appointment" class="btn-book-service">
              Записаться сейчас
            </router-link>
          </div>

          <div class="info-card">
            <h4>Почему выбирают нас?</h4>
            <ul>
              <li>✅ Опытные врачи</li>
              <li>✅ Современное оборудование</li>
              <li>✅ Безопасные препараты</li>
              <li>✅ Забота о каждом пациенте</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import { useRoute } from 'vue-router';
import apiClient from '../api/index';

const route = useRoute();
const service = ref(null);
const loading = ref(true);
const error = ref(null);

const fetchService = async (id) => {
  try {
    loading.value = true;
    error.value = null;
    const response = await apiClient.get(`/services/${id}/`);
    service.value = response.data;
  } catch (err) {
    error.value = "Услуга не найдена. Возможно, она была удалена.";
  } finally {
    loading.value = false;
  }
};

// Следим за изменением ID в URL и загружаем новую услугу
watch(() => route.params.id, (newId) => {
  if (newId) fetchService(newId);
});

onMounted(() => {
  if (route.params.id) {
    fetchService(route.params.id);
  }
});
</script>

<style scoped>
.service-page { padding: 60px 20px; min-height: 60vh; }

.back-link {
  display: inline-block;
  margin-bottom: 30px;
  color: #666;
  text-decoration: none;
  font-weight: 600;
  transition: color 0.3s;
}
.back-link:hover { color: #ff5c8a; }

.service-header {
  text-align: center;
  margin-bottom: 50px;
}

.service-icon-large {
  font-size: 80px;
  margin-bottom: 20px;
}

.service-title {
  font-size: 42px;
  font-weight: 900;
  color: #1a1a1a;
  margin-bottom: 15px;
}

.service-price-large {
  display: inline-block;
  font-size: 32px;
  font-weight: 800;
  color: #ff5c8a;
  background: #fff0f5;
  padding: 10px 30px;
  border-radius: 50px;
}

.service-body {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 40px;
}

.service-description {
  background: white;
  padding: 40px;
  border-radius: 24px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.03);
  border: 1px solid #f0f0f0;
}

.service-description h2 {
  font-size: 28px;
  margin-bottom: 20px;
  color: #1a1a1a;
}

.service-description p {
  color: #555;
  line-height: 1.8;
  font-size: 16px;
  margin-bottom: 30px;
}

.service-description h3 {
  font-size: 20px;
  margin-bottom: 15px;
  color: #1a1a1a;
}

.service-description ul {
  list-style: none;
  padding: 0;
}

.service-description li {
  padding: 10px 0;
  color: #444;
  border-bottom: 1px solid #f0f0f0;
  display: flex;
  align-items: center;
  gap: 10px;
}

.service-description li::before {
  content: '✅';
}

.service-sidebar {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.action-card {
  background: linear-gradient(135deg, #ff5c8a 0%, #ff8fa3 100%);
  padding: 30px;
  border-radius: 24px;
  color: white;
  text-align: center;
  box-shadow: 0 15px 30px rgba(255, 92, 138, 0.3);
}

.action-card h3 { font-size: 22px; margin-bottom: 10px; }
.action-card p { font-size: 14px; margin-bottom: 20px; opacity: 0.9; }

.btn-book-service {
  display: block;
  background: white;
  color: #ff5c8a;
  padding: 15px;
  border-radius: 50px;
  text-decoration: none;
  font-weight: 800;
  font-size: 16px;
  transition: transform 0.3s;
}
.btn-book-service:hover { transform: scale(1.05); }

.info-card {
  background: white;
  padding: 30px;
  border-radius: 24px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.03);
  border: 1px solid #f0f0f0;
}

.info-card h4 { font-size: 18px; margin-bottom: 15px; color: #1a1a1a; }
.info-card ul { list-style: none; padding: 0; }
.info-card li { padding: 8px 0; color: #555; font-size: 14px; }

.loading-state, .error-state {
  text-align: center;
  padding: 100px 20px;
}

.spinner {
  width: 50px; height: 50px;
  border: 5px solid #ffe4ec;
  border-top: 5px solid #ff5c8a;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 20px;
}

@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }

.btn-back {
  display: inline-block;
  margin-top: 20px;
  padding: 12px 24px;
  background: #ff5c8a;
  color: white;
  text-decoration: none;
  border-radius: 50px;
  font-weight: bold;
}

@media (max-width: 900px) {
  .service-body { grid-template-columns: 1fr; }
}
</style>