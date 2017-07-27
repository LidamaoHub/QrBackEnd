<template>
<div class="admin" style="padding:20px 15px">
	<header-nav></header-nav>
<router-view></router-view>	

</div>
	
</template>
<script>
	// import { conf } from '../conf' ;
	import HeaderNav from './header'
export default {
	components:{
		HeaderNav
	},
        data() {
                return {

                }
            },
            created() {},
            methods: {},
mounted(){}

	}


    
</script>