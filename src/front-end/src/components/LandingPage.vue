 <template>

  <div>
        <b-navbar toggleable="lg" type="dark" variant="info" fixed="top">
          <b-navbar-brand  href="/">Home</b-navbar-brand>
          <b-navbar-brand href="#about">Biography</b-navbar-brand>
          <b-navbar-brand href="#experience">Experience</b-navbar-brand>
          <b-navbar-brand href="#skills">Skills</b-navbar-brand>
          <b-navbar-brand href="#projects">projects</b-navbar-brand>
          <b-navbar-brand href="#">Memories Pics</b-navbar-brand>
          <b-navbar-brand href="#">GuestBook</b-navbar-brand>

          <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
<!--           <b-navbar-nav>
            <b-nav-item href="#">Link</b-nav-item>
            <b-nav-item href="#" disabled>Disabled</b-nav-item>
          </b-navbar-nav> -->

          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-nav-form>
              <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
              <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
            </b-nav-form>

            <b-nav-item-dropdown text="Lang" right>
              <b-dropdown-item href="#">EN</b-dropdown-item>
              <b-dropdown-item href="#">ES</b-dropdown-item>
              <b-dropdown-item href="#">RU</b-dropdown-item>
              <b-dropdown-item href="#">FA</b-dropdown-item>
            </b-nav-item-dropdown>

            <!-- <b-nav-item-dropdown right> -->
              <!-- Using 'button-content' slot -->
              <!-- <template #button-content>
                <em>User</em>
              </template>
              <b-dropdown-item href="#">Profile</b-dropdown-item>
              <b-dropdown-item href="#">Sign Out</b-dropdown-item>
            </b-nav-item-dropdown> -->
          </b-navbar-nav>
        </b-collapse>
        </b-navbar>
        <header class="header parallax">
          <div class="name">
            <div class="wrapper-name">
              <AnimateOnVisible name="fadeDown" ::duration="1">
                <br><br><br>
                <h1>{{ userName }}</h1>
              </AnimateOnVisible>
              <hr />
            <AnimateOnVisible name="fadeUp" ::duration="1">
              <p>{{ userStatus }}</p>
            </AnimateOnVisible>
            </div>
          </div>
        </header>
  </div>
</template>

<script>
export default {
  name: "LandingPage",
  data() {
    return {
      userName: 'Antoine Ulrich Maga',
      userStatus: 'Was Computer scientist, Marketing digital, Community manager and Copywritter Expert'
    };
  },
  methods: {

  }
};

</script>

<style scoped lang="scss">
@import "@/styles/constants.scss";

.header {
  padding: 20px;
  background-color: map-get($colors, dark);
}

.parallax {
  background-image: url("../assets/img/bg.jpg");
  background-attachment: fixed;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  height: 100%;
}

.name {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  margin: 0 auto;
  z-index: 400;

  .wrapper-name {
    width: 250px;
  }

  h1 {
    font-size: 2.3rem;
    padding: 2px 10px;
    text-align: center;
    text-transform: uppercase;
    color: whitesmoke;
  }

  p {
    font-size: 1.5rem;
    text-align: center;
    margin: 5px auto;
    color: whitesmoke;
  }

  hr {
    border: 1px solid whitesmoke;
  }
}

@media (min-width: #{map-get($breakpoints, small)}) {
  .name {
    .wrapper-name {
      width: 55%;
    }
    h1 {
      font-size: 2.8rem;
      padding: 4% 8%;
    }
    p {
      font-size: 2rem;
    }
  }
}
@media (min-width: #{map-get($breakpoints, medium)}) {
  .name {
    .wrapper-name {
      width: 450px;
    }
    h1 {
      font-size: 4rem;
      padding: 4% 10%;
    }
    p {
      font-size: 2.5rem;
    }
  }
}
@media only screen and (max-device-width: 1024px) {
  .parallax {
    background-attachment: scroll;
  }
}
</style>