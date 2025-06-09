<template>
    <button class="btn">
        <slot></slot>
    </button>
   
</template>

<script>

export default{
    name: 'base-button'
 

}
</script>


<style scoped>
.btn {
  background: #b71c1c;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 6px;
  cursor: pointer;
  margin-top: 10px;
}
.btn:hover {
  background: #8e1414;
}
</style>