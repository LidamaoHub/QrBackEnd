<template>
    <div class="">
        <div class="col-sm-6 col-md-4" v-for="(card,card_i) in topic_info">
            <div class="thumbnail">
                <img src="../../assets/img/i.jpg" alt="..." v-if="card.img_list==0">
                <img :src="card.img_list[0].url" alt="..." v-else>
                <div class="caption">
                    <p>{{ card.content}}</p>
                    <p>
                        <span class="btn btn-primary" role="button" @click="del_topic(card_i)">删除</span>
                        <span class="btn btn-default" role="button" @click="del_user(card_i)">永丰</span></p>
                </div>
            </div>
        </div>
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
                    topic_info: [],
                    loc_id: ""


                }
            },
            created() {
                let self = this
                let loc_id = self.$route.params["loc_id"]
                self.loc_id = loc_id
                self.$http.post(conf.url + "/get_topics", {
                    "loc_id": self.loc_id
                }).then(function (re) {
                    console.log(re)
                    if (!re.body.err) {
                        self.topic_info = re.body.topics
                    }
                })
            },
            methods: {
                del_topic: function (ind) {
                    let self = this
                    let card = self.topic_info[ind]
                    let card_obj = card._id
                    self.$http.post(conf.url + "/del_topic", {
                        "obj_id": card_obj
                    }).then(function (re) {
                        if (!re.body.err) {
                            self.topic_info.splice(ind, 1)
                            alert("成功删除")
                        }
                    })
                },
                del_user: function (ind) {
                    let weather = confirm("真的要永久删除该用户么?删除后该用户无法访问一物一码")
                    if(weather){
                    let self = this
                    let card = self.topic_info[ind]
                    self.$http.post(conf.url + "/del_user", {
                        "user_id": card.user_id,
                        "loc_id":self.loc_id
                    }).then(function (re) {
                        if (!re.body.err) {
alert("操作成功")
                        }

                    })
                    }


                }


            }


    }
</script>