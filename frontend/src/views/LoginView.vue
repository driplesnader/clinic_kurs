<template>
  <div class="login-page">
    <div class="login-box">
      <h2>Вход в личный кабинет</h2>
      <form @submit.prevent="handleLogin">
        <div class="form-group">
          <label>Логин</label>
          <input type="text" v-model="username" required />
        </div>
        <div class="form-group">
          <label>Пароль</label>
          <input type="password" v-model="password" required />
        </div>
        <button type="submit" class="btn-submit">Войти</button>
        <p v-if="error" class="error">{{ error }}</p>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import apiClient from '../api/index';

const username = ref('');
const password = ref('');
const error = ref('');
const router = useRouter();

const handleLogin = async () => {
  try {
    const response = await apiClient.post('/token/', {
      username: username.value,
      password: password.value
    });
    // Сохраняем токен в localStorage (чтобы не выходить при обновлении страницы)
    localStorage.setItem('access_token', response.data.access);
    localStorage.setItem('refresh_token', response.data.refresh);
    // Перенаправляем в личный кабинет
    router.push('/profile');
  } catch (err) {
    error.value = 'Неверный логин или пароль';
  }
};
</script>

<style scoped>
.login-page { display: flex; justify-content: center; align-items: center; min-height: 60vh; }
.login-box { background: white; padding: 40px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); width: 100%; max-width: 400px; }
.login-box h2 { text-align: center; margin-bottom: 30px; }
.form-group { margin-bottom: 20px; display: flex; flex-direction: column; gap: 8px; }
.form-group input { padding: 12px; border: 1px solid #ddd; border-radius: 10px; font-size: 16px; }
.btn-submit { width: 100%; padding: 14px; background: #ff5c8a; color: white; border: none; border-radius: 10px; font-size: 16px; font-weight: 700; cursor: pointer; }
.error { color: red; text-align: center; margin-top: 10px; }
</style>