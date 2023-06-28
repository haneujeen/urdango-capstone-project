<script setup>
import { ref } from 'vue';
import axios from 'axios';
import MyBus from './MyBus.vue'

const props = defineProps({
    station: Object,
    busList: Array
})

let selectedBus = ref(null)
let targetBus = ref(null)

const handleClick = async (bus) => {
    console.log(bus)
    selectedBus.value = bus
    try {
        const response = await axios.get(`http://localhost:8000/get_bus_pos_by_rtid/${selectedBus.value.busRouteId}`);
        const busesOnRoute = response.data.msgBody.itemList;
        targetBus.value = busesOnRoute.find(b => b.vehId === bus.vehId1);

        if (targetBus) {
            console.log("Selected: ", selectedBus.value.busRouteAbrv, selectedBus.value.busRouteId)
            console.log("Target: ", targetBus.value.plainNo, targetBus.value.lastStnId, targetBus.value.nextStId);
            
        } else {
            console.error("Bus not found in the list");
        }
    } catch (error) {
        console.error(error);
    }
}
</script>

<template>
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">{{ station.stNm }} ({{ station.arsId }})</h5>
            <ul class="list-group list-group-flush">
                <li 
                    class="list-group-item d-flex 
                        justify-content-between 
                        align-items-center"
                    v-for="bus in busList"
                >
                    <div>
                        {{ bus.busRouteAbrv }} to {{ bus.nxtStn }}
                        <span class="text-danger">{{ bus.arrmsg1 }}</span>
                    </div>
                    <button 
                        type="button" 
                        class="btn btn-warning m-2"
                        @click="handleClick(bus)"
                    >
                        Catch
                    </button>
                </li>
            </ul>
        </div>
    </div>
    <MyBus v-if="targetBus" :bus="targetBus" />
</template>
