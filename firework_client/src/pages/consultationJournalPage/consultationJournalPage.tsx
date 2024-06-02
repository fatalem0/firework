import * as React from "react";
import {PageContainer} from "@ant-design/pro-components";
import {Typography} from "antd";
import ConsultationsTable from "src/components/consultationsTable/consultationsTable";

const ConsultationsPage: React.FC = () => {
    return (
        <PageContainer
            header={{
                title: "",
                breadcrumb: {}
            }}
        >
            <Typography.Title>Журнал консультаций</Typography.Title>
            <ConsultationsTable />
        </PageContainer>
    );
};

export default ConsultationsPage;
