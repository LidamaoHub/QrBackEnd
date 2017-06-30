<template>

    <div>
        <div class="form parsley-form">

            <div class="panel panel-info">
                <div class="panel-heading" style="display:none;">
                    <h4>
                    <i class="fa fa-shopping-cart"></i>
                    商品信息
                </h4>
                </div>
                <div class="panel-body">
                    <div class="thumbnail">
                        <img src="https://static.bootcss.com/www/assets/img/webpack.png" width="100%" v-if="p.p_cover.url==''">
                        <img :src="p.p_cover.url" width="100%" v-else>
                    </div>
                    <h5 class="description">{{p.p_intro}}</h5>
                    <hr>
                    <div class="form-group">
                        <p class="small">
                        </p>
                        <label class="price">
                            <span class="title">优&nbsp;&nbsp;惠&nbsp;&nbsp;价：</span> <strong><i class="fa fa-cny"></i> {{p.p_type[type_index]['charge']}}</strong>元
                        </label>
                        <br>
                        <label class="price">
                            <span class="title">付款方式：</span> <span>{{payment_method}}</span>
                        </label>
                        <br>
                        <label class="price">
                            <span class="title">运&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;费：</span> <span>{{transport_method}}</span>
                        </label>
                    </div>
                    <div class="form-group">
                        <div data-toggle="buttons">
                            <label class="back_choose btn btn-default lh40 " v-for="(btn,btn_ind) in p.p_type" :class="{'active':btn_ind==type_index}" style="margin-right:10px;margin-top:10px">
                                <input type="radio" @click="change_amount_btn(btn_ind)"> {{btn.name}} {{btn.p_type}}
                                <i></i>
                            </label>
                        </div>
                    </div>

                    <hr>
                    <div class="form-group" style="display:none;">
                        <!--
                    <label>
                        <input min="1" max="99"
                        value="1"
                        autocomplete="off"
                        data-min-message="购买数量不能少于 %s 个"
                        data-max-message="购买数量不能超过 %s 个"
                        data-required-message="请设置商品数量"
                        data-required="true" type="number" id="number"
                        name="number" style="width:70px;" class="form-control" />
                    </label>
                    -->
                        <span style="font-size:16px;color:rgb(87,87,87);font-weight:normal;">总计：</span>
                        <label>1</label>
                        <input type="hidden" id="number" name="number" value="1">
                        <label class="price">
                            × &nbsp;<strong style="color:#ff3300;"><i class="fa fa-cny"></i> 398</strong>
                        </label>
                    </div>
                </div>
            </div>

            <div class="panel panel-info mt10">
                <div class="panel-heading">
                    <h4>
                    <i class="fa fa-user"></i>
                    收货人信息
                </h4>
                </div>
                <div class="panel-body">
                    <div class="form-group">
                        <input type="text" value="" placeholder="收货人" class="form-control" v-model="u.name">
                    </div>
                    <div class="form-group">
                        <input type="text" value="" placeholder="手机号" class="form-control" v-model="u.phone">
                    </div>
                    <address-picker :opts="obj" v-model="u.address">

                    </address-picker>
                    <div class="help-block">若区/县列表中找不到您所在地区，请在“详细街道地址”中注明即可</div>
                    <!-- /#region -->
                    <div class="form-group">
                        <input value="" placeholder="详细街道地址" type="text" class="form-control" v-model="u.address_detail">
                    </div>
                    <div class="form-group">
                        <input value="" placeholder="下单备注" class="form-control" type="text" v-model="u.info">
                    </div>
                </div>
                <!-- /#portlet-content -->
            </div>
            <div class="back_fixed">
                <button type="button" class="buy_now c_txt orange_bg" @click="save_info">提交订单</button>
            </div>

        </div>
<!--
        <p>
            {{ u }}
        </p>
-->
        <div class="alert alert-warning mt10" style="margin-bottom:60px">
            提交订单后，客服将会与你联系进行确认，请保持手机通讯畅通。
        </div>



    </div>
</template>
<script>
    import {conf} from '../../conf';
    export default {
        data() {
                return {
                    p_id: "",
                    obj: {
                        noLabel: false
                    },
                    p: {
                        p_name: "",
                        p_intro: "泰国原产地乳胶枕（一个好枕头要消耗30株泰国橡胶树一天的乳胶产量）",
                        p_type: [
                            {
                                "name": "泰国原产地乳胶枕",

                                "charge": 398
                    }
                    ],
                        p_cover: {
                            url: "http://www.vipchinashangcheng.com//imageFolder/20160323/53647044_1.jpg",
                            name: "名字"
                        },


                    },
                    payment_method: "货到付款",
                    transport_method: "商家包邮",
                    type_index: 0,

                    u: {
                        address: {
                            "province": "",
                            "city": "",
                            "district": ""
                        },
                        phone: "",
                        address_detail: "",
                        name: "",
                        info: ""
                    }
                }
            },
            methods: {
                change_amount_btn: function (i) {
                    var self = this
                    console.log(i)
                    this.type_index = i
                },
                save_info: function () {
                    let self = this
                    let isRight = true
                    var skuId = self.type_index; //套餐ID
                    console.log("!!!", skuId)
                    console.log(1)
                    var name = self.u.name.replace(/(^\s*)|(\s*$)/g, ""); //收货人
                    var tel = self.u.phone.replace(/(^\s*)|(\s*$)/g, ""); //联系手机
                    var province = self.u.address.province.replace(/(^\s*)|(\s*$)/g, ""); //省
                    var city = self.u.address.city.replace(/(^\s*)|(\s*$)/g, ""); //市
                    var area = self.u.address.district.replace(/(^\s*)|(\s*$)/g, ""); //区
                    var address = self.u.address_detail.replace(/(^\s*)|(\s*$)/g, ""); //区
                    var remark = self.u.info.replace(/(^\s*)|(\s*$)/g, "");
                    var rule = /^1[3-8][0-9]\d{4,8}$/;

                    if (name == '') {
                        alert("请填写收货人");
                        isRight = false;
                    } else if (tel == '') {
                        alert("请填写联系手机");
                        isRight = false;
                    } else if (tel.length != 11 || rule.test(tel) == false) {
                        alert("联系手机格式不对");
                        isRight = false;
                    } else if (province == '' || city == '' || area == '') {
                        alert("请选择地区");
                        isRight = false;
                    } else if (address == '') {
                        alert("请填写详细地址");
                        isRight = false;
                    } 
//                    else if (checkSpecChar(remark)) {
//                        alert("备注信息不能有特殊字符!");
//                        isRight = false;
//                    }

                    function checkSpecChar(t) {
                        var temp = false;
                        var re = /^[^@\/\'\\\"#$%&\^\*]+$/;
                        if (re.test(t))
                            temp = false;
                        else
                            temp = true;
                        return temp;
                    }

                    if (isRight) {
                        let o = {
                            p: self.p,
                            type: {
                                name: self.p.p_type[skuId]['name'],
                                charge:self.p.p_type[skuId]['charge'],
                            },
                            username: name,
                            phone: tel,
                            address: province + '-' + city + '-' + area ,
                            other: remark
                        }
                        self.$http.post(conf.url+"/new_order", {
                            "order": JSON.stringify(o)
                        }).then(function (re) {
                            if(!re.body.err){
                            self.$router.push({
                     path: '/success'
                    
                    })
                            }
                        })
                    }

                }

            },
            created() {
                let self = this
                let p_id = self.$route.params["p_id"]
                console.log(p_id)
                self.p_id = p_id
                self.$http.post(conf.url+"/get_p", {
                    "_id": self.p_id
                }).then(function (re) {
                    console.log(re.body.p)
                    if (!re.body.err) {
                        self.p = re.body.p

                    }else{
                    self.$router.push({
                     path: '/err'
                    
                    })
                    }
                })


            }

    }
</script>