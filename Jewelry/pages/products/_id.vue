<template>
    <div>
        <h1>{{product.name}}</h1>
        <p>{{product.desc}}</p>
        <hr />
        <p>Количество на складе: {{product.stock}}</p>
        <p>Цена: {{product.price}}</p>
        <p>Скидка: {{product.sale}}</p>
        <p>Вес изделия: {{product.weight}}</p>
        <p>Тип изделия: {{product.prodtype_id}}</p>
        <p>Материал: {{product.material_id}}</p>
        <p>Изображение {{product.image_id}}</p>
    </div>
</template>



<script>
export default {
    validate({params}) {
        return /^\d+$/.test(params.id)
    }, 

    async asyncData({params, error, $axios}) {
        try {
           const product = await $axios.$get('http://127.0.0.1:8000/product/'+params.id)
           return {product}
        } catch (e) {
            error(e)
        }
    }
}
</script>