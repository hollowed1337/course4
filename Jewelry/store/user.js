export const state = ()  => ({
    id:0,
    name:"",
    login:"",
    email:"",
    role_id:0,
    payment:0,
    password:"",
    reg_date:"" 

})


export const mutations = {
    storeId: (state, data) => {
        state.id = data
    },
    storeName: (state, data) => {
        state.name = data
    },
    storeLogin: (state, data) => {
        state.login = data
    },
    storeEmail: (state, data) => {
        state.email = data
    },
    storeRole: (state, data) => {
        state.role_id = data
    },
    storePayment: (state, data) => {
        state.payment = data
    },
    storePassword: (state, data) => {
        state.password = data
    },
}