<script setup>
import { useRoute } from 'vue-router';
import { ref, reactive, onMounted, computed } from 'vue';
import PulseLoader from 'vue-spinner/src/PulseLoader.vue';

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

const formatDate = (datetime) => {
    const date = new Date(datetime);
    return date.toLocaleString();
}


onMounted(() => {
    getArticle();
});
</script>

<template>
    <div v-if="article.isLoading" class="flex justify-center items-center h-screen">
        <PulseLoader color="#d97706" />
    </div>
    <div v-else class="max-w-3xl mx-auto my-10 p-6 bg-white shadow-lg rounded-lg">
        <h1 class="text-3xl font-bold text-orange-600 mb-4">{{ article.data.title }}</h1>

        <div class="text-gray-600 text-sm">
            <p><strong>Authors:</strong> {{ article.data.authors_display.join(', ') }}</p>
            <p><strong>Created:</strong> {{ formatDate(article.data.created_at) }}</p>
            <p><strong>Last Updated:</strong> {{ formatDate(article.data.updated_at) }}</p>
        </div>

        <div class="mt-4 flex flex-wrap">
            <span v-for="tag in article.data.tags_display" :key="tag"
                class="bg-orange-300 text-orange-800 text-xs font-semibold mr-2 px-2.5 py-0.5 rounded">
                #{{ tag }}
            </span>
        </div>

        <div class="mt-4 text-gray-700">
            <p>{{ article.data.content }}</p>
        </div>

        <div class="mt-6">
            <button @click="$router.push('/')"
                class="bg-orange-500 hover:bg-orange-600 text-white font-bold py-2 px-4 rounded">
                Back to News
            </button>
        </div>
    </div>
</template>
