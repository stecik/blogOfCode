<script setup>
import logo from "@/assets/icons/logo.png"
import { RouterLink, useRouter, useRoute } from "vue-router";
import { computed, ref, reactive } from "vue";
import { APP_NAME } from "@/constants";
import { useAuthStore } from "@/stores/auth";
import { useToast } from "vue-toastification";
import { customFetch } from "@/api";

const router = useRouter();
const route = useRoute();
const toast = useToast();
const authStore = useAuthStore();

const addArticeRoute = computed(() => {
    return authStore.isAuthenticated ? '/articles/add' : '/login';
})

const isActiveLink = (routePath) => {
    return route.path === routePath;
}

const handleLogout = async () => {
    const request = new Request("/api/users/logout/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${authStore.token}`
        }
    })
    try {
        const response = await customFetch("/api/users/logout/", "POST");
        const data = await response.json();
        if (response.ok) {
            authStore.logout();
            toast.success(data.detail);
            router.push('/login');
        } else {
            toast.error(data.error);
            throw new Error("Error logging out");
        }
    } catch (error) {
        console.log(error);
    }
}

</script>

<template>
    <nav class="bg-amber-600 border-b border-amber-500">
        <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
            <div class="flex h-20 items-center justify-between">
                <div class="flex flex-1 items-center justify-center md:items-stretch md:justify-start">
                    <RouterLink to="/" class="flex flex-shrink-0 items-center mr-4">
                        <img class="h-10 w-auto" :src="logo" alt="logo" />
                        <span class="hidden md:block text-white text-2xl font-bold ml-2">{{ APP_NAME }}</span>
                    </RouterLink>
                    <div class="md:ml-auto">
                        <div class="flex space-x-2">
                            <RouterLink to="/" :class="{ 'bg-amber-900': isActiveLink('/') }"
                                class="text-white hover:bg-amber-950 hover:text-white rounded-md px-3 py-2">
                                news</RouterLink>
                            <RouterLink :to="addArticeRoute" :class="{ 'bg-amber-900': isActiveLink('/articles/add') }"
                                class="text-white hover:bg-amber-950 hover:text-white rounded-md px-3 py-2">addArticle
                            </RouterLink>
                            <RouterLink v-if="authStore.isAuthenticated" to="/articles/my"
                                :class="{ 'bg-amber-900': isActiveLink('/articles/my') }"
                                class="text-white hover:bg-amber-950 hover:text-white rounded-md px-3 py-2">
                                myArticles
                            </RouterLink>
                        </div>
                    </div>
                    <div v-if="authStore.isAuthenticated" class="md:ml-auto">
                        <div class="flex space-x-2">
                            <RouterLink :to="'/profile/'" :class="{ 'bg-amber-900': isActiveLink('/profile/') }"
                                class="text-white hover:bg-amber-950 hover:text-white rounded-md px-3 py-2">
                                {{ authStore.user }}
                            </RouterLink>

                            <button @click="handleLogout()"
                                class="text-white hover:bg-amber-950 hover:text-white rounded-md px-3 py-2">
                                logout
                            </button>
                        </div>
                    </div>
                    <div v-else class=" md:ml-auto">
                        <div class="flex space-x-2">
                            <RouterLink to="/login" :class="{ 'bg-amber-900': isActiveLink('/login') }"
                                class="text-white hover:bg-amber-950 hover:text-white rounded-md px-3 py-2">
                                login</RouterLink>
                            <RouterLink to="/register" :class="{ 'bg-amber-900': isActiveLink('/register') }"
                                class="text-white hover:bg-amber-950 hover:text-white rounded-md px-3 py-2">
                                createAccount
                            </RouterLink>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </nav>

</template>