import { useAuthStore } from '@/stores/auth'

export const customFetch = async (url, method = 'GET', body = null, headers = {}) => {
    const authStore = useAuthStore()

    const createRequest = (url, customMethod, customBody, customHeaders) => {
        const headers = new Headers({
            'Content-Type': 'application/json',
            ...customHeaders,
        })
        const token = authStore.token
        if (token) {
            headers.set('Authorization', `Bearer ${token}`)
        }
        const options = {
            method: customMethod,
            headers,
            credentials: 'include',
            ...(body ? { body: JSON.stringify(customBody) } : {}),
        }
        return new Request(url, options)
    }

    try {
        const response = await fetch(createRequest(url, method, body, headers))
        if (response.ok) {
            return response
        }
        if (response.status === 401) {
            await authStore.refreshLogin()
            return await fetch(createRequest(url, method, body, headers))
        }
        return response
    } catch (error) {
        console.log(error)
    }
}
