<script setup>
import { defineProps, defineEmits } from 'vue';

const props = defineProps({
    modelValue: {
        type: [Array, String],
        default: () => ([]),
    },
    lbl: {
        type: String,
        default: '',
    },
    required: {
        type: Boolean,
        default: true,
    },
    options: {
        type: Array,
        default: () => [],
    },
    multiple: {
        type: Boolean,
        default: false,
    },
});

const emit = defineEmits(['update:modelValue']);

const handleSelection = (event) => {
    if (props.multiple) {
        const selectedValues = Array.from(event.target.selectedOptions).map(option => option.value);
        emit('update:modelValue', selectedValues);
    } else {
        emit('update:modelValue', event.target.value);
    }
};
</script>

<template>
    <div class="mb-4">
        <label v-if="lbl" class="block text-gray-700 font-bold mb-2">{{ lbl }}</label>
        <select class="border rounded w-full py-2 px-3 mb-2" :required="required" :multiple="multiple"
            @change="handleSelection">
            <option v-for="option in options" :key="option" :value="option"
                :selected="multiple ? modelValue.includes(option) : modelValue === option">
                {{ option }}
            </option>
        </select>
    </div>
</template>