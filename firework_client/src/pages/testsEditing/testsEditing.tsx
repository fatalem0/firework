// TOOD (thefirefox15): It's bad, but it is...
// @ts-nocheck
import * as React from "react";
import {PageContainer} from "@ant-design/pro-components";
import {CaretRightOutlined} from "@ant-design/icons";
import {Form, Collapse, Button, Select, InputNumber} from "antd";
import {useNavigate} from "react-router-dom";
import CheckboxGroupFormComponent from "src/formComponents/checkboxGroupFormComponent/checkboxGroupFormComponent";
import DynamicComponentsList from "src/components/dynamicComponentsList/dynamicComponentsList";
import InputFormComponent from "src/formComponents/inputFormComponent/inputFormComponent";
import PageLoadingWithParentComponent from "src/components/pageLoadingWithParentComponent/pageLoadingWithParentComponent";
import TestsEditingQuestionsList from "src/components/testsEditingQuestionsList/testsEditingQuestionsList";
import TestsEditingResultComponent from "src/components/testsEditingResultComponent/testsEditingResultComponent";
import testsProvider from "src/providers/testsProvider";
import {TestEditForm} from "src/types";
import {sleep} from "src/utils";

const activeKeysDefaultOpen = ["0", "1"];
const collapseRotateActiveAngle = 90;
const collapseRotateDisableAngle = 0;

const TestsEditing: React.FC = () => {
    const testId = React.useRef(location.pathname.match(/\/([^/]+)$/)?.[1]).current;
    const navigate = useNavigate();

    const [form] = Form.useForm<TestEditForm>();
    const [isFormSubmitting, setIsFormSubmitting] = React.useState<boolean>(false);
    const [isFormSubmitted, setIsFormSubmitted] = React.useState<boolean>(false);
    const [isLoading, changeIsLoading] = React.useState<boolean>(testId !== "testsEditing");

    React.useEffect(() => {
        if (testId === "testsEditing") {
            return;
        }
        const getTestInfo = async () => {
            await sleep(200);
            const testInfo = await testsProvider.getTest(testId);
            return testInfo;
        };
        try {
            changeIsLoading(true);
            form.setFieldsValue(getTestInfo());
        } catch (e) {
            navigate("/home");
        } finally {
            changeIsLoading(false);
        }
    }, [testId]);

    const submitTestSettings = async (values: TestEditForm) => {
        values.questionSettings = values.questionSettings.map((question) => {
            question.questionAnswers = question.questionAnswers.filter(
                (questionAnswerItem) => questionAnswerItem !== undefined
            );
            return question;
        });
        values.resultSettings = values.resultSettings.filter((elem) => elem !== undefined);
        try {
            setIsFormSubmitting(true);
            await testsProvider.createTest(values);
            setIsFormSubmitted(true);
        } catch (e) {
            console.error(e);
        } finally {
            setIsFormSubmitting(false);
        }
    };

    const renderPage = () => {
        return isLoading ? null : (
            <PageContainer
                header={{
                    title: "",
                    breadcrumb: {}
                }}
            >
                <PageLoadingWithParentComponent
                    isLoading={false}
                    body={
                        <Form<TestEditForm>
                            onFinish={submitTestSettings}
                            form={form}
                            layout="vertical"
                            disabled={isFormSubmitted}
                        >
                            <InputFormComponent
                                name="title"
                                label="Название теста"
                                errorMessage="Пожалуйста, введите название теста"
                                style={{maxWidth: 300}}
                            />
                            <CheckboxGroupFormComponent
                                label="Тип пользователя"
                                name="clientTypeActual"
                                items={[
                                    {
                                        value: "patient",
                                        text: "Пациент"
                                    },
                                    {
                                        value: "staff",
                                        text: "Мед. Персонал"
                                    },
                                    {
                                        value: "relatives",
                                        text: "Родственники"
                                    }
                                ]}
                            />
                            <Form.Item
                                label="Стадия заболевания"
                                required
                                rules={[{required: true, message: "Пожалуйста, выберите стадию заболевания"}]}
                                name="stageActual"
                            >
                                <Select
                                    style={{width: 250}}
                                    options={[
                                        {value: "justDiagnosed", label: <span>Недавно диагностировали</span>},
                                        {value: "cure", label: <span>Лечение</span>},
                                        {value: "therapy", label: <span>Терапия</span>},
                                        {value: "remission", label: <span>Ремиссия</span>},
                                        {value: "palliativeCare", label: <span>Палативное лечение</span>}
                                    ]}
                                    onChange={(e) => changeClientInfo({...clientInfo, stageActual: e})}
                                />
                            </Form.Item>
                            <Form.Item
                                label="Интервал"
                                name="interval"
                                required
                                rules={[
                                    {
                                        required: true,
                                        message: "Пожалуйста, введите интервал"
                                    }
                                ]}
                            >
                                <InputNumber
                                    className="tests_editing_result__range_container_from"
                                    min={0}
                                    prefix={<span>от:</span>}
                                />
                            </Form.Item>
                            <Collapse
                                bordered={false}
                                style={{background: "#F5F5F5"}}
                                expandIcon={({isActive}) => (
                                    <CaretRightOutlined
                                        rotate={isActive ? collapseRotateActiveAngle : collapseRotateDisableAngle}
                                    />
                                )}
                                defaultActiveKey={activeKeysDefaultOpen}
                            >
                                <Collapse.Panel header="Интервал оценивания" key="0">
                                    <TestsEditingResultComponent />
                                </Collapse.Panel>
                            </Collapse>
                            <DynamicComponentsList
                                body={<TestsEditingQuestionsList />}
                                useCollapse
                                useCollapseItem
                                collapseItemHeaderGenerator={(idx: number) => `Вопрос ${idx + 1}`}
                            />
                            <Button htmlType="submit" disabled={isFormSubmitting} loading={isFormSubmitting}>
                                Сохранить
                            </Button>
                        </Form>
                    }
                />
            </PageContainer>
        );
    };

    return <PageLoadingWithParentComponent isLoading={isLoading} body={renderPage()} />;
};

export default TestsEditing;
