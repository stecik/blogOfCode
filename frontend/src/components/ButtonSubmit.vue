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
    },
    width: {
        type: String,
        default: ""
    }
});

const emit = defineEmits();


</script>

<template>
    <button type="submit" :class="[color, `hover:${hoverColor}`, width]" class=" hover:cursor-pointer text-white 
    font-bold py-1.5 px-4 rounded focus:outline-none focus:shadow-outline" @click="emit('click')">
        {{ title }}
    </button>
</template>