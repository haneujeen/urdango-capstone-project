<script setup>
import { ref } from 'vue'
import axios from 'axios';
import SearchBar from './SearchBar.vue';
import StationList from './StationList.vue'

defineProps({
    msg: String,
})

const showList = ref(false);
const showCard = ref(false);
const showStop = ref(false);

const stationList = ref(null);

const handleSearchClick = async (query) => {
    showList.value = true;

    console.log(query)
    
    try {
        const response = await axios.get(`http://localhost:8000/get_station_by_name/${query}/`);
        stationList.value = response.data.msgBody.itemList;
        console.log(stationList.value)
    } catch (error) {
        console.error(error);
    }
}

const handleGetOnButtonClick = () => {
    showStop.value = true;
    showCard.value = false;
}
</script>

<template>
    <div class="spacing">
        <h1>{{ msg }}</h1>

        <SearchBar @search="handleSearchClick" />

        <StationList
            v-if="stationList"
            :stationList="stationList"
        />

        <p class="app-title">App Title</p>
    </div>
</template>

<style scoped>
.read-the-docs {
    color: #888;
}
.spacing > * {
    margin: 2rem 0;
}
</style>