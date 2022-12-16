<template>
    <section>
        <h1>Список товаров</h1>
        <ul>
            <li v-for="product of products" :key="product.id">
                <a href="#" @click.prevent="goTo(product)">{{product.name}}
                </a>
            </li>
        </ul>
    </section>
    </template>
    
    
    
    <script>
    export default {
        asyncData({$axios, error}) {
            return $axios.$get('http://127.0.0.1:8000/products/?skip=0&limit=100')
            .then(products => {
                return {
                    products
                }
            })
            .catch(err => {
                error(err)
            })
        },
        
        methods: {
            goTo(product) {
                this.$router.push("/products/" + product.id)
            }
        }
    }
    </script>