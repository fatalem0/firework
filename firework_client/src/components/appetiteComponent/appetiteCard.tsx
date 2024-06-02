import React from "react";
import InputFormComponent from "src/formComponents/inputFormComponent/inputFormComponent";
import RadioGroupFormComponent from "src/formComponents/radioGroupFormComponent/radioGroupFormComponent";

const AppetiteCard: React.FC = () => {
    return (
        <>
            <RadioGroupFormComponent
                name="appetiteDisordersActual"
                label="Нарушение аппетита"
                items={[
                    {
                        value: "increased",
                        text: "Повышен"
                    },
                    {
                        value: "decreased",
                        text: "Снижен"
                    }
                ]}
            />
            <InputFormComponent
                name="appetiteRegulationActionNote"
                label="Что пациент делает, чтобы отрегулировать нарушение"
                errorMessage="Пожалуйста, опишите что пациент делает, чтобы отрегулировать нарушение"
                isTextArea
            />
        </>
    );
};

export default AppetiteCard;
