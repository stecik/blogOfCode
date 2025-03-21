import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useAuthStore = defineStore('auth', () => {
    const user = ref(localStorage.getItem('user') || null)
    const userId = ref(localStorage.getItem('userId') || null)
    const isAuthenticated = computed(() => !!user.value)
    const token = ref(localStorage.getItem('token') || null)
    const refreshToken = ref(localStorage.getItem('refreshToken') || null)

    async function refreshLogin() {
        try {
            const request = new Request('/api/users/token/refresh/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ refresh: refreshToken.value }),
            })
            const response = await fetch(request)
            const data = await response.json()
            if (response.ok) {
                login(user.value, userId.value, data.access, data.refresh)
            }
        } catch (error) {
            console.log(error)
        }
    }

    function login(username, id, accessToken, renewToken) {
        user.value = username
        localStorage.setItem('user', username)
        userId.value = id
        localStorage.setItem('userId', id)
        token.value = accessToken
        localStorage.setItem('token', accessToken)
        refreshToken.value = renewToken
        localStorage.setItem('refreshToken', renewToken)
    }

    function logout() {
        user.value = null
        userId.value = null
        token.value = null
        refreshToken.value = null
        localStorage.removeItem('user')
        localStorage.removeItem('token')
        localStorage.removeItem('userId')
        localStorage.removeItem('refreshToken')
    }

    return {
        user,
        userId,
        token,
        refreshToken,
        isAuthenticated,
        login,
        logout,
        refreshLogin,
    }
})
