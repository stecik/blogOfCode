<script setup>
import ArticlesList from '@/components/ArticlesList.vue';
import { useAuthStore } from '@/stores/auth';

const authStore = useAuthStore();
</script>
<template>
    <div class="mt-10">
        <h2 class="text-3xl font-bold text-orange-600 mb-6 text-center">
            myArticles
        </h2>
    </div>
    <ArticlesList :fullArticleBtn="false" :editBtn="true" :delBtn="true" :filterByAuthorId="authStore.userId" />
</template>
