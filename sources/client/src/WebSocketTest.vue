<!-- WebSocketTest.vue -->
<script setup>
let socket;

function openConnection() {
    socket = new WebSocket('ws://localhost:8000/ws/target_bus/veh_id/bus_route_id/');

    socket.onopen = () => {
        socket.send(JSON.stringify({
            'message': 'Hello Server!'
        }));
    };

    socket.onmessage = (event) => {
        console.log('Message from server: ', event.data);
    };

    socket.onerror = (error) => {
        console.error('WebSocket error: ', error);
    };

    socket.onclose = (event) => {
        console.log('WebSocket closed: ', event);
    };
}

function closeConnection() {
    if (socket) {
        socket.close();
    }
}
</script>

<template>
    <div>
        WebSocket Test
        <button @click="openConnection">Open connection</button>
        <button @click="closeConnection">Close connection</button>
    </div>
</template>
