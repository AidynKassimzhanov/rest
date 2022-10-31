const vueApp = Vue.createApp({
    
    el: '#app',
    
    data() {
        return {
            womens: []
        }
 
    },

    created: function () {
        const vm = this;
        axios.get('/api/v1/womenlist')
        .then(function (response) {
            vm.womens = response.data.womens
            console.log(response.data.womens)
        })

    }


  })

  vueApp.mount('#app')