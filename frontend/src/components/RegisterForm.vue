<script setup>
import { reactive, ref } from 'vue';
import { useToast } from 'vue-toastification';
import { validatePassword } from '@/utils/passwdValidation';
import ButtonSubmit from './ButtonSubmit.vue';
import InputField from './InputField.vue';
import { customFetch } from '@/api';
import { useRouter } from 'vue-router';
import { compileScript } from 'vue/compiler-sfc';

const toast = useToast();
const router = useRouter();

const registerForm = reactive({
    first_name: '',
    last_name: '',
    username: '',
    email: '',
    password: '',
});

const passwordAgain = ref('');

const registerUser = async () => {
    console.log(registerForm);
    if (!validatePassword(registerForm.password, passwordAgain.value, toast)) {
        return;
    }
    try {
        const response = await customFetch("/api/users/register/", "POST", registerForm);
        const data = await response.json();
        console.log(data);
        if (!response.ok) {
            console.log(data);
            let err = ""
            if (data.email) {
                err = data.email[0]
            } else if (data.username) {
                err = data.username[0]
            } else {
                err = "An error occurred"
            }
            toast.error(err);
        }
        else {
            toast.success('User registered successfully. Please login');
            router.push('/login');
        }
    } catch (error) {
        console.error(error);
        toast.error('An error occurred');
    }

}

</script>


<template>

    <section>
        <div class="container m-auto max-w-2xl py-24">
            <div class="bg-white px-6 py-8 mb-4 shadow-md rounded-md border m-4 md:m-0">
                <h2 class=" text-3xl text-center font-semibold mb-6 text-amber-600">createNewAccount</h2>

                <form @submit.prevent="registerUser">
                    <InputField v-model="registerForm.first_name" lbl="firstName" plchldr="John" />
                    <InputField v-model="registerForm.last_name" lbl="lastName" plchldr="Doe" />
                    <InputField v-model="registerForm.username" lbl="username" plchldr="johnsmith23" />
                    <InputField v-model="registerForm.email" lbl="email" plchldr="john.doe@example.com" type="email" />
                    <InputField v-model="registerForm.password" lbl="password" plchldr="password" type="password" />
                    <InputField v-model="passwordAgain" lbl="passwordAgain" plchldr="passwordAgain" type="password" />
                    <ButtonSubmit title="register" />
                </form>

            </div>
        </div>
    </section>
</template>