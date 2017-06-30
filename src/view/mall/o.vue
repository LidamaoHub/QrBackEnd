<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-12">
                <table class="table table-bordered">
                    <thead>
                        <tr>
                            <th>时间</th>
                            <th>商品</th>
                            <th>种类</th>
                            <th>姓名</th>
                            <th>手机</th>
                            <th>地址</th>
                            <th>备注</th>
                            <th>处理</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(o,i) in order_list">
                            <td>{{o.timestamp}}</td>
                            <td>{{o.p_name}}</td>
                            <td>{{o.p_type.name}}-{{o.p_type.charge}}</td>
                            <td>{{o.username}}</td>
                            <td>{{o.phone}}</td>
                            <td>{{o.address}}</td>
                            <td>{{o.other}}</td>
                            <td><span class="btn btn-danger"  role="button" @click="del_o(i)">删除</span></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>
<script>
    import {conf} from '../../conf';
    export default {
        created() {
        let self = this
                let loc_id = this.$route.params["loc_id"]
        self.$http.post(conf.url+"/get_order_list",{"obj_id":loc_id}).then(function(re){
        
            if(!re.body.err){
            self.order_list = re.body.order_list 
            }
        })
        
        
        },
            data() {
                return {
                order_list:[]
                }

            },
            methods: {
                del_o:function(i){
                let self = this 
                let order_id = self.order_list[i]._id
                self.$http.post(conf.url+"/del_order",{order_id:order_id}).then(function(re){
                if(!re.body.err){
                self.order_list.splice(i,1)
                }
                })
                }
            
            }


    }
</script>