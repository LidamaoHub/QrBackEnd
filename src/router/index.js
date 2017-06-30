import Vue from 'vue'
import Router from 'vue-router'
import VueResource from 'vue-resource'
import Vuex from 'vuex'

import LocEdit from '../view/index/edit'
import LocIndex from '../view/index/index'
import LocReward from '../view/index/reward'
import LocOrder from '../view/index/order'
import LocTag from '../view/index/tag'
import LocTopic from '../view/index/topic'
import LocBlack from '../view/index/blackroom'

import LocsIndex from '../view/locs/index'
import LocsEdit from '../view/locs/edit'
import LocsList from '../view/locs/list'


import UserIndex from '../view/user/index'
import Login from '../view/user/login'
import Register from '../view/user/register'

import Other from '../view/other/index'

import Mall from '../view/mall/index'
import MallEdit from '../view/mall/e'
import MallOrder from '../view/mall/o'
import MallProduct from '../view/mall/p'
import MallFront from '../view/c/index'

Vue.use(Router)
Vue.use(VueResource)
Vue.use(Vuex)

export default new Router({
    routes: [
        {
            path: '/loc/:loc_id',
            name: 'Loc',
            component: LocIndex,
            children: [
                {
                    path: '',
                    name: 'LocIndex',
                    component: LocEdit,
                },
                {
                    path: 'topic',
                    name: 'LocTopic',
                    component: LocTopic
                },
                {
                    path: 'reward',
                    name: 'LocReward',
                    component: LocReward
                },
                {
                    path: 'order',
                    name: 'LocOrder',
                    component: LocOrder
                },
                {
                    path: 'tag',
                    name: 'LocTag',
                    component: LocTag
                },
                {
                    path: 'blackroom',
                    name: 'LocBlack',
                    component: LocBlack
                },
                {
                    path: 'index',
                    name: 'LocIndex',
                    component: LocEdit
                },
                 {
                    path: 'product',
                    name: 'MallProduct',
                    component: MallProduct
                },
                {
                    path: 'edit/:p_id',
                    name: 'MallEdit',
                    component: MallEdit
                },
                {
                    path: 'mall_order',
                    name: 'MallOrder',
                    component: MallOrder
                },
                ]
        },
        {
        path:"mall/:p_id",
            name:"MallFront"
            
        }
,        
        {
            path: '',
            name: 'locs_index',
            component: LocsIndex,
            children: [
                {
                    path: "",
                    name: "locs_list",
                    component: LocsList,
                },
                {
                    path: "edit/:loc_id",
                    name: "locs_list",
                    component: LocsEdit,
                }
            ]

        },
        {
            path: '/user',
            name: 'LoginT',
            component: UserIndex,
            children: [
                {
                    path: 'login',
                    name: 'UserLogin',
                    component: Login,
                },
                {
                    path: 'register',
                    name: 'UserRegister',
                    component: Register,
                },
            ]
        },
        {
            path: '/other',

            component: Other
        }

  ]
})