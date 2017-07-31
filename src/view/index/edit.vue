<template>
    <div id="app">
<div class="col-sm-6"></div>
        <div class="panel panel-default">
            <div class="panel-heading">栏目设置</div>
            <div class="panel-body">
                <form class="form-horizontal" role="form">

                    <div class="form-group">
                        <label for="chec" class="col-sm-2 control-label">
                            显示栏目
                        </label>
                        <div class="col-sm-10" id="chec">
                            <div class="checkbox">
                                <label>
                                    <input type="checkbox" value="time_line" v-model="column">话题
                                </label>
                                <label>
                                    <input type="checkbox" value="reward" v-model="column">捐赠
                                </label>
                                <label>
                                    <input type="checkbox" value="mall" v-model="column">购物
                                </label>
                                <label>
                                    <input type="checkbox" value="notice" v-model="column">公告
                                </label>
                            </div>
                        </div>
                    </div>
                    <div class="form-group">
                        <div class="col-sm-offset-2 col-sm-10">
                            <button class="btn btn-default" @click="update_col">
                                保存
                            </button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
        <div class="panel panel-default">
            <div class="panel-heading">组设置（暂时不可用）</div>
            <div class="panel-body">
                <form class="form-horizontal" role="form">

                    <div class="form-group">
                        <label for="chec" class="col-sm-2 control-label">
                            选择该地点所在组
                        </label>
                        <div class="col-sm-10" id="chec">
                            <div class="checkbox">
                                <label>
                                    <input type="checkbox">望江组
                                </label>
                                <label>
                                    <input type="checkbox">江安组
                                </label>
                                <label>
                                    <input type="checkbox">华西组
                                </label>
                                <label>
                                    <input type="checkbox">锦江组
                                </label>



                            </div>
                        </div>
                    </div>
                    <div class="form-group">
                        <div class="col-sm-offset-2 col-sm-10">
                            <button class="btn btn-default" @click="update_col">
                                保存
                            </button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
        <div class="panel panel-default">
            <div class="panel-heading">新增公告</div>
            <div class="panel-body">
                <div class="form-horizontal" role="form">

                    <div class="form-group">
                       <p class="col-sm-12">
                           <input name="" id="" class="form-control" placeholder="请填写标题" v-model="notice.title">
                       </p>
                       <p class="col-sm-12">
                           <textarea name="" id="" cols="30" class="form-control" rows="3" placeholder="请填写公告" v-model="notice.content">{{notice.content}}</textarea>
                       </p>
                        
                    </div>
                    <div class="form-group">
                        <div class="col-sm-12">
                            <button class="btn btn-default" @click="new_notice">
                                保存
                            </button>
                            

                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="panel panel-default">
            <div class="panel-heading">配文设置</div>
            <div class="panel-body">
                <div class="row">
                    <div class="col-sm-6 col-md-4">
                        <div class="thumbnail">
                            <img :src="loc_info.cover['url']" alt="...">
                            <div class="caption">
                                <h3>封面图片</h3>
                                <!--                                        <p><a href="#" class="btn btn-primary" role="button">更换图片</a> </p>-->
                            </div>
                        </div>
                    </div>
                    <div class="col-sm-6 col-md-4" v-for="card in loc_info.img_list">
                        <div class="thumbnail">
                            <img :src="card.url" alt="...">
                            <div class="caption">
                                <p>
                                    <textarea name="" id="" cols="30" class="form-control" rows="3" placeholder="请填写相册详细介绍" v-model="card.info"></textarea>
                                </p>
                                <p>
                                    <!--                                        <a href="#" class="btn btn-primary" role="button">更换图片</a>-->
                                    <span  class="btn btn-default" role="button" @click="update_img_intro">保存</span></p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>


</template>
<script>
    import FooterNav from '../../components/FooterNav';
    import HeaderNav from "../../components/HeaderNav";
    import LeftMenu from "../../components/LeftMenu";
    import {conf} from '../../conf'
import eventBus from '../../enentbus'
    export default {
        components: {
            FooterNav, HeaderNav, LeftMenu
        },
        data() {
            return {
                loc_info: {
                    cover: {
                        url: ""
                    },
                    content: ""

                },
                notice: {
                    title:"",
                content:""
                },
                loc_id: "",
                column: [],

            }
        },
        methods: {
            //之后也不会有loc_list了
            update_col: function () {
                let self = this
                let column = self.column
              
                if (column.indexOf("time_line") < 0) {
                    column.push("time_line")

                }
                self.$http.post(conf.url+"/update_loc", {
                    "loc_info": JSON.stringify({
                        "column": column
                    }),
                    "loc_id": self.loc_id
                }).then(function (re) {
                    if (!re.body.err) {
                        alert("成功")
                    }
                })

            },
            update_img_intro: function () {
                let self = this
                let card_img_list = JSON.stringify({
                    "img_list": self.loc_info.img_list
                })
                self.$http.post(conf.url+"/update_loc", {
                    "loc_info": card_img_list,
                    "loc_id": self.loc_id
                }).then(function (re) {
                    if (!re.body.err) {
                        alert("成功")
                    }
                })


            },
            new_notice: function () {
                let self = this
                if (self.notice != ""&&self.notice.content!=""&&self.notice.title!="") {
                    self.$http.post(conf.url+"/new_notice", {
                        "loc_id": self.loc_id,
                        "content": self.notice.content,
                        "title":self.notice.title
                    }).then(function (re) {
                        if (!re.body.err) {
                            let fa = confirm("确定发送?")
                            if(fa){
                                self.notice.content = ""
                                self.notice.title = ""
                                alert("发送成功")
                            }
                        }
                    })

                }else{
                    alert("请填写内容")
                }


            }

        },
        created() {
            let self = this
            let loc_id = self.$route.params["loc_id"]
            self.loc_id = loc_id
            self.$http.post(conf.url+"/get_loc", {
                "loc_id": loc_id
            }).then(function (re) {
                if (!re.body.err) {
                    let loc_info = re.body.loc_info
                    self.loc_info = loc_info
                    self.loc_list = loc_info.loc_list
                    self.column = loc_info.column
                }
            })
            self.$http.post(conf.url+"/get_notice", {
                "loc_id": self.loc_id
            }).then(function (re) {
                if (!re.body.err) {
                    console.log(re.body)
                    self.notice.content = re.body.content
                }
            })
            


        }

    }
</script>