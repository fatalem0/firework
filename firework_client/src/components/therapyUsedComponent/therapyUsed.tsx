import React from "react";
import {Checkbox, Form, Space} from "antd";
import InputFormComponent from "src/formComponents/inputFormComponent/inputFormComponent";

interface Props {
    openInput: boolean;
}

const TherapyUsed: React.FC<Props> = (props: Props) => {
    return (
        <Form.Item
            name="therapyUsed"
            required
            rules={[
                {
                    required: true,
                    message: "Пожалуйста, выберите один из пунктов выше"
                }
            ]}
        >
            <Checkbox.Group>
                <Space direction="vertical">
                    <Checkbox className="consultation_card__checkbox" value="useCognBehavTherapy">
                        Когнитивно-поведенческая
                    </Checkbox>
                    <Checkbox className="consultation_card__checkbox" value="useExistentialTherapy">
                        Экзистенцильная
                    </Checkbox>
                    <Checkbox className="consultation_card__checkbox" value="useWorkImagesTherapy">
                        Работа с внутренними образами
                    </Checkbox>
                    <Checkbox className="consultation_card__checkbox" value="useDecisionTherapy">
                        Сфокусированная на решении
                    </Checkbox>
                    <Checkbox className="consultation_card__checkbox" value="useAcceptanceTherapy">
                        Сфокусированная на принятии
                    </Checkbox>
                    <Checkbox className="consultation_card__checkbox" value="useArtTherapy">
                        Арт-терапия
                    </Checkbox>
                    <Checkbox className="consultation_card__checkbox" value="useBodilyOrientedTherapy">
                        Телесно-ориентированная
                    </Checkbox>
                    <Checkbox className="consultation_card__checkbox" value="useOtherTherapy">
                        Другая
                    </Checkbox>
                    {props.openInput && (
                        <InputFormComponent
                            name="useOtherTherapyNote"
                            errorMessage="Пожалуйста, заполните опишите подробно использованную терапию выше"
                            style={{marginBottom: 0}}
                            isTextArea
                        />
                    )}
                </Space>
            </Checkbox.Group>
        </Form.Item>
    );
};

export default TherapyUsed;
