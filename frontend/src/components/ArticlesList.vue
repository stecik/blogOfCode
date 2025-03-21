<script setup>
import { ref, onMounted, reactive } from 'vue';
import PulseLoader from 'vue-spinner/src/PulseLoader.vue';
import ArticleCard from "@/components/ArticleCard.vue";
import { customFetch } from '@/api';

const articles = reactive({
    data: [],
    isLoading: false
});

const loadedArticles = ref([]);

const getArticles = async () => {
    try {
        articles.isLoading = true;
        const response = await customFetch("/api/blog/articles/", "GET");
        const data = await response.json();
        articles.data = data;
        articles.isLoading = false;
    }
    catch (error) {
        console.log(error);
    }
    finally {
        articles.isLoading = false;
    }
}

const start = ref(0);
const end = ref(3);

const loadMore = (increment = 3) => {
    const data = articles.data.slice(start.value, end.value);
    start.value = end.value;
    end.value += increment;
    if (data.length > 0) {
        loadedArticles.value = [...loadedArticles.value, ...data];
    }
}


onMounted(async () => {
    await getArticles();
    loadMore();
})
</script>


<template>


    <section class="px-4 py-10">
        <div class="container-xl lg:container m-auto">
            <h2 class="text-3xl font-bold text-orange-600 mb-6 text-center">
                News
            </h2>
            <div v-if="articles.isLoading" class="text-center text-gray-500 py-6">
                <PulseLoader color="#d97706" />
            </div>
            <div v-else class="grid grid-cols-1 md:grid-cols-1 gap-6">
                <ArticleCard v-for="article in loadedArticles" :key="article.id" :article="article" />
            </div>
            <div class="flex justify-center my-3">
                <button @click="loadMore()"
                    class="bg-orange-500 hover:bg-orange-600 hover:cursor-pointer  text-white px-4 py-2 mt-4 rounded-md">
                    loadMore
                </button>
            </div>
        </div>
    </section>

</template>
