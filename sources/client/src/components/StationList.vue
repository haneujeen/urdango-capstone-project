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
    <div class="container bg-white rounded-4 shadow-sm py-3 pe-0" v-if="!selectedStation || !busList">
        <ul class="list-group list-group-flush overflow-auto custom-scroll" 
            style="max-height: 60vh"
        >
            <li 
                v-for="station in stationList"
                :key="station.stId"
                class="list-group-item bg-white border-0 rounded-4 m-0 me-2 pe-4 py-3 d-flex justify-content-between"
                @click="handleClick(station)"
                style="font-size: 1.2rem; "
            >
                <span 
                    class="badge rounded-3 d-flex align-items-center"
                    style="background-color: #a7bba0; color: #fffff0; font-weight: normal; width: 3.5rem;"
                >
                    {{ station.arsId }}
                </span>
                {{ station.stNm }} 
            </li>
        </ul>
    </div>
    
    <Station :station="selectedStation" :busList="busList" v-else />
</template>

<style scoped>
/* For web */
.list-group-item:hover {
    background-color: #ebebeb !important; 
}

/* For mobile devices */
.list-group-item:active {
    background-color: #ebebeb !important;
}

.custom-scroll::-webkit-scrollbar {
    width: 8px;
}

.custom-scroll::-webkit-scrollbar-track {
    background: #f1f1f1;
    border-radius: 4px;
}

.custom-scroll::-webkit-scrollbar-thumb {
    background: #888;
    border-radius: 4px;
}

.custom-scroll::-webkit-scrollbar-thumb:hover {
    background: #555;
}
</style>