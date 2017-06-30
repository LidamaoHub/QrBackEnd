<template>
    <div class="row">

        <div class="col-md-12">
            <div class="row">
                <div class="col-xs-6 col-md-3" v-for="(card,card_i) in loc_list">
                    <div class="thumbnail">
                        <img :src="card.cover.url" alt="封面" v-if="card.cover">
                        <img src="../../assets/img/i.jpg" alt="封面" v-else>
                        <div class="caption">
                            <h3 v-if="card.loc_name">{{ card.loc_name }}</h3>
                            <h3 v-else>未命名场景</h3>
                            <p v-if="card.content">{{ card.content }}</p>
                            <p v-else>未填写场景详细的介绍</p>
                            <p>
                                <router-link :to="'/edit/'+card._id+'/'"> <span class="btn btn-success">编辑</span></router-link>
                                <router-link :to="'/loc/'+card._id+'/'"> <span class="btn btn-primary">进入</span></router-link>

                                <span @click="create_qr(card.id,card_i)" class="btn btn-default" role="button">贴纸</span>
                                <span @click="online(card.id,1,card_i)" class="btn btn-success" role="button" v-if="card.state!=1">上线</span>
                                <span @click="online(card.id,0,card_i)" class="btn btn-danger" role="button" v-else>下线</span>
                                <router-link :to="'loc/'+card._id+'/product'" > <span class="btn btn-primary">商城</span></router-link>
                            </p>
                        </div>
                    </div>
                </div>

            </div>
            <button class="btn btn-primary" @click="new_loc">
                创建新地点
            </button>

        </div>
    </div>
</template>


<script>
    import {
        conf
    }
    from '../../conf'

    export default {
        props: ["message"],
        data() {
            return {
                loc_list: []
            }
        },
        created() {
            var self = this
            self.$http.get(conf.url + "/get_locs").then(function (re) {
                self.loc_list = re.body.locs
                console.log("!!!", self.loc_list)

            })

        },
        methods: {
            new_loc: function () {
                var self = this
                self.$http.post(conf.url + "/add_loc", {
                    "a": 1
                }).then(function (re) {
                    if (!re.body.err) {
                        var loc_id = re.body.loc_id
                        this.$router.push({
                            path: '/edit/' + loc_id
                        })
                    }
                })


            },
            create_qr: function (loc_id, ind) {
                let self = this
                self.$http.post(conf.url + "/get_qr", {
                    "loc_id": loc_id
                }).then(function (re) {
                    if (!re.body.err) {
                        let url = re.body.url
                        console.log(url)
                        self.loc_list[ind].cover.url = url


                    }
                })

            },
            online: function (loc_id, state, i) {
                let self = this
                self.$http.post(conf.url + "/change_online_type", {
                    "state": state,
                    "loc_id": loc_id
                }).then(function (re) {
                    if (!re.body.err) {
                        console.log(re.body)
                        self.loc_list[i].state = state
                        alert("操作成功")
                    } else {

                        if (re.body.type == 1) {
                            let get_money = confirm(re.body.reason)
                            if (get_money) {
                                alert("跳转到付钱")
                            } else {
                                alert("居然不付钱")
                            }
                        } else {
                            alert(re.body.reason)
                        }

                    }

                })

            }

        },



    }
</script>