<!-- <script setup>
import { defineProps, defineEmits, computed } from 'vue';
import { ref } from 'vue';

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

const inputValue = ref();

const isFocused = ref(false);
const onFocus = () => {
    isFocused.value = true;
};
const onBlur = () => {
    isFocused.value = false;
};

const emit = defineEmits(['update:modelValue']);
const style = computed(() => {
    return props.disabled ? "border rounded w-full py-2 px-3 mb-2 text-gray-500" : "border rounded w-full py-2 px-3 mb-2";
});

</script>

<template>
    <div class="mb-4">
        <label v-if="lbl" class="block text-gray-700 font-bold mb-2">{{ lbl }}</label>
        <input :type="type" :class="style" :placeholder="plchldr" :required="required" :disabled="disabled"
            :value="modelValue" @input="emit('update:modelValue', $event.target.value)" @focus="onFocus"
            @blur="onBlur" />

        <ul v-if="props.hints.length > 0 && isFocused"
            class="absolute w-full mt-2 bg-white border rounded-md shadow-lg">
            <li v-for="(hint, index) in props.hints" :key="index" class="px-4 py-2 cursor-pointer hover:bg-gray-200"
                @click="emit('update:modelValue', hint)">
                {{ hint }}
            </li>
        </ul>
    </div>
</template> -->


<script setup>
import { defineProps, defineEmits, computed } from 'vue';
import { ref } from 'vue';

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
    isFocused.value = false;
};

const emit = defineEmits(['update:modelValue']);
const style = computed(() => {
    return props.disabled ? "border rounded w-full py-2 px-3 mb-2 text-gray-500" : "border rounded w-full py-2 px-3 mb-2";
});

</script>

<template>
    <div class="mb-4 relative">
        <label v-if="lbl" class="block text-gray-700 font-bold mb-2">{{ lbl }}</label>
        <input :value="props.modelValue" :type="type" :class="style" :placeholder="plchldr" :required="required"
            :disabled="disabled" @focus="onFocus" @blur="onBlur"
            @input="emit('update:modelValue', $event.target.value)" />

        <ul v-if="props.hints.length > 0 && isFocused"
            class="absolute w-full mt-2 rounded-md bg-white border shadow-lg z-10">
            <li v-for="(hint, index) in props.hints" :key="index" class="px-4 py-2 cursor-pointer hover:bg-gray-200">
                {{ hint }}
            </li>
        </ul>
    </div>
</template>
