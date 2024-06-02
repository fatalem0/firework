import React from "react";
import {Radio, Form} from "antd";
import {RadioGroupItem} from "src/types";
import TextInputComponent from "src/formComponents/inputFormComponent/inputFormComponent";

interface Props {
    name: string;
    label?: string;
    style?: React.CSSProperties;
    items: RadioGroupItem[];
}

const RadioGroupFormComponent: React.FC<Props> = (props: Props) => {
    return (
        <Form.Item
            name={props.name}
            label={<span className="consultation_card__question-text">{props.label}</span>}
            required
            rules={[
                {
                    required: true,
                    message: "Пожалуйста, выберите один из пунктов выше"
                }
            ]}
            style={props.style}
        >
            <Radio.Group>
                {props.items.map((elem: RadioGroupItem, idx) => (
                    <>
                        <Radio
                            className="consultation_card__checkbox"
                            value={elem.value}
                            disabled={elem.disabled}
                            key={idx}
                        >
                            {elem.text}
                        </Radio>
                        {elem.textAreaItem && elem.isAreaItemOpen && (
                            <TextInputComponent
                                name={elem.textAreaItem.name}
                                label={elem.textAreaItem.label}
                                errorMessage={elem.textAreaItem.errorMessage}
                                style={elem.textAreaItem.style}
                                isTextArea={elem.textAreaItem.isTextArea}
                            />
                        )}
                    </>
                ))}
            </Radio.Group>
        </Form.Item>
    );
};

export default RadioGroupFormComponent;
