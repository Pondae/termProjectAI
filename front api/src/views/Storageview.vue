<template>
    Kuy
    <Storage :storage="x" v-for="x in storage" :key="x.id" />


</template>

<script>
import Service from "../services/DataService.js";
import Storage from "../components/Storage.vue";
// import History from "../components/History.vue";
export default {
  name: "Searchlist",
  components: {
    Storage,
    // History,
  },
  data() {
    return {
      storage: null,
    };
  },
  methods: {},
  created() {
    Service.storage()
      .then((response) => {
        this.storage = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>

<style scoped>
#Searchresult {
  /* margin: 2%; */
}
.btn-add-color {
  background-color: #2b6bcc;
  color: white;
  font-size: 16px;
  padding: 15px;
  border-radius: 25px;
  border: 0;
  cursor: pointer;
}
.col-4 {
  background-color: rgb(111, 156, 223);
}
#Storage {
  color: white;
}
#History {
  color: white;
}
</style>
