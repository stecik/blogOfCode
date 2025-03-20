<script setup>
import { ref } from 'vue';
import { useAuthStore } from '@/stores/auth';
import TagsList from '@/components/TagsList.vue';
import ButtonSubmit from '@/components/ButtonSubmit.vue';
import InputField from '@/components/InputField.vue';

const tags = ref(["dog", "cat", "bird"]);
</script>
<template>

    <section>
        <div class="container m-auto max-w-7xl py-24">
            <div class="bg-white px-6 py-8 mb-4 shadow-md rounded-md border m-4 md:m-0">
                <h2 class=" text-3xl text-center font-semibold mb-6 text-amber-600">createNewArticle</h2>
                <form class="mb-4">
                    <div class="my-4">
                        <label class="block text-gray-700 font-bold mb-2">tags</label>
                        <TagsList :tags="tags" />
                    </div>
                    <InputField lbl="tagName" plchldr="tagName" />
                    <ButtonSubmit title="addTag" />
                </form>
                <form>
                    <InputField lbl="title" plchldr="noClickBait" />
                    <ButtonSubmit title="postArticle" />

                    <InputField lbl="content" plchldr="writeYourArticleHere" type="textarea" />
                </form>
            </div>
        </div>
    </section>
</template>