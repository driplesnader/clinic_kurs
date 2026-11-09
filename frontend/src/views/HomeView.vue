<template>
  <div class="home-page">
    
    <!-- HERO SECTION -->
    <section class="hero-section">
      <div class="hero-background">
        <div class="glow-circle circle-1"></div>
        <div class="glow-circle circle-2"></div>
      </div>
      
      <div class="hero-container">
        <div class="hero-content">
          <div class="badge fade-in-up">✨ Лучшая клиника в Сургуте</div>
          <h1 class="hero-title fade-in-up delay-1">
            Заботимся о питомцах <br />
            <span class="gradient-text">с любовью и профессионализмом</span>
          </h1>
          <p class="hero-subtitle fade-in-up delay-2">
            Современная ветеринарная клиника с опытными специалистами, новейшим оборудованием и искренней любовью к животным.
          </p>
          <div class="hero-actions fade-in-up delay-3">
            <router-link to="/appointment" class="btn btn-primary">
              Записаться на приём
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </router-link>
            <router-link to="/vets" class="btn btn-secondary">
              Наши специалисты
            </router-link>
          </div>
          
          <div class="trust-indicators fade-in-up delay-4">
            <div class="avatars">
              <img src="/user1.jpg" alt="Клиент 1" class="avatar-img" />
              <img src="/user2.jpg" alt="Клиент 2" class="avatar-img" />
              <img src="/user3.jpg" alt="Клиент 3" class="avatar-img" />
              <div class="avatar plus">+2k</div>
            </div>
            <p>Нам доверяют более 2000 владельцев</p>
          </div>
        </div>

        <div class="hero-visual fade-in-up delay-2">
          <div class="image-wrapper">
            <!-- Карточка 1 -->
            <div class="floating-card card-1">
              <span class="icon">🩺</span>
              <div><strong>Опытные врачи</strong><small>Стаж от 5 лет</small></div>
            </div>
            <!-- Карточка 2 -->
            <div class="floating-card card-2">
              <span class="icon">❤️</span>
              <div><strong>Забота 24/7</strong><small>Всегда на связи</small></div>
            </div>
            <img src="/hero1.png" alt="Питомец" class="hero-image" />
          </div>
        </div>
      </div>
    </section>

    <!-- СЕКЦИЯ УСЛУГ -->
    <section class="services-section container">
      <div class="section-header">
        <h2 class="section-title">Основные направления клиники</h2>
        <p class="section-subtitle">Мы предлагаем полный спектр ветеринарных услуг для ваших любимцев</p>
      </div>

      <div v-if="loadingServices" class="loading-text">Загрузка услуг...</div>
      
      <div v-else class="services-grid">
        <router-link 
          v-for="service in services" 
          :key="service.id" 
          :to="{ path: `/service/${service.id}`, query: { img: getServiceImage(service.title) } }" 
          class="service-card"
        >
          <div class="service-image-wrap">
            <img :src="getServiceImage(service.title)" alt="Услуга" class="service-img" />
          </div>
          <div class="service-content">
            <h3>{{ service.title }}</h3>
            <p class="service-price">{{ service.price }} ₽</p>
            <span class="service-more">Подробнее →</span>
          </div>
        </router-link>
      </div>
    </section>

    <!-- БЛОК О КОМПАНИИ -->
    <section class="about-section">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">О компании</h2>
          <p class="section-subtitle">
            Мы — команда профессионалов, которые искренне любят животных. 
            Наша цель — сделать так, чтобы каждый питомец был здоров, а его хозяин — спокоен.
          </p>
        </div>
        
        <div class="team-image-container">
          <img src="/team.png" alt="Наша команда" class="team-img" />
        </div>
      </div>
    </section>

    <!-- СЕКЦИЯ ВРАЧЕЙ -->
    <section class="vets-preview-section container">
      <div class="section-header">
        <h2 class="section-title">Наши ветеринарные врачи</h2>
        <p class="section-subtitle">Квалифицированные специалисты, готовые помочь вашему питомцу</p>
      </div>

      <div v-if="loadingVets" class="loading-text">Загрузка врачей...</div>

      <div v-else class="vets-preview-grid">
        <div v-for="(vet, index) in vets.slice(0, 3)" :key="vet.id" class="vet-preview-card">
          <div class="vet-photo-wrapper">
            <img :src="`/doctor${(index % 3) + 1}.jpg`" alt="Врач" class="vet-photo" />
          </div>
          <div class="vet-info">
            <h3>{{ vet.first_name }} {{ vet.last_name }}</h3>
            <p class="speciality">{{ vet.speciality }}</p>
            <p class="description">{{ vet.description || 'Опытный специалист нашей клиники.' }}</p>
            <router-link to="/vets" class="btn btn-outline-small">Подробнее</router-link>
          </div>
        </div>
      </div>

      <div class="all-vets-btn">
        <router-link to="/vets" class="btn btn-secondary">Все специалисты</router-link>
      </div>
    </section>

    <!-- СЕКЦИЯ ПРЕИМУЩЕСТВ -->
    <section class="features-section">
      <div class="container features-container">
        <div class="features-text">
          <h2 class="section-title">Владельцы доверяют нам</h2>
          
          <div class="feature-item">
            <div class="feature-icon">⚡</div>
            <div><h4>Быстрая помощь</h4><p>Принимаем без очередей и долгих ожиданий.</p></div>
          </div>
          <div class="feature-item">
            <div class="feature-icon">🔬</div>
            <div><h4>Современное оборудование</h4><p>УЗИ, рентген и экспресс-анализы.</p></div>
          </div>
          <div class="feature-item">
            <div class="feature-icon">💎</div>
            <div><h4>Комфорт и забота</h4><p>Уютные кабинеты и внимательный персонал.</p></div>
          </div>
        </div>
        
        <div class="features-image">
           <img src="/feature-dog.png" alt="Довольный питомец" class="feature-img" />
        </div>
      </div>
    </section>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import apiClient from '../api/index';

const services = ref([]);
const vets = ref([]);
const loadingServices = ref(true);
const loadingVets = ref(true);

const getServiceImage = (title) => {
  const t = title.toLowerCase();
  if (t.includes('осмотр') || t.includes('консультация') || t.includes('терапевт')) return '/srv1.jpg';
  if (t.includes('вакцинация') || t.includes('прививка')) return '/srv2.jpg';
  if (t.includes('стерилизация')) return '/srv3.jpg';
  if (t.includes('кастрация')) return '/srv4.jpg';
  if (t.includes('узи') || t.includes('диагностика')) return '/srv5.jpg';
  if (t.includes('стрижка') || t.includes('когти') || t.includes('уши')) return '/srv6.jpg';
  return '/srv1.jpg';
};

const fetchServices = async () => {
  try {
    const res = await apiClient.get('/services/');
    services.value = res.data;
  } catch (error) {
    console.error("Ошибка загрузки услуг:", error);
  } finally {
    loadingServices.value = false;
  }
};

const fetchVets = async () => {
  try {
    const res = await apiClient.get('/doctors/');
    vets.value = res.data;
  } catch (error) {
    console.error("Ошибка загрузки врачей:", error);
  } finally {
    loadingVets.value = false;
  }
};

onMounted(() => {
  fetchServices();
  fetchVets();
});
</script>

<style scoped>
/* --- Общие стили --- */
.home-page { width: 100%; overflow: hidden; background: #fbf7f9; }
.container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }
.section-header { text-align: center; margin-bottom: 50px; margin-top: 80px; }
.section-title { font-size: 36px; font-weight: 900; color: #1a1a1a; margin-bottom: 15px; }
.section-subtitle { font-size: 18px; color: #666; max-width: 700px; margin: 0 auto; line-height: 1.6; }

/* --- HERO SECTION --- */
.hero-section { position: relative; padding: 60px 20px 100px; background: #faf5f7; overflow: hidden; }
.hero-background { position: absolute; top: 0; left: 0; width: 100%; height: 100%; overflow: hidden; z-index: 0; }
.glow-circle { position: absolute; border-radius: 50%; filter: blur(80px); opacity: 0.6; }
.circle-1 { width: 500px; height: 500px; background: #ffd1dc; top: -100px; right: -100px; animation: pulse 10s infinite alternate; }
.circle-2 { width: 400px; height: 400px; background: #e6e6fa; bottom: -50px; left: -100px; animation: pulse 8s infinite alternate-reverse; }
@keyframes pulse { 0% { transform: scale(1); } 100% { transform: scale(1.2); } }

.hero-container { max-width: 1200px; margin: 0 auto; display: flex; align-items: center; justify-content: space-between; gap: 40px; position: relative; z-index: 1; }
.hero-content { flex: 1; max-width: 550px; z-index: 2; }
.badge { display: inline-block; padding: 8px 16px; background: white; border-radius: 50px; font-size: 14px; font-weight: 600; color: #ff5c8a; box-shadow: 0 4px 15px rgba(255, 92, 138, 0.15); margin-bottom: 24px; }
.hero-title { font-size: 56px; line-height: 1.1; font-weight: 900; color: #1a1a1a; margin-bottom: 24px; letter-spacing: -1.5px; }
.gradient-text { background: linear-gradient(135deg, #ff5c8a 0%, #ff8fa3 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
.hero-subtitle { font-size: 18px; line-height: 1.7; color: #555; margin-bottom: 40px; }
.hero-actions { display: flex; gap: 16px; margin-bottom: 48px; }

.btn { padding: 16px 32px; border-radius: 50px; font-size: 16px; font-weight: 700; text-decoration: none; transition: all 0.3s ease; display: inline-flex; align-items: center; gap: 10px; }
.btn-primary { background: #ff5c8a; color: white; box-shadow: 0 10px 25px rgba(255, 92, 138, 0.4); }
.btn-primary:hover { background: #ff4074; transform: translateY(-3px); box-shadow: 0 15px 35px rgba(255, 92, 138, 0.5); }
.btn-secondary { background: white; color: #1a1a1a; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05); }
.btn-secondary:hover { transform: translateY(-3px); box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1); }

.trust-indicators { display: flex; align-items: center; gap: 16px; }
.avatars { display: flex; align-items: center; }
.avatar-img { width: 48px; height: 48px; border-radius: 50%; border: 3px solid white; object-fit: cover; margin-left: -12px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); background: #eee; }
.avatar-img:first-child { margin-left: 0; }
.avatar.plus { background: #ff5c8a; color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 14px; width: 48px; height: 48px; border-radius: 50%; border: 3px solid white; margin-left: -12px; z-index: 2; position: relative; }
.trust-indicators p { font-size: 14px; color: #666; font-weight: 500; }

.hero-visual { flex: 1.2; position: relative; display: flex; justify-content: flex-end; }
.image-wrapper { position: relative; width: 100%; max-width: 650px; padding-right: 0; display: flex; justify-content: flex-end; }
.hero-image { 
  width: 130%; max-width: 750px; height: auto; object-fit: contain; 
  position: relative; z-index: 1; animation: float 6s ease-in-out infinite; 
  filter: drop-shadow(0 30px 40px rgba(0,0,0,0.15)); margin-right: -50px; 
}
@keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-20px); } }

/* --- ИЗМЕНЕННЫЕ КАРТОЧКИ --- */
.floating-card { 
  position: absolute; 
  background: rgba(255, 255, 255, 0.4); /* Полупрозрачный фон */
  backdrop-filter: blur(12px); /* Размытие заднего фона (эффект стекла) */
  -webkit-backdrop-filter: blur(12px);
  padding: 16px 24px; 
  border-radius: 20px; 
  box-shadow: 0 10px 30px rgba(0,0,0,0.05); /* Мягкая тень */
  display: flex; 
  align-items: center; 
  gap: 14px; 
  z-index: 3; 
  border: 1px solid rgba(255, 255, 255, 0.6); /* Белая рамка для блика */
}

.floating-card .icon { font-size: 24px; }
.floating-card strong { display: block; font-size: 15px; color: #1a1a1a; }
.floating-card small { font-size: 13px; color: #555; }

/* Левая карточка - опускаем ниже */
.card-1 { 
  top: 25%; /* Было 15%, стало 25% (ниже) */
  left: 0; 
  animation: float-card 5s ease-in-out infinite; 
}

/* Правая карточка - оставляем как было */
.card-2 { 
  bottom: 15%; 
  right: 10%; 
  animation: float-card 5s ease-in-out infinite reverse; 
}

@keyframes float-card { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-15px); } }

/* --- SERVICES SECTION --- */
.services-section { padding-bottom: 80px; }
.services-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 30px; }
.service-card { background: white; border-radius: 24px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.04); transition: all 0.4s ease; text-decoration: none; color: inherit; border: 1px solid #f0f0f0; display: flex; flex-direction: column; }
.service-card:hover { transform: translateY(-10px); box-shadow: 0 20px 40px rgba(255, 92, 138, 0.15); border-color: #ffd1dc; }
.service-image-wrap { height: 180px; overflow: hidden; }
.service-img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s; }
.service-card:hover .service-img { transform: scale(1.1); }
.service-content { padding: 24px; text-align: center; display: flex; flex-direction: column; flex-grow: 1; }
.service-content h3 { font-size: 18px; font-weight: 800; color: #1a1a1a; margin-bottom: 10px; flex-grow: 1; }
.service-price { font-size: 22px; font-weight: 900; color: #ff5c8a; margin-bottom: 15px; }
.service-more { display: block; font-size: 14px; font-weight: 700; color: #888; transition: color 0.3s; }
.service-card:hover .service-more { color: #ff5c8a; }

/* --- ABOUT SECTION --- */
.about-section { background: white; padding: 80px 0; margin: 40px 0; }
.team-image-container { width: 100%; max-width: 900px; margin: 0 auto; background: transparent; box-shadow: none; }
.team-img { width: 100%; height: auto; display: block; object-fit: contain; mix-blend-mode: multiply; filter: drop-shadow(0px 15px 30px rgba(0, 0, 0, 0.1)); }

/* --- VETS PREVIEW SECTION --- */
.vets-preview-section { padding: 80px 0; }
.vets-preview-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin-bottom: 40px; }
.vet-preview-card { background: white; border-radius: 24px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.04); border: 1px solid #f0f0f0; transition: transform 0.3s; }
.vet-preview-card:hover { transform: translateY(-5px); }
.vet-photo-wrapper { height: 300px; overflow: hidden; background: #faf5f7; }
.vet-photo { width: 100%; height: 100%; object-fit: cover; }
.vet-info { padding: 24px; text-align: center; }
.vet-info h3 { font-size: 22px; font-weight: 800; margin-bottom: 5px; }
.vet-info .speciality { color: #ff5c8a; font-weight: 600; font-size: 15px; margin-bottom: 15px; }
.vet-info .description { color: #666; font-size: 14px; line-height: 1.5; margin-bottom: 20px; }
.btn-outline-small { padding: 10px 24px; border-radius: 50px; text-decoration: none; font-size: 14px; font-weight: 700; color: #ff5c8a; border: 1px solid #ff5c8a; transition: all 0.3s; }
.btn-outline-small:hover { background: #ff5c8a; color: white; }
.all-vets-btn { text-align: center; }

/* --- FEATURES SECTION --- */
.features-section { background: #fffafb; padding: 100px 0; }
.features-container { display: flex; align-items: center; gap: 60px; }
.features-text { flex: 1; }
.features-text .section-title { text-align: left; margin-bottom: 40px; }
.feature-item { display: flex; align-items: flex-start; gap: 20px; margin-bottom: 30px; }
.feature-icon { width: 60px; height: 60px; background: white; border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 28px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); flex-shrink: 0; }
.feature-item h4 { font-size: 18px; font-weight: 700; margin-bottom: 5px; }
.feature-item p { color: #666; font-size: 15px; line-height: 1.5; margin: 0; }
.features-image { flex: 1; display: flex; justify-content: center; align-items: center; }
.feature-img { width: 100%; max-width: 500px; height: auto; background: transparent; border-radius: 0; filter: drop-shadow(0px 20px 40px rgba(255, 92, 138, 0.3)); display: block; }

/* Анимации */
.fade-in-up { opacity: 0; animation: fadeInUp 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards; }
.delay-1 { animation-delay: 0.1s; } .delay-2 { animation-delay: 0.2s; } .delay-3 { animation-delay: 0.3s; } .delay-4 { animation-delay: 0.4s; }
@keyframes fadeInUp { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }

/* Адаптивность */
@media (max-width: 1024px) {
  .hero-image { width: 100%; margin-right: 0; }
  .hero-visual { justify-content: center; }
  .card-1 { left: -5%; }
}

@media (max-width: 900px) {
  .hero-container { flex-direction: column; text-align: center; }
  .hero-actions { justify-content: center; flex-direction: column; }
  .trust-indicators { justify-content: center; }
  .hero-visual { display: none; }
  .features-container { flex-direction: column; }
  .features-text .section-title { text-align: center; }
}
</style>