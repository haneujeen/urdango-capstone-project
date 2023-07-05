<!-- MyBus.vue -->
<script setup>
import { ref } from 'vue'

import BusScreen from './BusScreen.vue';
import SettingsCard from './SettingsCard.vue'

const props = defineProps({
    bus: Object
})
</script>

<template>
    <div>
        <BusScreen :bus="bus"/>
        <SettingsCard/>
        <!-- <StopRequestButton/> -->
    </div>
</template>