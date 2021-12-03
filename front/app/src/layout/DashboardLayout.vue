<template>
  <div class="wrapper">
    <side-bar title="НЕФТЕLOVE" backgroundImage="img/bg.jpg">
      <mobile-menu slot="content"></mobile-menu>
      <sidebar-link to="/admin/overview">
        <i class="nc-icon nc-planet"></i>
        <p>Инфо</p>
      </sidebar-link>
      <sidebar-link to="/admin/tasks">
        <i class="nc-icon nc-spaceship"></i>
        <p>Задания</p>
      </sidebar-link>
      <sidebar-link to="/admin/alertlist">
        <i class="nc-icon nc-alien-33"></i>
        <p>События</p>
      </sidebar-link>

      <template slot="bottom-links">
        <team-bage />
      </template>
    </side-bar>
    <div class="main-panel">
      <top-navbar></top-navbar>

      <dashboard-content @click="toggleSidebar"> </dashboard-content>

      <content-footer></content-footer>
    </div>
  </div>
</template>
<style lang="scss">
</style>
<script>
import TopNavbar from "./TopNavbar.vue";
import ContentFooter from "./ContentFooter.vue";
import DashboardContent from "./Content.vue";
import MobileMenu from "./MobileMenu.vue";
import TeamBage from "../components/TeamBage.vue";
export default {
  components: {
    TopNavbar,
    ContentFooter,
    DashboardContent,
    MobileMenu,
    TeamBage,
  },
  methods: {
    toggleSidebar() {
      if (this.$sidebar.showSidebar) {
        this.$sidebar.displaySidebar(false);
      }
    },
  },
};
</script>
