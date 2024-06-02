import "./consultationsTable.scss";

import * as React from "react";
import {Link} from "react-router-dom";
import {useMount} from "react-use";
import {SearchOutlined, RightCircleOutlined, CheckOutlined, DownOutlined} from "@ant-design/icons";
import {Result, Table, Button, Input, notification, FormInstance, Row, Typography} from "antd";
import {ColumnsType} from "antd/es/table";
import ConsultationFormPopup from "src/components/consultationPopup/ConsultationPopup";
import FormPopup from "src/components/formPopup/formPopup";
import PageLoadingWithParentComponent from "src/components/pageLoadingWithParentComponent/pageLoadingWithParentComponent";
import TimeLabel from "src/components/timeLabel/timeLabel";
import consultationQueries from "src/queries/consultationQueries";
import {Consultation, ConsultationForm} from "src/types";
import {sleep} from "src/utils";

interface Props {
    clientEmail?: string;
}

const columns: ColumnsType<Consultation> = [
    {
        title: "",
        key: "action",
        render: (_, record) => (
            <Link to={`/consultationsCardPage/${record.public_id}`}>
                <RightCircleOutlined style={{color: "#868FA0"}} />
            </Link>
        )
    },
    {
        title: "Дата консультации",
        dataIndex: "date",
        key: "date",
        width: "min-content",
        render: (_, record) => <TimeLabel time={record.created} />
    },
    {
        title: "E-mail",
        dataIndex: "email",
        key: "email",
        width: "min-content",
        filterDropdown: ({setSelectedKeys, selectedKeys, confirm, clearFilters}) => (
            <div style={{padding: 8}}>
                <Input
                    className="consultation_tab__input"
                    placeholder="Поиск почты"
                    value={selectedKeys[0]}
                    onChange={(e) => setSelectedKeys(e.target.value ? [e.target.value] : [])}
                    onPressEnter={() => confirm()}
                />
                <Button
                    className="consultation_tab__button-search"
                    type="primary"
                    onClick={() => confirm()}
                    icon={<SearchOutlined />}
                    size="small"
                >
                    Поиск
                </Button>
                <Button onClick={clearFilters} size="small" className="consultation_tab__button-reset">
                    Сбросить
                </Button>
            </div>
        ),
        filterIcon: (filtered) => <DownOutlined style={{color: filtered ? "#1890ff" : undefined}} />,
        onFilter: (value, record) =>
            record.clientEmail.toLowerCase().includes(typeof value === "string" ? value.toLowerCase() : ""),
        render: (_, record) => <a href={`mailto:${record.clientEmail}`}>{record.clientEmail}</a>
    },
    {
        title: "ФИО специалиста",
        dataIndex: ["firstNameDoctor", "lastNameDoctor", "middleNameDoctor"],
        key: "fullNameDoctor",
        width: "min-content",
        filterDropdown: ({setSelectedKeys, selectedKeys, confirm, clearFilters}) => (
            <div style={{padding: 8}}>
                <Input
                    className="consultation_tab__input"
                    placeholder="Поиск ФИО специалиста"
                    value={selectedKeys[0]}
                    onChange={(e) => setSelectedKeys(e.target.value ? [e.target.value] : [])}
                    onPressEnter={() => confirm()}
                />
                <Button
                    className="consultation_tab__button-search"
                    type="primary"
                    onClick={() => confirm()}
                    icon={<SearchOutlined />}
                    size="small"
                >
                    Поиск
                </Button>
                <Button onClick={clearFilters} size="small" className="consultation_tab__button-reset">
                    Сбросить
                </Button>
            </div>
        ),
        filterIcon: (filtered) => <DownOutlined style={{color: filtered ? "#1890ff" : undefined}} />,
        onFilter: (value, record) =>
            typeof value === "string" ? record.specialistFullName.toLowerCase().includes(value.toLowerCase()) : false,
        render: (_, record) => <span> {`${record.specialistFullName}`}</span>
    },
    {
        title: "ФИО клиента",
        dataIndex: ["firstName", "lastName", "middleName"],
        key: "fullName",
        width: "min-content",
        filterDropdown: ({setSelectedKeys, selectedKeys, confirm, clearFilters}) => (
            <div style={{padding: 8}}>
                <Input
                    className="consultation_tab__input"
                    placeholder="Поиск ФИО"
                    value={selectedKeys[0]}
                    onChange={(e) => setSelectedKeys(e.target.value ? [e.target.value] : [])}
                    onPressEnter={() => confirm()}
                />
                <Button
                    className="consultation_tab__button-search"
                    type="primary"
                    onClick={() => confirm()}
                    icon={<SearchOutlined />}
                    size="small"
                >
                    Поиск
                </Button>
                <Button onClick={clearFilters} size="small" className="consultation_tab__button-reset">
                    Сбросить
                </Button>
            </div>
        ),
        filterIcon: (filtered) => <DownOutlined style={{color: filtered ? "#1890ff" : undefined}} />,
        onFilter: (value, record) =>
            typeof value === "string" ? record.clientFullName.toLowerCase().includes(value.toLowerCase()) : false,
        render: (_, record) => <span> {`${record.clientFullName}`}</span>
    },
    {
        title: "Тип",
        dataIndex: "userType",
        key: "userType",
        width: "min-content",
        render: (text, record) => <span>{record.statusConsultationActual}</span>
    },
    {
        title: "Статус",
        dataIndex: "status",
        key: "status",
        width: "min-content",
        render: (text, record) => <span>{record.validationStatusActual}</span>
    }
];

const ConsultationsTable: React.FC<Props> = (props: Props) => {
    const listConsultations = consultationQueries.listConsultations();
    const createConsultation = consultationQueries.createConsultation();
    const [api, contextHolder] = notification.useNotification();
    const [isRegFormOpen, setIsRegFormOpen] = React.useState<boolean>(false);
    const [data, setData] = React.useState<Consultation[]>();
    const [isFormSubmitting, setIsFormSubmitting] = React.useState<boolean>(false);
    const [isLoading, changeIsLoading] = React.useState<boolean>(true);

    const openNotification = (title: string, description: string) => {
        api.info({
            message: title,
            description,
            placement: "bottomRight",
            icon: <CheckOutlined style={{color: "#b0fc38"}} />
        });
    };

    useMount(async () => {
        await sleep(100);
        await listConsultations.refetch();
    });

    React.useEffect(() => {
        if (!listConsultations.data) {
            return;
        }
        const listConsultationsData = listConsultations.data;
        changeIsLoading(true);
        if (props.clientEmail) {
            setData(listConsultationsData?.filter((item) => item.clientEmail === props.clientEmail) || []);
        } else {
            setData(listConsultationsData || []);
        }
    }, [props.clientEmail, listConsultations.data]);

    React.useEffect(() => {
        changeIsLoading(!data);
    }, [data]);

    const submitRegForm = async (values: ConsultationForm, form: FormInstance<ConsultationForm>) => {
        let public_id = "";
        try {
            setIsFormSubmitting(true);
            const createdConsultation = await createConsultation.mutateAsync(values);
            public_id = createdConsultation.public_id;
            setIsRegFormOpen(false);
            openNotification("Консультация создана", "");

            await sleep(1000);
            form.resetFields();
        } catch (e) {
            console.error("Ocurred error: ", e);
        } finally {
            setIsFormSubmitting(false);
            // eslint-disable-next-line no-unsafe-finally
            return public_id;
        }
    };

    return (
        <>
            {contextHolder}
            <Row align="middle" justify="space-between">
                <Typography.Title></Typography.Title>
                <Button type="primary" onClick={() => setIsRegFormOpen(true)} style={{backgroundColor: "#265189"}}>
                    Добавить консультацию
                </Button>
            </Row>
            <PageLoadingWithParentComponent
                isLoading={isLoading}
                body={
                    <Table
                        columns={columns}
                        dataSource={data}
                        rowKey={(record) => record.public_id}
                        pagination={{pageSize: 20}}
                        loading={{delay: 100, spinning: false}}
                        size="middle"
                        locale={{
                            filterConfirm: "Применить",
                            filterReset: "Сбросить",
                            emptyText: (
                                <Result
                                    icon={<></>}
                                    title={
                                        props.clientEmail
                                            ? "У этого человека не были ни одной консультации. Для добавления новой коснультации нажмите на кнопку справа сверху от таблицы."
                                            : "На данный момент не существует ни одной консультации. Для добавления новой коснультации нажмите на кнопку справа сверху от таблицы."
                                    }
                                ></Result>
                            )
                        }}
                    />
                }
            />
            <FormPopup
                isOpen={isRegFormOpen}
                changeIsOpen={setIsRegFormOpen}
                formBody={
                    <ConsultationFormPopup
                        onSubmitFunc={submitRegForm}
                        isFormSubmitting={isFormSubmitting}
                        clientEmail={props.clientEmail}
                    />
                }
            />
        </>
    );
};

export default ConsultationsTable;
