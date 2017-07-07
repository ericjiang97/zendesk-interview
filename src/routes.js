import React from "react";
import { Route, IndexRoute } from "react-router";

import App from "./components/base/App";
import HomePage from "./components/pages/Home";

const routes = (
    <Route path="/" component={App}>
        <IndexRoute components={HomePage} />
    </Route>
);

export default routes;
