import Home from './components/Home';
import NewsInput from './components/NewsInput';
import ShowResult from './components/ShowResult';
import History from './components/History';
import PageNotFound from './components/PageNotFound';

const routes = [
  { path: '/', redirect: '/Home' },
  { path:'/Home', component: Home },
  { path:'/NewsInput', component: NewsInput },
  { path:'/ShowResult', component: ShowResult },
  { path:'/History', component: History},
  { path: '*', component: PageNotFound }
];

export default routes;
