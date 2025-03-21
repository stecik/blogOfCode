<script setup>
import { ref, reactive, onMounted } from 'vue';
import { useToast } from 'vue-toastification';
import { validatePassword } from '@/utils/passwdValidation';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';
import ButtonSubmit from '@/components/ButtonSubmit.vue';
import InputField from '@/components/InputField.vue';
import { customFetch } from '@/api';

const router = useRouter();
const toast = useToast();
const authStore = useAuthStore();

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
    userData.loading = true;
    try {
        const response = await customFetch("/api/users/user/", "GET");
        const data = await response.json();
        if (response.ok) {
            userData.data = data;
        }
    } catch (error) {
        console.log(error);
    }
    finally {
        userData.loading = false;
    }
}

const editProfile = async () => {
    try {
        const response = await customFetch("/api/users/user/", "PATCH", userData.data);
        if (response.ok) {
            toast.success("Profile updated successfully");
        }
        else {
            toast.error("An error occurred");
        }
    } catch (error) {
        console.log(error);
        toast.error("An error occurred");
    } finally {
        getUserData();
    }

}


const changePassword = async () => {
    if (!validatePassword(changePasswdForm.new_password, newPasswordAgain.value, toast)) {
        return;
    }
    try {
        const response = await customFetch("/api/users/user/change-password/", "PATCH", changePasswdForm);
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
    if (confirm("Are you sure you want to delete your account?")) {
        try {
            const response = await customFetch("/api/users/user/", "DELETE", deleteAccountForm);
            if (response.ok) {
                toast.success("Account deleted successfully");
                authStore.logout();
                router.push("/login");
            }
            else {
                const data = await response.json();
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

    <section>
        <div class="container m-auto max-w-2xl py-4 pt-15">
            <div class="bg-white px-6 py-8 mb-4 shadow-md rounded-md border m-4 md:m-0">
                <h2 class=" text-3xl text-center font-semibold mb-6 text-amber-600">profileInfo</h2>
                <form @submit.prevent="editProfile">

                    <InputField lbl="firstName" v-model="userData.data.first_name" />
                    <InputField lbl="lastName" v-model="userData.data.last_name" />
                    <InputField lbl="username" v-model="userData.data.username" />
                    <InputField lbs="email" v-model="userData.data.email" />
                    <InputField lbl="isAdmin" v-model="userData.data.is_staff" :disabled="true" />
                    <InputField lbl="isSuperUser" v-model="userData.data.is_superuser" :disabled="true" />
                    <InputField lbl="isOnline" v-model="userData.data.is_online" :disabled="true" />
                    <ButtonSubmit title="saveChanges" />

                </form>

            </div>
        </div>

        <div class="container m-auto max-w-2xl py-4">
            <div class="bg-white px-6 py-8 mb-4 shadow-md rounded-md border m-4 md:m-0">
                <h2 class=" text-3xl text-center font-semibold mb-6 text-amber-600">changePassword</h2>

                <form @submit.prevent="changePassword">

                    <InputField lbl="oldPassword" type="password" v-model="changePasswdForm.old_password" />
                    <InputField lbl="newPassword" type="password" v-model="changePasswdForm.new_password" />
                    <InputField lbl="newPasswordAgain" type="password" v-model="newPasswordAgain" />
                    <ButtonSubmit title="changePassword" />

                </form>

            </div>
        </div>
        <div class="container m-auto max-w-2xl py-4">
            <div class="bg-white px-6 py-8 mb-4 shadow-md rounded-md border m-4 md:m-0">
                <h2 class=" text-3xl text-center font-semibold mb-6 text-red-600">dangerZone</h2>
                <form @submit.prevent="deleteAccount">
                    <InputField lbl="password" plchldr="password" type="password"
                        v-model="deleteAccountForm.password" />
                    <ButtonSubmit title="deleteAccount" color="bg-red-700" hoverColor="hover:bg-red-800" />
                </form>

            </div>
        </div>


    </section>

</template>
