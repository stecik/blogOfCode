<script setup>
import ArticleList from "@/components/ArticlesList.vue";
import FilterBar from "@/components/FilterBar.vue";

</script>
<template>
    <div class="mt-10">
        <h2 class="text-3xl font-bold text-orange-600 mb-6 text-center">
            news
        </h2>
    </div>
    <FilterBar />
    <ArticleList :fullArticleBtn="true" />
</template>