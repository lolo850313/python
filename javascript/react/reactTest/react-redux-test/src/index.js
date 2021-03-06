import ReactDOM from 'react-dom';
import './index.css';
import Header from './containers/Header';
import Content from './containers/Content';
import {React, Component} from 'react'
import { Provider } from 'react-redux'
import { createStore } from 'redux'

const themeReducer = ( state, action) => {
  if(!state) {
    return {
      themeColor: 'red'
    }
  }

  switch (action.type) {
    case 'CHANGE_COLOR':
      return {
        ...state,
        themeColor : action.themeColor
      }  
    default:
      return state
  }
}

const store = createStore(themeReducer)

class Index extends Component {
  render() {
      return (
          <div>
            <Header />
            <Content />
          </div>
      )
  }
}

ReactDOM.render(
  <Provider store={store}>
    <Index />
  </Provider>,
  document.getElementById('root')
);
