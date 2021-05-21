<template>
    <div>
        Please login to view this {{ type }}
    </div>
</template>
<script>
export default {
     name: "LoginToView",
     props: ['type']
}
</script>
<style scoped>
div {
    width: 100%;
    height: 400px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 2em;
    font-family: consolas;
}
</style>