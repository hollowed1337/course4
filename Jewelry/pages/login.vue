<template>
    <form>
        <h1>Авторизация</h1>

        <div class="form-group">
            <input type="text" class="form-control">
        </div>

        <div class="form-group">
            <input type="password" class="form-control">
        </div>
        <button class="btn btn-primaty">Авторизоваться</button>
        
        <p>
            <nuxt-link to="/">На главную</nuxt-link>
        </p>
    </form>
    
</template>

<script>
export default {
    layout: 'empty'
}
</script>

<style scoped>
form {
    width: 600px;
}

</style>