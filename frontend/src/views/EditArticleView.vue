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
import { useRoute } from 'vue-router';
import PulseLoader from 'vue-spinner/src/PulseLoader.vue';

const toast = useToast();
const route = useRoute();

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
// TODO: bind to articleForm.data - need to be mapped to ids
const categoriesMap = ref({});
const selectedCategories = ref();

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
    const data = await response.json();
    categoriesMap.value = Object.fromEntries(
        data.map((category) => [category.name, category.id])
    );
    categories.value = Object.keys(categoriesMap.value);
};

const getArticle = async () => {
    try {
        const respose = await customFetch(`/api/blog/articles/${route.params.id}/`, 'GET');
        const data = await respose.json();
        articleForm.data.title = data.title;
        articleForm.data.content = data.content;
        articleForm.data.categories = data.categories;
        articleForm.data.tags = data.tags;
        articleForm.data.authors = data.authors;
    } catch (error) {
        console.error(error);
    }

};

const addArticle = async () => {
    // for (const category of selectedCategories.value) {
    //     articleForm.categories.push(categoriesMap.value[category]);
    // }
    // try {
    //     const response = await customFetch('/api/blog/articles/', 'POST', articleForm);
    //     if (response.ok) {
    //         toast.success('Article created successfully');
    //         articleForm.title = '';
    //         articleForm.content = '';
    //         articleForm.categories = [];
    //         articleForm.tags = [];
    //     } else {
    //         toast.error('Article creation failed');
    //     }
    // } catch (error) {
    //     console.error(error);
    // }
};

const clearAllTags = () => {
    articleForm.tags = [];
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
                    <ButtonSubmit title="addTag" />
                </form>
                <ButtonSubmit @click="clearAllTags" title="clearAllTags" color="bg-red-700" hoverColor="bg-red-800" />
                <form class="mb-4" @submit.prevent="addArticle">
                    <SelectField v-model="selectedCategories" lbl="category" :options="categories" :multiple="true" />
                    <InputField v-model="articleForm.data.title" lbl="title" plchldr="noClickBait" />
                    <div class="card">
                        <Editor v-model="articleForm.data.content" editorStyle="height: 320px" />
                    </div>
                    <ButtonSubmit title="createArticle" />
                </form>
            </div>
        </div>
    </section>
</template>