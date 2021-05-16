<template>
  <div>
    <h3>{{ userName }}</h3>
    <div class="data"><strong>E-mail:</strong> {{ userEmail }}</div>
    <div class="data"><strong>Phone:</strong> {{ userPhone }}</div>
    <div class="data"><strong>City:</strong> {{ userCity }}</div>
    <div class="data"><strong>Languages:</strong> {{ user.lang }}</div>
    <SocialBar :links="links"/>
  </div>
</template>

<script>
import SocialBar from './SocialBar.vue'

export default {
    name: 'PersonnalCard',
    props: ['user', 'links'],
    data() {
      return {
        userName: "Antoine Ulrich Maga",
        userEmail: "maga@yahoo.com",
        userPhone: "699 64 97 11",
        userCity: "Yaoundé, Cameroon"

      };
    },
    components: {
        SocialBar,
    }
}
</script>

<style scoped lang="scss">
    @import '@/styles/constants.scss';

    .data {
        margin-bottom: 15px;
    }
</style>