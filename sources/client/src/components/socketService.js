// socketService.js
export default class SocketService {
    constructor() {
        this.socket = null
    }

    connect(uuid, veh_id, bus_route_id, targetBus) {
        this.socket = new WebSocket(`ws://localhost:8000/ws/target_bus/${uuid}/${veh_id}/${bus_route_id}/`);

        this.socket.onopen = () => {
            console.log('Web Socket is created')
        }

        this.socket.onclose = () => {
            console.log('WebSocket closed')
        }

        this.socket.onerror = (error) => {
            console.error('WebSocket error: ', error)
        }

        // Listen for incoming messages and update targetBus
        this.socket.onmessage = (event) => {
            const data = JSON.parse(event.data)
            console.log("targetBus.value set to ", data)
            targetBus.value = data
        }
    }

    send(data) {
        this.socket.send(JSON.stringify(data));
    }

    disconnect() {
        this.socket.close()
    }
}
