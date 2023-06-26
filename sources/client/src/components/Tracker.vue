<script setup>
import { ref } from 'vue'
import SearchBar from './SearchBar.vue';
import StationList from './StationList.vue'

defineProps({
    msg: String,
})

const showList = ref(false);
const showCard = ref(false);
const showStop = ref(false);

const url = 'http://ws.bus.go.kr/api/rest/stationinfo/getStationByName?serviceKey=GMDNZxLlo35v0mYu1b%2BEExd5aIdZ93RCUBhUBo2w73LWCtz%2Ft%2F%2FKdGfzDVUdcyqljjwvNa5Dtd56uELhovFZRw%3D%3D&stSrch=덕성'
const key = 'GMDNZxLlo35v0mYu1b%2BEExd5aIdZ93RCUBhUBo2w73LWCtz%2Ft%2F%2FKdGfzDVUdcyqljjwvNa5Dtd56uELhovFZRw%3D%3D'
    
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

        <SearchBar @search="handleSearchClick" />

        <StationList v-if="showList" @list-item-click="handleListItemClick" />

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