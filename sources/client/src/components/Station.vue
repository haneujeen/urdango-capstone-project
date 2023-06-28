<script setup>
import { ref } from 'vue';
import axios from 'axios';
import MyBus from './MyBus.vue';

const props = defineProps({
    station: Object,
    busList: Array
});

let selectedBus = ref(null);
let targetBus = ref(null);

const handleClick = (bus) => {
    console.log("busRouteAbrv: ", bus.busRouteAbrv, " to ", bus.nxtStn)
    console.log("busRouteId: ", bus.busRouteId, "vehId1: ", bus.vehId1)
    console.log("My vehId = bus.vehId1")
    
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
                        busRouteAbrv: {{ bus.busRouteAbrv }} to {{ bus.nxtStn }}
                        busRouteId: {{ bus.busRouteId }}
                        vehId1: {{ bus.vehId1 }}
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
