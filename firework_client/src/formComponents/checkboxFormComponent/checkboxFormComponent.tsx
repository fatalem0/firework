import React from "react";
import {Checkbox, Form} from "antd";

interface Props {
    name: string;
    style?: React.CSSProperties;
    text: string;
    onChange?: (value: boolean) => void;
}

const CheckboxFormComponent: React.FC<Props> = (props: Props) => {
    const provideValueToOnChangeProp = (value: boolean) => {
        if (!props.onChange) {
            return;
        }
        props.onChange(value);
    };

    return (
        <Form.Item name={props.name} style={props.style}>
            <Checkbox
                className="consultation_card__checkbox"
                onChange={(e) => provideValueToOnChangeProp(e.target.checked)}
            >
                {props.text}
            </Checkbox>
        </Form.Item>
    );
};

export default CheckboxFormComponent;
