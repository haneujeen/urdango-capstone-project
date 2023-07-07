<script setup>
import { ref, inject } from 'vue'
import axios from 'axios';
import SearchBar from './SearchBar.vue';
import StationList from './StationList.vue'

defineProps({
    msg: String,
})

const stationList = ref(null);
const pageholder = ref(null)

const hide = inject('hide');

const handleSearchClick = async (query) => {
    console.log(query)
    
    try {
        const response = await axios.get(`http://localhost:8000/get_station_by_name/${query}/`);
        console.log(response.data.msgHeader.headerCd);

        if (response.data.msgHeader.headerCd === "0") {
            stationList.value = response.data.msgBody.itemList;
            console.log(stationList.value);
        } else {
            pageholder.value = response.data.msgHeader.headerMsg;
        }

        // UI related
        hide.value = true;

        // TODO: If stationList.value.stNm is not unique, send the request to getStationByUid endpoint
        // to get the direction and specify the station

    } catch (error) {
        console.error(error);
        pageholder.value = 'An unexpected error occurred';
        
        // UI related
        hide.value = true;
    }
}
</script>

<template>
    <div class="spacing">
        <SearchBar @search="handleSearchClick" />

        <StationList v-if="stationList" :stationList="stationList" />
        <div v-else>{{ pageholder }}</div>
        <br/>
        <p class="app-title mt-3">App Title</p>
    </div>
</template>

<style scoped>
.app-title {
    color: #888;
}
.spacing > * {
    margin: 2rem 0;
}
</style>