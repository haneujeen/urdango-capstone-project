<script setup>
import { ref } from 'vue'

defineProps({
    msg: String,
})
const showList = ref(false);
const showCard = ref(false);
const showStop = ref(false);

const handleSearchClick = () => {
    showList.value = true;
}

const handleListItemClick = () => {
    showList.value = false;
    showCard.value = true;
}

const handleGetOnButtonClick = () => {
    showStop.value = true;
    showCard.value = false;
}
</script>

<template>
    <div>
        <h1>{{ msg }}</h1>

        <div class="input-group input-group-lg">
            <input type="text" class="form-control" placeholder="search station">
            <button class="btn btn-outline-secondary" type="button" @click="handleSearchClick">search</button>
        </div>

        <ul class="list-group list-group-flush" v-if="showList">
            <li class="list-group-item" @click="handleListItemClick">a</li>
            <li class="list-group-item">b</li>
        </ul>

        <div class="card" v-if="showCard">
            <div class="card-body">
                <h5 class="card-title">station name (01234)</h5>
                <ul class="list-group list-group-flush">
                    <li class="list-group-item">
                        vehicle arrives in 3 minutes...
                        <button type="button" class="btn btn-light" @click="handleGetOnButtonClick">button</button>
                    </li>
                    <!-- Other list items -->
                </ul>
            </div>
        </div>

        <div v-if="showStop">
            <p>this stop is ..., next stop is ....</p>
            <button type="button" class="btn btn-warning">stop</button>
        </div>

        <p class="app-title">App Title</p>
    </div>
</template>

<style scoped>
.read-the-docs {
    color: #888;
}
</style>