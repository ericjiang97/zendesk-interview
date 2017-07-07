import React from "react";
import Avatar from "material-ui/Avatar";
import {
    Card,
    CardActions,
    CardHeader,
    CardMedia,
    CardTitle,
    CardText
} from "material-ui/Card";
import FlatButton from "material-ui/FlatButton";

const CardExampleWithAvatar = props =>
    <Card>
        <CardHeader
            title={props.name}
            subtitle="Client"
            avatar={
                <Avatar>
                    {props.name.split(" ")[0][0] + props.name.split(" ")[1][0]}
                </Avatar>
            }
        />
        <CardTitle title="Something is Wrong!" subtitle="Hello!" />
        <CardText>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec
            mattis pretium massa. Aliquam erat volutpat. Nulla facilisi. Donec
            vulputate interdum sollicitudin. Nunc lacinia auctor quam sed
            pellentesque. Aliquam dui mauris, mattis quis lacus id, pellentesque
            lobortis odio.
        </CardText>
        <CardActions>
            <FlatButton label="Action1" />
            <FlatButton label="Action2" />
        </CardActions>
    </Card>;

export default CardExampleWithAvatar;
