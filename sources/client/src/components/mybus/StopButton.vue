<!-- StopButton.vue -->
<script setup>
import { ref, onMounted, nextTick } from 'vue'

const stopRequested = ref(false)

</script>

<template>
    <!-- This sends request to the bus's receiver module the user's on right now. -->
    <p class="text-start pt-3"></p>
    <div class="card border-0 px-0 pb-0 text-muted bg-light shadow-sm" style="border-radius: 25px;">
        <div class="m-4 mb-3">
            <button id="stopButton" class="btn btn-lg rounded-5 py-4" 
                :class="[
                    { 'btn-light': !stopRequested, 'btn-danger': stopRequested },
                    { 'shadow': !stopRequested, 'shadow-sm': stopRequested }
                ]"
                :disabled="stopRequested"
                style="border: 10px solid #ffffff;"
                data-bs-toggle="modal" data-bs-target="#staticBackdrop"
            >
                <span class="h5">STOP</span>
                <!-- TODO: add data for users with physical disadvantage -->
                <!-- checkbox: Request additional aid when exiting -->
            </button>
        </div>
        <div class="card-footer text-bg-light border-0 text-start" style="border-radius: 0 0 25px 25px">
            <p class="m-0"><small>Device Name: My iPhone Requested User: Someone</small></p>
        </div>
    </div>

    <!-- Modal -->
    <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="staticBackdropLabel"></h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    This immediately sends request to the bus's receiver module the user's on at the moment.
                    A user cannot take back once the request is sent.
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-danger" data-bs-dismiss="modal" @click="stopRequested = true">Get me out</button>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
/* For web */
#stopButton:hover {
    background-color: #ce7474 !important; 
}

/* For mobile devices */
#stopButton:active {
    background-color: #c45e5e !important;
}
</style>