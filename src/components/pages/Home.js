import React from "react";
import { connect } from "react-redux";
import TopBar from "../app/TopBar";
import { Row, Col } from "react-flexbox-grid";

import TicketCard from "../app/tickets/TicketCard";
import RandomName from "random-name"; //to make dev a bit fun!

class LandingPage extends React.Component {
    render() {
        return (
            <div>
                <TopBar />
                Hello World!
                <Row>
                    <Col xs lg>
                        <TicketCard name={RandomName()} />
                    </Col>
                    <Col xs lg>
                        <TicketCard name={RandomName()} />
                    </Col>
                    <Col xs lg>
                        <TicketCard name={RandomName()} />
                    </Col>
                    <Col xs lg>
                        <TicketCard name={RandomName()} />
                    </Col>
                    <Col xs lg>
                        <TicketCard name={RandomName()} />
                    </Col>
                </Row>
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
