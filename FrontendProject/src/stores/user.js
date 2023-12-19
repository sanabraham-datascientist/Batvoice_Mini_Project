import { defineStore } from 'pinia'
import axios from 'axios'

export const useUserStore = defineStore({



id: 'user',

state: () => (user,
     {
        isAuthenticated: false,
        id: null,
        name: null,
        is_superuser:false  
}),
actions: {
   
    setUserInfo(user) {
        console.log('setUserInfo', user)
        this.user.id = user.id
        this.user.name = user.name
        this.user.isAuthenticated = user.isAuthenticated
        this.user.is_superuser = user.is_superuser
        console.log("set user");

        localStorage.setItem('user.id', this.user.id)
        localStorage.setItem('user.name', this.user.name)
        localStorage.setItem('user.isAuthenticated', this.user.isAuthenticated)
        localStorage.setItem('user.is_superuser ', this.is_superuser )

        console.log('User', this.user)
    },
}
})