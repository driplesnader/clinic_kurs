<template>
  <div class="app-wrapper">
    <header class="site-header">
      <div class="container header-inner">
        <router-link to="/" class="brand-link">
          <div class="brand-logo">🐾</div>
          <div class="brand-text">
            <div class="brand-title">Добрый хвост</div>
            <div class="brand-sub">Ветеринарная клиника</div>
          </div>
        </router-link>
<nav class="main-nav">
  <router-link to="/">Главная</router-link>
  <router-link to="/vets">Врачи</router-link>
  
  <!-- Выпадающее меню для услуг -->
  <div class="dropdown">
    <span class="dropdown-toggle">Услуги ▼</span>
    <div class="dropdown-menu">
      <router-link to="/appointment">Терапия</router-link>
      <router-link to="/appointment">Хирургия</router-link>
      <router-link to="/appointment">Стерилизация</router-link>
      <router-link to="/appointment">Кастрация</router-link>
    </div>
  </div>

  <router-link to="/appointment">Записаться</router-link>
</nav>

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
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(15px);
  -webkit-backdrop-filter: blur(15px);
  border-bottom: 1px solid rgba(0, 0, 0, 0.05);
  position: sticky;
  top: 0;
  z-index: 50;
  transition: all 0.3s ease;
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

.brand-logo {
  font-size: 30px;
}

.brand-title {
  font-weight: 800;
  font-size: 18px;
}

.brand-sub {
  font-size: 12px;
  color: #6b7280;
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

.main-nav a:hover {
  background: #fff0f5;
  color: #ff5c8a;
}

.main-nav a.router-link-active {
  background: #ff5c8a;
  color: white;
  box-shadow: 0 4px 15px rgba(255, 92, 138, 0.3);
}

.site-footer {
  margin-top: 50px;
  padding: 30px 0;
  text-align: center;
  border-top: 1px solid rgba(0, 0, 0, 0.04);
  color: #6b7280;
}
/* Стили для выпадающего меню в шапке */
.dropdown {
  position: relative;
  display: inline-block;
  margin-left: 10px;
}

.dropdown-toggle {
  cursor: pointer;
  font-weight: 600;
  color: #444;
  padding: 10px 18px;
  border-radius: 50px;
  transition: all 0.3s ease;
  display: inline-block;
}

.dropdown-toggle:hover {
  background: #fff0f5;
  color: #ff5c8a;
}

.dropdown-menu {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  background: white;
  min-width: 180px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
  border-radius: 16px;
  padding: 10px 0;
  z-index: 100;
  flex-direction: column;
}

.dropdown:hover .dropdown-menu {
  display: flex;
}

.dropdown-menu a {
  padding: 10px 20px;
  color: #444;
  text-decoration: none;
  font-size: 15px;
  transition: background 0.2s;
}

.dropdown-menu a:hover {
  background: #fff0f5;
  color: #ff5c8a;
}
</style>