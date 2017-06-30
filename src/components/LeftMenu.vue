<template>
    <ul class="nav nav-stacked nav-pills">
                    <li :class="{'active':$route.name=='LocIndex'}">
                        <router-link to="index" >编辑场景</router-link>
                    </li>
                    <li :class="{'active':$route.name=='LocTopic'}">
                        <router-link to="topic">帖子管理</router-link>
                    </li>
                    <li :class="{'active':$route.name=='LocBlack'}">
                        <router-link to="blackroom">封禁管理</router-link>
                    </li>
                    <li :class="{'active':$route.name=='LocReward'}">
                        <router-link to="reward">捐赠管理</router-link>
                    </li>
                    <li :class="{'active':$route.name=='LocOrder'}">
                        <router-link to="order">订单管理</router-link>
                    </li>
                    <li :class="{'active':$route.name=='MallProduct'}">
                        <router-link to="product">商品列表</router-link>
                    </li>
                    <li :class="{'active':$route.name=='MallOrder'}">
                        <router-link to="mall_order">商品订单</router-link>
                    </li>
                    <li>
                        {{fooCount}}
                    </li>
                    
<!--
                    <li :class="{'active':$route.name=='LocTag'}">
                        <router-link to="tag">生成贴纸</router-link>
                    </li>
-->
                </ul>
</template>
<script>
    import eventBus from '../enentbus'
  
export default{
    data(){
    return {
    fooCount : 0
    }},
    mounted: function() {
		
		// 这里必须将 this 绑定在组件实例上。如果不使用 bind , 也可以使用箭头函数。
	}
}
</script>