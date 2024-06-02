import * as React from "react";
import {Link} from "react-router-dom";
import {useMount} from "react-use";
import {Result, Table, Input, Button, Typography} from "antd";
import {SearchOutlined, DownOutlined, RightCircleOutlined} from "@ant-design/icons";
import {PageContainer} from "@ant-design/pro-components";
import {ColumnsType} from "antd/es/table";
import PageLoadingWithParentComponent from "src/components/pageLoadingWithParentComponent/pageLoadingWithParentComponent";
import TimeLabel from "src/components/timeLabel/timeLabel";
import clientQueries from "src/queries/clientQueries";
import {Client} from "src/types";
import {sleep} from "src/utils";

const columns: ColumnsType<Client> = [
    {
        title: "",
        key: "action",
        render: (_, record) => (
            <Link to={`/clientsCard/${record.public_id}`}>
                <RightCircleOutlined style={{color: "#868FA0"}} />
            </Link>
        )
    },
    {
        title: "ФИО",
        dataIndex: ["firstName", "lastName", "middleName"],
        key: "fullName",
        width: "min-content",
        filterDropdown: ({setSelectedKeys, selectedKeys, confirm, clearFilters}) => (
            <div style={{padding: 8}}>
                <Input
                    placeholder="Поиск ФИО"
                    value={selectedKeys[0]}
                    onChange={(e) => setSelectedKeys(e.target.value ? [e.target.value] : [])}
                    onPressEnter={() => confirm()}
                    style={{width: 188, marginBottom: 8, display: "block"}}
                />
                <Button
                    type="primary"
                    onClick={() => confirm()}
                    icon={<SearchOutlined />}
                    size="small"
                    style={{width: 90, marginRight: 8}}
                >
                    Поиск
                </Button>
                <Button onClick={clearFilters} size="small" style={{width: 90}}>
                    Сбросить
                </Button>
            </div>
        ),
        filterIcon: (filtered) => <DownOutlined style={{color: filtered ? "#1890ff" : undefined}} />,
        onFilter: (value, record) =>
            typeof value === "string" ? record.clientFullName.toLowerCase().includes(value.toLowerCase()) : false,
        render: (_, record) => <span>{record.clientFullName}</span>
    },
    {
        title: "Почта",
        dataIndex: "email",
        key: "email",
        width: "min-content",
        filterDropdown: ({setSelectedKeys, selectedKeys, confirm, clearFilters}) => (
            <div style={{padding: 8}}>
                <Input
                    placeholder="Поиск почты"
                    value={selectedKeys[0]}
                    onChange={(e) => setSelectedKeys(e.target.value ? [e.target.value] : [])}
                    onPressEnter={() => confirm()}
                    style={{width: 188, marginBottom: 8, display: "block"}}
                />
                <Button
                    type="primary"
                    onClick={() => confirm()}
                    icon={<SearchOutlined />}
                    size="small"
                    style={{width: 90, marginRight: 8}}
                >
                    Поиск
                </Button>
                <Button onClick={clearFilters} size="small" style={{width: 90}}>
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
        title: "Локализация заболевания",
        dataIndex: "userStatus",
        key: "userStatus",
        width: "min-content",
        render: (_, record) => <span>{record.stageActual}</span>
    },
    {
        title: "Тип",
        dataIndex: "userType",
        key: "userType",
        width: "min-content",
        render: (text, record) => <span>{record.clientTypeActual}</span>
    },
    {
        title: "Дата регистрации",
        dataIndex: "updated",
        key: "updated",
        width: "min-content",
        render: (_, record) => <TimeLabel time={record.clientCreated} />
    }
];

const ClientsPage: React.FC = () => {
    const listClients = clientQueries.listClients();
    const [clients, changeClients] = React.useState<Client[]>();
    const [isLoading, changeIsLoading] = React.useState<boolean>(true);

    useMount(async () => {
        await sleep(100);
        await listClients.refetch();
    });

    React.useEffect(() => {
        changeIsLoading(true);
        changeClients(listClients.data);
    }, [listClients.data]);

    React.useEffect(() => {
        changeIsLoading(!clients);
    }, [clients]);

    return (
        <PageContainer
            header={{
                title: "",
                breadcrumb: {}
            }}
        >
            <Typography.Title>Клиенты</Typography.Title>
            <PageLoadingWithParentComponent
                isLoading={isLoading}
                body={
                    <Table
                        columns={columns}
                        dataSource={clients}
                        rowKey={(record) => record.public_id}
                        pagination={{pageSize: 20, showSizeChanger: false}}
                        size="middle"
                        loading={{delay: 100, spinning: false}}
                        locale={{
                            filterConfirm: "Применить",
                            filterReset: "Сбросить",
                            emptyText: (
                                <Result icon={<></>} title="Клиенты здесь появятся как только вы их добавите."></Result>
                            )
                        }}
                    />
                }
            />
        </PageContainer>
    );
};

export default ClientsPage;
