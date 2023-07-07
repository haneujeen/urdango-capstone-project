<script setup>
import axios from 'axios';

import { onMounted, ref, provide } from 'vue';
import { useStore } from 'vuex';
import { Tooltip } from 'bootstrap';

import Tracker from './components/Tracker.vue'
import Nav from './components/Nav.vue';

const store = useStore();
const hide = ref(false);

provide('hide', hide);

onMounted(async () => {
    // Bootstrap stuff
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new Tooltip(tooltipTriggerEl);
    })

    // For push notification subscription
    try {
        const response = await axios.get('http://localhost:8000/get_uuid/');
        console.log(response.data.uuid)
        store.commit('setUUID', response.data.uuid);
        console.log('UUID saved:', store.state.uuid);
    } catch (error) {
        console.error('Error while getting UUID:', error);
    }
});
</script>

<template>
    <div>
        <a href="https://vuejs.org/" target="_blank" v-if="!hide">
            <img src="./assets/otter-solid.svg" class="logo vue" alt="Vue logo" 
                data-bs-toggle="tooltip" 
                data-bs-title="She's just an otter 😮"
            />
        </a>
        <div :class="['tracker-container', { 'tracker-container-top': hide }]">
            <Tracker msg="" />
        </div>
    </div> 
    <Nav />
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #fff);
}
.tracker-container {
    transition: margin-top 0.5s ease-in-out;
    margin-top: 30px;
}

.tracker-container-top {
    margin-top: 0;
}
</style>
