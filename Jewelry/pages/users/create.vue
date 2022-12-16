<template>
    <section>
        <h1>Создание пользователя</h1>

        <div class="form-group">
        Имя <input type="name" class="form-control">
        </div>

        <div class="form-group">
        Почта <input type="email" class="form-control">
        </div>

        <div class="form-group">
        Логин <input type="login" class="form-control">
        </div>

        <div class="form-group">
        Пароль <input type="password" class="form-control">
        </div>

        <button class="btn btn-primaty" @click.prevent="createUser(user)">Создать</button>

        <div>
            <nuxt-link to="/">На главную</nuxt-link>
        </div>
    </section>
</template>



<style scoped>
form {
    width: 600px;
}
</style>


<script>
export default {
    // methods: {
    //     async createUser(id) {
    //         await $axios.$post('http://127.0.0.1:8000/user/'+id)
    //     },
    // }
}
</script>