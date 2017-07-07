import React from "react";
import { Provider } from "react-redux";
import ReactDOM from "react-dom";
import { syncHistoryWithStore } from "react-router-redux";
import registerServiceWorker from "./registerServiceWorker";
import "./index.css";
import { Router, browserHistory } from "react-router";
import routes from "./routes";
import myStore from "./store";
import { MuiThemeProvider } from "material-ui";
import injectTapEventPlugin from "react-tap-event-plugin";

import "bootstrap/dist/css/bootstrap.min.css";

injectTapEventPlugin();
const history = syncHistoryWithStore(browserHistory, myStore);

ReactDOM.render(
    <MuiThemeProvider>
        <Provider store={myStore}>
            <Router routes={routes} history={history} />
        </Provider>
    </MuiThemeProvider>,
    document.getElementById("root")
);

registerServiceWorker();
