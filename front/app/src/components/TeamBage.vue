<template>
  <div class="team">
    <div class="team__wrapper">
      <span class="team__text">Created by</span>
      <img class="team__img" src="img/team.jpg">
    </div>
    
  </div>
</template>

<script>
export default {
  name: 'TeamBage'
}
</script>

<style lang="scss">
.team{
  display: flex;
  justify-content: center;

  .team__wrapper{
    display: flex;
    justify-content: center;
    opacity: 0.5;
    border: 2px solid #b277eb;
    padding: 10px;
  }
  

  .team__img{
    height: 105px;
  }

  .team__text{
    writing-mode: vertical-rl;
    text-orientation: upright;
    font-size: 10px;
    text-transform: uppercase;
    text-align: center;
    font-weight: 900;
    color: #b277eb;
    margin-right: 10px;
  }
}
</style>