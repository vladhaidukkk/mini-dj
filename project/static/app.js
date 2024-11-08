const { createApp, ref } = Vue;

createApp({
  setup() {
    const orders = ref([]);

    axios.get('/api/orders?format=json').then((response) => {
      orders.value = response.data;
    });

    return {
      orders,
    };
  },
}).mount('#app');
