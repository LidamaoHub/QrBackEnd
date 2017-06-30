<template>

    <div>
        <div class="container-fluid">

            <div class="center-block " style="width:400px;margin-top:100px">
                <h3 style="text-align:center">新组织注册</h3>
                <div class="form-group">
                    <label for="exampleInputEmail1">输入你的邮件</label>
                    <input type="email" class="form-control" id="exampleInputEmail1" placeholder="Email" v-model="username">
                </div>
                <div class="form-group">
                    <label for="exampleInputPassword1">输入你的密码</label>
                    <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password" v-model="pass">
                </div>
                <div class="form-group">
                    <label for="exampleInputPassword2">再次输入密码</label>
                    <input type="password" class="form-control" id="exampleInputPassword2" placeholder="Password" v-model="repass">
                    <br><span v-if="pass!=repass" style="color:red">两次密码不相同</span>
                </div>
                <button @click="register" class="btn btn-default">提交</button>
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
                    username: "",
                    pass: "",
                    repass: ""
                }
            },
            methods: {
                register: function () {
                    var self = this
                    if (self.username && self.pass && self.repass && self.pass == self.repass) {
                        self.$http.post(conf.url+"/regist", {
                            "username": self.username,
                            "password": self.pass
                        }).then(function (re) {
                            var r = re.body
                            if (r.err) {
                                alert("未知错误,注册失败")
                            } else {
                                self.$router.push({
                                    path:'/'
                                })

                            }
                        })

                    } else {
                        alert("请核对你的用户信息")
                    }

                }
            }

    }
</script>