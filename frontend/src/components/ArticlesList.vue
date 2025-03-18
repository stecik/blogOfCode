<script setup>
import { ref, onMounted, reactive } from 'vue';
import PulseLoader from 'vue-spinner/src/PulseLoader.vue';
import ArticleCard from "@/components/ArticleCard.vue";

const articles = reactive({
    data: [],
    isLoading: false
});

const getArticles = async () => {
    articles.isLoading = true;
    const response = await fetch("/api/blog/articles/");
    const data = await response.json();
    console.log(data);
    articles.data = data;
    articles.isLoading = false;
}


onMounted(async () => {
    getArticles();
})
</script>


<template>


    <section class="px-4 py-10">
        <div class="container-xl lg:container m-auto">
            <h2 class="text-3xl font-bold text-amber-500 mb-6 text-center">
                News
            </h2>
            <div v-if="articles.isLoading" class="text-center text-gray-500 py-6">
                <PulseLoader color="#d97706" />
            </div>
            <div v-else class="grid grid-cols-1 md:grid-cols-1 gap-6">
                <ArticleCard v-for="article in articles.data" :key="article.id" :article="article" />
            </div>
            <button class="bg-amber-500 text-white px-4 py-2 mt-4 rounded-md">loadMore</button>

        </div>
    </section>

</template>
