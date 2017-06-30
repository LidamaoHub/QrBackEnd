<template>
    <div>
        <div class="container-fluid">
            <header-nav message="hello!"></header-nav>
            <div class="row">
                <div class="col-md-2">
                    <left-menu  ></left-menu>
                </div>
                <div class="col-md-10">
                    <router-view></router-view>
                </div>
            </div>

            <footer-nav></footer-nav>
        </div>
    </div>


</template>
<script>
    import FooterNav from '../../components/FooterNav';
    import HeaderNav from "../../components/HeaderNav";
    import LeftMenu from "../../components/LeftMenu";
    import {conf} from '../../conf'
    export default {
        components: {
            FooterNav, HeaderNav, LeftMenu
        },
        data() {
            return {
            }
        },
        created() {
            this.$http.get(conf.url+"/check").then(
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