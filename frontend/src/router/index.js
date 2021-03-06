import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/product',
    name: 'Product',
    component: () => import('../views/Product.vue')
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue')
  },
  {
    path: '/contact',
    name: 'Contact',
    component: () => import('../views/Contact.vue')
  },
  {
    path: '/wishlist',
    name: 'Wishlist',
    component: () => import('../views/user/Wishlist.vue')
  },
  {
    path: '/profile',
    name: 'Profile',
    component: () => import('../views/user/Profile.vue')
  },
  {
    path: '/cart',
    name: 'Cart',
    component: () => import('../views/Cart.vue')
  },
  {
    path: '/checkout',
    name: 'Checkout',
    component: () => import('../views/user/Checkout.vue')
  },
  {
    path: '/orders',
    name: 'Orders',
    component: () => import('../views/user/Orders.vue')
  },
  {
    path: '/cats',
    name: 'Categories',
    component: () => import('../views/Cats.vue')
  },
  {
    path: '/shop-grid',
    name: 'Shop Grid',
    component: () => import('../views/ShopGrid.vue')
  },
  {
    path: '/shop-grid/:catName',
    name: 'Category',
    component: () => import('../views/ShopGrid.vue')
  },
  {
    path: '/shop-grid/:catName/:subCatName',
    name: 'SubCategory',
    component: () => import('../views/ShopGrid.vue')
  },
  {
    path: '/shop-grid/:search',
    name: 'Search',
    component: () => import('../views/ShopGrid.vue')
  },
  {
    path: '/product/:product_name',
    name: 'Product',
    component: () => import('../views/Product.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
