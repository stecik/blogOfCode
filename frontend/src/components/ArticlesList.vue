<script setup>
import { ref, onMounted, reactive, defineProps } from 'vue';
import PulseLoader from 'vue-spinner/src/PulseLoader.vue';
import ArticleCard from "@/components/ArticleCard.vue";
import { customFetch } from '@/api';
import ButtonSubmit from './ButtonSubmit.vue';

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

const filterOptions = reactive(localStorage.getItem('filterOptions') ? JSON.parse(localStorage.getItem('filterOptions')) : {
    orderBy: 'date',
    order: 'desc',
    filterCategory: 'all',
});

const loadedArticles = ref([]);

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
