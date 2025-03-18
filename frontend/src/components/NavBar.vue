<script setup>
import logo from "@/assets/icons/logo.png"
import { RouterLink, useRoute } from "vue-router";
import { APP_NAME } from "@/constants";

const isActiveLink = (routePath) => {
    return useRoute().path === routePath;
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
                            <RouterLink to="/articles/add" :class="{ 'bg-amber-900': isActiveLink('/articles/add') }"
                                class="text-white hover:bg-amber-950 hover:text-white rounded-md px-3 py-2">addArticle
                            </RouterLink>
                        </div>
                    </div>
                    <div class="md:ml-auto">
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