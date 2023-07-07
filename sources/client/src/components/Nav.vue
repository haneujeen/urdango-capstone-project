<!-- Nav.vue -->
<script setup>
import { useStore } from 'vuex';
import { onMounted } from 'vue';
import { Tooltip } from 'bootstrap';

onMounted(() => {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new Tooltip(tooltipTriggerEl)
    })
});
</script>

<template>
    <ul class="nav nav-pills nav-fill 
        fixed-bottom p-2
        d-flex justify-content-evenly"
        style="width: 100vw;" 
    >
        <li class="nav-item d-flex justify-content-center">
            <a class="nav-link active rounded-4" 
                aria-current="page" 
                href="/" 
                style="max-width: 50px;"
                data-bs-toggle="tooltip" 
                data-bs-title="Tap this to go back to the homepage" 
            >
                <i class="fa-solid fa-house" style="color: #fffff0;"></i>
                
            </a>
        </li>
        <li class="nav-item d-flex justify-content-center">
            <a class="nav-link active rounded-4" 
                aria-current="page" 
                href="/" 
                style="max-width: 50px;"
                data-bs-toggle="tooltip" 
                data-bs-title="Manage how you want to receive the push message" 
            >
                <i class="fa-solid fa-lg fa-gear" style="color: #fffff0;"></i>
                
            </a>
        </li>
    </ul>
</template>

<style scoped>
ul {
    background-color: #333;
}

.nav-link {
    color: #fffff0;
    background-color: #4a4949 !important;
}
</style>
