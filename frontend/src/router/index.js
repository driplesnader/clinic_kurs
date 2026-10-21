import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import VetsView from '../views/VetsView.vue'
import AppointmentView from '../views/AppointmentView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'home', component: HomeView },
    { path: '/vets', name: 'vets', component: VetsView },
    { path: '/appointment', name: 'appointment', component: AppointmentView }
  ]
})

export default router