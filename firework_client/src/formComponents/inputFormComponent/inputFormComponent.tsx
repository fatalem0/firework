import React from "react";
import {Input, Form} from "antd";
import {TextInputFormItem} from "src/types";

const InputFormComponent: React.FC<TextInputFormItem> = (props: TextInputFormItem) => {
    const provideValueToOnChangeProp = (value: string) => {
        if (!props.onChange) {
            return;
        }
        props.onChange(value);
    };
    const renderInputItem = () => {
        return props.isTextArea ? (
            <Input.TextArea
                className="consultation_card__question-text-area"
                placeholder="Введите текст"
                onChange={(e) => provideValueToOnChangeProp(e.target.value)}
                disabled={props.disabled}
            />
        ) : (
            <Input
                className="consultation_card__question-text-area"
                placeholder="Введите текст"
                onChange={(e) => provideValueToOnChangeProp(e.target.value)}
                disabled={props.disabled}
            />
        );
    };

    return (
        <>
            {props.errorMessage && (
                <Form.Item
                    name={props.name}
                    className="consultation_card__question-text"
                    label={props.label}
                    required
                    rules={[
                        {
                            required: true,
                            message: props.errorMessage
                        }
                    ]}
                    style={props.style}
                >
                    {renderInputItem()}
                </Form.Item>
            )}
            {!props.errorMessage && (
                <Form.Item
                    name={props.name}
                    className="consultation_card__question-text"
                    label={props.label}
                    style={props.style}
                >
                    {renderInputItem()}
                </Form.Item>
            )}
        </>
    );
};

export default InputFormComponent;
