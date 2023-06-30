<!-- Switch.vue -->
<script setup>
import { ref, watch, onMounted } from 'vue'

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
            await subscribeUserToPush(registration);
        } else {
            await unsubscribeUserFromPush(registration);
        }
    }
});

const subscribeUserToPush = async (registration) => {
    console.log('Start subscribing')
    const subscription = await registration.pushManager.subscribe({
        userVisibleOnly: true,
        applicationServerKey: urlBase64ToUint8Array(
            'BEl62iUYgUivxIkv69yViEuiBIa-Ib9-SkvMeAtA3LFgDzkrxZJjSgSnfckjBJuBkr3qBUYIHBQFLXYp5Nksh8U',
        ),
    });

    console.log('User is subscribed.', JSON.stringify(subscription));
    // TODO: Send the subscription object to server
    return subscription;
};

const unsubscribeUserFromPush = async (registration) => {
    const subscription = await registration.pushManager.getSubscription();
    if (subscription) {
        await subscription.unsubscribe();
        console.log('User is unsubscribed.');
    }
    // TODO: Tell server that this user unsubscribed
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

// Replace with server's public key
const applicationServerPublicKey = 'SERVER_PUBLIC_KEY';
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