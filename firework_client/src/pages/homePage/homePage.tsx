import "./homePage.scss";

import * as React from "react";
import {PageContainer} from "@ant-design/pro-components";
import {Row, Descriptions, Col} from "antd";
import {Chart} from "react-google-charts";
import {User, Consultation, TestResult} from "src/types";
import {useMount} from "react-use";
import {sleep} from "src/utils";
import PageLoadingWithParentComponent from "src/components/pageLoadingWithParentComponent/pageLoadingWithParentComponent";
import consultationQueries from "src/queries/consultationQueries";
import testQueries from "src/queries/testQueries";
import userQueries from "src/queries/userQueries";

const HomePage: React.FC = () => {
    const listUsers = userQueries.listUsers();
    const listConsultations = consultationQueries.listConsultations();
    const listTests = testQueries.listTests();
    const [tests, setTests] = React.useState<TestResult[]>();
    const [users, changeUsers] = React.useState<User[]>();
    const [consultations, setConsultations] = React.useState<Consultation[]>();
    const [isLoading, changeIsLoading] = React.useState<boolean>(true);

    useMount(async () => {
        await sleep(100);
        await listUsers.refetch();
        await listConsultations.refetch();
        await listTests.refetch();
    });

    React.useEffect(() => {
        if (!listUsers.data) {
            return;
        }
        changeUsers(listUsers.data);
    }, [listUsers.data]);

    React.useEffect(() => {
        if (!listConsultations.data) {
            return;
        }
        setConsultations(listConsultations.data);
    }, [listConsultations.data]);

    React.useEffect(() => {
        if (!listTests.data) {
            return;
        }
        setTests(listTests.data);
    }, [listTests.data]);

    React.useEffect(() => {
        changeIsLoading(!tests || !users || !consultations);
    }, [tests, users, consultations]);

    const getChartData = () => {
        if (!users) {
            return;
        }
        return [
            ["Task", "Hours per Day"],
            ["Клиенты", users.filter((item) => item.userTypeActual === "Клиент").length],
            ["Сотрудники", users.filter((item) => item.userTypeActual === "Сотрудник").length],
            ["Родственники", users.filter((item) => item.userTypeActual === "Родственник").length]
        ];
    };

    const renderPage = () => {
        return isLoading || !consultations || !tests ? (
            <></>
        ) : (
            <Row gutter={[10, 10]}>
                <Col span={14}>
                    <Chart
                        chartType="PieChart"
                        data={getChartData()}
                        width={"100%"}
                        options={{
                            backgroundColor: "transparent",
                            slices: {
                                0: {color: "#F8ECDF"},
                                1: {color: "#6D9FDB"},
                                2: {color: "#CAB5E0"}
                            },
                            fontName: "Montserrat"
                        }}
                        height={"400px"}
                    />
                </Col>
                <Col span={10}>
                    <Descriptions>
                        <Descriptions.Item
                            span={3}
                            label={<span className="home_page__logo_desc_text">Количество консультаций</span>}
                        >
                            <span className="home_page__logo_desc_text">{consultations.length}</span>
                        </Descriptions.Item>
                        <Descriptions.Item
                            span={3}
                            label={<span className="home_page__logo_desc_text">Количество тестов</span>}
                        >
                            <span className="home_page__logo_desc_text">{tests.length}</span>
                        </Descriptions.Item>
                    </Descriptions>
                </Col>
            </Row>
        );
    };

    return (
        <PageContainer
            header={{
                title: "",
                breadcrumb: {}
            }}
            className="home_page__container"
        >
            <Row className="home_page__logo_container">
                <h1 className="home_page__logo_text-top">ВИРТУАЛЬНАЯ КЛИНИКА</h1>
                <h1 className="home_page__logo_text-bottom">ОНКОПСИХОЛОГИИ</h1>
            </Row>
            <PageLoadingWithParentComponent isLoading={isLoading} body={renderPage()} />
        </PageContainer>
    );
};

export default HomePage;
