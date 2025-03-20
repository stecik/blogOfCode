<script setup>
import { defineProps, defineEmits, computed } from 'vue';

const props = defineProps({
    modelValue: {
        type: [String, Number, Boolean],
        default: null
    },
    lbl: {
        type: String,
        default: '',
    },
    plchldr: {
        type: String,
        default: '',
    },
    disabled: {
        type: Boolean,
        default: false,
    },
    required: {
        type: Boolean,
        default: true,
    },
    type: {
        type: String,
        default: 'text',
    },
});

const emit = defineEmits(['update:modelValue']);
const style = computed(() => {
    return props.disabled ? "border rounded w-full py-2 px-3 mb-2 text-gray-500" : "border rounded w-full py-2 px-3 mb-2";
});

</script>

<template>
    <div class="mb-4">
        <label v-if="lbl" class="block text-gray-700 font-bold mb-2">{{ lbl }}</label>
        <input :type="type" :class="style" :placeholder="plchldr" :required="required" :disabled="disabled"
            :value="modelValue" @input="emit('update:modelValue', $event.target.value)" />
    </div>
</template>