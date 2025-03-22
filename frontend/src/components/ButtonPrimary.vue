<script setup>
import { defineProps } from 'vue';

const props = defineProps({
    link: String,
    title: String
});

</script>

<template>
    <RouterLink :to="link"
        class="bg-orange-500 hover:bg-orange-600 text-white font-bold py-2 px-4 rounded hover:cursor-pointer">
        {{ title }}
    </RouterLink>
</template>