<script setup>
import { defineProps } from 'vue';

const props = defineProps({
    tags: Array,
});
</script>

<template>
    <span v-for="tag in props.tags">
        <button class="bg-orange-300 text-center text-orange-800 pl-2 pr-2 pt-0.5 pb-0.5 mr-2 font-semibold rounded">
            #{{ tag }}
        </button>
    </span>
</template>