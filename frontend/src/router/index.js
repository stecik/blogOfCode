import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import RegisterView from '@/views/RegisterView.vue'
import AddArticleView from '@/views/AddArticleView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import UserProfileView from '@/views/UserProfileView.vue'
import MyArticlesView from '@/views/MyArticlesView.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView,
        },
        {
            path: '/login',
            name: 'login',
            component: LoginView,
        },
        {
            path: '/register',
            name: 'register',
            component: RegisterView,
        },
        {
            path: '/articles/add',
            name: 'add',
            component: AddArticleView,
        },
        {
            path: '/profile',
            name: 'profile',
            component: UserProfileView,
        },
        {
            path: '/articles/my',
            name: 'my-articles',
            component: MyArticlesView,
        },
    ],
})

export default router
