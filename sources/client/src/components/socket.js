// socket.js
export function connect(uuid, veh_id, bus_route_id, targetBus) {
    const socket = new WebSocket(`ws://localhost:8000/ws/target_bus/${uuid}/${veh_id}/${bus_route_id}/`);

    socket.onopen = () => {
        console.log('Web Socket is created')
    };

    // Listen for incoming messages and update targetBus
    socket.onmessage = (event) => {
        const data = JSON.parse(event.data);
        console.log("targetBus.value set to ", data)
        targetBus.value = data
    };

    socket.onerror = (error) => {
        console.error('WebSocket error: ', error);
    };

    socket.onclose = (event) => {
        console.log('WebSocket closed: ', event);
    };

    return socket
}


export function disconnect(socket) {
    socket.close();
}