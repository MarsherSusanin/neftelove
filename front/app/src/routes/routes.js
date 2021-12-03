import DashboardLayout from '../layout/DashboardLayout.vue'
// GeneralViews
import NotFound from '../pages/NotFoundPage.vue'

// Admin pages
import Overview from '../pages/Overview.vue'
import TaskList from '../pages/TaskList.vue'
import TaskAdd from '../pages/TaskAdd.vue'
import TaskUpdate from '../pages/TaskUpdate.vue'
import MaterialList from '../pages/MaterialList.vue'
import AlertList from '../pages/AlertList.vue'

const routes = [
  {
    path: '/',
    component: DashboardLayout,
    redirect: '/admin/overview'
  },
  {
    path: '/admin',
    component: DashboardLayout,
    redirect: '/admin/overview',
    children: [
      {
        path: 'overview',
        name: 'Overview',
        component: Overview
      },
      {
        path: 'tasks',
        name: 'Tasks',
        component: TaskList,
      },
      {
        path: 'tasks/add',
        name: 'CreateTask',
        component: TaskAdd
      },
      {
        path: 'tasks/:id',
        name: 'UpdateTask',
        component: TaskUpdate
      },
      {
        path: 'materials',
        name: 'Materials',
        component: MaterialList,
      },
      {
        path: 'alertList',
        name: 'AlertList',
        component: AlertList,
      },
    ]
  },
  { path: '*', component: NotFound }
]

/**
 * Asynchronously load view (Webpack Lazy loading compatible)
 * The specified component must be inside the Views folder
 * @param  {string} name  the filename (basename) of the view to load.
function view(name) {
   var res= require('../components/Dashboard/Views/' + name + '.vue');
   return res;
};**/

export default routes
