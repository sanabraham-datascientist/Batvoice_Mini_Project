import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AudioDetailView from '../views/AudioDetail.vue'
import AudioUpdateView from '../views/AudioUpdate.vue'
import LoginView from '../views/Login.vue'
import SignUpView from '../views/SignUp.vue'
import AddAudio from '../views/AddAudio.vue'
import AdminView from '../views/Admin.vue'
const routes = [
  
  {
    path: '',
    name: 'home',
    component: HomeView
  },
  {
    path: '/admin',
    name: 'admin',
    component: AdminView
  },
   {
    path: '/api/audios/:id/',
    name: 'audiodetail',
    component: AudioDetailView
  },
  {
    path: '/api/audios/:id/update/',
    name: 'audioupdate',
    component: AudioUpdateView
  },
  {
    path: '/api/audios/add',
    name: 'add-audio',
    component: AddAudio
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
