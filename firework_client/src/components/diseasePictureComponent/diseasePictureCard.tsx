import React from "react";
import InputFormComponent from "src/formComponents/inputFormComponent/inputFormComponent";
import RadioGroupFormComponent from "src/formComponents/radioGroupFormComponent/radioGroupFormComponent";

interface Props {
    openInput: boolean;
}

const DiseasePictureCard: React.FC<Props> = (props: Props) => {
    return (
        <>
            <InputFormComponent
                name="opinionPersonIllnessNote"
                label="Отношение пациента к болезни"
                errorMessage="Пожалуйста, опишите отношение пациента к болезни"
                isTextArea
            />
            <InputFormComponent
                name="opinionOnsetOfDiseaseNote"
                label="С чем пациент связывает начало болезни"
                errorMessage="Пожалуйста, опишите начало болезни"
                isTextArea
            />
            <InputFormComponent
                name="opinionTreatmentNote"
                label="Отношение пациента к лечению"
                errorMessage="Пожалуйста, опишите отношение пациента к лечению"
                isTextArea
            />
            <InputFormComponent
                name="opinionFutureNote"
                label="Что пациент думает о будущем"
                errorMessage="Пожалуйста, опишите что думает пациент о будущем"
                isTextArea
            />
            <InputFormComponent
                name="copingNote"
                label="Копинг"
                errorMessage="Пожалуйста, опишите ведущие копинги"
                isTextArea
                style={{marginBottom: 0}}
            />
            <RadioGroupFormComponent
                name="hasActiveCopingSpecies"
                items={[
                    {
                        text: "Активные копинги",
                        value: true
                    },
                    {
                        text: "Пассивные копинги",
                        value: false
                    }
                ]}
            />
            <RadioGroupFormComponent
                name="hasGoodDevelopedCoping"
                label="Копинги развиты"
                items={[
                    {
                        text: "Хорошо",
                        value: true
                    },
                    {
                        text: "Плохо",
                        value: false
                    }
                ]}
            />
            <RadioGroupFormComponent
                name="hasAlexithymiaPresumed"
                label="Алексетимия"
                items={[
                    {
                        text: "Предполагается",
                        value: true
                    },
                    {
                        text: "Не предполагается",
                        value: false,
                        textAreaItem: {
                            name: "alexithymiaNote",
                            isTextArea: true,
                            style: {marginBottom: 0, width: "300px"}
                        },
                        isAreaItemOpen: props.openInput
                    }
                ]}
            />
        </>
    );
};

export default DiseasePictureCard;
