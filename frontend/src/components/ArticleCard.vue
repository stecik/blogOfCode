<script setup>
import { defineProps, ref, computed, defineEmits } from 'vue';
import { formatDate } from '@/utils/formatDate';
import TagsList from './TagsList.vue';
import ButtonPrimary from './ButtonPrimary.vue';
import ButtonSubmit from './ButtonSubmit.vue';
import { useToast } from 'vue-toastification';
import { customFetch } from '@/api';
import { useRouter } from 'vue-router';

const toast = useToast();
const router = useRouter();

const props = defineProps({
    article: {
        type: Object,
        default: () => ({})
    },
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
});

const authorLabel = computed(() => {
    return props.article.authors_display.length > 1 ? "Authors" : "Author";
});

const truncContent = (content) => {
    return content.length > 200 ? content.substring(0, 100) + "..." : content;
}

const isDeleting = ref(false);

const deleteArticle = async () => {
    try {
        if (isDeleting.value) return;
        isDeleting.value = true;
        if (!confirm('Are you sure you want to delete this article?')) return;
        const response = await customFetch(`/api/blog/articles/${props.article.id}/`, 'DELETE');
        if (response.ok) {
            toast.success('Article deleted successfully');
            emit('deleted', props.article.id);
        } else {
            toast.error('Failed to delete article');
        }
    } catch (error) {
        console.error(error);
        toast.error('Failed to delete article');
    } finally {
        isDeleting.value = false;
    }
}

const editArticle = async () => {
    router.push(`/articles/${props.article.id}/edit`);
}

const emit = defineEmits(['deleted']);

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
                <div v-html="truncContent(article.content)"></div>
            </div>

            <div class="border border-gray-100 mb-5"></div>
            <span>
                <span v-if="fullArticleBtn" class="mr-2">
                    <ButtonPrimary :link="'/articles/' + article.id" title="fullArticle" />
                </span>
                <span v-if="editBtn" class="mr-2">
                    <ButtonSubmit @click="editArticle" title="edit" />
                </span>
                <span v-if="delBtn" class="mr-2">
                    <ButtonSubmit @click="deleteArticle" title="delete" color="bg-red-700" hoverColor="bg-red-800" />
                </span>
            </span>
        </div>
    </div>

</template>