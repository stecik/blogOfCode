<script setup>
import { ref, reactive } from 'vue';
import { useToast } from 'vue-toastification';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';
import ButtonSubmit from './ButtonSubmit.vue';
import InputField from './InputField.vue';
import { customFetch } from '@/api';

const toast = useToast();
const router = useRouter();
const authStore = useAuthStore();

const loginForm = reactive({
    username: '',
    password: '',
});

const handleLogin = async () => {
    try {
        const response = await customFetch("/api/users/login/", "POST", loginForm);
        const data = await response.json();
        if (response.ok) {
            toast.success('Login successful');
            authStore.login(loginForm.username, data.user.id, data.access, data.refresh);
            router.push('/');
        } else {
            toast.error(data.detail);
        }

    } catch (error) {
        toast.error('Something went wrong');
    }

};

</script>


<template>
    <section>
        <div class="container m-auto max-w-2xl py-24">
            <div class="bg-white px-6 py-8 mb-4 shadow-md rounded-md border m-4 md:m-0">
                <h2 class=" text-3xl text-center font-semibold mb-6 text-amber-600">login</h2>
                <form @submit.prevent="handleLogin">

                    <InputField lbl="username" plchldr="username" v-model="loginForm.username" />
                    <InputField lbl="password" plchldr="password" type="password" v-model="loginForm.password" />
                    <ButtonSubmit title="login" />

                </form>
            </div>
        </div>
    </section>
</template>