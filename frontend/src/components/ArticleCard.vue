<script setup>
import { defineProps, ref, computed } from 'vue';
import { formatDate } from '@/utils/formatDate';
import TagsList from './TagsList.vue';

const props = defineProps({
    article: Object,
});

const authorLabel = computed(() => {
    return props.article.authors_display.length > 1 ? "Authors" : "Author";
});

const truncContent = (content) => {
    return content.length > 200 ? content.substring(0, 100) + "..." : content;
}

</script>

<template>

    <div class="bg-white rounded-xl shadow-md relative">
        <div class="p-4">
            <div class="mb-6">
                <div class="text-gray-600 my-2 flex justify-between w-full">
                    <span>{{ formatDate(article.created_at) }}</span>
                    <span>{{ `lastUpdate: ${formatDate(article.updated_at)}` }}</span>
                </div>
                <div class="text-gray-600 my-2">
                    <strong>{{ `${authorLabel}: ` }}</strong>{{ `${article.authors_display.join(", ")}` }}
                </div>
                <div class="my-4">
                    <TagsList :tags="article.tags_display" />
                </div>

                <div class="my-4">
                    <span v-for="category in article.categories_display" class="text-gray-700 mr-2 text-xl">
                        {{ `${category} ` }}
                    </span>
                </div>
                <h3 class="text-3xl text-orange-600 font-bold">{{ article.title }}</h3>

            </div>

            <div class="mb-5">
                <div>{{ truncContent(article.content) }} </div>
            </div>

            <div class="border border-gray-100 mb-5"></div>

            <RouterLink :to="'/articles/' + article.id" class="h-[36px] bg-orange-500 hover:bg-orange-600 
                text-white px-4 py-2 rounded-lg text-center text-sm">
                fullArticle
            </RouterLink>
        </div>
    </div>

</template>