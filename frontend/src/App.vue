<template>
  <div class="app-wrapper">
    <header class="site-header">
      <div class="container header-inner">
        <router-link to="/" class="brand-link">
          <img src="/logo.png" alt="Логотип" class="brand-logo-img" />
          <div class="brand-text">
            <div class="brand-title">Добрый хвост</div>
            <div class="brand-sub">Ветеринарная клиника</div>
          </div>
        </router-link>

        <!-- Кнопка бургер для мобильных -->
        <button class="burger" @click="isMobileMenuOpen = !isMobileMenuOpen">
          <span></span>
          <span></span>
          <span></span>
        </button>
        
        <!-- Меню (добавлен класс mobile для открытия) -->
        <nav class="main-nav" :class="{ 'mobile-open': isMobileMenuOpen }">
          <router-link to="/" @click="isMobileMenuOpen = false">Главная</router-link>
          <router-link to="/vets" @click="isMobileMenuOpen = false">Врачи</router-link>
          
          <div class="dropdown">
            <span class="dropdown-toggle">Услуги ▼</span>
            <div class="dropdown-menu">
              <router-link 
                v-for="service in servicesMenu" 
                :key="service.id" 
                :to="`/service/${service.id}`"
                @click="isMobileMenuOpen = false"
              >
                {{ service.title }}
              </router-link>
            </div>
          </div>

          <router-link to="/appointment" @click="isMobileMenuOpen = false">Записаться</router-link>
          <router-link to="/profile" @click="isMobileMenuOpen = false">Личный кабинет</router-link>
          <router-link to="/login" class="login-btn" @click="isMobileMenuOpen = false">Вход</router-link>
        </nav>
      </div>
    </header>

    <main class="container" style="margin-top: 40px; min-height: 60vh;">
      <router-view />
    </main>

    <footer class="site-footer">
      <div class="container">
        <p>© 2026 «Добрый хвост». Все права защищены.</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import apiClient from './api/index';

const servicesMenu = ref([]);
const isMobileMenuOpen = ref(false); // Состояние для мобильного меню

onMounted(async () => {
  try {
    const response = await apiClient.get('/services/');
    servicesMenu.value = response.data; 
  } catch (error) {
    console.error("Ошибка загрузки меню услуг", error);
  }
});
</script>

<style>
body {
  margin: 0;
  font-family: Inter, "Segoe UI", Arial, sans-serif;
  background: #fbf7f9;
  color: #111;
}

.container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 20px;
}

.site-header {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(15px);
  border-bottom: 1px solid rgba(0, 0, 0, 0.05);
  position: sticky;
  top: 0;
  z-index: 50;
}

.header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 15px 0;
}

.brand-link {
  display: flex;
  gap: 12px;
  align-items: center;
  text-decoration: none;
  color: inherit;
}

.brand-logo-img { width: 45px; height: 45px; object-fit: contain; }
.brand-title { font-weight: 800; font-size: 18px; }
.brand-sub { font-size: 12px; color: #6b7280; }

.main-nav {
  display: flex;
  align-items: center;
}

.main-nav a {
  margin-left: 10px;
  text-decoration: none;
  color: #444;
  font-weight: 600;
  padding: 10px 18px;
  border-radius: 50px;
  transition: all 0.3s ease;
}

.main-nav a:hover { background: #fff0f5; color: #ff5c8a; }
.main-nav a.router-link-active { background: #ff5c8a; color: white; box-shadow: 0 4px 15px rgba(255, 92, 138, 0.3); }

.dropdown { position: relative; display: inline-block; margin-left: 10px; }
.dropdown-toggle { cursor: pointer; font-weight: 600; color: #444; padding: 10px 18px; border-radius: 50px; transition: all 0.3s ease; display: inline-block; }
.dropdown-toggle:hover { background: #fff0f5; color: #ff5c8a; }

.dropdown-menu {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  background: white;
  min-width: 280px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
  border-radius: 16px;
  padding: 10px 0;
  z-index: 100;
  flex-direction: column;
}

.dropdown:hover .dropdown-menu { display: flex; }

.dropdown-menu a {
  padding: 12px 20px;
  color: #444;
  text-decoration: none;
  font-size: 14px;
  margin-left: 0;
  border-radius: 0;
  white-space: normal;
  line-height: 1.4;
}

.dropdown-menu a:hover { background: #fff0f5; color: #ff5c8a; }

.login-btn { background: #ff5c8a !important; color: white !important; box-shadow: 0 4px 10px rgba(255, 92, 138, 0.3); }
.site-footer { margin-top: 50px; padding: 30px 0; text-align: center; border-top: 1px solid rgba(0, 0, 0, 0.04); color: #6b7280; }

/* --- АДАПТАЦИЯ (Мобильные устройства) --- */
.burger {
  display: none;
  flex-direction: column;
  gap: 5px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 5px;
}

.burger span {
  display: block;
  width: 25px;
  height: 3px;
  background: #ff5c8a;
  border-radius: 3px;
  transition: 0.3s;
}

@media (max-width: 900px) {
  .burger { display: flex; }
  
  .main-nav {
    position: fixed;
    top: 70px;
    left: -100%;
    width: 100%;
    height: calc(100vh - 70px);
    background: white;
    flex-direction: column;
    align-items: center;
    padding-top: 30px;
    transition: left 0.3s ease;
    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    overflow-y: auto;
  }

  .main-nav.mobile-open { left: 0; }

  .main-nav a, .dropdown, .dropdown-toggle {
    margin: 10px 0;
    font-size: 18px;
    width: 90%;
    text-align: center;
  }

  .dropdown { display: flex; flex-direction: column; align-items: center; }
  .dropdown-menu { position: static; box-shadow: none; min-width: 100%; align-items: center; }
}
</style>