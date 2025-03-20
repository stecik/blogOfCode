<script setup>
import { defineProps, defineEmits } from 'vue';

const props = defineProps({
    title: String,
    color: {
        type: String,
        default: "bg-orange-500"
    },
    hoverColor: {
        type: String,
        default: "bg-orange-600"
    }
});

const emit = defineEmits();

</script>

<template>
    <button type="submit" :class="[color, hoverColor]" class=" hover:cursor-pointer text-white 
    font-bold py-2 px-4 rounded w-full focus:outline-none focus:shadow-outline" @click="emit('click')">
        {{ title }}
    </button>
</template>