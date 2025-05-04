<script setup>
import { defineProps, defineEmits, computed } from 'vue';
import { ref, watch } from 'vue';

// TODO: Autoscroll with arrow keys

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
    hints: {
        type: Array,
        default: () => []
    }
});

const isFocused = ref(false);
const onFocus = () => {
    isFocused.value = true;
};
const onBlur = () => {
    setTimeout(() => {
        isFocused.value = false;
    }, 150);
};

const activeIdx = ref(-1);

const handleKeydown = (event) => {
    if (event.key === 'Enter') {
        event.preventDefault();
        if (activeIdx.value > 0) {
            emit('update:modelValue', props.hints[activeIdx.value]);
        }
        isFocused.value = false;
    }
    else if (event.key === 'Escape') {
        event.preventDefault();
        isFocused.value = false;
    }
    else if (event.key === 'ArrowDown') {
        event.preventDefault();
        activeIdx.value = (activeIdx.value + 1) % props.hints.length;
    } else if (event.key === 'ArrowUp') {
        event.preventDefault();
        activeIdx.value = (activeIdx.value - 1 + props.hints.length) % props.hints.length;
    }
};

const emit = defineEmits(['update:modelValue']);
const style = computed(() => {
    return props.disabled ? "border rounded w-full py-2 px-3 mb-2 text-gray-500" : "border rounded w-full py-2 px-3 mb-2";
});

watch(() => props.hints, () => {
    activeIdx.value = -1;
});

</script>
<template>
    <div class="mb-4 relative">
        <label v-if="lbl" class="block text-gray-700 font-bold mb-2">{{ lbl }}</label>
        <input :value="props.modelValue" :type="type" :class="style" :placeholder="plchldr" :required="required"
            :disabled="disabled" @focus="onFocus" @blur="onBlur" @keydown="handleKeydown"
            @input="emit('update:modelValue', $event.target.value)" />

        <ul v-if="props.hints.length > 0 && isFocused"
            class="absolute w-full rounded-md bg-white border shadow-lg z-10 max-h-40 overflow-y-auto">
            <li v-for="(hint, index) in props.hints" :key="index" :class="[
                'px-4 py-2 cursor-pointer hover:bg-gray-200',
                index === activeIdx ? 'bg-gray-200' : ''
            ]" @mousedown="emit('update:modelValue', hint)">
                {{ hint }}
            </li>
        </ul>
    </div>
</template>
