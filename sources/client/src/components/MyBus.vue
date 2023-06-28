<script setup>
import { ref } from 'vue'

const props = defineProps({
    bus: Object // What's different between getting prop as array and getting it as an object?
})
</script>

<template>
    <div>
        <p>{{ bus.plainNo }}</p>
        <!-- <BusScreen/> -->
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
        <p>{{ bus.rtNm }} Estimated Time: {{ bus.traTime }} Travel Speed: {{ bus.traSpd }}</p>
        <p>Last Station Id: {{ bus.lastStnId }}</p>
        <p>Next Station Id: {{ bus.nstnId }}</p>
        <p>Last Station: {{ bus.lastStnNm }}</p>
        <p>Next Station: {{ bus.nstnNm }}</p>
        <!-- <StopRequestButton/> -->
    </div>
</template>