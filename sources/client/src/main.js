import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import store from './store'

import 'bootstrap/dist/css/bootstrap.css'

if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js')
    .then((registration) => {
        console.log(registration)
        console.log('ServiceWorker registered with scope: ', registration.scope)
    }).catch((err) => {
        console.log('registration failed :(', err);
    })
}

createApp(App).use(store).mount('#app')

import 'bootstrap/dist/js/bootstrap.js';