<!-- BusScreen.vue -->
<script setup>
import { ref } from 'vue'
import SettingsCard from './SettingsCard.vue'

const busData = ref({
            rtNm: 'Bus 123',
            plainNo: 'Plate ABC 123',
            lastStnNm: 'Current Station',
            this_station_name: 'Next Station',
            next_station_name: 'Following Station'
        })
</script>

<template>
        <div class="card border-0 px-0 pb-0 text-muted shadow" style="background: linear-gradient(#f6f6f6 0%, #ffffff 100%); border-radius: 25px;">
            <div class="card-body text-start mx-4 mb-3">
                <div class="mb-3 stop">
                    <p class="m-0"><small>Current Stop</small></p>
                    <h5>{{ busData.lastStnNm }}</h5>
                </div>
                <div class="mb-3 stop next">
                    <div class="row">
                        <div class="col-8">
                            <p class="m-0"><small>Current Stop</small></p>
                            <h5>{{ busData.this_station_name }}</h5>
                        </div>
                        <div class="col-4">badges</div>
                    </div>
                </div>
                <div class="mb-3 stop">
                    <p class="m-0"><small>Current Stop</small></p>
                    <h5>{{ busData.next_station_name }}</h5>
                </div>
            </div>
            <div class="card-footer text-bg-danger border-0 text-start" style="border-radius: 0 0 25px 25px">
                <p class="m-0"><small>{{ busData.rtNm }} {{ busData.plainNo }} Speed: km/h Estimated Time: 000</small></p>
            </div>
        </div>
        <SettingsCard/>
</template>

<style scoped>
.card-body {
    position: relative;
    padding-left: 30px;
}
.card-body::before {
    content: '';
    position: absolute;
    left: 15px; 
    top: 0;
    height: 100%;
    width: 5px;
    background: linear-gradient(to bottom, transparent, #000, #000, #000, transparent);
}
.stop {
    position: relative;
    padding-left: 15px; 
}
.stop::before {
    content: '';
    position: absolute;
    left: -20px;  
    top: 50%;
    width: 15px;
    height: 15px;
    background: #111;
    border-radius: 50%;
    transform: translateY(-50%);
}
.stop.next::after {
    content: '';
    position: absolute;
    left: -17px;  
    top: 50%;
    width: 9px;
    height: 9px;
    background: #fff;
    border-radius: 50%;
    transform: translateY(-50%);
    animation: blink 2s infinite;
}
@keyframes blink {
    0% { opacity: 1; }
    50% { opacity: 0; }
    100% { opacity: 1; }
}
</style>