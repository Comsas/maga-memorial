<template>
  <div class="paragraph">
    <h3>{{pres_title}}</h3>
    <div class="begin">{{content.metadata.pres_first}}</div>
    <p>{{content.metadata.pres_second}}</p>
  </div>
</template>

<script>
export default {
    name: 'Description',
    props: ['content'],
    data() {
      return {
        pres_title: "WHO HE WAS ?"
      };
    }
}
</script>

<style scoped lang="scss">
    @import '@/styles/constants.scss';

    .paragraph {
        color: map-get($colors, primary);
        .begin {
            color: map-get($colors, secondary);
        }
    }
</style>