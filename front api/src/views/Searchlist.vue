<template>
  <br />
  <h1>Search Website</h1>
  <hr />
  <div class="container">
    <div class="row">
      <div class="col-4">
      </div>
      <div class="col-4">
        <form @submit.prevent="searcWebsite">
          <br />
          <div class="form-group">
            <label for="exampleInputPassword1">Searching:</label>
            <input
              class="form-control"
              type="text"
              v-model="queryweb"
              placeholder="website input"
            />
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </div>
      <div class="col-4">
      </div>
    </div>
  </div>
  <div>
    <br />
    <h3>THESE ARE LINKS IN WEBSITE</h3>
    <hr />

     
      <History :history="x" v-for="x in history" :key="x.id" />
    
    <!-- <div>
      <h4 id="History">History</h4>
      <History :dataBM25="k" v-for="k in dataBM25" :key="k.id" />
    </div> -->
  </div>
</template>

<script>
import Service from "../services/DataService.js";
import History from "../components/History.vue";
// import History from "../components/History.vue";
export default {
  name: "Searchlist",
  components: {
    History,
    // History,
  },
  data() {
    return {
      queryweb: "",
      history: null,
   
    };
  },
  methods: {
    searcWebsite() {
      console.log(this.queryweb);
      Service.searcWebsite(this.queryweb)
        .then((response) => {
          this.history = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    }
  },
  created() {},
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
#Storage{
  color: white;
}
#History{
  color: white;
}
</style>
