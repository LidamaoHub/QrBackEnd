<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-12">
                <div class="row">
                    <div class="col-md-3">

                        <div class="thumbnail">
                            <img src="https://cdn.dribbble.com/users/5276/screenshots/3534703/pig_allyoucaneat_kendrickkidd_1x.jpg" alt="..." v-if="p_info.p_cover.url==''">
                            <img :src="p_info.p_cover.url" alt="..." v-else>

                            <div class="caption">
                                <h3><span v-if="p_info.p_name">{{p_info.p_name}}</span><span v-else>商品名称</span></h3>
                                <p><span v-if="p_info.p_intro">{{p_info.p_intro}}</span><span v-else>商品名称</span></p>
                                <span v-for="c in p_info.p_type"><span type="button" class="btn btn-default" >{{c.name }} - {{c.charge}}</span>&nbsp;</span>

                            </div>

                        </div>
                    </div>
                    <div class="col-md-9">
                        <div>
                            <div class="form-group">
                                <label for="exampleInputEmail1">商品名称</label>
                                <input type="text" class="form-control" id="exampleInputEmail1" placeholder="商品名称" v-model="p_info.p_name">
                            </div>
                            <div class="form-group">
                                <label for="exampleInputPassword1">商品简介</label>
                                <input type="text" class="form-control" id="exampleInputPassword1" placeholder="商品简介" v-model="p_info.p_intro">
                            </div>
                            <div class="form-group">
                                <label for="exampleInputFile">上传封面</label>
                                <input type="file" id="exampleInputFile" @change="prepare_img">
                                <p v-if="info" style="color:red">{{info}}</p>

                            </div>
                            <div v-for="(c,i) in p_info.p_type">
                                <div class="form-inline">
                                    <div class="form-group">

                                        <div class="input-group">
                                            <div class="input-group-addon">类型名称</div>
                                            <input type="text" class="form-control" id="exampleInputAmount" placeholder="类型名称" v-model="c.name">
                                        </div>
                                    </div>
                                    <div class="form-group">

                                        <div class="input-group">
                                            <div class="input-group-addon">类型价格</div>
                                            <input type="number" class="form-control" id="exampleInputAmount" placeholder="类型价格" v-model="c.charge">
                                            <div class="input-group-addon">元</div>
                                        </div>
                                    </div>
                                    <button class="btn btn-danger" @click="del_type(i)">删除</button>
                                </div>
                                <br>
                            </div>
                            <button class="btn btn-default" @click="add_type">增加一个商品类型</button>
                            <br>
                            <br>
                            <button class="btn btn-primary" @click="save_p">保存商品</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    import "lrz"
import {conf} from '../../conf';
    export default {
        data() {
                return {
                    p_id: "",
                    p_info: {
                        p_name: "",
                        p_intro: "",
                        p_cover: {},
                        p_type: [
                            {
                                name: "第一种",
                                charge: 369
                        }]
                    },
                    info: ""
                }
            },
            created() {
                let self = this
                let p_id = self.$route.params["p_id"]
                self.p_id = p_id
                self.$http.post(conf.url+"/get_p", {
                    "_id": p_id
                }).then(function (re) {
                    if (!re.body.err) {
                        console.log(re)
                        self.p_info = re.body.p
                    }
                })

            },
            methods: {
                add_type: function () {
                    let self = this
                    self.p_info.p_type.push({
                        name: "新类型",
                        charge: 0
                    })


                },
                del_type: function (i) {
                    let self = this
                    self.p_info.p_type.splice(i, 1)
                },
                save_p: function () {
                    console.log("11")
                    let self = this
                    self.$http.post(conf.url+"/update_p", {
                        "info": JSON.stringify(self.p_info),
                        "_id": self.p_id
                    }).then(function (re) {
                        if (!re.body.err) {
                            self.$router.push({
                                path: '/loc/'+self.$route.params["loc_id"]+'/product'

                            })

                        }
                    })

                },

                prepare_img: function (e) {

                    let self = this
                    var f = e.target.files[0]
                    self.info = "图片上传中,请勿操作"
                    lrz(f).then(function (r) {
                        console.log(r.origin)
                        var form_data = new FormData()
                        form_data.append("files", f)

                        self.$http.post(conf.url+"/upload_img", form_data).then(function (re) {
                            if (!re.body.err) {

                                self.p_info.p_cover.url = re.body.url
                                self.p_info.p_cover.name = self.p_info.p_name
                                self.info = ""


                            }
                        })
                    })



                },


            }

    }
</script>