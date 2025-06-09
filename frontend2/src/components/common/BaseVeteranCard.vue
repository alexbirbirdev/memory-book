<template >
    <router-link :to="link" class="veteran-card shadow-sm rounded-xl hover:shadow-lg duration-300">
        <img src="/images/soldier-icon.png" alt="">
        <div class="content">
            <h1 class="full-name text-black">Петров Иван Иванович</h1>
            <p class="desc text-black">15.05.1926-07.04.1943</p>
            <p></p>
        </div>
    </router-link>
</template>
<script>
export default {
    name: 'veteran-card',
    props: {
        link: {
            type: String,
            default: ''
        }
    },
    
}
</script>
<style scoped>
.veteran-card {
  background: white;
  padding: 10px;
  /* flex: 1; */
  display: flex;
  flex-direction: row;
  gap: 20px;
}
h1{
    font-weight: 700;
}
p{
    overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  max-width: 150px;
}
</style>