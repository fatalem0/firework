import * as React from "react";
import {Result, Table, Tag, Row} from "antd";
import {useMount} from "react-use";
import {ColumnsType} from "antd/es/table";
import PageLoadingWithParentComponent from "src/components/pageLoadingWithParentComponent/pageLoadingWithParentComponent";
import TimeLabel from "src/components/timeLabel/timeLabel";
import testQueries from "src/queries/testQueries";
import {TestResult} from "src/types";
import {sleep} from "src/utils";

interface Props {
    userId?: string;
}

const columns: ColumnsType<TestResult> = [
    {
        title: "ФИО пользователя",
        dataIndex: "usedId",
        key: "usedId",
        width: "min-content",
        render: (_, record) => <span>{record.clientFullName}</span>
    },
    {
        title: "Email",
        dataIndex: "email",
        key: "email",
        width: "min-content",
        render: (_, record) => <span>{record.email}</span>
    },
    {
        title: "Дата прохождения",
        dataIndex: "date",
        key: "date",
        width: "min-content",
        render: (_, record) => <TimeLabel time={record.startDate} />
    },
    {
        title: "Название теста",
        dataIndex: "title",
        key: "title",
        width: "min-content",
        render: (_, record) => <span>{record.name}</span>
    },
    {
        title: "Результат",
        dataIndex: "title",
        key: "title",
        width: "min-content",
        render: (_, record) => <Tag color={record.total > 500 ? "red" : "blue"}>{record.total}</Tag>
    }
];

const TestsTable: React.FC<Props> = (props: Props) => {
    const listTests = testQueries.listTests();
    const [data, setData] = React.useState<TestResult[]>();
    const [isLoading, changeIsLoading] = React.useState<boolean>(true);

    useMount(async () => {
        await sleep(100);
        await listTests.refetch();
    });

    React.useEffect(() => {
        if (!listTests) {
            return;
        }
        const listTestsData = listTests.data;
        changeIsLoading(true);
        if (props.userId) {
            setData(listTestsData?.filter((item) => item.user_id === props.userId));
        } else {
            setData(listTestsData);
        }
    }, [props.userId, listTests.data]);

    React.useEffect(() => {
        changeIsLoading(!data);
    }, [data]);

    return (
        <PageLoadingWithParentComponent
            isLoading={isLoading}
            body={
                <Table
                    columns={columns}
                    dataSource={data}
                    rowKey={(record) => record.public_id}
                    pagination={false}
                    size="middle"
                    loading={{delay: 100, spinning: false}}
                    locale={{
                        emptyText: <Result icon={<></>} title="В поиске не найдено подходящих результатов"></Result>
                    }}
                />
            }
        />
    );
};

export default TestsTable;
