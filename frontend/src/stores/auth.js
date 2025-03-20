import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useAuthStore = defineStore('auth', () => {
    const user = ref(localStorage.getItem('user') || null)
    const userId = ref(localStorage.getItem('userId') || null)
    const isAuthenticated = computed(() => !!user.value)
    const token = ref(localStorage.getItem('token') || null)

    function login(username, id, access_token) {
        user.value = username
        localStorage.setItem('user', username)
        userId.value = id
        localStorage.setItem('userId', id)
        token.value = access_token
        localStorage.setItem('token', access_token)
    }

    function logout() {
        user.value = null
        userId.value = null
        token.value = null
        localStorage.removeItem('user')
        localStorage.removeItem('token')
        localStorage.removeItem('userId')
    }

    return { user, userId, token, isAuthenticated, login, logout }
})
