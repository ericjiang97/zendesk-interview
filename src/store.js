import { createStore, combineReducers, applyMiddleware } from "redux";
import thunk from "redux-thunk";

import { routerReducer } from "react-router-redux";

const store = createStore(
    combineReducers({
        routing: routerReducer
    }),
    applyMiddleware(thunk)
);

export default store;
