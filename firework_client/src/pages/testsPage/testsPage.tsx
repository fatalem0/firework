import * as React from "react";
import {PageContainer} from "@ant-design/pro-components";
import TestsTable from "src/components/testsTable/testsTable";

const TestsPage: React.FC = () => {
    return (
        <PageContainer
            header={{
                title: "",
                breadcrumb: {}
            }}
        >
            <TestsTable />
        </PageContainer>
    );
};

export default TestsPage;
