<template>
    <div>
        <div class="container-fluid">

            <div class="row">
                <div class="col-md-6">
                    <div class="col-sm-6 col-md-8 center-block">
                        <div class="thumbnail">
                            <img src="../../assets/img/i.jpg" alt="..." v-if="!loc_info.cover.url">
                            <img :src="loc_info.cover.url" alt="..." v-else>
                            <div class="caption">
                                <h3>{{loc_info.loc_name}}</h3>
                                <p>{{loc_info.content}}</p>
                                <p>
                                    <router-link :to="'/loc/'+loc_id+'/'"> <span class="btn btn-primary">进入</span></router-link>

                                    <a href="#" class="btn btn-default" role="button">生成贴纸</a></p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-md-6">
                    <h4>创建新地点</h4>
                    <div class="form-group">
                        <label for="exampleInputEmail1">
                            场景名称
                        </label>
                        <input type="email" class="form-control" id="exampleInputEmail1" v-model="loc_info.loc_name" />
                    </div>
                    <div class="form-group">

                        <label for="exampleInputPassword1">
                            介绍文字
                        </label>
                        <textarea class="form-control" id="exampleInputPassword1" v-model="loc_info.content"></textarea>
                    </div>
                    <div class="form-group">

                        <label for="exampleInputFile">
                            上传图片
                        </label>
                        <input type="file" multiple name="upload" @change="prepare_img" style="display:none" id="add_img">
                        <div class="row">
                            <div class="col-md-3 col-xs-3" style="margin-bottom:20px" onclick="document.getElementById('add_img').click()"><img src="../../assets/img/add_img.jpg" style="border:1px dashed gray" alt="..." class="img-rounded img-responsive"></div>

                            <div class="col-md-3 col-xs-3 " style="margin-bottom:20px" v-for="(img,i) in loc_info.img_list">
                                <img :src="img.url" alt="上传图片" class="img-rounded img-responsive new_img_upload">
                                <span class="img_del" @click="del_img(i)">x</span>
                                <span class="img_upload_info " v-if="img.upload==0||img.upload==1">{{['未上传','上传中'][img.upload]}}</span>

                            </div>

                        </div>
                        <button type="submit" class="btn btn-default" @click="upload_img">
                            上传图片
                        </button>
                        
                    </div>
                    
                    <button type="submit" class="btn btn-default" @click="save_loc">
                        保存
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    import "lrz"

    import {conf} from '../../conf'

    export default {

        data() {
                return {
                    loc_info: {
                        content: "",
                        loc_name: "",
                        img_count: 0,
                        img_list: [],
                        cover: {},
                        loc_list: []

                    },
                    loc_id: ""

                }
            },
            methods: {
                prepare_img: function (e) {
                    var self = this
                    var files = e.target.files
                    for (var i = 0; i < files.length; i++) {
                        lrz(files[i]).then(function (r) {
                            console.log(r.origin)
                            self.loc_info.img_list.push({
                                "img_f": r.file,
                                "url": r.base64,
                                "upload": 0
                            })

                        })
                    }


                },
                del_img: function (i) {
                    var self = this
                    self.loc_info.img_list.splice(i, 1)

                    if (self.loc_info.img_list[i]["url"]) {

                    }

                },
                upload_img: function () {
                    var self = this
                    self.loc_info.img_list.forEach(function (e, i) {
                        if (e.upload == 0) {
                            var files = e.img_f
                            self.loc_info.img_list[i]["upload"] = 1
                            var form_data = new FormData()
                            form_data.append("files", files)
                            self.$http.post(conf.url+"/upload_img", form_data).then(function (re) {
                                if (!re.body.err) {
                                    console.log("zjjkdhakls",re.body)
                                    self.loc_info.img_list[i]["upload"] = 2
                                    self.loc_info.img_list[i]["url"] = re.body.url
                                    self.loc_info.img_list[i]["info"] = ""
                                    self.loc_info.img_list[i]["src"] = re.body.url
                                    self.loc_info.img_list[i]["h"] = re.body.h
                                    self.loc_info.img_list[i]["w"] = re.body.w

                                }
                            })
                        }
                    })


                },
                save_loc: function () {
                    var self = this
                    var loc_info = self.loc_info
                    console.log(loc_info)
                    var img_l = loc_info.img_list.map(function (x) {
                        return {
                            "url": x.url,
                            "upload": 2,
                            "info": x.info,
                            "src": x.url,
                            "h":x.h,
                            "w":x.w
                        }
                    })
                    if (img_l.length > 0 && Object.keys(self.loc_info.cover) == 0) {
                        let cover = img_l.splice(0, 1)
                        self.loc_info.cover = cover[0]
                    }
                    self.loc_info.img_list = img_l

                    self.$http.post(conf.url+"/update_loc", {
                        "loc_info": JSON.stringify(self.loc_info),
                        "loc_id": self.$route.params["loc_id"]
                    }).then(function (re) {
                        if (!re.body.err) {
                            self.$router.push({
                                path: '/'
                            })

                        }
                    })


                }
            },
            created() {
                var self = this
                let loc_id = self.$route.params['loc_id']
                self.loc_id = loc_id
                this.$http.post(conf.url+"/get_loc", {
                    "loc_id": loc_id
                }).then(function (re) {
                    if (!re.body.err) {
                        self.loc_info = re.body.loc_info
                        console.log(self.loc_info.cover)
                    }

                })

            }
    }
</script>