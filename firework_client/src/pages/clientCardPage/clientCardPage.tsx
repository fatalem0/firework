import "./clientCardPage.scss";

import * as React from "react";
import {useLocation, useNavigate} from "react-router-dom";
import {PageContainer} from "@ant-design/pro-components";
import {Row, Col, Tabs, Form, Descriptions} from "antd";
import {ClientInfo} from "src/types";
import clientQueries from "src/queries/clientQueries";
import TimeLabel from "src/components/timeLabel/timeLabel";
import ConsultationsTable from "src/components/consultationsTable/consultationsTable";
import TestsTable from "src/components/testsTable/testsTable";
import CheckboxGroupFormComponent from "src/formComponents/checkboxGroupFormComponent/checkboxGroupFormComponent";
import PageLoadingWithParentComponent from "src/components/pageLoadingWithParentComponent/pageLoadingWithParentComponent";

const ClientCardPage: React.FC = () => {
    const [form] = Form.useForm<ClientInfo>();
    const location = useLocation();
    const navigate = useNavigate();
    const id = React.useRef(location.pathname.match(/\/([^/]+)$/)?.[1]).current;
    const getClient = clientQueries.getClient();
    const [openInput, setOpenInput] = React.useState<boolean>(false);
    const [isLoading, changeIsLoading] = React.useState<boolean>(true);

    const [client, changeClient] = React.useState<ClientInfo>();

    React.useEffect(() => {
        changeIsLoading(true);
        if (!id) {
            navigate("/home");
            return;
        }
        getClient.mutateAsync(id).catch(() => navigate("/home"));
    }, [id]);

    React.useEffect(() => {
        const clientData = getClient.data;
        changeClient(clientData || undefined);
        form.setFieldsValue(clientData ?? {});
        setOpenInput(clientData?.recomendationType.includes("Другое") ?? false);
    }, [getClient.data]);

    React.useEffect(() => {
        if (client) {
            changeIsLoading(false);
        }
    }, [client]);

    const renderTabs = () => {
        return isLoading || !client ? (
            <></>
        ) : (
            <Tabs defaultActiveKey="1">
                <Tabs.TabPane tab="Общая информация" key="1">
                    <Form<ClientInfo> form={form}>
                        <Row gutter={[24, 24]}>
                            <Col span={8}>
                                <h3 className="client_card__subtitle">О клиенте</h3>
                                <Descriptions contentStyle={{fontSize: "16px"}}>
                                    <Descriptions.Item
                                        span={3}
                                        label={<span className="client_card__descriptions_title">ФИО</span>}
                                    >
                                        {client.clientFullName}
                                    </Descriptions.Item>
                                    <Descriptions.Item
                                        span={3}
                                        label={
                                            <span className="client_card__descriptions_title">
                                                Локализация заболевания
                                            </span>
                                        }
                                    >
                                        {client.diseaseLocation}
                                    </Descriptions.Item>
                                    <Descriptions.Item
                                        span={3}
                                        label={<span className="client_card__descriptions_title">Тип клиента</span>}
                                    >
                                        <span>{client.clientTypeActual}</span>
                                    </Descriptions.Item>
                                    <Descriptions.Item
                                        span={3}
                                        label={<span className="client_card__descriptions_title">Этап болезни</span>}
                                    >
                                        {client.stageActual}
                                    </Descriptions.Item>
                                    <Descriptions.Item
                                        span={3}
                                        label={
                                            <span className="client_card__descriptions_title">Дата регистрации</span>
                                        }
                                    >
                                        <TimeLabel time={client.clientCreated} />
                                    </Descriptions.Item>
                                    <Descriptions.Item
                                        span={3}
                                        label={
                                            <span className="client_card__descriptions_title">
                                                Месяцев после лечения
                                            </span>
                                        }
                                    >
                                        {`${client.monthsAfterTreatment} месяц(ев)`}
                                    </Descriptions.Item>
                                    <Descriptions.Item
                                        span={3}
                                        label={
                                            <span className="client_card__descriptions_title">
                                                Опыт работы с психологом
                                            </span>
                                        }
                                    >
                                        {client.workWithPsychologist ? "Есть" : "Нет"}
                                    </Descriptions.Item>
                                </Descriptions>
                            </Col>
                            <Col span={8}>
                                <h3 className="client_card__subtitle">Вид лечения</h3>
                                <CheckboxGroupFormComponent
                                    name="cureType"
                                    items={[
                                        {
                                            text: "Химеотерапия",
                                            value: "Химеотерапия"
                                        },
                                        {
                                            text: "Лучевая терапия",
                                            value: "Лучевая терапия"
                                        },
                                        {
                                            text: "Операция",
                                            value: "Операция"
                                        },
                                        {
                                            text: "Таргетная терапия",
                                            value: "Таргетная терапия"
                                        },
                                        {
                                            text: "Гормонотерапия",
                                            value: "Гормонотерапия"
                                        },
                                        {
                                            text: "Паллиативное лечение",
                                            value: "Паллиативное лечение"
                                        }
                                    ]}
                                    disabled
                                    unrequired
                                />
                            </Col>
                            <Col span={8}>
                                <h3 className="client_card__subtitle">Что хочет получить от платформы</h3>
                                <CheckboxGroupFormComponent
                                    name="recomendationType"
                                    items={[
                                        {
                                            text: "Информацию о том, как справляться с эмоциями",
                                            value: "Информацию о том, как справляться с эмоциями"
                                        },
                                        {
                                            text: "Упражнения, чтобы самому приводить себя в норму",
                                            value: "Упражнения, чтобы самому приводить себя в норму"
                                        },
                                        {
                                            text: "Группу поддержки",
                                            value: "Группу поддержки"
                                        },
                                        {
                                            text: "Индивидуальную работу с психологом",
                                            value: "Индивидуальную работу с психологом"
                                        },
                                        {
                                            text: "Другое",
                                            value: "Другое",
                                            textAreaItem: {
                                                name: "recomendationDescription",
                                                errorMessage:
                                                    "Пожалуйста, опишите что именно хочет получить клиент от платформы"
                                            },
                                            isAreaItemOpen: openInput
                                        }
                                    ]}
                                    unrequired
                                    disabled
                                />
                            </Col>
                        </Row>
                    </Form>
                </Tabs.TabPane>
                <Tabs.TabPane tab="Консультации" key="2">
                    <PageContainer
                        header={{
                            title: "",
                            breadcrumb: {}
                        }}
                    >
                        <ConsultationsTable clientEmail={client.clientEmail} />
                    </PageContainer>
                </Tabs.TabPane>
                <Tabs.TabPane tab="Тесты" key="3">
                    <PageContainer
                        header={{
                            title: "",
                            breadcrumb: {}
                        }}
                    >
                        <TestsTable userId={client.public_user_id} />
                    </PageContainer>
                </Tabs.TabPane>
            </Tabs>
        );
    };

    return (
        <PageContainer>
            <h1 className="client_card__title">Карточка клиента</h1>
            <PageLoadingWithParentComponent isLoading={isLoading} body={renderTabs()} />
        </PageContainer>
    );
};

export default ClientCardPage;
