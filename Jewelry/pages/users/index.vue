<template>
    <section>
        <h1>Страница пользователей</h1>
        <ul>
            <li v-for="user of users" :key="user.id">
                <a href="#" @click.prevent="goTo(user)">{{user.name}} ({{user.email}})</a>
            </li>
        </ul>
        <button @click.prevent="createUser()">Новый пользователь</button>
    </section>
    </template>
    
    
    
    <script>
    export default {
        asyncData({$axios, error}) {
            return $axios.$get('http://127.0.0.1:8000/users')
            .then(users => {
                return {
                    users
                }
            })
            .catch(err => {
                error(err)
            })
        },
        
        methods: {
            goTo(user) {
                this.$router.push("/users/" + user.id)
            },
            createUser() {
                this.$router.push("/users/create")
            }
        }
    }
    </script>