import "./testDescCard.scss";

import * as React from "react";
import {Descriptions} from "antd";
import bevis from "src/utils/bevis";

interface Props {
    answers: string[];
    questions: string[];
}

const b = bevis("ard-desc");

const TestDescCard: React.FC<Props> = ({answers, questions}) => {
    const RenderData = () => {
        return questions.map((item, idx) => (
            <Descriptions.Item
                span={3}
                label={
                    <span className={b("item-title")} key={idx}>
                        {item}
                    </span>
                }
            >
                {answers[idx]}
            </Descriptions.Item>
        ));
    };

    return <Descriptions>{RenderData()}</Descriptions>;
};

export default TestDescCard;
