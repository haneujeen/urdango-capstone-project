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
    <div class="input-group input-group-lg shadow rounded">
        <input 
            type="text" 
            class="form-control border-0 rounded-start" 
            aria-label="Search station"
            placeholder="Search station"
            v-model="query"
            @keyup.enter="search"
            style="border-right: none;"
        >
        <span class="input-group-text bg-transparent border-0 p-0 pe-2 rounded-end">
            <button 
                class="btn bg-transparent border-0 px-0"
                @click="search"
            >
                <i 
                    class="fas fa-search text-white p-2 bg-danger" 
                    style="border-radius: 25%;"
                ></i>
            </button>
        </span>
    </div>
</template>

<style scoped>
.rounded-start {
    border-radius: .25rem 0 0 .25rem !important;
}

.rounded-end {
    border-radius: 0 .25rem .25rem 0 !important;
}
</style>

