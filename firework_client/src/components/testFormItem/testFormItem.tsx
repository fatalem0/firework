// TOOD (thefirefox15): It's bad, but it is...
// @ts-nocheck
import * as React from "react";
import {Button, Form, Slider} from "antd";
import CheckboxGroupFormComponent from "src/formComponents/checkboxGroupFormComponent/checkboxGroupFormComponent";
import RadioGroupFormComponent from "src/formComponents/radioGroupFormComponent/radioGroupFormComponent";
import {TestType, TestAnswer} from "src/types";
import InputFormComponent from "src/formComponents/inputFormComponent/inputFormComponent";

interface Props {
    question: string;
    questionNumber: number;
    answers: TestAnswer[];
    type: TestType;
    submitFunc: (values: number[]) => Promise<void>;
    isLoading: boolean;
}

interface FormFields {
    result: number[];
}

const TestFormItem: React.FC<Props> = (props: Props) => {
    const [form] = Form.useForm<FormFields>();

    const onSubmit = async (values) => {
        if (props.type !== "Checkbox") {
            values["result"] = [values["result"]];
        }
        await props.submitFunc(values["result"]);
    };

    const renderAnswers = () => {
        if (props.questionNumber === -1) {
            return null;
        }
        const answers = props.answers.map((item) => ({
            value: item.answerNumber,
            text: item.answerText
        }));
        const label = `${props.questionNumber}. ${props.question}`;

        if (props.type === "Checkbox") {
            return <CheckboxGroupFormComponent label={label} name="result" items={answers} />;
        } else if (props.type === "Radio Button") {
            return <RadioGroupFormComponent label={label} name="result" items={answers} />;
        } else if (props.type === "Text") {
            return <InputFormComponent label={label} name="result" />;
        }

        const minValue = props.answers.reduce(
            (acc, current) => Math.min(acc, current.answerNumber),
            props.answers[0].answerNumber
        );
        const maxValue = props.answers.reduce(
            (acc, current) => Math.max(acc, current.answerNumber),
            props.answers[0].answerNumber
        );

        return (
            <Form.Item
                label={<span className="consultation_card__question-text">{label}</span>}
                name="result"
                initialValue={minValue}
            >
                <Slider min={minValue} max={maxValue} trackStyle={{background: "#aac1de"}} />
            </Form.Item>
        );
    };

    return (
        <Form<FormFields> layout="vertical" className="tests__form" form={form} onFinish={onSubmit}>
            {renderAnswers()}
            {props.questionNumber !== -1 && (
                <Button disabled={props.isLoading} loading={props.isLoading} htmlType="submit">
                    Далее
                </Button>
            )}
        </Form>
    );
};

export default TestFormItem;
