<template>
    <div>
       <table class="table table-bordered">
				<thead>
					<tr>
						<th style="min-width: 77px">
							发布日期
						</th>
						<th style="min-width: 90px">
							标题
						</th>
						<th>
							内容
						</th>
						<th style="min-width: 90px">
							操作
						</th>
					</tr>
				</thead>
				<tbody>
					<tr v-for='(notice,i) in notices'>
						<td>
							{{notice.time}}
						</td>
						<td>
							{{notice.title}}
						</td>
						<td>
							{{notice.content}}
						</td>
						<td>
							<button class="btn btn-primary" style="margin-bottom:10px;" @click="edit(i)">修改</button>
							<button class="btn btn-danger" @click='del(notice.id,i)'>删除</button>
						</td>
					</tr>
				</tbody>
       </table>
      
        <!-- <a @click="open" role="button" class="btn" data-toggle="modal">需要帮助?</a> -->
                <div class="modal fade" id="856799" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">
                                    ×
                                </button>
                                <h4 class="modal-title" id="myModalLabel">
                                标题
                            </h4>
                            </div>
                            <div class="modal-body">
                                 <div class="form-group">
    <label for="title">标题</label>
    <input type="text" class="form-control" id="title" v-model='temp.title'>
  </div>
   <div class="form-group">
    <label for="content">内容</label>
    <input type="text" class="form-control" id="content" v-model='temp.content' >
  </div>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-default" data-dismiss="modal">
                                    取消
                                </button>
                                <button type="button" class="btn btn-primary" @click="update()">
                                    更新
                                </button>
                            </div>
                        </div>
                    </div>
        </div>   

   </div>


</template>
<script>
	import {conf} from '../../conf' 
export default {
        data() {
                return {
notices:[],
temp:{
	title:"",
	content:"",
	id:''
}
                }
            },
            created() {
            	let self = this
            	let loc_id = self.$route.params["loc_id"]
                self.loc_id = loc_id
            	self.$http.post(conf.url+"/get_notices",{"loc_id":loc_id}).then(function(re){
if(!re.body.err){
self.notices = re.body.notices

console.log(self.notices)
}

            	})

            },
            methods: {
            	edit:function(id){
				let self = this
				let no = self.notices[id]
				self.temp.title = no.title
				self.temp.content = no.content
				self.temp.id = no.id
				self.notice_index = id
				$('#856799').modal()
            	},
            	update:function(){
            		let self = this
            		let t = {"type":'update',"notice":JSON.stringify(self.temp)}
            		
            		self.$http.post(conf.url+"/update_notice",t).then(function(re){
            			if(!re.body.err){
            				alert("修改成功")
            				let id = self.notice_index
            				self.notices[id].content = self.temp.content
    						self.notices[id].title = self.temp.title
    						self.temp = {
											title:"",
											content:"",
											id:''
										}
							$('#856799').modal('hide')
            			}
            		})
            	},
            	del:function(id,index){
            		let self = this
            		let t = {
            			"type":"delate",
            			"id":id
            		}
            		let a = confirm("你确定要删除这条公告么?(无法撤销)")
            		if(a){
            			self.$http.post(conf.url+"/update_notice",t).then(function(re){

            			if(!re.body.err){
            				self.notices.splice(index,1)

            			}
            		})
            		}
            		


            	}

            },
mounted(){}


    }
</script>