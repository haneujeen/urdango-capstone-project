<!-- StationList.vue -->
<script setup>
import { ref } from 'vue';
import axios from 'axios';
import Station from './Station.vue';

const props = defineProps({
    stationList: Array
})

let selectedStation = ref(null);
let busList = ref(null)

const handleClick = async (station) => {
    console.log("Clicked")
    selectedStation.value = {'stNm': station.stNm, 'arsId': station.arsId}
    try {
        const response = await axios.get(`http://localhost:8000/get_station_by_uid/${station.arsId}`);
        busList.value = response.data.msgBody.itemList;
    } catch (error) {
        console.error(error);
    }
}
</script>

<template>
    <ul class="list-group list-group-flush" v-if="!selectedStation || !busList">
        <li 
            v-for="station in stationList"
            :key="station.stId"
            class="list-group-item" 
            @click="handleClick(station)"
        >
            {{ station.stNm }}
        </li>
    </ul>

    <Station :station="selectedStation" :busList="busList" v-else />
</template>
