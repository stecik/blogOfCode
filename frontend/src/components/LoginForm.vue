<script setup>
import { ref, reactive } from 'vue';
import { useToast } from 'vue-toastification';
import { useRouter } from 'vue-router';

const toast = useToast();
const router = useRouter();

const loginForm = reactive({
    username: '',
    password: '',
});

const login = async () => {
    try {
        const request = new Request("/api/users/login/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(loginForm),
        })
        const response = await fetch(request);
        const data = await response.json();
        if (response.ok) {
            toast.success('Login successful');
            console.log(data);
            localStorage.setItem('token', data.access);
            localStorage.setItem('user', data.user.username);
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
                <form @submit.prevent="login">

                    <div class="mb-4">
                        <label class="block text-gray-700 font-bold mb-2">username</label>
                        <input v-model="loginForm.username" type="text" id="username" name="username"
                            class="border rounded w-full py-2 px-3 mb-2" placeholder="johndoe124" required />
                    </div>

                    <div class="mb-4">
                        <label class="block text-gray-700 font-bold mb-2">password</label>
                        <input v-model="loginForm.password" type="password" id="password" name="password"
                            class="border rounded w-full py-2 px-3 mb-2" placeholder="password" required />
                    </div>

                    <button type="submit" class=" bg-amber-600 hover:bg-amber-950 hover:cursor-pointer text-white font-bold py-2 px-4 rounded-full w-full
                            focus:outline-none focus:shadow-outline">
                        login
                    </button>

                </form>
            </div>
        </div>
    </section>
</template>