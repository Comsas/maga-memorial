<template>
  <center>
    <div class="photo">
        <a>
            <img :src="getImgUrl()" alt="photo"/>
        </a>
    </div>
  </center>
</template>

<script>
export default {
    name: 'Photo',
    data() {
        return {
            img: "maga2.jpeg"
        };
    },
    methods: {
        getImgUrl() {
            return require('../assets/img/'+this.img);
        },
    },
}
</script>

<style scoped lang="scss">
    .photo {
        a:focus {
            outline: none;
        }
        img {
            width: 200px;
            height: 200px;
            border-radius: 50%;
            display: inline-block;
        }
    }
    img {
        max-width: 100%;
    }
</style>