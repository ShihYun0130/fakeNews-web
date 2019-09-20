import Home from './components/Home';
import NewsInput from './components/NewsInput';
import ShowResult from './components/ShowResult';
import NewsList from './components/NewsList';
import PageNotFound from './components/PageNotFound';
import UserList from './components/UserList';
import Chart from './components/Chart';
import About from './components/About';



const routes = [
  { path: '/', redirect: '/Home' },
  { path:'/Home', component: Home },
  { path:'/NewsInput', component: NewsInput },
  { path:'/ShowResult', component: ShowResult },
  { path:'/NewsList', component: NewsList},
  { path:'/UserList', component: UserList},
  { path:'/Chart', component: Chart},
  { path:'/About', component: About},


  { path: '*', component: PageNotFound }
];

export default routes;
