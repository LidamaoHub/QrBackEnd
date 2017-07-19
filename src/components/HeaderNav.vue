<template>
    <div class="row">
        <div class="col-md-12">
            <nav class="navbar navbar-default" role="navigation">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                        <span class="sr-only">Toggle navigation</span><span class="icon-bar"></span><span class="icon-bar"></span><span class="icon-bar"></span>
                    </button>
                    <router-link to='/' class="navbar-brand">一物一码</router-link>
                </div>
                <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                    <ul class="nav navbar-nav">
                        <li class="active">
                            <a href="#">项目首页</a>
                        </li>
                        <li class="dropdown">
                            <a href="#" class="dropdown-toggle" data-toggle="dropdown">场景列表<strong class="caret"></strong></a>
                            <ul class="dropdown-menu">
                                <li v-for="loc in loc_list">
                                    <router-link :to="{path:'/edit/'+loc._id+'/'}">{{loc.loc_name}}</router-link>
                                </li>

                                <!--
                                <li class="divider">
                                </li>
-->

                            </ul>
                        </li>
                        <li>
                            <a href="#">给我付钱</a>
                        </li>
                        

                    </ul>
                    <ul class="nav navbar-nav navbar-right">
                        <li>
                            <a href="#">通知（10）</a>
                        </li>
                        <li class="dropdown">
                            <a href="#" class="dropdown-toggle" data-toggle="dropdown">李大猫先生<strong class="caret"></strong></a>
                            <ul class="dropdown-menu">
                                <li>
                                    <a href="#">账号设置</a>
                                </li>
                                <li>
                                    <a href="#">财务管理</a>
                                </li>
                                <li v-if="open_id_url">
                                    <a :href="open_id_url" target="_blank">绑定支付</a>
                                </li>

                                <li class="divider">
                                </li>
                                <li>
                                    <a href="#" @click="quiet">退出</a>
                                </li>
                            </ul>
                        </li>
                    </ul>
                </div>
            </nav>
        </div>
    </div>
</template>


<script>
    import {
        conf
    }
    from '../conf'
    export default {
        data() {
                return {
                    loc_list: [],
                    init_group_wechat: '',
                    group_id: "",
                    open_id_url: "",
                    open_id:false

                }
            },
            created() {
                var self = this
                self.$http.get(conf.url + "/get_locs").then(function (re) {
                    self.loc_list = re.body.locs
                })
            },
            methods:{
                quiet:function(){
                    let self = this
                    let t = confirm("你确定要退出当前账户吗?")
                    if(t){
                        self.$http.post(conf.url+"/quiet",{}).then(function(re){
if(!re.body.err){
    self.$router.push({
        path:"/user/login"
    })
}

                    })
                    }
                    

                }
            }


    }
</script>