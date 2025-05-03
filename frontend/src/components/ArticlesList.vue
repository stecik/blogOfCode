<script setup>
import { ref, onMounted, reactive, defineProps } from 'vue';
import PulseLoader from 'vue-spinner/src/PulseLoader.vue';
import ArticleCard from "@/components/ArticleCard.vue";
import { customFetch } from '@/api';
import ButtonSubmit from './ButtonSubmit.vue';
import FilterBar from './FilterBar.vue';
import { watch } from 'vue';

const props = defineProps({
    editBtn: {
        type: Boolean,
        default: false
    },
    delBtn: {
        type: Boolean,
        default: false
    },
    fullArticleBtn: {
        type: Boolean,
        default: false
    },
    filterByAuthorId: {
        type: Number,
        default: null
    }

});

const articles = reactive({
    data: [],
    isLoading: false
});

const loadedArticles = ref([]);
const filteredArticles = ref([]);

const removeArticle = (id) => {
    loadedArticles.value = loadedArticles.value.filter(article => article.id !== id);
}

const getArticles = async () => {
    try {
        articles.isLoading = true;
        const url = props.filterByAuthorId ? `/api/blog/articles/?author=${props.filterByAuthorId}` : "/api/blog/articles/";
        const response = await customFetch(url, "GET");
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
    const data = filteredArticles.value.slice(start.value, end.value);
    start.value = end.value;
    end.value += increment;
    if (data.length > 0) {
        loadedArticles.value = [...loadedArticles.value, ...data];
    }
}

const filterArticles = () => {
    filteredArticles.value = filterCategory(articles.data)
}

const filterCategory = (articles) => {
    console.log(filterOptions.value.filterCategory);
    console.log(articles);
    if (filterOptions.value.filterCategory === 'all') {
        return articles;
    }
    return articles.filter(article => article.categories_display.includes(filterOptions.value.filterCategory));
}

const filterUpdated = ref(false);
const filterOptions = ref({
    orderBy: 'date',
    order: 'desc',
    filterCategory: 'all',
});

watch(filterUpdated, (newVal) => {
    if (newVal) {
        console.log(loadedArticles.value);
        filterUpdated.value = false
        filterArticles();
        start.value = 0;
        end.value = 3;
        loadedArticles.value = [];
        console.log(loadedArticles.value);
        loadMore();
        console.log(loadedArticles.value);
    }
})


onMounted(async () => {
    await getArticles();
    filterArticles();
    loadMore();
})


</script>


<template>
    <FilterBar v-model:filterOptions="filterOptions" v-model:updated="filterUpdated" />
    <section class="px-4 py-10">
        <div>{{ filterUpdated }}</div>
        <div class="container-xl lg:container m-auto">
            <div v-if="articles.isLoading" class="text-center text-gray-500 py-6">
                <PulseLoader color="#d97706" />
            </div>
            <div v-else class="grid grid-cols-1 md:grid-cols-1 gap-6">
                <ArticleCard v-for="article in loadedArticles" :key="article.id" :article="article"
                    :fullArticleBtn="fullArticleBtn" :editBtn="editBtn" :delBtn="delBtn" @deleted="removeArticle" />
            </div>
            <div class="flex justify-center my-7">
                <ButtonSubmit @click="loadMore()" title="loadMore" />
            </div>
        </div>
    </section>

</template>
