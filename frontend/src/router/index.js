import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home/Home'
import Main from '@/views/Home/Main'
import Project from '@/views/Home/Project'
import Team from '@/views/Home/Team'
import Welcome from '@/views/Home/Main/Welcome'
import Verify from '@/views/Home/Main/Verify'
import Demo from '@/views/Home/Main/Demo'
import Repair from '@/views/Home/Main/Repair'
import Attack from '@/views/Home/Main/Attack'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect: '/home'
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/logo',
    redirect: '/home'
  },
  {
    path: '/home',
    component: Home,
    redirect: '/main',
    children: [
      {
        path: '/main',
        component: Main,
        redirect: '/welcome',
        children: [
          {
            path: '/welcome',
            component: Welcome
          },
          {
            path: '/verify',
            component: Verify
          },
          {
            path: '/attack',
            component: Attack
          },
          // {
          //   path: '/image',
          //   redirect: '/adversarial',
          //   component: Image,
          //   children: [
          //     {
          //       path: '/adversarial',
          //       component: Adversarial
          //     },
          //     {
          //       path: '/backdoor',
          //       component: Backdoor
          //     }
          //   ]
          // },
          {
            path: '/repair',
            redirect: '/demo',
            component: Repair,
            children: [
              {
                path: '/demo',
                component: Demo
              }
            ]
          },
          {
            path: '/project',
            component: Project
          }
          // {
          //   path: '/text',
          //   component: Textattack
          // }
        ]

      },
      // {
      //   path: '/project',
      //   component: Project
      // },
      {
        path: '/team',
        component: Team
      }
    ]
  }
]

const router = new VueRouter({
  routes
})

export default router
