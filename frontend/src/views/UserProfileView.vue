<script setup>
import { ref, reactive, onMounted } from 'vue';
import { useToast } from 'vue-toastification';
import { validatePassword } from '@/utils/passwdValidation';
import { useRouter } from 'vue-router';

const router = useRouter();
const toast = useToast();

const userData = reactive({
    data: {},
    loading: false,
})

const changePasswdForm = reactive({
    old_password: "",
    new_password: "",
})

const newPasswordAgain = ref("");

const getUserData = async () => {
    const request = new Request("/api/users/user/", {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem('token')}`
        }
    })
    try {
        const response = await fetch(request);
        const data = await response.json();
        if (response.ok) {
            userData.data = data;
        }
    } catch (error) {
        console.log(error);
    }
}

const editProfile = async () => {
    const request = new Request("/api/users/user/", {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem('token')}`
        },
        body: JSON.stringify(userData.data)
    })
    try {
        const response = await fetch(request);
        if (response.ok) {
            toast.success("Profile updated successfully");
        }
        else {
            toast.error("An error occurred");
        }
    } catch (error) {
        console.log(error);
        toast.error("An error occurred");
    }
    finally {
        getUserData();
    }
}


const changePassword = async () => {
    if (!validatePassword(changePasswdForm.new_password, newPasswordAgain.value, toast)) {
        return;
    }
    const request = new Request("/api/users/user/change-password/", {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem('token')}`
        },
        body: JSON.stringify(changePasswdForm)
    })
    try {
        const response = await fetch(request);
        const data = await response.json();
        if (response.ok) {
            toast.success("Password changed successfully");
        }
        else {
            toast.error(data.error);
        }
    } catch (error) {
        console.log(error);
        toast.error("An error occurred");
    }
    finally {
        changePasswdForm.old_password = "";
        changePasswdForm.new_password = "";
        newPasswordAgain.value = "";
    }
}

const deleteAccountForm = reactive({
    password: ""
})
const deleteAccount = async () => {
    const request = new Request("/api/users/user/", {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem('token')}`
        },
        body: JSON.stringify(deleteAccountForm)
    })
    if (confirm("Are you sure you want to delete your account?")) {
        try {
            const response = await fetch(request);
            const data = await response.json();
            if (response.ok) {
                toast.success("Account deleted successfully");
                localStorage.removeItem('token');
                router.push("/login");
            }
            else {
                toast.error(data.error);
            }
        } catch (error) {
            console.log(error);
            toast.error("An error occurred");
        }
        finally {
            deleteAccountForm.password = "";
        }
    }
}


onMounted(() => {
    getUserData();
})
</script>

<template>

    <section class="bg-green-50">
        <div class="container m-auto max-w-2xl py-4 pt-15">
            <div class="bg-white px-6 py-8 mb-4 shadow-md rounded-md border m-4 md:m-0">
                <h2 class=" text-3xl text-center font-semibold mb-6 text-amber-600">profileInfo</h2>
                <form @submit.prevent="editProfile">

                    <div class="mb-4">
                        <label class="block text-gray-700 font-bold mb-2">firstName</label>
                        <input v-model="userData.data.first_name" type="text" id="firstName" name="firstName"
                            class="border rounded w-full py-2 px-3 mb-2" required />
                    </div>

                    <div class="mb-4">
                        <label class="block text-gray-700 font-bold mb-2">lastName</label>
                        <input v-model="userData.data.last_name" type="text" id="lastName" name="lastName"
                            class="border rounded w-full py-2 px-3 mb-2" required />
                    </div>

                    <div class="mb-4">
                        <label class="block text-gray-700 font-bold mb-2">username</label>
                        <input v-model="userData.data.username" type="text" id="username" name="username"
                            class="border rounded w-full py-2 px-3 mb-2" required />
                    </div>

                    <div class="mb-4">
                        <label class="block text-gray-700 font-bold mb-2">email</label>
                        <input v-model="userData.data.email" type="email" id="email" name="email"
                            class="border rounded w-full py-2 px-3 mb-2" required />
                    </div>

                    <div class="mb-4">
                        <label class="block text-gray-500 font-bold mb-2">isAdmin</label>
                        <input v-model="userData.data.is_staff" type="" id="isAdmin" name="isAdmin" disabled
                            class="border rounded w-full py-2 px-3 mb-2 text-gray-500" required />
                    </div>

                    <div class="mb-4">
                        <label class="block text-gray-500 font-bold mb-2">isSuperUser</label>
                        <input v-model="userData.data.is_superuser" type="" id="isSuperUser" name="isSuperUser" disabled
                            class="border rounded w-full py-2 px-3 mb-2 text-gray-500" required />
                    </div>

                    <div class="mb-4">
                        <label class="block text-gray-500 font-bold mb-2">isOnline</label>
                        <input v-model="userData.data.is_active" type="" id="isOnline" name="isOnline" disabled
                            class="border rounded w-full py-2 px-3 mb-2 text-gray-500" required />
                    </div>

                    <button type="submit" class=" bg-amber-600 hover:bg-amber-950 hover:cursor-pointer text-white font-bold py-2 px-4 rounded-full w-full
                            focus:outline-none focus:shadow-outline">
                        saveChanges
                    </button>

                </form>


            </div>
        </div>

        <div class="container m-auto max-w-2xl py-4">
            <div class="bg-white px-6 py-8 mb-4 shadow-md rounded-md border m-4 md:m-0">
                <h2 class=" text-3xl text-center font-semibold mb-6 text-amber-600">changePassword</h2>
                <form @submit.prevent="changePassword">

                    <div class="mb-4">
                        <label class="block text-gray-700 font-bold mb-2">oldPassword</label>
                        <input v-model="changePasswdForm.old_password" type="password" id="oldPassword"
                            name="oldPassword" class="border rounded w-full py-2 px-3 mb-2" required />
                    </div>

                    <div class="mb-4">
                        <label class="block text-gray-700 font-bold mb-2">newPassword</label>
                        <input v-model="changePasswdForm.new_password" type="password" id="newPassword"
                            name="newPassword" class="border rounded w-full py-2 px-3 mb-2" required />
                    </div>

                    <div class="mb-4">
                        <label class="block text-gray-700 font-bold mb-2">newPasswordAgain</label>
                        <input v-model="newPasswordAgain" type="password" id="newPasswordAgain" name="newPasswordAgain"
                            class="border rounded w-full py-2 px-3 mb-2" required />
                    </div>

                    <button type="submit" class=" bg-amber-600 hover:bg-amber-950 hover:cursor-pointer text-white font-bold py-2 px-4 rounded-full w-full
                            focus:outline-none focus:shadow-outline">
                        saveChanges
                    </button>

                </form>

            </div>
        </div>
        <div class="container m-auto max-w-2xl py-4">
            <div class="bg-white px-6 py-8 mb-4 shadow-md rounded-md border m-4 md:m-0">
                <h2 class=" text-3xl text-center font-semibold mb-6 text-red-600">dangerZone</h2>
                <form @submit.prevent="deleteAccount">

                    <div class="mb-4">
                        <label class="block text-gray-700 font-bold mb-2">password</label>
                        <input v-model="deleteAccountForm.password" type="password" id="passsword" name="oldPassword"
                            class="border rounded w-full py-2 px-3 mb-2" required />
                    </div>


                    <button type="submit" class=" bg-red-700 hover:bg-amber-950 hover:cursor-pointer text-white font-bold py-2 px-4 rounded-full w-full
                            focus:outline-none focus:shadow-outline">
                        deleteAccount
                    </button>

                </form>

            </div>
        </div>

    </section>

</template>
