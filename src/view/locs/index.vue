<template>
    <div>
        <div class="container-fluid">
            <header-nav ></header-nav>
            <router-view></router-view>
            <footer-nav></footer-nav>
        </div>
    </div>


</template>
<script>
    import FooterNav from '../../components/FooterNav';
    import HeaderNav from "../../components/HeaderNav";
    import {
        conf
    }
    from '../../conf'

    export default {
        components: {
            FooterNav, HeaderNav
        },
        data() {
            return {
                isNowPage: true
            }
        },
        methods: {



        },
        created() {
            this.$http.get(conf.url + "/check").then(
                function (re) {
                    var self = this
                    var r = re.body
                    if (r.err) {

                        this.$router.push({
                            path: '/user/login'
                        })

                    }
                }
            )

        }

    }
</script>