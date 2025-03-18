<script setup>
import { defineProps, ref, computed } from 'vue';
const props = defineProps({
    article: Object,
});

const author_label = computed(() => {
    return props.article.authors_display.length > 1 ? "Authors" : "Author";
});

const truncContent = (content) => {
    return content.length > 200 ? content.substring(0, 100) + "..." : content;
}

const formatDateTime = (datetime) => {
    const date = new Date(datetime);
    return date.toLocaleString();
}

</script>

<template>

    <div class="bg-white rounded-xl shadow-md relative">
        <div class="p-4">
            <div class="mb-6">
                <div class="text-gray-600 my-2 flex justify-between w-full">
                    <span>{{ formatDateTime(article.created_at) }}</span>
                    <span>{{ `lastUpdate: ${formatDateTime(article.updated_at)}` }}</span>
                </div>
                <div class="text-gray-600 my-2">{{ `${author_label}: ${article.authors_display.join(", ")}` }}</div>
                <div class="my-4">
                    <span v-for="tag in article.tags_display">
                        <button class="bg-amber-600 text-center text-white rounded-3xl pl-2 pr-2 pt-0.5 pb-0.5 mr-2">
                            {{ `#${tag}` }}
                        </button>
                    </span>
                </div>

                <div class="my-4">
                    <span v-for="category in article.categories_display" class="text-gray-700 mr-2 text-xl">
                        {{ `${category} ` }}
                    </span>
                </div>
                <h3 class="text-3xl text-amber-500 font-bold">{{ article.title }}</h3>

            </div>

            <div class="mb-5">
                <div>{{ truncContent(article.content) }} </div>
            </div>

            <div class="border border-gray-100 mb-5"></div>

            <RouterLink :to="'/articles/' + article.id" class="h-[36px] bg-amber-600 hover:bg-amber-950 text-white px-4 py-2 rounded-lg text-center
                    text-sm">fullArticle</RouterLink>
        </div>
    </div>

</template>