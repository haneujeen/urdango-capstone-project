<!-- SearchBar.vue -->
<script setup>
import { ref } from 'vue';

const emit = defineEmits(['search'])
const query = ref('')

const search = () => {
    emit('search', query.value)
}
</script>

<template>
    <div class="input-group input-group-lg">
        <input 
            type="text" 
            class="form-control" 
            placeholder="search station"
            v-model="query"
        >
        <button 
            class="btn btn-outline-secondary" 
            type="button" 
            @click="search"
        >
            Search
        </button>
    </div>
</template>