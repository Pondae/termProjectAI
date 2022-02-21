<template>
  <nav class="navbar">
    <router-link to="/storageview" class="nav-link">
      <h5 id="AS">Storage</h5>
    </router-link>
    <router-link to="/" class="nav-link">
      <h5 id="AS">Search Web</h5>
    </router-link>
  </nav>
  <div>
    <router-view />
  </div>
  <br />
  <br />
  <br />
</template>

<script>
export default {};
</script>

<style>
#inline {
  display: inline-block;
  margin-right: 10px;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: rgb(111, 156, 223);
}

.navbar {
  padding: 10px;
  text-align: end;
  background-color: #030853;
}

.page-layout {
  padding: 0 50px 0 50px;
}
#AS {
  color: white;
}
</style>
