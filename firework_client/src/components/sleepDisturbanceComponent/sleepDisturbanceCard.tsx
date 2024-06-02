import React from "react";
import InputFormComponent from "src/formComponents/inputFormComponent/inputFormComponent";
import CheckboxGroupFormComponent from "../../formComponents/checkboxGroupFormComponent/checkboxGroupFormComponent";
import RadioGroupFormComponent from "src/formComponents/radioGroupFormComponent/radioGroupFormComponent";

interface Props {
    openInput: boolean;
}

const SleepDisturbanceCard: React.FC<Props> = (props: Props) => {
    return (
        <>
            <CheckboxGroupFormComponent
                name="sleepDisturbance"
                items={[
                    {
                        value: "isHardToFallAsleep",
                        text: "Нарушение засыпания"
                    },
                    {
                        value: "hasFrequentWaking",
                        text: "Частое пробуждение"
                    },
                    {
                        value: "isAwakeEarly",
                        text: "Проснуться рано",
                        textAreaItem: {
                            name: "earlyAwakeningNote",
                            style: {marginBottom: 0}
                        },
                        isAreaItemOpen: props.openInput
                    },
                    {
                        value: "hasSleepDeprivation",
                        text: "Чувство после сна, что не выспался"
                    },
                    {
                        value: "hasIncreasedDrowsiness",
                        text: "Повышение сонливости: много спит и ночью и днем"
                    }
                ]}
            />
            <RadioGroupFormComponent
                name="isCopeWithSleepDisturbancesActual"
                label="Справляется"
                items={[
                    {
                        text: "Самостоятельно",
                        value: "bySelf"
                    },
                    {
                        text: "С помощью медикаментов",
                        value: "withMedicine"
                    },
                    {
                        text: "Не справляется",
                        value: "cantСope"
                    }
                ]}
            />
            <InputFormComponent name="sleepNote" isTextArea />
        </>
    );
};

export default SleepDisturbanceCard;
