import * as React from "react";
import {PageLoading} from "@ant-design/pro-components";

interface Props {
    isLoading: boolean;
    body: React.ReactElement;
}

const PageLoadingWithParentComponent: React.FC<Props> = (props: Props) => {
    return (
        <>
            {props.isLoading && <PageLoading spinning={props.isLoading} fullscreen />}
            {!props.isLoading && props.body}
        </>
    );
};

export default PageLoadingWithParentComponent;
