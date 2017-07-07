import React from "react";
import { connect } from "react-redux";
import { IconButton, AppBar } from "material-ui";
import MenuIcon from "material-ui/svg-icons/navigation/menu";
import ArrowBackIcon from "material-ui/svg-icons/navigation/arrow-back";
import { browserHistory } from "react-router";

import ZendeskImage from "../../images/zendesk-relationshapes-logo.svg";

const MenuIconButton = () =>
    <IconButton>
        <MenuIcon style={{ width: 30, height: 40, fill: "#03363d" }} />
    </IconButton>;

const BackButton = () =>
    <IconButton onTouchTap={browserHistory.goBack}>
        <ArrowBackIcon style={{ width: 30, height: 40, fill: "#03363d" }} />
    </IconButton>;

const TopBarLg = ({ home }) =>
    <AppBar
        style={{ background: "#fff" }}
        iconElementLeft={home ? <MenuIconButton /> : <BackButton />}
        title={
            <div
                style={{
                    color: "#03363d",
                    display: "flex",
                    verticalAlign: "center"
                }}
            >
                <a
                    style={{
                        verticalAlign: "center",
                        position: "relative",
                        float: "left",
                        color: "#03363d",
                        fontFamily: "Roboto"
                    }}
                >
                    <img alt="zendesk" src={ZendeskImage} height={40} />
                </a>
                Ticket Viewer
            </div>
        }
    />;

const TopBar = props => {
    const home = props.home;
    return <TopBarLg home={home} />;
};

export default connect()(TopBar);
