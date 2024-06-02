import React from "react";
import CheckboxGroupFormComponent from "src/formComponents/checkboxGroupFormComponent/checkboxGroupFormComponent";
import InputFormComponent from "src/formComponents/inputFormComponent/inputFormComponent";
import RadioGroupFormComponent from "src/formComponents/radioGroupFormComponent/radioGroupFormComponent";

import "./objectiveCard.scss";

const ObjectiveCard: React.FC = () => {
    return (
        <>
            <InputFormComponent
                name="featuresConversationsNote"
                label="Особенности беседы"
                errorMessage="Пожалуйста, опишите особенности беседы"
                isTextArea
            />
            <RadioGroupFormComponent
                name="hasAnxiety"
                label="Тревога"
                items={[
                    {
                        text: "Есть",
                        value: true
                    },
                    {
                        text: "Нет",
                        value: false
                    }
                ]}
            />
            <RadioGroupFormComponent
                name="hasContinuousDuration"
                label="Тревога"
                items={[
                    {
                        text: "Более 2 недель",
                        value: true
                    },
                    {
                        text: "Менее 2 недель",
                        value: false
                    }
                ]}
            />
            <CheckboxGroupFormComponent
                name="groupOneFields"
                label="Группа 1"
                items={[
                    {
                        text: "Постоянное снижение настроения",
                        value: "hasPersistentLowMood"
                    },
                    {
                        text: "Утрата интересов",
                        value: "hasLossInterest"
                    },
                    {
                        text: "Снижение энергии или усталось после минимальных усилий",
                        value: "hasEnergyDecline"
                    }
                ]}
            />
            <CheckboxGroupFormComponent
                name="groupTwoFields"
                label="Группа 2"
                items={[
                    {
                        text: "Снижение концентрации внимания",
                        value: "hasDecliningAttention"
                    },
                    {
                        text: "Чувство вины и никчемность",
                        value: "hasGuilt"
                    },
                    {
                        text: "Снижение самооценки и уверенности в себе",
                        value: "hasLowerSelfesteem"
                    },
                    {
                        text: "Изменение аппетита и веса",
                        value: "hasAppetiteChange"
                    },
                    {
                        text: "Нарушение сна",
                        value: "hasSleepDisturbance"
                    },
                    {
                        text: "Пессимистические мысли и погружение в себя",
                        value: "hasPessimisticThoughts"
                    },
                    {
                        text: "Безнадежность",
                        value: "hasHopelessness"
                    },
                    {
                        text: "Суицидальные мысли и действия",
                        value: "hasSuicidalThoughts"
                    }
                ]}
            />
            <InputFormComponent
                name="symptomAtRelationshipNote"
                label="Влияние симптомов на межличностные отношения"
                errorMessage="Пожалуйста, опишите влияние симптомов"
                isTextArea
            />
            <InputFormComponent
                name="suicidalThoughtsNote"
                label="Суицидальные мысли"
                errorMessage="Пожалуйста, опишите есть ли суицидальные мысли у клиента"
                isTextArea
            />
        </>
    );
};

export default ObjectiveCard;
