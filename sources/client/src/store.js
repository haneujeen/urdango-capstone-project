// store.js
import { createStore } from 'vuex';

export default createStore({
    state() {
        return {
            uuid: null,
        };
    },
    mutations: {
        setUUID(state, uuid) {
            state.uuid = uuid;
        },
    },
});
