import * as React from "react";
import {useSearchParams, useNavigate, createSearchParams, Link} from "react-router-dom";
import {PageContainer} from "@ant-design/pro-components";
import {Typography, Row, Col, Form, Select, Button} from "antd";
import PageLoadingWithParentComponent from "src/components/pageLoadingWithParentComponent/pageLoadingWithParentComponent";
import TestFormItem from "src/components/testFormItem/testFormItem";
import clientQueries from "src/queries/clientQueries";
import testQueries from "src/queries/testQueries";
import {TestQuestion, TestQuestionsResult, Client, TestInfo} from "src/types";
import {sleep} from "src/utils";

import "./testPage.scss";

interface TestSpan {
    email: string;
    testId: string;
}

const TestPage: React.FC = () => {
    const navigate = useNavigate();

    const [form] = Form.useForm<TestSpan>();
    const [searchParams] = useSearchParams();
    const getQuestion = testQueries.getQuestion();
    const postAnswer = testQueries.postAnswer();
    const getQuestionsResult = testQueries.getQuestionsResult();
    const getAvailTests = testQueries.getAvailTests();
    const listClientsWithoutRetry = clientQueries.listClientsWithoutRetry();

    const [clients, changeClients] = React.useState<Client[]>();
    const [tests, changeTests] = React.useState<TestInfo[]>();
    const [isLoading, changeIsLoading] = React.useState<boolean>(true);
    const [isLoadingQuestion, changeIsLoadingQuestion] = React.useState<boolean>(true);
    const [isLoadingQuestionSpan, changeIsLoadingQuestionSpan] = React.useState<boolean>(false);
    const [testId, changeTestId] = React.useState<string>("");
    const [email, changeEmail] = React.useState<string>("");
    const [curQuestion, changeCurQuestion] = React.useState<TestQuestion>();
    const [testResult, changeTestResult] = React.useState<TestQuestionsResult>();

    const submitAnswer = async (answerNumber: number[]) => {
        if (!curQuestion) {
            return;
        }
        changeIsLoading(true);
        try {
            await postAnswer.mutateAsync({
                user_id: curQuestion.user_id,
                test_id: testId,
                test_question_id: curQuestion.test_question_id,
                answerNumber
            });
            changeIsLoading(false);
            changeIsLoadingQuestion(true);
            await sleep(200);
            const result = await getQuestion.mutateAsync({email, test_id: testId});
            changeCurQuestion(result);
            if (result.result_id && result.questionNumber === -1) {
                const endDescription = await getQuestionsResult.mutateAsync(result.result_id);
                changeTestResult(endDescription);
            }
        } catch (e) {
            console.error(e);
            changeIsLoadingQuestion(false);
        } finally {
            changeIsLoading(false);
        }
    };

    const getAvailClients = async () => {
        try {
            changeIsLoadingQuestion(true);
            await sleep(100);
            const clients = await listClientsWithoutRetry.mutateAsync();
            const tests = await getAvailTests.mutateAsync();
            changeTests(tests);
            changeClients(clients);
            form.setFieldsValue({email, testId});
        } catch (e) {
            console.error(e);
        } finally {
            changeIsLoadingQuestion(false);
        }
    };

    React.useEffect(() => {
        const getCurQuestion = async (email: string, test_id: string) => {
            const result = await getQuestion.mutateAsync({email, test_id});
            changeCurQuestion(result);
            if (result.result_id && result.questionNumber === -1) {
                const endDescription = await getQuestionsResult.mutateAsync(result.result_id);
                changeTestResult(endDescription);
            }
            changeIsLoading(false);
        };
        const testId = searchParams.get("id") ?? "";
        const email = searchParams.get("email") ?? "";
        changeTestId(testId);
        changeEmail(email);
        if (!email || !testId) {
            changeIsLoading(false);
            getAvailClients();
            return;
        }
        try {
            changeIsLoadingQuestion(true);
            getCurQuestion(email, testId);
        } catch (e) {
            console.error(e);
            changeIsLoadingQuestion(false);
        }
    }, [searchParams]);

    React.useEffect(() => {
        if (!curQuestion) {
            return;
        }
        if (curQuestion.result_id && curQuestion.questionNumber === -1) {
            return;
        }
        changeIsLoadingQuestion(false);
    }, [curQuestion]);

    React.useEffect(() => {
        if (!testResult) {
            return;
        }
        changeIsLoadingQuestion(false);
    }, [testResult]);

    const updateTestsInfo = async (testInfo: TestSpan) => {
        changeIsLoadingQuestionSpan(true);
        navigate({
            pathname: "",
            search: createSearchParams({
                id: testInfo.testId,
                email: testInfo.email
            }).toString()
        });
        changeIsLoadingQuestionSpan(false);
    };

    const renderAvailClients = () => {
        if (!clients) {
            return;
        }
        return clients.map((client: Client) => ({
            value: client.clientEmail,
            label: client.clientFullName
        }));
    };

    const renderAvailTests = () => {
        if (!tests) {
            return;
        }
        return tests.map((test) => ({
            value: test.public_id,
            label: test.name
        }));
    };

    const renderPage = () => {
        return isLoadingQuestion ? (
            <></>
        ) : (
            <PageContainer>
                {curQuestion && (
                    <Row align="middle" justify="center">
                        <div className="test_page__question_header">
                            <Row align="middle" justify="center">
                                <Typography.Title className="test_page__question_title">
                                    {curQuestion.questionNumber !== -1 ? curQuestion.name : "Результаты теста"}
                                </Typography.Title>
                            </Row>
                        </div>
                    </Row>
                )}
                {(!testId || !email) && !curQuestion && (
                    <Row align="middle" justify="center">
                        <div className="test_page__question_container">
                            <Form<TestSpan> onFinish={updateTestsInfo} form={form} layout="vertical">
                                <Form.Item
                                    label="Тест"
                                    name="testId"
                                    required
                                    rules={[
                                        {
                                            required: true,
                                            message: "Выберите тест"
                                        }
                                    ]}
                                >
                                    <Select options={renderAvailTests()} />
                                </Form.Item>
                                <Form.Item
                                    label="Пользователь"
                                    name="email"
                                    required
                                    rules={[
                                        {
                                            required: true,
                                            message: "Выберите пользователя"
                                        }
                                    ]}
                                >
                                    <Select options={renderAvailClients()} />
                                </Form.Item>
                                <Row justify="end">
                                    <Button
                                        disabled={isLoadingQuestionSpan}
                                        loading={isLoadingQuestionSpan}
                                        type="primary"
                                        htmlType="submit"
                                    >
                                        Открыть тест
                                    </Button>
                                </Row>
                            </Form>
                        </div>
                    </Row>
                )}
                {curQuestion && (
                    <Row align="middle" justify="center">
                        <div className="test_page__question_container">
                            <Row className="test_page__question_container-inner">
                                {testResult && (
                                    <>
                                        <span className="test_page__question_result__recommendations">
                                            Наши рекомендации: {testResult.recommendation}
                                        </span>
                                        <span className="test_page__question_result__desc">
                                            {testResult.description}
                                        </span>
                                    </>
                                )}
                                <Col span={18}>
                                    <TestFormItem
                                        questionNumber={curQuestion.questionNumber}
                                        question={curQuestion.title}
                                        answers={curQuestion.test_answers}
                                        type={curQuestion.questionTypeActual}
                                        submitFunc={submitAnswer}
                                        isLoading={isLoading}
                                    />
                                </Col>
                                {curQuestion.questionNumber !== -1 && (
                                    <Col span={6}>
                                        <Row align="top" justify="end">
                                            <span className="test_page__question_progress__text">{`${curQuestion.questionNumber}/${curQuestion.numberOfQuestions}`}</span>
                                        </Row>
                                    </Col>
                                )}
                            </Row>
                            {curQuestion.questionNumber === -1 && <Link to="/home">Вернуться на главную страницу</Link>}
                        </div>
                    </Row>
                )}
            </PageContainer>
        );
    };

    return <PageLoadingWithParentComponent isLoading={isLoadingQuestion} body={renderPage()} />;
};

export default TestPage;
