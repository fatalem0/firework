// TOOD (thefirefox15): It's bad, but it is...
// @ts-nocheck
import * as React from "react";
import {Form, Select, Button, Space} from "antd";
import DynamicComponentsList from "src/components/dynamicComponentsList/dynamicComponentsList";
import InputFormComponent from "src/formComponents/inputFormComponent/inputFormComponent";
import TestsEditingQuestionsComponent from "src/components/testsEditingQuestionsComponent/testsEditingQuestionsComponent";

interface Props {
    itemIdx: number;
    uid: number;
    length: number;
    outerUid: number;
    addItem: () => void;
    removeItem: (elem: number) => void;
}

const availTestTypes = {
    "Множетсвенный выбор": "checkbox",
    Ползунок: "select",
    "Ввод текста": "text",
    "Выбор одного ответа": "radio"
};

const TestsEditingQuestionsList: React.FC<Props> = (props: Props) => {
    const renderAvailTests = () => {
        const result = [];
        for (const [label, value] of Object.entries(availTestTypes)) {
            result.push({
                value,
                label
            });
        }
        return result;
    };

    return (
        <>
            <div className="tests_editing_result__container" key={props.itemIdx}>
                <InputFormComponent
                    name={["questionSettings", props.uid, "question"]}
                    errorMessage="Пожалуйста, введите результат прохождения теста"
                />
                <Form.Item
                    label="Формат ответа"
                    name={["questionSettings", props.uid, "questionType"]}
                    className="consultation_card__question-text"
                    required
                    rules={[
                        {
                            required: true,
                            message: "Выберите формат ответа"
                        }
                    ]}
                >
                    <Select options={renderAvailTests()} />
                </Form.Item>
                <DynamicComponentsList outerUid={props.itemIdx} body={<TestsEditingQuestionsComponent />} />
            </div>
            <Space>
                {props.length > 1 && (
                    <Button
                        onClick={() => props.removeItem(props.uid)}
                        className="tests_editing_result__add_question_btn"
                        danger
                    >
                        Удалить вопрос
                    </Button>
                )}
                {props.length - 1 === props.itemIdx && (
                    <Button onClick={() => props.addItem()} className="tests_editing_result__add_question_btn">
                        Добавить вопрос
                    </Button>
                )}
            </Space>
        </>
    );
};

export default TestsEditingQuestionsList;
