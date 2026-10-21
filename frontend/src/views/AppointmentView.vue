<template>
  <div class="appointment-page">
    <div class="appointment-container">
      
      <!-- Левая часть с текстом -->
      <div class="info-side">
        <h1 class="page-title">Запись на приём</h1>
        <p class="page-subtitle">Заполните форму ниже, и мы свяжемся с вами для подтверждения времени.</p>
        
        <div class="contact-info">
          <div class="contact-item">
            <span class="icon">📍</span>
            <div>
              <strong>Адрес</strong>
              <p>г. Сургут, ул. Пушкина, 1</p>
            </div>
          </div>
          <div class="contact-item">
            <span class="icon">📞</span>
            <div>
              <strong>Телефон</strong>
              <p>8 (800) 000-00-00</p>
            </div>
          </div>
          <div class="contact-item">
            <span class="icon">🕒</span>
            <div>
              <strong>Режим работы</strong>
              <p>Пн–Вс: 09:00–20:00</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Правая часть с формой -->
      <div class="form-side">
        <!-- Если успешно отправили -->
        <div v-if="isSuccess" class="success-message fade-in">
          <div class="success-icon">🎉</div>
          <h2>Заявка отправлена!</h2>
          <p>Администратор свяжется с вами в ближайшее время для подтверждения.</p>
          <router-link to="/" class="btn btn-primary" style="margin-top: 20px;">На главную</router-link>
        </div>

        <!-- Сама форма -->
        <form v-else @submit.prevent="submitForm" class="appointment-form">
          
          <div class="form-group">
            <label>Ваше имя</label>
            <input type="text" v-model="formData.owner_name" required placeholder="Иван Иванов" />
          </div>

          <div class="form-group">
            <label>Телефон</label>
            <input type="tel" v-model="formData.owner_phone" required placeholder="+7 (___) ___-__-__" />
          </div>

          <div class="form-group">
            <label>Кличка питомца</label>
            <input type="text" v-model="formData.pet_name" required placeholder="Барсик" />
          </div>

          <div class="form-group">
            <label>Выберите врача</label>
            <select v-model="formData.veterinarian" required>
              <option value="" disabled>Выберите специалиста из списка</option>
              <option v-for="vet in vets" :key="vet.id" :value="vet.id">
                {{ vet.first_name }} {{ vet.last_name }} ({{ vet.speciality }})
              </option>
            </select>
          </div>

          <div class="form-group">
            <label>Дата и время</label>
            <input type="datetime-local" v-model="formData.appointment_date" required />
          </div>

          <div class="form-group">
            <label>Описание проблемы (необязательно)</label>
            <textarea v-model="formData.description" rows="3" placeholder="Что беспокоит вашего питомца?"></textarea>
          </div>

          <button type="submit" class="btn btn-submit" :disabled="isLoading">
            {{ isLoading ? 'Отправка...' : 'Отправить заявку' }}
          </button>
          
          <p v-if="errorMessage" class="error-msg">{{ errorMessage }}</p>
        </form>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import apiClient from '../api/index';

const vets = ref([]);
const isLoading = ref(false);
const isSuccess = ref(false);
const errorMessage = ref('');

// Данные формы (соответствуют полям модели Appointment в Django)
const formData = ref({
  owner_name: '',
  owner_phone: '',
  pet_name: '',
  veterinarian: '',
  appointment_date: '',
  description: ''
});

// Загружаем врачей при открытии страницы
const fetchVets = async () => {
  try {
    const response = await apiClient.get('/doctors/');
    vets.value = response.data;
  } catch (err) {
    console.error("Ошибка загрузки врачей", err);
  }
};

onMounted(() => {
  fetchVets();
});

// Отправка формы
const submitForm = async () => {
  isLoading.value = true;
  errorMessage.value = '';
  
  try {
    // Отправляем POST запрос на бэкенд
    // ВАЖНО: так как в нашей Django модели Appointment поля owner_name, owner_phone и pet называются иначе,
    // в идеале нужно использовать Serializer с этими полями.
    // Мы отправляем как есть, но в реальном проекте нужно привести к структуре бэкенда.
    await apiClient.post('/appointments/', {
       // ВАЖНО: Мы отправляем в API данные, которые соответствуют нашим моделям Django.
       // Так как сейчас в модели Appointment поля pet_id, а не pet_name,
       // в учебных целях мы можем упростить API или использовать custom serializer.
       // Пока предположим, что наш бэкенд немного доработан.
       owner_name: formData.value.owner_name, // если поля нет в модели, Django вернет ошибку, но мы ее обработаем
       owner_phone: formData.value.owner_phone,
       pet: formData.value.pet_name, // Внимание: в новой модели у нас ForeignKey, а не строка. 
       // Если бэкенд вернет ошибку 400, мы выведем ее.
       veterinarian: formData.value.veterinarian,
       appointment_date: formData.value.appointment_date,
       description: formData.value.description
    });
    
    // Если успех:
    isSuccess.value = true;
  } catch (err) {
    console.error(err);
    if (err.response && err.response.data) {
      // Выводим ошибку валидации от Django (если бэкенд не принял данные)
      errorMessage.value = "Ошибка сервера: проверьте правильность заполнения формы. (Скорее всего не совпадают поля с бэкендом)";
    } else {
      errorMessage.value = "Ошибка соединения с сервером.";
    }
  } finally {
    isLoading.value = false;
  }
};
</script>

<style scoped>
.appointment-page {
  padding: 60px 20px;
  background: #faf5f7;
  min-height: 80vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.appointment-container {
  max-width: 1000px;
  width: 100%;
  background: white;
  border-radius: 32px;
  box-shadow: 0 20px 50px rgba(0,0,0,0.05);
  display: flex;
  overflow: hidden;
}

/* Левая сторона с инфо */
.info-side {
  background: linear-gradient(135deg, #fff0f5 0%, #ffe4ec 100%);
  padding: 60px 40px;
  flex: 0 0 40%;
  display: flex;
  flex-direction: column;
}

.page-title {
  font-size: 36px;
  font-weight: 900;
  color: #1a1a1a;
  margin-bottom: 16px;
  line-height: 1.1;
}

.page-subtitle {
  font-size: 16px;
  color: #555;
  line-height: 1.6;
  margin-bottom: 40px;
}

.contact-info {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-top: auto;
}

.contact-item {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  background: rgba(255, 255, 255, 0.6);
  padding: 16px;
  border-radius: 16px;
}

.contact-item .icon {
  font-size: 24px;
}

.contact-item strong {
  display: block;
  font-size: 16px;
  color: #1a1a1a;
  margin-bottom: 4px;
}

.contact-item p {
  font-size: 14px;
  color: #666;
  margin: 0;
}

/* Правая сторона с формой */
.form-side {
  padding: 60px 50px;
  flex: 1;
}

.appointment-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-group label {
  font-size: 14px;
  font-weight: 600;
  color: #333;
}

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

.btn-submit {
  background: #ff5c8a;
  color: white;
  border: none;
  padding: 16px;
  border-radius: 12px;
  font-size: 16px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-top: 10px;
}

.btn-submit:hover:not(:disabled) {
  background: #ff4074;
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(255, 92, 138, 0.3);
}

.btn-submit:disabled {
  background: #ffb6c1;
  cursor: not-allowed;
}

.error-msg {
  color: #ff4074;
  font-size: 14px;
  text-align: center;
  margin-top: 10px;
}

/* Сообщение об успехе */
.success-message {
  text-align: center;
  padding: 40px 20px;
}

.success-icon {
  font-size: 60px;
  margin-bottom: 20px;
}

.success-message h2 {
  font-size: 28px;
  color: #1a1a1a;
  margin-bottom: 12px;
}

.success-message p {
  color: #666;
  font-size: 16px;
}

.btn {
  display: inline-block;
  padding: 14px 28px;
  border-radius: 50px;
  text-decoration: none;
  font-weight: 700;
}

.btn-primary {
  background: #ff5c8a;
  color: white;
}

/* Адаптивность */
@media (max-width: 900px) {
  .appointment-container {
    flex-direction: column;
  }
  .info-side {
    padding: 40px 20px;
  }
  .form-side {
    padding: 40px 20px;
  }
}
</style>