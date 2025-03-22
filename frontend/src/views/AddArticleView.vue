<script setup>
import { ref, onMounted, reactive } from 'vue';
import { useAuthStore } from '@/stores/auth';
import TagsList from '@/components/TagsList.vue';
import ButtonSubmit from '@/components/ButtonSubmit.vue';
import InputField from '@/components/InputField.vue';
import SelectField from '@/components/SelectField.vue';
import Editor from 'primevue/editor';
import { useToast } from 'vue-toastification';
import { customFetch } from '@/api';

const authStore = useAuthStore();
const toast = useToast();

const articleForm = reactive({
    title: '',
    content: '',
    categories: [],
    tags: [],
    authors: [authStore.userId],
});

const categories = ref([]);
const tagField = ref('');

const addTag = () => {
    if (tagField.value === '') {
        return
    };
    articleForm.tags.push(tagField.value);
    tagField.value = '';
};

const getCategories = async () => {
    const response = await customFetch('/api/blog/categories/', 'GET');
    categories.value = await response.json();
};

const addArticle = async () => {
    try {
        const response = await customFetch('/api/blog/articles/', 'POST', articleForm);
        if (response.ok) {
            toast.success('Article created successfully');
            articleForm.title = '';
            articleForm.content = '';
            articleForm.categories = [];
            articleForm.tags = [];
        } else {
            toast.error('Article creation failed');
        }
    } catch (error) {
        console.error(error);
    }
};

const clearAllTags = () => {
    articleForm.tags = [];
};

onMounted(() => {
    getCategories();
});

</script>
<template>

    <section>
        <div class="container m-auto max-w-7xl py-24">
            <div class="bg-white px-6 py-8 mb-4 shadow-md rounded-md border m-4 md:m-0">
                <h2 class=" text-3xl text-center font-semibold mb-6 text-amber-600">createNewArticle</h2>
                <form class="mb-4" @submit.prevent="addTag">
                    <div class="my-4">
                        <label class="block text-gray-700 font-bold mb-2">tags</label>
                        <TagsList :tags="articleForm.tags" />
                    </div>
                    <InputField v-model="tagField" lbl="tagName" plchldr="tagName" :required="false" />
                    <span class="mr-2">
                        <ButtonSubmit title="addTag" />
                    </span>
                    <ButtonSubmit @click="clearAllTags" title="clearAllTags" color="bg-red-700"
                        hoverColor="bg-red-800" />
                </form>

                <form class="mb-4" @submit.prevent="addArticle">
                    <SelectField v-model="articleForm.categories" lbl="category" :options="categories"
                        :multiple="true" />
                    <InputField v-model="articleForm.title" lbl="title" plchldr="noClickBait" />
                    <div class="card">
                        <Editor v-model="articleForm.content" editorStyle="height: 320px" />
                    </div>
                    <div class="mt-5">
                        <ButtonSubmit title="createArticle" />
                    </div>
                </form>
            </div>
        </div>
    </section>
</template>