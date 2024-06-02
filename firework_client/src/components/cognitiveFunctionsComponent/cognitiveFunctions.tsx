import React from "react";
import InputFormComponent from "src/formComponents/inputFormComponent/inputFormComponent";

const CognitiveFunctions: React.FC = () => {
    return (
        <>
            <InputFormComponent
                name="cognUnderstandingOfInfoNote"
                label="Понимание информации"
                errorMessage="Пожалуйста, опишите понимание информации"
                isTextArea
            />
            <InputFormComponent
                name="cognMemoizationOfInfoNote"
                label="Запоминание информации"
                errorMessage="Пожалуйста, опишите запоминание информации"
                isTextArea
            />
            <InputFormComponent name="cognSpeechNote" label="Речь" errorMessage="Пожалуйста, опишите речь" isTextArea />
            <InputFormComponent
                name="cognPraxisNote"
                label="Праксис"
                errorMessage="Пожалуйста, опишите праксис"
                isTextArea
            />
            <InputFormComponent
                name="cognSocIntelligenceNote"
                label="Социальный интеллект"
                errorMessage="Пожалуйста, опишите социальный интеллект"
                isTextArea
            />
        </>
    );
};

export default CognitiveFunctions;
