import Home from './components/Home';
import NewsInput from './components/NewsInput';
import ShowResult from './components/ShowResult';
import ShowResult2 from './components/ShowResult2';
import NewsList from './components/NewsList';
import PageNotFound from './components/PageNotFound';
import UserList from './components/UserList';
import Chart from './components/Chart';
import About from './components/About';
import ShowUserResult from './components/ShowUserResult';



const routes = [
  { path: '/', redirect: '/Home' },
  { path:'/Home', component: Home },
  { path:'/NewsInput', component: NewsInput },
  { path:'/ShowResult', name: "ShowResult", component: ShowResult },
  { path:'/ShowResult2', component: ShowResult2 },
  { path:'/NewsList', component: NewsList},
  { path:'/UserList', component: UserList},
  { path:'/Chart', component: Chart},
  { path:'/About', component: About},
  { path:'/ShowUserResult', component: ShowUserResult },


  { path: '*', component: PageNotFound }
];

export default routes;
