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
            Здоровье вашего питомца — <br />
            <span class="gradient-text">наша главная забота</span>
          </h1>
          <p class="hero-subtitle fade-in-up delay-2">
            Современная ветеринарная клиника с опытными специалистами, новейшим оборудованием и искренней любовью к животным.
          </p>
          <div class="hero-actions fade-in-up delay-3">
            <router-link to="/appointment" class="btn btn-primary">
              Записаться на приём
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M5 12h14M12 5l7 7-7 7"/>
              </svg>
            </router-link>
            <router-link to="/vets" class="btn btn-secondary">
              Наши специалисты
            </router-link>
          </div>
          
          <div class="trust-indicators fade-in-up delay-4">
            <div class="avatars">
              <div class="avatar" style="background: #ffe4ec; display: flex; align-items: center; justify-content: center; font-size: 20px;">🐱</div>
              <div class="avatar" style="background: #e0f7fa; display: flex; align-items: center; justify-content: center; font-size: 20px;">🐶</div>
              <div class="avatar" style="background: #f8f0ff; display: flex; align-items: center; justify-content: center; font-size: 20px;">🐰</div>
              <div class="avatar plus">+2k</div>
            </div>
            <p>Нам доверяют более 2000 владельцев</p>
          </div>
        </div>

        <div class="hero-visual fade-in-up delay-2">
          <div class="image-wrapper">
            <div class="floating-card card-1">
              <span class="icon">🩺</span>
              <div>
                <strong>Опытные врачи</strong>
                <small>Стаж от 5 лет</small>
              </div>
            </div>
            
            <div class="floating-card card-2">
              <span class="icon">❤️</span>
              <div>
                <strong>Забота 24/7</strong>
                <small>Всегда на связи</small>
              </div>
            </div>
            
            <!-- ВРЕМЕННАЯ ЗАГЛУШКА ВМЕСТО ФОТО -->
            <div class="image-placeholder">
              <span class="placeholder-emoji">🐶</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- СЕКЦИЯ УСЛУГ -->
    <section class="services-section">
      <div class="section-header">
        <h2 class="section-title">Наши услуги</h2>
        <p class="section-subtitle">Полный спектр ветеринарной помощи для ваших любимцев</p>
      </div>

      <div class="services-grid">
        <!-- Карточка 1 -->
        <div class="service-card">
          <div class="service-img-placeholder bg-1">
            <span>💉</span>
          </div>
          <div class="service-content">
            <h3>Терапия</h3>
            <p>Консультации, диагностика и лечение острых и хронических заболеваний.</p>
            <router-link to="/appointment" class="service-link">Записаться →</router-link>
          </div>
        </div>

        <!-- Карточка 2 -->
        <div class="service-card">
          <div class="service-img-placeholder bg-2">
            <span>🔪</span>
          </div>
          <div class="service-content">
            <h3>Хирургия</h3>
            <p>Плановые и экстренные операции на современном оборудовании.</p>
            <router-link to="/appointment" class="service-link">Записаться →</router-link>
          </div>
        </div>

        <!-- Карточка 3 -->
        <div class="service-card">
          <div class="service-img-placeholder bg-3">
            <span>💊</span>
          </div>
          <div class="service-content">
            <h3>Стерилизация</h3>
            <p>Безопасная и современная стерилизация с полным уходом после операции.</p>
            <router-link to="/appointment" class="service-link">Записаться →</router-link>
          </div>
        </div>

        <!-- Карточка 4 -->
        <div class="service-card">
          <div class="service-img-placeholder bg-4">
            <span>🩹</span>
          </div>
          <div class="service-content">
            <h3>Кастрация</h3>
            <p>Современная и безопасная операция, требующая тщательного ухода.</p>
            <router-link to="/appointment" class="service-link">Записаться →</router-link>
          </div>
        </div>
      </div>
    </section>

    <!-- СЕКЦИЯ ПРЕИМУЩЕСТВ -->
    <section class="features-section">
      <div class="features-grid">
        <div class="feature-card">
          <div class="feature-icon-wrap bg-pink">
            <span class="feature-icon">⚡</span>
          </div>
          <h3>Быстрая помощь</h3>
          <p>Принимаем без очередей. Онлайн-запись занимает всего 1 минуту.</p>
        </div>
        
        <div class="feature-card">
          <div class="feature-icon-wrap bg-blue">
            <span class="feature-icon">🔬</span>
          </div>
          <h3>Современная диагностика</h3>
          <p>УЗИ, рентген, экспресс-анализы — всё для точной постановки диагноза.</p>
        </div>
        
        <div class="feature-card">
          <div class="feature-icon-wrap bg-purple">
            <span class="feature-icon">💎</span>
          </div>
          <h3>Комфорт и забота</h3>
          <p>Уютные кабинеты без стресса для животных и внимательный персонал.</p>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
/* Базовые настройки */
.home-page { 
  width: 100%; 
  overflow: hidden; 
}

/* --- HERO SECTION --- */
.hero-section {
  position: relative; 
  padding: 80px 20px 100px;
  background: #faf5f7; 
  overflow: hidden;
}

.hero-background {
  position: absolute; 
  top: 0; 
  left: 0; 
  width: 100%; 
  height: 100%;
  overflow: hidden; 
  z-index: 0;
}

.glow-circle {
  position: absolute; 
  border-radius: 50%; 
  filter: blur(80px); 
  opacity: 0.6;
}

.circle-1 {
  width: 500px; 
  height: 500px; 
  background: #ffd1dc;
  top: -100px; 
  right: -100px; 
  animation: pulse 10s infinite alternate;
}

.circle-2 {
  width: 400px; 
  height: 400px; 
  background: #e6e6fa;
  bottom: -50px; 
  left: -100px; 
  animation: pulse 8s infinite alternate-reverse;
}

@keyframes pulse {
  0% { transform: scale(1); }
  100% { transform: scale(1.2); }
}

.hero-container {
  max-width: 1200px; 
  margin: 0 auto; 
  display: flex;
  align-items: center; 
  justify-content: space-between;
  gap: 60px; 
  position: relative; 
  z-index: 1;
}

.hero-content { 
  flex: 1; 
  max-width: 600px; 
}

.badge {
  display: inline-block; 
  padding: 8px 16px; 
  background: white;
  border-radius: 50px; 
  font-size: 14px; 
  font-weight: 600; 
  color: #ff5c8a;
  box-shadow: 0 4px 15px rgba(255, 92, 138, 0.15); 
  margin-bottom: 24px;
}

.hero-title {
  font-size: 56px; 
  line-height: 1.1; 
  font-weight: 900;
  color: #1a1a1a; 
  margin-bottom: 24px; 
  letter-spacing: -1.5px;
}

.gradient-text {
  background: linear-gradient(135deg, #ff5c8a 0%, #ff8fa3 100%);
  -webkit-background-clip: text; 
  -webkit-text-fill-color: transparent; 
  background-clip: text;
}

.hero-subtitle { 
  font-size: 18px; 
  line-height: 1.7; 
  color: #555; 
  margin-bottom: 40px; 
}

.hero-actions { 
  display: flex; 
  gap: 16px; 
  margin-bottom: 48px; 
}

.btn {
  padding: 16px 32px; 
  border-radius: 50px; 
  font-size: 16px;
  font-weight: 700; 
  text-decoration: none; 
  transition: all 0.3s ease;
  display: inline-flex; 
  align-items: center; 
  gap: 10px;
}

.btn-primary {
  background: #ff5c8a; 
  color: white;
  box-shadow: 0 10px 25px rgba(255, 92, 138, 0.4);
}

.btn-primary:hover { 
  background: #ff4074; 
  transform: translateY(-3px); 
  box-shadow: 0 15px 35px rgba(255, 92, 138, 0.5); 
}

.btn-secondary { 
  background: white; 
  color: #1a1a1a; 
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05); 
}

.btn-secondary:hover { 
  transform: translateY(-3px); 
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1); 
}

.trust-indicators { 
  display: flex; 
  align-items: center; 
  gap: 16px; 
}

.avatars { 
  display: flex; 
}

.avatar {
  width: 48px; 
  height: 48px; 
  border-radius: 50%; 
  border: 3px solid white;
  background-size: cover; 
  background-position: center; 
  margin-left: -12px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}

.avatar:first-child { 
  margin-left: 0; 
}

.avatar.plus {
  background: #ff5c8a; 
  color: white; 
  display: flex; 
  align-items: center;
  justify-content: center; 
  font-weight: 700; 
  font-size: 14px;
}

.trust-indicators p { 
  font-size: 14px; 
  color: #666; 
  font-weight: 500; 
}

/* Визуальная часть (Заглушка) */
.hero-visual { 
  flex: 1; 
  position: relative; 
  display: flex; 
  justify-content: center; 
}

.image-wrapper { 
  position: relative; 
  width: 100%; 
  max-width: 500px; 
  padding-right: 30px; /* Отступ, чтобы карточка не срезалась */
}

.image-placeholder {
  width: 100%; 
  height: 450px;
  background: linear-gradient(135deg, #ffe4ec 0%, #ffcce0 100%);
  border-radius: 30px; 
  display: flex; 
  align-items: center; 
  justify-content: center;
  box-shadow: 0 30px 40px rgba(255, 92, 138, 0.2);
  position: relative; 
  z-index: 2;
  animation: float 6s ease-in-out infinite;
}

.placeholder-emoji { 
  font-size: 150px; 
}

@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-20px); }
}

.floating-card {
  position: absolute; 
  background: rgba(255, 255, 255, 0.9); 
  backdrop-filter: blur(10px);
  padding: 16px 24px; 
  border-radius: 20px; 
  box-shadow: 0 15px 35px rgba(0,0,0,0.08);
  display: flex; 
  align-items: center; 
  gap: 14px; 
  z-index: 3;
  border: 1px solid rgba(255,255,255,0.6);
}

.floating-card .icon { 
  font-size: 24px; 
}

.floating-card strong { 
  display: block; 
  font-size: 15px; 
  color: #1a1a1a; 
}

.floating-card small { 
  font-size: 13px; 
  color: #888; 
}

.card-1 { 
  top: 10%; 
  left: -10%; 
  animation: float-card 5s ease-in-out infinite; 
}

.card-2 { 
  bottom: 10%; 
  right: 0%; 
  animation: float-card 5s ease-in-out infinite reverse; 
}

@keyframes float-card {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-15px); }
}

/* --- SERVICES SECTION --- */
.services-section { 
  padding: 100px 20px; 
  max-width: 1200px; 
  margin: 0 auto; 
}

.section-header { 
  text-align: center; 
  margin-bottom: 60px; 
}

.section-title { 
  font-size: 40px; 
  font-weight: 800; 
  color: #1a1a1a; 
  margin-bottom: 16px; 
  letter-spacing: -1px; 
}

.section-subtitle { 
  font-size: 18px; 
  color: #666; 
}

.services-grid { 
  display: grid; 
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); 
  gap: 30px; 
}

.service-card {
  background: white; 
  border-radius: 24px; 
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0,0,0,0.04); 
  transition: all 0.4s ease;
  display: flex; 
  flex-direction: column; 
  border: 1px solid #f0f0f0;
}

.service-card:hover { 
  transform: translateY(-10px); 
  box-shadow: 0 20px 40px rgba(255, 92, 138, 0.15); 
}

/* Красивые градиентные заглушки для услуг */
.service-img-placeholder {
  height: 200px; 
  display: flex; 
  align-items: center; 
  justify-content: center;
  font-size: 60px; 
  transition: transform 0.5s ease;
}

.service-card:hover .service-img-placeholder { 
  transform: scale(1.1); 
}

.bg-1 { background: linear-gradient(135deg, #e0f7fa 0%, #b2ebf2 100%); }
.bg-2 { background: linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%); }
.bg-3 { background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); }
.bg-4 { background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); }

.service-content { 
  padding: 24px; 
  display: flex; 
  flex-direction: column; 
  flex-grow: 1; 
}

.service-content h3 { 
  font-size: 22px; 
  font-weight: 800; 
  color: #1a1a1a; 
  margin-bottom: 12px; 
}

.service-content p { 
  color: #666; 
  font-size: 15px; 
  line-height: 1.6; 
  margin-bottom: 20px; 
  flex-grow: 1; 
}

.service-link { 
  color: #ff5c8a; 
  font-weight: 700; 
  text-decoration: none; 
  font-size: 15px; 
  transition: color 0.3s ease; 
}

.service-link:hover { 
  color: #ff4074; 
}

/* --- FEATURES SECTION --- */
.features-section {
  padding: 80px 20px; 
  max-width: 1200px; 
  margin: 0 auto;
  background: #fffafb; 
  border-radius: 40px; 
  margin-bottom: 80px;
}

.features-grid { 
  display: grid; 
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); 
  gap: 30px; 
}

.feature-card {
  background: white; 
  padding: 40px 30px; 
  border-radius: 30px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.03); 
  transition: all 0.4s ease; 
  border: 1px solid #f0f0f0;
}

.feature-card:hover { 
  transform: translateY(-10px); 
  box-shadow: 0 20px 50px rgba(255, 92, 138, 0.15); 
  border-color: #ffd1dc; 
}

.feature-icon-wrap {
  width: 70px; 
  height: 70px; 
  border-radius: 20px;
  display: flex; 
  align-items: center; 
  justify-content: center;
  margin-bottom: 24px; 
  font-size: 32px;
}

.bg-pink { background: #fff0f5; }
.bg-blue { background: #f0f8ff; }
.bg-purple { background: #f8f0ff; }

.feature-card h3 { 
  font-size: 22px; 
  font-weight: 700; 
  color: #1a1a1a; 
  margin-bottom: 12px; 
}

.feature-card p { 
  color: #666; 
  line-height: 1.6; 
  font-size: 15px; 
}

/* Анимации */
.fade-in-up { 
  opacity: 0; 
  animation: fadeInUp 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards; 
}

.delay-1 { animation-delay: 0.1s; }
.delay-2 { animation-delay: 0.2s; }
.delay-3 { animation-delay: 0.3s; }
.delay-4 { animation-delay: 0.4s; }

@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Адаптивность */
@media (max-width: 1024px) {
  .hero-title { font-size: 44px; }
  .card-1 { left: 0; }
  .card-2 { right: 0; }
}

@media (max-width: 768px) {
  .hero-container { flex-direction: column; text-align: center; }
  .hero-content { max-width: 100%; }
  .hero-title { font-size: 36px; }
  .hero-actions { justify-content: center; flex-direction: column; }
  .trust-indicators { justify-content: center; }
  .hero-visual { display: none; }
  .services-grid { grid-template-columns: 1fr; }
}
</style>