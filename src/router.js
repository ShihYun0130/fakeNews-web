import Home from './components/Home';
import NewsInput from './components/NewsInput';
import ShowResult from './components/ShowResult';
import ShowResult2 from './components/ShowResult2';
import NewsList from './components/NewsList';
import PageNotFound from './components/PageNotFound';
import UserList from './components/UserList';
import Statistics from './components/Statistics';
import About from './components/About';
import ShowUserResult from './components/ShowUserResult';
import ErrorPage from './components/ErrorPage';



const routes = [
  { path: '/', redirect: '/Home' },
  { path:'/Home', component: Home },
  { path:'/NewsInput', component: NewsInput },
  { path:'/ShowResult', name: "ShowResult", component: ShowResult },
  { path:'/ShowResult2', name: "ShowResult2", component: ShowResult2 },
  { path:'/NewsList', component: NewsList},
  { path:'/UserList', component: UserList},
  { path:'/Statistics', component: Statistics},
  { path:'/About', component: About},
  { path:'/ShowUserResult', component: ShowUserResult },
  { path:'/ErrorPage', name: "ErrorPage", component: ErrorPage },
  { path: '*', component: PageNotFound }
];

export default routes;
