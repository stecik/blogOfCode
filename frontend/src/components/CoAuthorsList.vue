<script setup>
import { defineProps } from 'vue';

const props = defineProps({
    coAuthors: Array,
});
</script>

<template>
    <span v-for="author in props.coAuthors" :key="author">
        <button
            class="bg-orange-300 text-center text-orange-800 pl-2 pr-2 pt-0.5 pb-0.5 mr-2 mb-2 font-semibold rounded">
            {{ author }}
        </button>
    </span>
</template>
