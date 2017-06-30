<template>
    <div>
        <top></top>
        <router-view></router-view>
    </div>

</template>
<script>
    import {conf} from '../../conf';
    import Top from "../c/top"
 
    export default {
        components: {
            Top
        },
        data() {
            return {

            }
        },
        created() {
            let self = this
            self.$http.get(conf.url+"/check").then(function (re) {
                if (re.body.err) {
                    console.log(re)
                    self.$router.push({
                        path: '/admin/login'
                    })


                }
            })

        },
        methods: {}
        
    }
</script>