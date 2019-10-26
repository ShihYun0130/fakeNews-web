<template>
  <div class="errorPage">
    <div class="sorryText">I'm sorry.</div>
    <div class="errorText">很抱歉，查不到這篇新聞的相關資料。<br/>請試著搜尋其他新聞。</div>
  </div>
</template>

<script>
export default {
    name: "ErrorPage",
}
</script>

<style>
.errorPage {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
}
.errorText {
    color: white;
    text-align: center;
}
.sorryText {
    width: 30vw;
    height: 30vw;
    border: white 1px solid;
    margin: 20px;
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 100px;
    font-size: 80px;
}
</style>