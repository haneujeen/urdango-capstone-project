<!-- BusScreen.vue -->
<script setup>
/** Field description
 * 'vehicle_id': Unique identifier for the bus
 * 'line_name': The bus route or line name
 * 'plate_number'
 * 'travel_time': Time until the bus reaches The next immediate stop
 * 'current_speed': Current traveling speed of the bus
 * 'is_last_car': Whether there's no more buses scheduled after this bus
 * 'previous_station' (id and name): Most recent stop the bus departed from
 * 'station' (id and name): The next immediate stop bus is arriving
 * 'next_station' (id and name): The proceeding bus stop
 */
const props = defineProps({
    bus: Object
})
</script>

<template>
        <div class="card border-0 px-0 pb-0 text-muted shadow-sm" style="background: linear-gradient(#f6f6f6 0%, #fff 100%); border-radius: 25px;">
            <div class="card-body text-start mx-4 mb-3">
                <div class="mb-3 stop">
                    <p class="m-0"><small>Current Stop</small></p>
                    <h5>{{ bus.previous_station_name }}</h5>
                </div>
                <div class="mb-3 stop next">
                    <div class="row">
                        <div class="col-8">
                            <p class="m-0"><small>Current Stop</small></p>
                            <h5>{{ bus.station_name }}</h5>
                        </div>
                        <div class="col-4">badges</div>
                    </div>
                </div>
                <div class="mb-3 stop">
                    <p class="m-0"><small>Current Stop</small></p>
                    <h5>{{ bus.next_station_name }}</h5>
                </div>
            </div>
            <div class="card-footer text-bg-danger border-0 text-start" style="border-radius: 0 0 25px 25px">
                <p class="m-0"><small>{{ bus.line_name }} {{ bus.plate_number }} Speed: {{ bus.current_speed }} km/h Time left to {{ bus.station_name }}: {{ bus.travel_time }}s</small></p>
            </div>
        </div>
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
    width: 8px;
    background: linear-gradient(to bottom, transparent, #ccc, #ccc, #ccc, transparent);
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
    width: 18px;
    height: 18px;
    background: #ccc;
    border-radius: 50%;
    transform: translateY(-50%);
}
.stop.next::after {
    content: '';
    position: absolute;
    left: -16px;  
    top: 50%;
    width: 10px;
    height: 10px;
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