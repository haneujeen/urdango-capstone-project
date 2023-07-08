<!-- Switch.vue -->
<script setup>
import { ref, watch, onMounted } from 'vue'
import axios from 'axios';
import { useStore } from 'vuex'

const applicationServerPublicKey = 'BCF8KCNOWaJWdTyTnRZF0cvEahPTLDzF9kO_rwqSYYIT-WDb9vi4ghVl9ztPig-pdAb1pLm4xYxOdziElgosz3Q';
const store = useStore();
const uuid = store.state.uuid;
let isChecked = ref(false);
const isDisabled = ref(false);
const BASE_URL = 'http://localhost:8000'

// Check service worker and push manager support onMounted
onMounted(async () => {
    if ('serviceWorker' in navigator && 'PushManager' in window) {
        try {
            const registration = await navigator.serviceWorker.ready;
            const subscription = await registration.pushManager.getSubscription();
            console.log('Service Worker ready state:', navigator.serviceWorker.ready);
            if (subscription) {
                isChecked.value = true;
            }
        } catch (error) {
            console.error('Error during serviceWorker.ready or getSubscription(): ', error);
        }
    } else {
        console.log('Service Worker and/or Push Manager is not supported in this browser');
        isDisabled.value = true
    }
});

watch(isChecked, async (newVal) => {
    if ('serviceWorker' in navigator && 'PushManager' in window) {
        const registration = await navigator.serviceWorker.ready;
        if (newVal) {
            await subscribeUserToPush(uuid, registration);
        } else {
            await unsubscribeUserFromPush(uuid, registration);
        }
    }
});

const convertBase64ToUint8Array = (base64String) => {
    const padding = '='.repeat((4 - (base64String.length % 4)) % 4);
    const base64 = (base64String + padding)
        .replace(/-/g, '+')
        .replace(/_/g, '/');

    const rawData = window.atob(base64);
    const outputArray = new Uint8Array(rawData.length);

    for (let i = 0; i < rawData.length; ++i) {
        outputArray[i] = rawData.charCodeAt(i);
    }

    return outputArray;
};

const subscribeUserToPush = async (uuid, registration) => {
    console.log('Start subscribing')

    let subscription;
    try {
        subscription = await registration.pushManager.subscribe({
            userVisibleOnly: true,
            applicationServerKey: convertBase64ToUint8Array(applicationServerPublicKey),
        });
        console.log('User is subscribed.', subscription.toJSON());
    } catch (error) {
        console.error('Error during subscription: ', error);
        throw error;
    }

    try {
        const response = await axios.post(`${BASE_URL}/subscription/`, {
            uuid: uuid, 
            subscription: subscription.toJSON()
        });

        console.log('Server received the subscription data 📦')
        console.log(response.data);
    } catch (error) {
        console.error('Error during axios post: ', error);
        throw error;
    }

    return response;
};

const unsubscribeUserFromPush = async (uuid, registration) => {
    const subscription = await registration.pushManager.getSubscription();
    if (subscription) {
        await subscription.unsubscribe();
        
        try {
            const response = await axios.delete(`${BASE_URL}/subscription/`, {data: {uuid: uuid}});
            console.log('Unsubscribed from server:', response.data);
        } catch (error) {
            console.error('Error unsubscribing from server:', error);
        }
    }
};
</script>

<template>
    <input 
        class="form-check-input" 
        type="checkbox" 
        role="switch" 
        id="pushNotificationSwitch" 
        :disabled="isDisabled" 
        v-model="isChecked"
    >
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