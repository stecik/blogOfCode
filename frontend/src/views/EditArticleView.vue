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
import { useRoute, useRouter } from 'vue-router';
import PulseLoader from 'vue-spinner/src/PulseLoader.vue';

const toast = useToast();
const route = useRoute();
const router = useRouter();
const authStore = useAuthStore();

const articleForm = reactive({
    data: {
        title: '',
        content: '',
        categories: [],
        tags: [],
        authors: [],
    },
    isLoading: false,

});

const categories = ref([]);
const tagField = ref('');

const addTag = () => {
    if (tagField.value === '') {
        return
    };
    articleForm.data.tags.push(tagField.value);
    tagField.value = '';
};

const getCategories = async () => {
    const response = await customFetch('/api/blog/categories/', 'GET');
    categories.value = await response.json();
};

const getArticle = async () => {
    try {
        const respose = await customFetch(`/api/blog/articles/${route.params.id}/`, 'GET');
        const data = await respose.json();
        articleForm.data.title = data.title;
        articleForm.data.content = data.content;
        articleForm.data.categories = data.categories_display;
        articleForm.data.tags = data.tags_display;
        articleForm.data.authors = [authStore.userId];

    } catch (error) {
        console.error(error);
    }
};

const updateArticle = async () => {
    console.log(articleForm.data);
    try {
        const response = await customFetch(`/api/blog/articles/${route.params.id}/`, 'PATCH', articleForm.data);
        console.log(response.status);
        if (response.ok) {
            toast.success('Article updated successfully');
            router.push('/articles/my');
        } else {
            toast.error('Article update failed');
        }
    } catch (error) {
        console.error(error);
    }
};

const clearAllTags = () => {
    articleForm.data.tags = [];
};

onMounted(() => {
    getCategories();
    getArticle();
});

</script><template>
    <section>
        <div v-if="articleForm.isLoading">
            <PulseLoader color="#d97706" />
        </div>
        <div v-else class="container m-auto max-w-7xl py-24">
            <div class="bg-white px-6 py-8 mb-4 shadow-md rounded-md border m-4 md:m-0">
                <h2 class=" text-3xl text-center font-semibold mb-6 text-amber-600">editArticle</h2>
                <form class="mb-4" @submit.prevent="addTag">
                    <div class="my-4">
                        <label class="block text-gray-700 font-bold mb-2">tags</label>
                        <TagsList :tags="articleForm.data.tags" />
                    </div>
                    <InputField v-model="tagField" lbl="tagName" plchldr="tagName" :required="false" />
                    <span class="mr-2">
                        <ButtonSubmit title="addTag" />
                    </span>
                    <ButtonSubmit @click="clearAllTags" title="clearAllTags" color="bg-red-700"
                        hoverColor="bg-red-800" />
                </form>

                <form class="mb-4" @submit.prevent="updateArticle">
                    <SelectField v-model="articleForm.data.categories" lbl="category" :options="categories"
                        :multiple="true" />
                    <InputField v-model="articleForm.data.title" lbl="title" plchldr="noClickBait" />
                    <div class="card">
                        <Editor v-model="articleForm.data.content" editorStyle="height: 320px" />
                    </div>
                    <div class="mt-5">
                        <ButtonSubmit title="updateArticle" />
                    </div>
                </form>
            </div>
        </div>
    </section>
</template>