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
    <div class="card border-0 shadow-sm rounded-4" v-if="!targetBus">
        <div class="card-body">
            <h5 class="card-title">
                <i class="fa-brands fa-lg fa-playstation" style="color: #333;"></i>
                {{ station.stNm }} ({{ station.arsId }})
                You're heading towards {{ station.next }}
            </h5>
            <ul class="list-group list-group-flush">
                <li 
                    class="list-group-item d-flex 
                        justify-content-between 
                        align-items-center"
                    v-for="bus in busList"
                >
                    <div>
                        routeType: {{ bus.routeType }}
                        <!-- 노선유형 (1:공항 w, 2:마을, 3:간선 b, 4:지선 g, 5:순환 y, 6:광역 r, 7:인천, 8:경기, 9:폐지, 0:공용 g) -->
                        busRouteAbrv: {{ bus.busRouteAbrv }} to {{ bus.nxtStn }}
                        <!-- busRouteAbrv: 노선명 (안내용 – 마을버스 제외)
                            rtNm: 노선명 (DB관리용) 
                            ref: https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15000303
                        -->
                        busRouteId: {{ bus.busRouteId }}
                        vehId1: {{ bus.vehId1 }}
                        <!-- vehId1 === 0: Bus stopped running -->
                        <span class="text-danger">
                            {{ bus.arrmsg1 }}
                            <i class="fa-solid fa-van-shuttle fa-bounce" 
                                style="color: #3a88fe;"
                            ></i>
                        </span>
                        {{ bus.vehId2 }}
                        <span v-if="bus.vehId1 === '0' && bus.vehId2 !== '0'">
                            vehId2: {{ bus.vehId2 }}
                            <i class="fa-solid fa-van-shuttle fa-bounce" 
                                style="color: #3a88fe;"
                            ></i>
                        </span>
                        <span v-if="bus.vehId1 === '0' && bus.vehId2 === '0'">
                            pj party on street :(
                            <i class="fa-solid fa-van-shuttle" 
                                style="color: #3a88fe;"
                            ></i>
                        </span>
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

<style scoped>
* {
    color: #333;
}
</style>