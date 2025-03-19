import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useAuthStore = defineStore('auth', () => {
    const user = ref(localStorage.getItem('user') || null)
    const isAuthenticated = computed(() => !!user.value)
    const token = ref(localStorage.getItem('token') || null)

    function login(username, access_token) {
        user.value = username
        localStorage.setItem('user', username)
        token.value = access_token
        localStorage.setItem('token', access_token)
    }

    function logout() {
        user.value = null
        token.value = null
        localStorage.removeItem('user')
        localStorage.removeItem('token')
    }

    return { user, token, isAuthenticated, login, logout }
})
