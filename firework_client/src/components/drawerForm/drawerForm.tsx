import "./drawerForm.scss";

import * as React from "react";
import {Drawer, Space, Button} from "antd";

interface FormProps {
    title: string;
    isFormOpen: boolean;
    changeIsFormOpen: (value: boolean) => void;
    formBody: React.ReactElement;
    hasCloseBtn?: boolean;
    width?: number;
}

const DrawerForm: React.FC<FormProps> = ({title, isFormOpen, changeIsFormOpen, formBody, hasCloseBtn, width}) => {
    return (
        <Drawer
            title={<h3 className="drawer-form__text">{title}</h3>}
            width={width ? width : 350}
            onClose={() => changeIsFormOpen(false)}
            open={isFormOpen}
            closable={false}
            extra={
                hasCloseBtn ? (
                    <Space style={{paddingTop: "15px"}}>
                        <Button onClick={() => changeIsFormOpen(false)}>Close</Button>
                    </Space>
                ) : null
            }
        >
            {formBody}
        </Drawer>
    );
};

export default DrawerForm;
