<template>
    <div>
        <h1>{{user.name}}</h1>
        <hr />
        <p>Email: {{user.email}}</p>
        <p>Логин: {{user.login}}</p>
        <p>Данные оплаты: {{user.payment}}</p>
        <p>Дата регистрации: {{user.reg_date}}</p>
        <p>Роль: {{user.role_id}}</p>

        <div>
            <button @click.prevent="deleteUser(user.id)">Удалить</button>
        </div>
        
        <div>
            <button @click.prevent="editUser(user)">Изменить</button>
        </div>
    </div>
</template>


<script>
export default {
    validate({params}) {
        return /^\d+$/.test(params.id)
    },
    async asyncData({params, $axios}) {
        try {
           const user = await $axios.$get('http://127.0.0.1:8000/user/'+params.id)
           return {user}
        } catch (e) {
            error(e)
        }
    },
    methods: {
        async deleteUser(id) {
            await this.$axios.$delete('http://127.0.0.1:8000/user/'+id)
        }, 
        
        editUser(user) {
        }
    }
}
</script>