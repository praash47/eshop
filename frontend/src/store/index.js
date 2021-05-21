import { createStore } from "vuex"
import { accessCookie } from '../views/functions'

const store = createStore({
    state: {
        user: accessCookie("user"),
    }
})

export default store