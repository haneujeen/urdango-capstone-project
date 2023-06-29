<!-- Switch.vue -->
<script setup>
</script>

<template>
    <input class="form-check-input" type="checkbox" role="switch" id="pushNotificationSwitch" checked>
</template>

<style scoped>
.form-check-input {
    width: 2.2em;
    height: 1.1em;
}
.form-check-input:checked::before {
    background-color: #ffc107 !important; /* checked color */
}
</style>