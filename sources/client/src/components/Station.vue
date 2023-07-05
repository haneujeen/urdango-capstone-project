<!-- Station.vue -->
<script setup>
import { ref, onUnmounted } from 'vue';
import { useStore } from 'vuex';
import SocketService from './socketService';
import MyBus from './MyBus.vue';
import { connect, disconnect } from './socket'

const props = defineProps({
    station: Object,
    busList: Array
});

const store = useStore()
const uuid = store.state.uuid
// const socketService = new SocketService()

let targetBus = ref(null);

const handleClick = async (bus) => {
    console.log("busRouteAbrv: ", bus.busRouteAbrv, " to ", bus.nxtStn)
    console.log("busRouteId: ", bus.busRouteId, "vehId1: ", bus.vehId1)
    console.log("adirection: ", bus.adirection)
    console.log("My vehId = bus.vehId1")
    
    connect(uuid, bus.vehId1, bus.busRouteId, targetBus);

    // Connect to the server
    // socketService.connect(uuid, bus.vehId1, bus.busRouteId, targetBus)

    // socketService.onMessage((data) => {
    //     targetBus.value = data
    // })
}

// onUnmounted(() => {
//    socketService.disconnect()
// })
</script>

<template>
    <div class="card" v-if="!targetBus">
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
