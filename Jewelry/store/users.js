export const state = ()  => ({
    data: []
})


export const mutations = {
    storeUsers: (state, data) => {
        state.data = data
    }
}