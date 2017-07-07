import React from "react";
import { connect } from "react-redux";
import TopBar from "../app/TopBar";

class LandingPage extends React.Component {
    render() {
        return (
            <div>
                <TopBar />
                Hello World!
            </div>
        );
    }
}

const mapStateToProps = state => {
    return {
        course: state.course
    };
};

export default connect(mapStateToProps)(LandingPage);
