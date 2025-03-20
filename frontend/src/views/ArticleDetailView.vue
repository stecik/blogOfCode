<script setup>
import { useRoute } from 'vue-router';
import { ref, reactive, onMounted, computed } from 'vue';
import PulseLoader from 'vue-spinner/src/PulseLoader.vue';
import { formatDate } from '@/utils/formatDate';
import TagsList from '@/components/TagsList.vue';
import ButtonPrimary from '@/components/ButtonPrimary.vue';

const route = useRoute();
const articleId = ref(route.params.id);
const article = reactive({
    data: {},
    isLoading: true,
});

const getArticle = async () => {
    article.isLoading = true;
    try {
        article.isLoading = true;
        const response = await fetch(`/api/blog/articles/${articleId.value}/`);
        const data = await response.json();
        article.data = data;
    } catch (error) {
        console.error(error);
    }
    finally {
        article.isLoading = false;
    }
}

const authorLabel = computed(() => {
    return article.data.authors_display.length > 1 ? "Authors" : "Author";
});

onMounted(() => {
    getArticle();
});
</script>

<template>
    <div v-if="article.isLoading" class="flex justify-center items-center h-screen">
        <PulseLoader color="#d97706" />
    </div>
    <div v-else class="max-w-7xl mx-auto my-10 p-6 bg-white shadow-lg rounded-lg">
        <h1 class="text-3xl font-bold text-orange-600 mb-4">{{ article.data.title }}</h1>

        <div class="text-gray-600 text-sm">
            <p class="my-2"><strong>{{ authorLabel }}:</strong> {{ article.data.authors_display.join(', ') }}</p>
            <p class="my-2"><strong>Created:</strong> {{ formatDate(article.data.created_at) }}</p>
            <p class="my-2"><strong>Last Updated:</strong> {{ formatDate(article.data.updated_at) }}</p>
        </div>
        <div class="mt-4 flex flex-wrap">
            <TagsList :tags="article.data.tags_display" />
        </div>
        <hr class="border border-gray-100 my-6">
        <div class="mt-4 text-gray-700">
            <div v-html="article.data.content"></div>
        </div>

        <div class="mt-6">
            <ButtonPrimary link="/" />
        </div>
    </div>
</template>
