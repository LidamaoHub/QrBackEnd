<template>
    <div id="app">
        <router-view ></router-view>
               
    </div>
</template>

<script>
    import './assets/js/jquery.min.js';
    import './assets/js/bs.js';
    import './assets/js/scripts.js';
    import FooterNav from './components/FooterNav';
    import HeaderNav from "./components/HeaderNav";
    import LeftMenu from "./components/LeftMenu";
 

export default {
        name: 'app',
        components: {
            FooterNav, HeaderNav, LeftMenu
        },
}
</script>
<style lang="css">
    @import './assets/css/bootstrap.min.css';
    @import './assets/css/style.css';
</style>