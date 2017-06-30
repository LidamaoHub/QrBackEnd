<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-sm-4 col-md-4" v-for="(p,i) in p_list">
                <div class="thumbnail">
                    <img src="https://cdn.dribbble.com/users/5276/screenshots/3534703/pig_allyoucaneat_kendrickkidd_1x.jpg" :alt="p.p_cover.name" v-if="p.p_cover.url==''">
                    <img :src="p.p_cover.url" :alt="p.p_cover.name" v-else>
                    <div class="caption">
                        <h3>{{p.p_name}}</h3>
                        <p>{{p.p_intro}}</p>
                        <p>
                            <router-link :to="'edit/'+p._id" class="btn btn-primary">修改</router-link>
<!--                            <a href="#" class="btn btn-default" role="button">下架(暂时无法使用)</a>-->
                            <span @click="del_card(i)" class="btn btn-default" role="button">删除</span>
                            <router-link :to="'/product/'+p._id" target="_blank" ><span class="btn btn-default">前往页面</span></router-link>
                            </p>
                    </div>
                </div>
            </div>
        </div>
        <button type="button" class="btn btn-primary" @click="create_p" >创建新商品</button>
    </div>

</template>
<script>
    import {conf} from '../../conf';
    export default {
        data() {
                return {
                    p_list: []
                }

            },
            created() {
                let self = this
                let loc_id = this.$route.params["loc_id"]
                this.loc_id = loc_id
                self.$http.post(conf.url+"/get_p_list",{"obj_id":loc_id}).then(function (re) {
                    if (!re.body.err) {
                        self.p_list = re.body.p_list
                    }
                })
            },
            methods: {
                create_p: function () {

                    let self = this
                    self.$http.post(conf.url+"/create_p",{"loc_id":self.loc_id}).then(function (re) {
                        if (!re.body.err) {
                            console.log(re)
                            self.$router.push({
                                path: 'edit/' + re.body._id
                            })

                        }
                    })
                },
                del_card: function (i) {
                    let self = this
                    self.$http.post(conf.url+"/update_p", {
                        "info": JSON.stringify({
                            "state": 1
                        }),
                        "_id": self.p_list[i]["_id"]
                    }).then(function (re) {

                        if (!re.body.err) {
                            console.log(re)
                            self.p_list.splice(i, 1)

                        }
                    })
                }
            }
    }
</script>