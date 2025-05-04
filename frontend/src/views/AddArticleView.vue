<script setup>
import { ref, onMounted, reactive } from 'vue';
import { useAuthStore } from '@/stores/auth';
import TagsList from '@/components/TagsList.vue';
import CoAuthorsList from '@/components/CoAuthorsList.vue';
import ButtonSubmit from '@/components/ButtonSubmit.vue';
import InputField from '@/components/InputField.vue';
import SelectField from '@/components/SelectField.vue';
import Editor from 'primevue/editor';
import { useToast } from 'vue-toastification';
import { customFetch } from '@/api';
import { useRouter } from 'vue-router';
import { watch } from 'vue';


const authStore = useAuthStore();
const toast = useToast();
const router = useRouter();

const articleForm = reactive({
    title: '',
    content: '',
    categories: [],
    tags: [],
    authors: [authStore.userId],
});

const categories = ref([]);
const tagField = ref('');
const coAuthorField = ref('');
const coAuthors = ref([]);

const addTag = () => {
    if (tagField.value === '') {
        return
    };
    if (articleForm.tags.includes(tagField.value)) {
        toast.error('This tag already exists');
        return;
    } else if (tagField.value.length < 3) {
        toast.error('Tag must be at least 3 characters long');
        return;
    } else if (tagField.value.length > 20) {
        toast.error('Tag must be less than 20 characters long');
        return;
    }
    articleForm.tags.push(tagField.value);
    tagField.value = '';
};

const getCategories = async () => {
    const response = await customFetch('/api/blog/categories/', 'GET');
    categories.value = await response.json();
};

const addArticle = async () => {
    try {
        for (const coAuthor of coAuthors.value) {
            const userId = await usernameToId(coAuthor);
            if (userId !== null) {
                articleForm.authors.push(userId);
            }
        }
        const response = await customFetch('/api/blog/articles/', 'POST', articleForm);
        if (response.ok) {
            toast.success('Article created successfully');
            articleForm.title = '';
            articleForm.content = '';
            articleForm.categories = [];
            articleForm.tags = [];
            articleForm.authors = [authStore.userId];
            router.push('/articles/my');
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

const clearCoAuthors = () => {
    coAuthors.value = [];
};

const addCoAuthor = async () => {
    if (coAuthorField.value === '') {
        return
    };
    if (coAuthorField.value === authStore.user) {
        toast.error('You cannot add yourself as a co-author');
        return;
    } else if (coAuthors.value.includes(coAuthorField.value)) {
        toast.error('This user is already a co-author');
        return;
    } else if (!hints.value.includes(coAuthorField.value)) {
        toast.error('This user does not exist');
        return;
    }
    coAuthors.value.push(coAuthorField.value);
    coAuthorField.value = '';
};

const usernameToId = async (username) => {
    try {
        const response = await customFetch('/api/users/user-to-id/', 'POST', { "username": username });
        const data = await response.json();
        if (!response.ok) {
            toast.error('User not found');
            return null;
        }
        return data.id;
    } catch (error) {
        console.error('Error fetching user ID:', error);
        return null;
    }
};

const hints = ref([]);

const getHints = async () => {
    try {
        const response = await customFetch('/api/users/hint/', 'POST', { "prefix": coAuthorField.value });
        const data = await response.json();
        hints.value = data;
    } catch (error) {
        console.error('Error fetching usernames:', error);
        hints.value = [];
    }
};

watch(coAuthorField, () => {
    if (coAuthorField.value.length < 1) {
        hints.value = [];
        return;
    }
    setTimeout(() => {
        if (coAuthorField.value.length < 1) {
            hints.value = [];
            return;
        }
        getHints();
    }, 500);
});

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
                    <ButtonSubmit @click="clearAllTags" title="clearAllTags" color="bg-red-700" hoverColor="bg-red-800"
                        type="button" />
                </form>

                <form class="mb-4" @submit.prevent="addCoAuthor">
                    <CoAuthorsList :co-authors="coAuthors" />
                    <InputField v-model="coAuthorField" lbl="co-authors" plchldr="username" :required="false"
                        :hints="hints" />
                    <span class="mr-2">
                        <ButtonSubmit title="addCoAuthor" />
                    </span>
                    <ButtonSubmit @click="clearCoAuthors" title="clearCoAuthors" color="bg-red-700"
                        hoverColor="bg-red-800" type="button" />
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
