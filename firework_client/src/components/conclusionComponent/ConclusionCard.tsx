import React from "react";
import CheckboxGroupFormComponent from "src/formComponents/checkboxGroupFormComponent/checkboxGroupFormComponent";
import InputFormComponent from "src/formComponents/inputFormComponent/inputFormComponent";
import RadioGroupFormComponent from "src/formComponents/radioGroupFormComponent/radioGroupFormComponent";

interface Props {
    openInput: boolean;
}

const ConclusionCard: React.FC<Props> = (props: Props) => {
    return (
        <>
            <InputFormComponent name="conclNotes" label="Заметки" isTextArea />
            <CheckboxGroupFormComponent
                name="conclusionCard"
                items={[
                    {
                        value: "hasAdaptationDisorder",
                        text: "Расстройство адаптации"
                    },
                    {
                        value: "hasAnxietyDisorder",
                        text: "Тревожное расстройство"
                    },
                    {
                        value: "hasDepressionClinical",
                        text: "Депрессия клиническая"
                    },
                    {
                        value: "hasAcutePsyReact",
                        text: "Острая психологическая реакция"
                    },
                    {
                        value: "hasPostDisorder",
                        text: "Посттравматическое расстройство"
                    },
                    {
                        value: "hasConclOther",
                        text: "Другое",
                        textAreaItem: {
                            name: "conclOtherNote",
                            style: {marginBottom: 0},
                            errorMessage: "Пожалуйста, опишите пункт выше"
                        },
                        isAreaItemOpen: props.openInput
                    }
                ]}
            />
            <InputFormComponent
                name="conclFirstPlanNote"
                label="На первый план выходит"
                errorMessage="Пожалуйста, опишите что выходит на первый план"
                isTextArea
            />
            <InputFormComponent
                name="conclOnBackgroundNote"
                label="На фоне"
                errorMessage="Пожалуйста, опишите что происходит на фоне"
                isTextArea
            />
            <RadioGroupFormComponent
                name="hasInnerPicture"
                label="Внутренняя картина болезни"
                items={[
                    {
                        value: true,
                        text: "Сформирована"
                    },
                    {
                        value: false,
                        text: "Не сформирована"
                    }
                ]}
            />
            <InputFormComponent
                name="conclTargetNote"
                label="Мишени психотерапии"
                errorMessage="Пожалуйста, опишите мишени психотерапии"
                isTextArea
            />
        </>
    );
};

export default ConclusionCard;
