import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import VetsView from '../views/VetsView.vue'
import AppointmentView from '../views/AppointmentView.vue'
import LoginView from '../views/LoginView.vue'
import ProfileView from '../views/ProfileView.vue'
import ServiceView from '../views/ServiceView.vue' // <-- Импортируем новую страницу

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'home', component: HomeView },
    { path: '/vets', name: 'vets', component: VetsView },
    { path: '/appointment', name: 'appointment', component: AppointmentView },
    { path: '/login', name: 'login', component: LoginView },
    { path: '/profile', name: 'profile', component: ProfileView },
    
    // Новый маршрут: страница конкретной услуги по ее ID
    { path: '/service/:id', name: 'service', component: ServiceView } 
  ]
})

export default router