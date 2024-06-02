// TOOD (thefirefox15): It's bad, but it is...
// @ts-nocheck
import * as React from "react";
import {Collapse} from "antd";
import {CaretRightOutlined} from "@ant-design/icons";

interface ElemProps {
    itemIdx: number;
    outerUid: number;
    uid: number;
    addItem: () => void;
    removeItem: (elem: number) => void;
    length: number;
}

interface Props {
    body: React.ReactElement<ElemProps>;
    useCollapse?: boolean;
    useCollapseItem?: boolean;
    outerUid?: number;
    collapseItemHeaderGenerator?: (idx: number) => string;
}

const activeKeysDefaultOpen = Array.from(Array(1000).keys());
const collapseRotateActiveAngle = 90;
const collapseRotateDisableAngle = 0;

const DynamicComponentsList: React.FC<Props> = (props: Props) => {
    const [activeItems, changeActiveItems] = React.useState<number[]>([0]);
    const [currentCreatedItemsCount, changeCurrentCreatedItemsCount] = React.useState<number>(0);

    const addItem = () => {
        changeCurrentCreatedItemsCount(currentCreatedItemsCount + 1);
        changeActiveItems([...activeItems, currentCreatedItemsCount + 1]);
    };

    const removeItem = (elem: number) => {
        const itemIdx = activeItems.findIndex((item) => item === elem);
        changeActiveItems([...activeItems.slice(0, itemIdx), ...activeItems.slice(itemIdx + 1)]);
    };

    const renderItem = (idx: number, item: number) => {
        return props?.useCollapseItem && props.collapseItemHeaderGenerator ? (
            <Collapse.Panel header={props.collapseItemHeaderGenerator(idx)} key={idx}>
                {React.cloneElement(props.body, {
                    itemIdx: idx,
                    uid: item,
                    addItem,
                    removeItem,
                    length: activeItems.length,
                    outerUid: props.outerUid
                })}
            </Collapse.Panel>
        ) : (
            React.cloneElement(props.body, {
                itemIdx: idx,
                uid: item,
                addItem,
                removeItem,
                length: activeItems.length,
                outerUid: props.outerUid
            })
        );
    };

    return props?.useCollapse ? (
        <Collapse
            bordered={false}
            style={{background: "#F5F5F5"}}
            expandIcon={({isActive}) => (
                <CaretRightOutlined rotate={isActive ? collapseRotateActiveAngle : collapseRotateDisableAngle} />
            )}
            defaultActiveKey={activeKeysDefaultOpen}
        >
            {activeItems.map((item, idx) => renderItem(idx, item))}
        </Collapse>
    ) : (
        activeItems.map((item, idx) => renderItem(idx, item))
    );
};

export default DynamicComponentsList;
