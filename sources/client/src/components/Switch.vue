<!-- Switch.vue -->
<script setup>
import { ref, watch, onMounted } from 'vue'
import axios from 'axios';
import { useStore } from 'vuex'

const store = useStore()
const uuid = store.state.uuid

let isChecked = ref(false)
const isDisabled = ref(false)

// Check service worker and push manager support onMounted
onMounted(() => {
    if ('serviceWorker' in navigator && 'PushManager' in window) {
        navigator.serviceWorker.ready
        .then(function(registration) {
                registration.pushManager.getSubscription()
                .then(function(subscription) {
                    if (subscription) {
                        isChecked.value = true;
                    }
                    console.log('Service Worker ready state:', navigator.serviceWorker.ready);
                }).catch(function(error) {
                    console.log('Error during getSubscription(): ', error);
                });
        }).catch(function(error) {
            console.log('Error during serviceWorker.ready: ', error);
        });
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

const subscribeUserToPush = async (uuid, registration) => {
    console.log('Start subscribing')

    let subscription;
    try {
        subscription = await registration.pushManager.subscribe({
            userVisibleOnly: true,
            applicationServerKey: urlBase64ToUint8Array(
                applicationServerPublicKey,
            ),
        });
        console.log('User is subscribed.', subscription.toJSON());
    } catch (error) {
        console.error('Error during subscription: ', error);
        throw error;
    }

    const data = subscription.toJSON()

    let response;
    try {
        response = await axios.post('http://localhost:8000/subscription/', {
            uuid: uuid, 
            subscription: data
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
        console.log('User is unsubscribed.');
        
        // Send a request to your server to delete the subscription
        try {
            const response = await axios.delete(`http://localhost:8000/subscription/`, uuid);
            console.log('Unsubscribed from server:', response.data);
        } catch (error) {
            console.error('Error unsubscribing from server:', error);
        }
    }
};

const urlBase64ToUint8Array = (base64String) => {
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

const applicationServerPublicKey = 'BCF8KCNOWaJWdTyTnRZF0cvEahPTLDzF9kO_rwqSYYIT-WDb9vi4ghVl9ztPig-pdAb1pLm4xYxOdziElgosz3Q';
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