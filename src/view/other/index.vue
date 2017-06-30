<template>
    <div>
        <img :src="x.avatar" alt="" v-for="x in user_list" style="display:inline-block;width:100px;height:100px">

    </div>
</template>
<script>
    import {conf} from '../../conf'

    export default {
        data() {
                return {
                    user_list: []
                }
            },
            created() {
                let self = this
                self.$http.get(conf.url+"/get_user_list_").then(function (re) {
                    console.log(re)
                    self.user_list = re.body.user_list

                })

            }

    }
</script>