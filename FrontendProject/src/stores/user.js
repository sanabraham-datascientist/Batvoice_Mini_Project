import { defineStore } from 'pinia'
import axios from 'axios'

export const useUserStore = defineStore({



id: 'user',

state: () => ({
    user: {
        isAuthenticated: false,
        id: null,
        name: null,
        email: null,
        access: null,
        refresh: null,
    }
}),
actions: {
    initStore() {
        console.log('initStore', localStorage.getItem('user.access'))

        if (localStorage.getItem('user.access')) {
            console.log('User has access!')

            this.user.access = localStorage.getItem('user.access')
            this.user.refresh = localStorage.getItem('user.refresh')
            this.user.id = localStorage.getItem('user.id')
            this.user.name = localStorage.getItem('user.name')
            this.user.email = localStorage.getItem('user.email')
            this.user.isAuthenticated = true

            this.refreshToken()

            console.log('Initialized user:', this.user)
        }
    },

    setToken(data) {
        console.log('setToken', data)

        this.user.access = data.access
        this.user.refresh = data.refresh
        this.user.isAuthenticated = true

        localStorage.setItem('user.access', data.access)
        localStorage.setItem('user.refresh', data.refresh)

        console.log('user.access: ', localStorage.getItem('user.access'))
    },

   

    setUserInfo(user) {
        console.log('setUserInfo', user)

        this.user.id = user.id
        // #this.user.name = user.name
        console.log("set user");
      // this.user.email = user.email

        localStorage.setItem('user.id', this.user.id)
        // localStorage.setItem('user.name', this.user.name)
        localStorage.setItem('user.email', this.user.email)

        console.log('User', this.user)
    },


}
})