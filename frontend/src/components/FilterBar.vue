<script setup>
import { ref, onMounted, reactive } from 'vue'
import ButtonSubmit from './ButtonSubmit.vue';
import SelectField from './SelectField.vue';
import { customFetch } from '@/api';

const categories = ref(["all"]);
const filter = reactive({
    orderBy: 'date',
    order: 'desc',
    filterCategory: 'all',
});

const getCategories = async () => {
    try {
        const response = await customFetch("/api/blog/categories/", "GET");
        const data = await response.json();
        categories.value.push(...data)
    } catch (error) {
        console.error('Error fetching categories:', error);
    }
}

const saveFilterOptions = () => {
    const filterOptions = {
        orderBy: filter.orderBy,
        order: filter.order,
        filterCategory: filter.filterCategory,
    };
    localStorage.setItem('filterOptions', JSON.stringify(filterOptions));
}

onMounted(() => {
    getCategories();
});


</script>

<template>
    <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
        <div>
            <SelectField v-model="filter.orderBy" lbl="orderBy" :options="['date', 'title', 'author']" />
        </div>

        <div>
            <SelectField v-model="filter.order" lbl="order" :options="['asc', 'desc']" />
        </div>

        <div>
            <SelectField v-model="filter.filterCategory" lbl="filterCategory" :options=categories />
        </div>

        <div class="mt-1.5">
            <ButtonSubmit title="filter" :on="saveFilterOptions" />
        </div>
    </div>
</template>
