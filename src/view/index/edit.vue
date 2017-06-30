<template>
    <div id="app">

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
                                    <input type="checkbox" value="time_line" v-model="loc_list">话题
                                </label>
                                <label>
                                    <input type="checkbox" value="reward" v-model="loc_list">捐赠
                                </label>
                                <label>
                                    <input type="checkbox" value="mall" v-model="loc_list">购物
                                </label>
                                <label>
                                    <input type="checkbox" value="notice" v-model="loc_list">公告
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
            <div class="panel-heading">发送公告</div>
            <div class="panel-body">
                <div class="form-horizontal" role="form">

                    <div class="form-group">
                       <p>
                           <textarea name="" id="" cols="30" class="form-control" rows="3" placeholder="请填写公告" v-model="notice.content">{{notice.content}}</textarea>
                       </p>
                        
                    </div>
                    <div class="form-group">
                        <div class="col-sm-offset-2 col-sm-10">
                            <button class="btn btn-default" @click="update_notice">
                                保存
                            </button>
                                                                <span  class="btn btn-default" role="button" @click="addBar">保1存</span>

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
                content:""
                },
                loc_id: "",
                loc_list: [],

            }
        },
        methods: {
            addBar: function() {
			// 触发事件
			eventBus.$emit('addBar',1)	
		},
            update_col: function () {
                let self = this
                let loc_list = self.loc_list
                console.log(loc_list.indexOf("time_line"))
                if (loc_list.indexOf("time_line") < 0) {
                    loc_list.push("time_line")

                }
                self.$http.post(conf.url+"/update_loc", {
                    "loc_info": JSON.stringify({
                        "loc_list": loc_list
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
            update_notice: function () {
                let self = this
                                console.log(self.notice.content)

                if (self.notice != "") {
                    self.$http.post(conf.url+"/update_notice", {
                        "loc_id": self.loc_id,
                        "content": self.notice.content
                    }).then(function (re) {
                        if (!re.body.err) {
                            
                            alert("搞定")
                        }
                    })

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