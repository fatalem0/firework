import * as React from "react";
import {Form, InputNumber, Typography, Button} from "antd";
import {CloseOutlined} from "@ant-design/icons";
import InputFormComponent from "src/formComponents/inputFormComponent/inputFormComponent";

interface Props {
    itemIdx: number;
    uid: number;
    outerUid: number;
    length: number;
    addItem: () => void;
    removeItem: (elem: number) => void;
}

const TestsEditingQuestionsComponent: React.FC<Props> = (props: Props) => {
    return (
        <>
            <Typography.Title className="tests_editing_result__title">
                Вариант ответа {props.itemIdx + 1}
                {props.length > 1 && (
                    <CloseOutlined
                        className="tests_editing_result__delete_icon"
                        onClick={() => props.removeItem(props.uid)}
                    />
                )}
            </Typography.Title>
            <InputFormComponent
                name={["questionSettings", props.outerUid, "questionAnswers", props.uid, "value"]}
                errorMessage="Пожалуйста, введите вариант ответа"
            />
            <Form.Item
                label={`Оценка для ответа ${props.itemIdx + 1}`}
                name={["questionSettings", props.outerUid, "questionAnswers", props.uid, "score"]}
                className="consultation_card__question-text"
                required
                rules={[
                    {
                        required: true,
                        message: "Пожалуйста, введите оценку для ответа"
                    }
                ]}
            >
                <InputNumber min={0} />
            </Form.Item>
            {props.length - 1 === props.itemIdx && (
                <Button onClick={() => props.addItem()} className="tests_editing_result__add_btn">
                    Добавить ответ
                </Button>
            )}
        </>
    );
};

export default TestsEditingQuestionsComponent;
