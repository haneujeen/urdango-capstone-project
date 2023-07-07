<!-- SearchBar.vue -->
<script setup>
import { ref, onMounted } from 'vue';
import { Tooltip } from 'bootstrap';

onMounted(() => {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new Tooltip(tooltipTriggerEl)
    })
});

const emit = defineEmits(['search']);
const query = ref('');

const search = () => {
    emit('search', query.value);
};

</script>

<template>
    <div class="input-group input-group-lg shadow-sm rounded-3 mt-0">
        <input 
            id="search-input"
            type="text" 
            class="form-control border-0 rounded-start" 
            aria-label="Search station"
            placeholder="Search station"
            v-model="query"
            @keyup.enter="search"
            style="border-right: none;"
            required
        >
        <button 
            id="search-button"
            type="button"
            class="btn bg-white border-0 px-0 pe-2 rounded-end"
            @click="search"
            
        >
            <i class="fas fa-search p-2" 
                style="border-radius: 25%;"
                data-bs-toggle="tooltip" 
                data-bs-title="Search for a train station or a bus stop"
            ></i>
        </button>
    </div>
</template>

<style scoped>
.rounded-start {
    border-radius: .7rem 0 0 .7rem !important;
}

.rounded-end {
    border-radius: 0 .7rem .7rem 0 !important;
}

i {
    color: #bbb;
    transition: background-color 0.5s ease;
}

/* Change the background color of the <i> element when something is typed in the input box */
input:valid ~ .btn > i {
    color: white;
    background-color: #0d6efd !important;
}

input:focus {
    box-shadow: none !important;
}
</style>

