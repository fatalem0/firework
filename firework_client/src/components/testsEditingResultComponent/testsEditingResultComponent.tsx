import "./testsEditingResultComponent.scss";

import * as React from "react";
import {Form, InputNumber, Space, Typography, Button, Select} from "antd";
import {CloseOutlined} from "@ant-design/icons";
import InputFormComponent from "src/formComponents/inputFormComponent/inputFormComponent";

const availStressLevels = {
    "Зеленый": "green",
    "Желтный": "yellow",
    "Красный": "red"
};

const TestsEditingResultComponent: React.FC = () => {
    const [activeItems, changeActiveItems] = React.useState<number[]>([0]);
    const [currentCreatedItemsCount, changeCurrentCreatedItemsCount] = React.useState<number>(0);

    const addItem = () => {
        changeCurrentCreatedItemsCount(currentCreatedItemsCount + 1);
        changeActiveItems([...activeItems, currentCreatedItemsCount + 1]);
    };

    const removeItem = (elem: number) => {
        const itemIdx = activeItems.findIndex((item) => item === elem);
        changeActiveItems([...activeItems.slice(0, itemIdx), ...activeItems.slice(itemIdx + 1)]);
    };

    const renderAvailStressLevels = () => {
        const result = [];
        for (const [label, value] of Object.entries(availStressLevels)) {
            result.push({
                value,
                label
            });
        }
        return result;
    };

    const renderResultItem = (itemIdx: number, uid: number) => {
        return (
            <div className="tests_editing_result__container" key={itemIdx}>
                <Typography.Title className="tests_editing_result__title">
                    Интервал оценки {itemIdx + 1}
                    {activeItems.length > 1 && (
                        <CloseOutlined className="tests_editing_result__delete_icon" onClick={() => removeItem(uid)} />
                    )}
                </Typography.Title>
                <InputFormComponent
                    name={["resultSettings", uid, "resultText"]}
                    label="Результат проохождения"
                    errorMessage="Пожалуйста, введите результат прохождения теста"
                />
                <Form.Item
                    label="Уровень стресса"
                    name={["resultSettings", uid, "stressLevelActual"]}
                    className="consultation_card__question-text"
                    required
                    rules={[
                        {
                            required: true,
                            message: "Выберите уровень стресса"
                        }
                    ]}
                >
                    <Select options={renderAvailStressLevels()} />
                </Form.Item>
                <span className="tests_editing_result__range_text">Интервал оценки:</span>
                <Space className="tests_editing_result__range_container">
                    <Form.Item
                        name={["resultSettings", uid, "from"]}
                        required
                        rules={[
                            {
                                required: true,
                                message: "Пожалуйста, введите минимальное значение порога"
                            }
                        ]}
                    >
                        <InputNumber
                            className="tests_editing_result__range_container_from"
                            min={0}
                            prefix={<span>от:</span>}
                        />
                    </Form.Item>
                    <Form.Item
                        name={["resultSettings", uid, "to"]}
                        required
                        rules={[
                            {
                                required: true,
                                message: "Пожалуйста, введите максимальное значение порога"
                            }
                        ]}
                    >
                        <InputNumber
                            className="tests_editing_result__range_container_to"
                            min={0}
                            prefix={<span>до:</span>}
                        />
                    </Form.Item>
                </Space>
                <InputFormComponent
                    name={["resultSettings", uid, "resultDesc"]}
                    label="Описание результата"
                    errorMessage="Пожалуйста, введите описание результата"
                />
            </div>
        );
    };

    return (
        <>
            {activeItems.map((item, idx) => renderResultItem(idx, item))}
            <Button onClick={() => addItem()} className="tests_editing_result__add_btn">
                Добавить интервал
            </Button>
        </>
    );
};

export default TestsEditingResultComponent;
