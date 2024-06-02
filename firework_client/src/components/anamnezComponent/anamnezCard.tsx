import React from "react";
import InputFormComponent from "src/formComponents/inputFormComponent/inputFormComponent";
import RadioGroupFormComponent from "src/formComponents/radioGroupFormComponent/radioGroupFormComponent";

interface Props {
    openInput: boolean;
}

const AnamnesisCard: React.FC<Props> = (props: Props) => {
    return (
        <>
            <InputFormComponent
                name="oncologyTime"
                label="Как долго живет с онкологическим диагнозом"
                errorMessage="Пожалуйста, введите как долго клиент живет с диагнозом"
                isTextArea
            />
            <InputFormComponent
                name="emotionReactOnco"
                label="Какие эмоциональные реакции были в момент первого озвучивания подтверждения диагноза"
                errorMessage="Пожалуйста, введите как эмоциональные реакциии были у клиента были"
                isTextArea
            />
            <InputFormComponent
                name="experiencingEmotion"
                label="Как справлялся с теми реакциями"
                errorMessage="Пожалуйста, введите как клиент справлялся с теми реакциями"
                isTextArea
            />
            <InputFormComponent
                name="usuallyHelpEmotion"
                label="Что помогает обычно справляться с эмоциональными реакциями"
                errorMessage="Пожалуйста, введите что помогает клиенту справляться"
                isTextArea
            />
            <InputFormComponent
                name="usuallyNoHelpEmotion"
                label="Что не помогает вообще или в конкретном случае не помогло"
                errorMessage="Пожалуйста, введите что не помогает клиенту справляться"
                isTextArea
            />
            <RadioGroupFormComponent
                label="Есть ли связь с психотравмой"
                name="hasConnectionPsychotrauma"
                items={[
                    {
                        value: true,
                        text: "Да"
                    },
                    {
                        value: false,
                        text: "Нет",
                        textAreaItem: {
                            name: "connectionPsychotraumaNote",
                            style: {marginBottom: 0, width: "300px"},
                            errorMessage: "Пожалуйста, опишите связь с психотравмой",
                            isTextArea: true
                        },
                        isAreaItemOpen: props.openInput
                    }
                ]}
            />
        </>
    );
};

export default AnamnesisCard;
