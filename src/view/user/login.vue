<template>

    <div>
        <div class="center-block " style="width:400px;margin-top:100px">
            <h3 style="text-align:center">请先登录</h3>
            <div class="form-group">
                <label for="exampleInputEmail1">输入你的账号</label>
                <input type="email" class="form-control" id="exampleInputEmail1" placeholder="Email" v-model="username">
            </div>
            <div class="form-group">
                <label for="exampleInputPassword1">输入你的密码</label>
                <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password" v-model="password">
            </div>


            <button @click="login()" class="btn btn-default">登录</button>
            <router-link :to="{path:'register'}">
                <button class="btn btn-primary">注册</button>
            </router-link>
        </div>
    </div>




</template>
<script src="https://cdn.bootcss.com/jquery/3.2.0/core.js"></script>
<script>
    import {
        conf
    }
    from '../../conf'
    export default {
        data() {
                return {
                    username: "",
                    password: ""

                }
            },
            methods: {

                login: function () {
                    var self = this
                    if (self.username && self.password) {
                        this.$http.post(conf.url+"/login", {
                            "username": self.username,
                            "password": self.password
                        }).then(
                            function (re) {
                                var r = re.body
                                console.log(r)
                                if(!r.err){
                                this.$router.push({
                            path: '/'
                        })
                                }else{
                                console.log(r)
                                }
                            }
                        )
                    } else {
                        alert("请完善登录信息")
                    }

                }


            }

    }
</script>