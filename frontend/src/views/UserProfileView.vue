<script setup>
import { ref, reactive, onMounted } from 'vue';

const userData = reactive({
    data: {},
    loading: false,
})

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

onMounted(() => {
    getUserData();
})
</script>
<template>
    <div v-for="(value, key) in userData.data" :key="key">
        <p>{{ key }}: {{ value }}</p>
    </div>
</template>
