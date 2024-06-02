import React from "react";
import CheckboxGroupFormComponent from "src/formComponents/checkboxGroupFormComponent/checkboxGroupFormComponent";

interface Props {
    isTrainingComplete: boolean;
    isHomeworkSelected: boolean;
    isAdditionalSelected: boolean;
}

const RecommendationsCard: React.FC<Props> = (props: Props) => {
    return (
        <>
            <CheckboxGroupFormComponent
                name="recommendationsCard"
                items={[
                    {
                        value: "recomNeuroStudy",
                        text: "Пройти дополнительное нейропсихологическое исследование"
                    },
                    {
                        value: "recomPathoStudy",
                        text: "Пройти дополнительное патопсихологическое исследование"
                    },
                    {
                        value: "recomContactSpecialist",
                        text: "Обратиться к врачу-психотерапевту/психиатру"
                    },
                    {
                        value: "recomPassTraining",
                        text: "Пройти тренинг",
                        textAreaItem: {
                            name: "recomPassTrainingNote",
                            style: {marginBottom: 0},
                            errorMessage: "Пожалуйста, опишите пункт выше"
                        },
                        isAreaItemOpen: props.isTrainingComplete
                    },
                    {
                        value: "recomHomework",
                        text: "Домашнее задание",
                        textAreaItem: {
                            name: "recomHomeworkNote",
                            style: {marginBottom: 0},
                            errorMessage: "Пожалуйста, опишите пункт выше"
                        },
                        isAreaItemOpen: props.isHomeworkSelected
                    },
                    {
                        value: "recomPsychocorrection",
                        text: "Психокоррекция по запросу"
                    },
                    {
                        value: "recomAdditionalPsychometry",
                        text: "Пройти дополнительную психометрию",
                        textAreaItem: {
                            name: "recomAdditionalPsychometryNote",
                            style: {marginBottom: 0},
                            errorMessage: "Пожалуйста, опишите пункт выше"
                        },
                        isAreaItemOpen: props.isAdditionalSelected
                    }
                ]}
            />
        </>
    );
};

export default RecommendationsCard;
