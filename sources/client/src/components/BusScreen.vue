<script setup>
import { ref } from 'vue'

const busData = ref({
            rtNm: 'Bus 123',
            plainNo: 'Plate ABC 123',
            lastStnNm: 'Current Station',
            this_station_name: 'Next Station',
            next_station_name: 'Following Station'
        })

const stopRequested = ref(false)

const requestStop = () => {
    stopRequested.value = !stopRequested.value
}
</script>

<template>
        <div class="card border-0 px-0 pb-0 text-muted shadow" style="background: linear-gradient(#f6f6f6 0%, #ffffff 100%); border-radius: 25px;">
            
            <div class="card-body text-start mx-4 mb-3">
                <div class="mb-3 stop">
                    <p class="m-0"><small>Current Stop</small></p>
                    <h5>{{ busData.lastStnNm }}</h5>
                </div>
                <div class="mb-3 stop next">
                    <p class="m-0"><small>Current Stop</small></p>
                    <h5>{{ busData.this_station_name }}</h5>
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
        <p class="text-start pt-3">REQUEST STOP</p>
        
        <div class="card border-0 px-0 pt-0 text-muted bg-light" style="border-radius: 25px;">
            <div class="card-header text-bg-light border-0 text-start" style="border-radius: 25px 25px 0 0">
                <p class="m-0"><small>Device Name: My iPhone Requested User: Someone</small></p>
            </div>
            <div class="m-4 mb-3">
                <button class="btn btn-lg btn-light text-dark rounded-pill border-0" :class="{ 'active': stopRequested }" @click="requestStop">
                    Request Stop
                </button>
            </div>
            <div class="mx-3 text-start text-muted" style="border-radius: 25px;">
                <span class="form-check form-switch">
                    <input class="form-check-input input-lg" type="checkbox" role="switch" id="flexSwitchCheckChecked" checked>
                    <label class="form-check-label" for="flexSwitchCheckChecked">Push Notification</label>
                </span>
           
            </div>
        </div>

</template>

<style scoped>
.form-check-input {
    width: 3em;
    height: 1em;
}
.form-check-input:checked::before {
    background-color: #ffc107 !important; /* checked color */
}
.active {
    background-color: rgb(220, 72, 72) !important;
    color: white !important;
}
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