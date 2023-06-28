<script setup>
import { ref } from 'vue'

const props = defineProps({
    bus: Object // What's different between getting prop as array and getting it as an object?
})
</script>

<template>
    <div>
        <p>{{ bus.plainNo }}</p>
        <p>Last Station Id: {{ bus.lastStnId }}</p>
        <p>Next Station Id: {{ bus.nstnId }}</p>
        <p>Last Station: {{ bus.lastStnNm }}</p>
        <p>Next Station: {{ bus.nstnNm }}</p>
        <!-- <BusScreen/> -->
    </div>
</template>