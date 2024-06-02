import * as React from "react";
import {PageContainer} from "@ant-design/pro-components";
import {useMount} from "react-use";
import {Result, Table, Typography, Row, Button, Input, notification, FormInstance} from "antd";
import {SearchOutlined, CheckOutlined, DownOutlined} from "@ant-design/icons";
import {ColumnsType} from "antd/es/table";
import DrawerForm from "src/components/drawerForm/drawerForm";
import PageLoadingWithParentComponent from "src/components/pageLoadingWithParentComponent/pageLoadingWithParentComponent";
import RegisterFormPopup from "src/components/registerPopup/RegisterPopup";
import TimeLabel from "src/components/timeLabel/timeLabel";
import userQueries from "src/queries/userQueries";
import {User, UserForm} from "src/types";
import {sleep} from "src/utils";

const columns: ColumnsType<User> = [
    {
        title: "ФИО",
        dataIndex: "lastName",
        key: "lastName",
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
            typeof value === "string"
                ? record.firstName.toLowerCase().includes(value.toLowerCase()) ||
                  record.lastName.toLowerCase().includes(value.toLowerCase()) ||
                  (record.middleName ? record.middleName.toLowerCase().includes(value.toLowerCase()) : false)
                : false,
        render: (_, record) => <span>{`${record.lastName} ${record.firstName} ${record.middleName ?? "-"}`}</span>
    },
    {
        title: "E-mail",
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
            record.email.toLowerCase().includes(typeof value === "string" ? value.toLowerCase() : ""),
        render: (_, record) => <span>{record.email}</span>
    },
    {
        title: "Пол",
        dataIndex: "sex",
        key: "sex",
        width: "min-content",
        render: (_, record) => <span>{record.sexActual === "Мужской" ? "М" : "Ж"}</span>
    },
    {
        title: "Телефон",
        dataIndex: "phoneNumber",
        key: "phoneNumber",
        width: "min-content",
        render: (_, record) => <span>{record.phoneNumber}</span>
    },
    {
        title: "Тип",
        dataIndex: "userType",
        key: "userType",
        width: "min-content",
        render: (_, record) => <span>{record.userTypeActual}</span>
    },
    {
        title: "Дата создания",
        dataIndex: "created",
        key: "created",
        width: "min-content",
        render: (_, record) => <TimeLabel time={record.created} />
    },
    {
        title: "Дата последнего обновления",
        dataIndex: "updated",
        key: "updated",
        width: "min-content",
        render: (_, record) => <TimeLabel time={record.updated} />
    }
];

const UsersPage: React.FC = () => {
    const [api, contextHolder] = notification.useNotification();
    const listUsers = userQueries.listUsers();
    const createUser = userQueries.createUser();
    const [users, changeUsers] = React.useState<User[]>();
    const [isRegFormOpen, setIsRegFormOpen] = React.useState<boolean>(false);
    const [isFormSubmitting, setIsFormSubmitting] = React.useState<boolean>(false);
    const [isLoading, changeIsLoading] = React.useState<boolean>(true);

    useMount(async () => {
        await sleep(100);
        await listUsers.refetch();
    });

    const openNotification = (title: string, description: string) => {
        api.info({
            message: title,
            description,
            placement: "bottomRight",
            icon: <CheckOutlined style={{color: "#b0fc38"}} />
        });
    };

    React.useEffect(() => {
        if (!listUsers.data) {
            return;
        }
        changeIsLoading(true);
        changeUsers(listUsers.data || []);
    }, [listUsers.data]);

    React.useEffect(() => {
        changeIsLoading(!users);
    }, [users]);

    const submitRegForm = async (values: UserForm, form: FormInstance<UserForm>) => {
        try {
            setIsFormSubmitting(true);
            await createUser.mutateAsync(values);
            setIsRegFormOpen(false);
            openNotification("Пользователь был создан", "");

            await sleep(1000);
            form.resetFields();
        } catch (e) {
            console.error("Ocurred error: ", e);
        } finally {
            setIsFormSubmitting(false);
        }
    };

    return (
        <PageContainer
            header={{
                title: "",
                breadcrumb: {}
            }}
        >
            {contextHolder}
            <Row align="middle" justify="space-between">
                <Typography.Title></Typography.Title>
                <Button type="primary" onClick={() => setIsRegFormOpen(true)} style={{backgroundColor: "#265189"}}>
                    Зарегистрировать пользователя
                </Button>
            </Row>
            <PageLoadingWithParentComponent
                isLoading={isLoading}
                body={
                    <Table
                        columns={columns}
                        dataSource={users}
                        rowKey={(record) => record.public_id}
                        pagination={false}
                        size="middle"
                        loading={{delay: 100, spinning: false}}
                        locale={{
                            emptyText: (
                                <Result
                                    icon={<></>}
                                    title="Пользователи здесь появятся как только вы их добавите. Для этого используйте кнопку справа сверху таблицы."
                                ></Result>
                            )
                        }}
                    />
                }
            />
            <DrawerForm
                isFormOpen={isRegFormOpen}
                changeIsFormOpen={setIsRegFormOpen}
                formBody={<RegisterFormPopup onSubmitFunc={submitRegForm} isFormSubmitting={isFormSubmitting} />}
                title="Регистрация нового пользователя"
                width={500}
            />
        </PageContainer>
    );
};

export default UsersPage;
