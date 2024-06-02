import * as React from "react";
import {parseISO} from "date-fns";
import {format} from "date-fns-tz";

interface Props {
    time: string;
}

const TimeLabel: React.FC<Props> = (props: Props) => {
    return <span>{format(parseISO(props.time), "yyyy-MM-dd kk:mm")}</span>;
};

export default TimeLabel;
