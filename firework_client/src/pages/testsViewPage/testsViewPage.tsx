import * as React from "react";
import {PageContainer} from "@ant-design/pro-components";
import {useNavigate} from "react-router-dom";
import {EditOutlined} from "@ant-design/icons";
import {Result, Table, Row, Typography, Button} from "antd";
import {useMount} from "react-use";
import {ColumnsType} from "antd/es/table";
import testQueries from "src/queries/testQueries";
import {TestInfo} from "src/types";
import {sleep} from "src/utils";
import PageLoadingWithParentComponent from "src/components/pageLoadingWithParentComponent/pageLoadingWithParentComponent";

const TestsViewPage: React.FC = () => {
    const navigate = useNavigate();
    const listAvailTests = testQueries.listAvailTests();
    const [tests, changeTests] = React.useState<TestInfo[]>();
    const [isLoading, changeIsLoading] = React.useState<boolean>(true);

    const columns: ColumnsType<TestInfo> = [
        {
            title: "Название теста",
            dataIndex: "name",
            key: "name",
            render: (_, record) => <span>{record.name}</span>
        },
        {
            title: "Минимальное количество баллов",
            dataIndex: "minScore",
            key: "minScore",
            width: "min-content",
            render: (_, record) => <span>{record.minScore}</span>
        },
        {
            title: "Максимальное количетсво баллов",
            dataIndex: "maxScore",
            key: "maxScore",
            width: "min-content",
            render: (_, record) => <span>{record.maxScore}</span>
        },
        {
            title: "Количество вопросов",
            dataIndex: "numberOfQuestions",
            key: "numberOfQuestions",
            width: "min-content",
            render: (_, record) => (
                <Row align="middle" justify="space-between">
                    <span>{record.numberOfQuestions}</span>
                    <Button
                        type="text"
                        icon={<EditOutlined />}
                        onClick={() => navigate(`/testsEditing/${record.public_id}`)}
                    />
                </Row>
            )
        }
    ];

    useMount(async () => {
        await sleep(100);
        await listAvailTests.refetch();
    });

    React.useEffect(() => {
        if (!listAvailTests.data) {
            return;
        }
        changeIsLoading(true);
        changeTests(listAvailTests.data || []);
    }, [listAvailTests.data]);

    React.useEffect(() => {
        changeIsLoading(!tests);
    }, [tests]);

    return (
        <PageContainer
            header={{
                title: "",
                breadcrumb: {}
            }}
        >
            <Row align="middle" justify="space-between">
                <Typography.Title />
                <Button type="primary" onClick={() => navigate("/testsEditing")} style={{backgroundColor: "#265189"}}>
                    Создать тест
                </Button>
            </Row>
            <PageLoadingWithParentComponent
                isLoading={isLoading}
                body={
                    <Table
                        columns={columns}
                        dataSource={tests}
                        rowKey={(record) => record.public_id}
                        pagination={false}
                        loading={{delay: 100, spinning: false}}
                        size="middle"
                        locale={{
                            emptyText: <Result icon={<></>} title="В поиске не найдено подходящих результатов"></Result>
                        }}
                    />
                }
            />
        </PageContainer>
    );
};

export default TestsViewPage;
