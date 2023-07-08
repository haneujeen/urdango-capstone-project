<!-- MyBus.vue -->
<script setup>
import { ref } from 'vue'

import BusScreen from './mybus/BusScreen.vue';
import StopButton from './mybus/StopButton.vue'
import Switch from './mybus/Switch.vue'

const props = defineProps({
    bus: Object
})
</script>

<template>
    <div>
        <BusScreen :bus="bus"/>
        <StopButton/>
        <div class="mx-3 text-start text-muted mt-3">
            <span class="form-check form-switch">
                <Switch/>
                <label class="form-check-label" for="pushNotificationSwitch">Push Notification</label>
            </span>
        </div>
    </div>
</template>