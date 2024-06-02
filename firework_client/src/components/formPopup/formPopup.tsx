import * as React from "react";
import {Modal} from "antd";

interface Props {
    isOpen: boolean;
    changeIsOpen: (value: boolean) => void;
    formBody: React.ReactElement;
}

const FormPopup: React.FC<Props> = (props: Props) => {
    return (
        <Modal width={450} open={props.isOpen} onCancel={() => props.changeIsOpen(false)} footer={[]}>
            {props.formBody}
        </Modal>
    );
};

export default FormPopup;
