<script setup>
import ArticlesList from '@/components/ArticlesList.vue';
import { useAuthStore } from '@/stores/auth';

const authStore = useAuthStore();
</script>
<template>
    <ArticlesList :fullArticleBtn="false" :editBtn="true" :delBtn="true" :filterByAuthorId="authStore.userId" />
</template>