import React from "react";
import {Checkbox, Form, Space} from "antd";
import {TextInputFormItem} from "src/types";
import InputFormComponent from "src/formComponents/inputFormComponent/inputFormComponent";

interface CheckBoxItem {
    value: string;
    text: string;
    textAreaItem?: TextInputFormItem;
    isAreaItemOpen?: boolean;
}

type CheckboxValueType = string | number | boolean;

interface Props {
    name: string;
    label?: string;
    style?: React.CSSProperties;
    items: CheckBoxItem[];
    unrequired?: boolean;
    onChange?: (value: CheckboxValueType[]) => void;
    disabled?: boolean;
}

const CheckboxGroupFormComponent: React.FC<Props> = (props: Props) => {
    const provideValueToOnChangeProp = (value: CheckboxValueType[]) => {
        if (!props.onChange) {
            return;
        }
        props.onChange(value);
    };

    return (
        <Form.Item
            name={props.name}
            label={props.label ? <span className="consultation_card__question-text">{props.label}</span> : ""}
            required={props.unrequired ? !props.unrequired : false}
            rules={[
                {
                    required: true,
                    message: "Пожалуйста, выберите один из пунктов выше"
                }
            ]}
            style={props.style}
        >
            <Checkbox.Group onChange={(e) => provideValueToOnChangeProp(e)} disabled={props.disabled}>
                <Space direction="vertical">
                    {props.items.map((elem: CheckBoxItem, idx) => (
                        <>
                            <Checkbox className="consultation_card__checkbox" value={elem.value} key={idx}>
                                {elem.text}
                            </Checkbox>
                            {elem.textAreaItem && elem.isAreaItemOpen && (
                                <InputFormComponent
                                    name={elem.textAreaItem.name}
                                    label={elem.textAreaItem.label}
                                    errorMessage={elem.textAreaItem.errorMessage}
                                    style={elem.textAreaItem.style}
                                    onChange={elem.textAreaItem.onChange}
                                    disabled={props.disabled}
                                    isTextArea
                                />
                            )}
                        </>
                    ))}
                </Space>
            </Checkbox.Group>
        </Form.Item>
    );
};

export default CheckboxGroupFormComponent;
