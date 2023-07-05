<script setup>
import { useStore } from 'vuex';
import Tracker from './components/Tracker.vue'
import WebSocketTest from './WebSocketTest.vue';
import { onMounted } from 'vue';
import axios from 'axios';

const store = useStore();

onMounted(async () => {
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
        <a href="https://vuejs.org/" target="_blank">
            <img src="./assets/otter-solid.svg" class="logo vue" alt="Vue logo" />
        </a>
        <Tracker msg="" />
        <WebSocketTest/>
    </div>
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
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
