import * as React from "react";
import {ClientTypeName} from "src/types";

import "./clientTypeItem.scss";

interface Props {
    clientType: ClientTypeName;
}

const clientTypeToClassName = {
    client: "client_type-client",
    employer: "client_type-worker",
    close: "client_type-close"
};

const clientTypeToRuame = {
    client: "Клиент",
    employer: "Сотрудник",
    close: "Родственник"
};

const ClientTypeItem: React.FC<Props> = (props: Props) => {
    return (
        <span className={`client_type ${clientTypeToClassName[props.clientType]}`}>
            {clientTypeToRuame[props.clientType]}
        </span>
    );
};

export default ClientTypeItem;
