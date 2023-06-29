<!-- SettingsCard.vue -->
<script setup>
import { ref } from 'vue'
import Switch from './Switch.vue';

const stopRequested = ref(false)

const requestStop = () => {
    stopRequested.value = !stopRequested.value
}
</script>

<template>
        <p class="text-start pt-3">REQUEST STOP</p>
        <div class="card border-0 px-0 pb-0 text-muted bg-light" style="border-radius: 25px;">
            <div class="m-4 mb-3">
                <button class="btn btn-lg btn-light text-dark rounded-pill border-0" :class="{ 'active': stopRequested }" @click="requestStop">
                    Request Stop
                </button>
            </div>
            <div class="mx-3 text-start text-muted">
                <span class="form-check form-switch">
                    <Switch/>
                    <label class="form-check-label" for="pushNotificationSwitch">Push Notification</label>
                </span>
            </div>
            <div class="card-footer text-bg-light border-0 text-start" style="border-radius: 0 0 25px 25px">
                <p class="m-0"><small>Device Name: My iPhone Requested User: Someone</small></p>
            </div>
        </div>

</template>

<style scoped>
.active {
    background-color: rgb(220, 72, 72) !important;
    color: white !important;
}
</style>