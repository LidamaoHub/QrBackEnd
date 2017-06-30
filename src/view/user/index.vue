<template>

    <div>
        <div class="container-fluid">
            <header-nav></header-nav>

            <router-view></router-view>
            <footer-nav></footer-nav>
        </div>
    </div>




</template>
<script>
    import FooterNav from '../../components/FooterNav';
    import HeaderNav from "../../components/HeaderNav";

    export default {
        components: {
            FooterNav, HeaderNav
        },
        data() {
            return {

            }
        },
        methods: {
            check_session: function (r) {
                var r = r.data
                if (r["err"]) {
                    this.$router.push({path: 'login'})
                } else {
                    return r
                }
            },
            


        }

    }
</script>