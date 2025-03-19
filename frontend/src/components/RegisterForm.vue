<script setup>
import { reactive, ref } from 'vue';
import { useToast } from 'vue-toastification';

const toast = useToast();

const registerForm = reactive({
    first_name: '',
    last_name: '',
    username: '',
    email: '',
    password: '',
});

const passwordAgain = ref('');

const registerUser = async () => {
    if (!validatePassword()) {
        return;
    }
    try {
        const request = new Request("/api/users/register/", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(registerForm),
        });
        const response = await fetch(request);
        if (!response.ok) {
            throw new Error('An error occurred');
        }
        else {
            toast.success('User registered successfully. Please login');
        }
    } catch (error) {
        console.error(error);
        toast.error('An error occurred');
    }

}

const validatePassword = () => {
    if (registerForm.password !== passwordAgain.value) {
        toast.error('Passwords do not match');
    }
}

</script>


<template>

    <section class="bg-green-50">
        <div class="container m-auto max-w-2xl py-24">
            <div class="bg-white px-6 py-8 mb-4 shadow-md rounded-md border m-4 md:m-0">
                <h2 class=" text-3xl text-center font-semibold mb-6">createNewAccount</h2>
                <form @submit.prevent="registerUser">

                    <div class="mb-4">
                        <label class="block text-gray-700 font-bold mb-2">firstName</label>
                        <input v-model="registerForm.first_name" type="text" id="firstName" name="firstName"
                            class="border rounded w-full py-2 px-3 mb-2" placeholder="John" required />
                    </div>

                    <div class="mb-4">
                        <label class="block text-gray-700 font-bold mb-2">lastName</label>
                        <input v-model="registerForm.last_name" type="text" id="lastName" name="lastName"
                            class="border rounded w-full py-2 px-3 mb-2" placeholder="Smith" required />
                    </div>

                    <div class="mb-4">
                        <label class="block text-gray-700 font-bold mb-2">username</label>
                        <input v-model="registerForm.username" type="text" id="username" name="username"
                            class="border rounded w-full py-2 px-3 mb-2" placeholder="johnsmith32" required />
                    </div>

                    <div class="mb-4">
                        <label class="block text-gray-700 font-bold mb-2">email</label>
                        <input v-model="registerForm.email" type="email" id="email" name="email"
                            class="border rounded w-full py-2 px-3 mb-2" placeholder="example@example.com" required />
                    </div>

                    <div class="mb-4">
                        <label class="block text-gray-700 font-bold mb-2">password</label>
                        <input v-model="registerForm.password" type="password" id="password" name="password"
                            class="border rounded w-full py-2 px-3 mb-2" placeholder="password" required />
                    </div>

                    <div class="mb-4">
                        <label class="block text-gray-700 font-bold mb-2">passwordAgain</label>
                        <input v-model="passwordAgain" type="password" id="passwordAgain" name="paswordAgain"
                            class="border rounded w-full py-2 px-3 mb-2" placeholder="password" required />
                    </div>

                    <button type="submit" class=" bg-amber-600 hover:bg-amber-950 hover:cursor-pointer text-white font-bold py-2 px-4 rounded-full w-full
                            focus:outline-none focus:shadow-outline">
                        Register
                    </button>

                </form>
            </div>
        </div>
    </section>
</template>