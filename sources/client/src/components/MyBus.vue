<script setup>
import { ref } from 'vue'

import BusScreen from './BusScreen.vue';

const props = defineProps({
    bus: Object
})
</script>

<template>
    <div>
        <!-- <p>{{ bus.plainNo }}</p> -->
        <!-- last station, upcoming station, proceeding station 
            estimated time to the upcoming station and speed (km/h)
            current vehicle's destination
            list of buses arriving upcoming station:
            
            {{ bus.lastStation, bus.upcomingStation, bus.proceedingStation }}
            {{ bus.lastStation.id, bus.lastStation.name }}
            {{ bus.travelTime, bus.travelSpeed }}
            {{ bus.destination }}
            {{ station.busList }}
        -->
        <!--<p>{{ bus.rtNm }} Estimated Time: {{ bus.traTime }} Travel Speed: {{ bus.traSpd }}</p>
        <p>Last Station Id: {{ bus.lastStnId }}</p>
        <p>Next Station Id: {{ bus.this_station_id }}</p>
        <p>Last Station: {{ bus.lastStnNm }}</p>
        <p>Next Station: {{ bus.this_station_name }}</p>
        <p>IsLast: {{ bus.isLast }}</p>
        <p>Next Next Station: {{ bus.next_station_id }} {{ bus.next_station_name }}</p>
        -->
        <BusScreen/>
        <!-- <StopRequestButton/> -->
    </div>
</template>