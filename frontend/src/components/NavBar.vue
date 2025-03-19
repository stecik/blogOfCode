<script setup>
import logo from "@/assets/icons/logo.png"
import { RouterLink, useRouter, useRoute } from "vue-router";
import { computed } from "vue";
import { APP_NAME } from "@/constants";

const router = useRouter();
const route = useRoute();

const isActiveLink = (routePath) => {
    return route.path === routePath;
}

const logout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    router.push('/login');
}

const isLoggedIn = () => {
    return localStorage.getItem('token') !== null;
}

const username = computed(() => {
    return localStorage.getItem('user');
})


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
                            <RouterLink to="/articles/add" :class="{ 'bg-amber-900': isActiveLink('/articles/add') }"
                                class="text-white hover:bg-amber-950 hover:text-white rounded-md px-3 py-2">addArticle
                            </RouterLink>
                        </div>
                    </div>
                    <div v-if="isLoggedIn()" class="md:ml-auto">
                        <div class="flex space-x-2">
                            <RouterLink :to="'/profile/'" :class="{ 'bg-amber-900': isActiveLink('/profile/') }"
                                class="text-white hover:bg-amber-950 hover:text-white rounded-md px-3 py-2">
                                {{ username }}
                            </RouterLink>

                            <button @click="logout()"
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