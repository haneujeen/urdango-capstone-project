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

const handleClick = async (bus) => {
    console.log("busRouteAbrv: ", bus.busRouteAbrv, " to ", bus.nxtStn)
    console.log("busRouteId: ", bus.busRouteId, "vehId1: ", bus.vehId1)
    console.log("My vehId = bus.vehId1")
    
    try {
        const lastStnIdResponse = await axios.get(`http://localhost:8000/get_bus_pos_by_veh_id/${bus.vehId1}`)
        targetBus.value = lastStnIdResponse.data.msgBody.itemList[0]
        console.log(targetBus.value)
        console.log("Last station of vehicle ", targetBus.value.plainNo, ": ", targetBus.value.lastStnId)
    
        const nstnId1Response = await axios.get(`http://localhost:8000/get_arr_info_by_route_all/${bus.busRouteId}`)
        const item = (nstnId1Response.data.msgBody.itemList).find(i => i.vehId1 === targetBus.value.vehId)
        console.log(item)
        console.log("Creating field nstnId in targetBus ref")
        targetBus.value.nstnId = item.nstnId1
        console.log(`Vehicle Id of Target Bus: ${targetBus.value.vehId}
                    Last Station Id and Next Station Id of Target Bus: ${targetBus.value.lastStnId} ${targetBus.value.nstnId}`)

        const stnNameResponse = await axios.get(`http://localhost:8000/get_arr_info_by_route_all/${bus.busRouteId}`)
        const lastStnNmItem = (stnNameResponse.data.msgBody.itemList).find(i => i.stId === targetBus.value.lastStnId)
        const nstnNmItem = (stnNameResponse.data.msgBody.itemList).find(i => i.stId === targetBus.value.nstnId)
        console.log(lastStnNmItem, nstnNmItem)
        console.log(lastStnNmItem.stNm, nstnNmItem.stNm, "😆😆😆")
    } catch (error) {
        console.error(error);
    }
}

const fetchStationName = async (stnId) => {

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
