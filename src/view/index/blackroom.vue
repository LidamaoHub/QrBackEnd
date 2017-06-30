<template>
    <div>
        <table class="table table-bordered" >
            <thead>
                <tr>
                    <th>
                        用户ID
                    </th>
                    <th>
                        用户名
                    </th>
                    <th>
                        OpenId
                    </th>
                    <th>
                        操作
                    </th>
                </tr>
            </thead>
            <tbody>

                <tr v-for="(b,i) in block_list">
                    <td>
                        {{b.user_info['_id']}}
                    </td>
                    <td>
                        {{b.user_info.nick_name}}
                    </td>
                    <td>
                        {{b.user_info.open_id}}
                    </td>
                    <td>
                        <button type="button" class="btn btn-primary" @click="unblock(i)">解封</button>
                    </td>
                </tr>

            </tbody>
        </table>


    </div>
</template>
<script>
    import {
        conf
    }
    from '../../conf'
    export default {

        data() {
                return {
                    block_list: []
                }
            },

            created() {
                let self = this
                let loc_id = self.$route.params["loc_id"]
                self.loc_id = loc_id
                this.$http.post(conf.url + "/get_block_user", {
                    "loc_id": self.loc_id
                }).then(
                    function (re) {
                        if (!re.body.err) {
                            self.block_list = re.body.block_list

                        }
                    }
                )

            },
            methods: {
                unblock: function (i) {
                    let self = this
                    let user_info = self.block_list[i]["user_info"]
                    let user_id = user_info.id
                    self.$http.post(conf.url + "/unblock_user", {
                        "user_id": user_id,
                        "loc_id":self.loc_id
                    }).then(function (re) {
                        if (!re.body.err) {
                            alert("解封成功")
                        }
                    })



                }

            }

    }
</script>