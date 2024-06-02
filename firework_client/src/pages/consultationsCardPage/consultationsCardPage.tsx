// TOOD (thefirefox15): It's bad, but it is...
// @ts-nocheck
import "./consultationsCardPage.scss";

import * as React from "react";
import {useLocation, useNavigate} from "react-router-dom";
import {Collapse, Typography, Form, Button, Descriptions, notification} from "antd";
import {CaretRightOutlined, CheckOutlined} from "@ant-design/icons";
import AnamnesisCard from "src/components/anamnezComponent/anamnezCard";
import AppetiteCard from "src/components/appetiteComponent/appetiteCard";
import CognitiveFunctions from "src/components/cognitiveFunctionsComponent/cognitiveFunctions";
import ConclusionCard from "src/components/conclusionComponent/ConclusionCard";
import DiseasePictureCard from "src/components/diseasePictureComponent/diseasePictureCard";
import InputFormComponent from "src/formComponents/inputFormComponent/inputFormComponent";
import ObjectiveCard from "src/components/objectiveComponent/objectiveCard";
import PageLoadingWithParentComponent from "src/components/pageLoadingWithParentComponent/pageLoadingWithParentComponent";
import RadioGroupFormComponent from "src/formComponents/radioGroupFormComponent/radioGroupFormComponent";
import RecommendationsCard from "src/components/recommendationsComponent/recommendationsCard";
import SleepDisturbanceCard from "src/components/sleepDisturbanceComponent/sleepDisturbanceCard";
import TherapyUsed from "src/components/therapyUsedComponent/therapyUsed";
import TimeLabel from "src/components/timeLabel/timeLabel";
import consultationsProvider from "src/providers/consultationsProvider";
import {Consultation} from "src/types";
import {sleep, downloadFile} from "src/utils";

const activeKeysOnFirstAppointment = ["1", "2", "3", "4", "5", "6", "7", "8", "9"];
const activeKeysDefaultOpen = ["1", "2"];
const activeKeysOnSecondAppointment = ["1", "6", "7", "8", "9"];
const collapseRotateActiveAngle = 90;
const collapseRotateDisableAngle = 0;
const consultationUpdateInterval = 10000; // every 10 seconds
const formCheckboxes = [
    "hasAcutePsyReact",
    "hasAdaptationDisorder",
    "hasAnxietyDisorder",
    "hasAppetiteChange",
    "hasConclOther",
    "hasDecliningAttention",
    "hasDepressionClinical",
    "hasEnergyDecline",
    "hasFrequentWaking",
    "hasGuilt",
    "hasHopelessness",
    "hasIncreasedDrowsiness",
    "hasLossInterest",
    "hasLowerSelfesteem",
    "hasPersistentLowMood",
    "hasPessimisticThoughts",
    "hasPostDisorder",
    "hasSleepDeprivation",
    "hasSleepDisturbance",
    "hasSuicidalThoughts",
    "isAwakeEarly",
    "isHardToFallAsleep",
    "recomAdditionalPsychometry",
    "recomContactSpecialist",
    "recomHomework",
    "recomNeuroStudy",
    "recomPassTraining",
    "recomPathoStudy",
    "recomPsychocorrection",
    "useAcceptanceTherapy",
    "useArtTherapy",
    "useBodilyOrientedTherapy",
    "useCognBehavTherapy",
    "useDecisionTherapy",
    "useExistentialTherapy",
    "useOtherTherapy",
    "useWorkImagesTherapy"
];
const groupOneFields = ["hasPersistentLowMood", "hasLossInterest", "hasEnergyDecline"];
const groupTwoFields = [
    "hasDecliningAttention",
    "hasGuilt",
    "hasLowerSelfesteem",
    "hasAppetiteChange",
    "hasSleepDisturbance",
    "hasPessimisticThoughts",
    "hasHopelessness",
    "hasSuicidalThoughts"
];
const sleepDisturbance = [
    "isHardToFallAsleep",
    "hasFrequentWaking",
    "isAwakeEarly",
    "hasSleepDeprivation",
    "hasIncreasedDrowsiness"
];
const therapyUsed = [
    "useCognBehavTherapy",
    "useExistentialTherapy",
    "useWorkImagesTherapy",
    "useDecisionTherapy",
    "useAcceptanceTherapy",
    "useArtTherapy",
    "useBodilyOrientedTherapy",
    "useOtherTherapy"
];
const conclusionCard = [
    "hasAdaptationDisorder",
    "hasAnxietyDisorder",
    "hasDepressionClinical",
    "hasAcutePsyReact",
    "hasPostDisorder",
    "hasConclOther"
];
const recommendationsCard = [
    "recomNeuroStudy",
    "recomPathoStudy",
    "recomContactSpecialist",
    "recomPassTraining",
    "recomHomework",
    "recomPsychocorrection",
    "recomAdditionalPsychometry"
];

interface FieldData {
    name: string | number | (string | number)[];
    value?: any;
    touched?: boolean;
    validating?: boolean;
    errors?: string[];
}

const ConsultationCardPage = () => {
    const location = useLocation();
    const navigate = useNavigate();
    const id = React.useRef(location.pathname.match(/\/([^/]+)$/)?.[1]).current;
    const [form] = Form.useForm<Consultation>();
    const [api, contextHolder] = notification.useNotification();
    const [activeKeys, setActiveKeys] = React.useState<string[]>(activeKeysOnFirstAppointment);
    const [consultationCard, changeConsultationCard] = React.useState<Consultation>();
    const [formFields, changeFormFields] = React.useState<FieldData[]>();
    const [isFormSubmitting, setIsFormSubmitting] = React.useState<boolean>(false);
    const [isLoading, changeIsLoading] = React.useState<boolean>(true);
    // input fields
    const [hasConnectionPsychotrauma, changeHasConnectionPsychotrauma] = React.useState<boolean>(false);
    const [hasAlexithymiaPresumed, changeHasAlexithymiaPresumed] = React.useState<boolean>(false);
    const [isAwakeEarly, changeIsAwakeEarly] = React.useState<boolean>(false);
    const [useOtherTherapy, changeUseOtherTherapy] = React.useState<boolean>(false);
    const [hasConclOther, changeHasConclOther] = React.useState<boolean>(false);
    const [isTrainingComplete, setIsTrainingComplete] = React.useState<boolean>();
    const [isHomeworkSelected, setIsHomeworkSelected] = React.useState<boolean>();
    const [isAdditionalSelected, setIsAdditionalSelected] = React.useState<boolean>();

    const openNotification = (title: string, description: string) => {
        api.info({
            message: title,
            description,
            placement: "bottomRight",
            icon: <CheckOutlined style={{color: "#b0fc38"}} />
        });
    };

    const updateInputsFields = (fields: Consultation) => {
        if (!fields) {
            return;
        }
        changeHasConnectionPsychotrauma(fields["hasConnectionPsychotrauma"] ?? false);
        changeHasAlexithymiaPresumed(fields["hasAlexithymiaPresumed"] ?? false);
        changeIsAwakeEarly(fields["isAwakeEarly"] ?? false);
        changeUseOtherTherapy(fields["useOtherTherapy"] ?? false);
        changeHasConclOther(fields["hasConclOther"] ?? false);
        setIsTrainingComplete(fields["recomPassTraining"] ?? false);
        setIsHomeworkSelected(fields["recomHomework"] ?? false);
        setIsAdditionalSelected(fields["recomAdditionalPsychometry"] ?? false);
    };

    const parseConsultationFields = (fields: Consultation) => {
        const createAllowedFields = (field: string, allowedFields: string[]) => {
            let parsedFields = {};
            for (const allowedField of allowedFields) {
                parsedFields[allowedField] = fields[allowedField] ?? false;
            }
            fields[field] = [];
            for (const [fieldName, value] of Object.entries(parsedFields)) {
                if (value) {
                    fields[field].push(fieldName);
                }
            }
        };

        createAllowedFields("conclusionCard", conclusionCard);
        createAllowedFields("groupOneFields", groupOneFields);
        createAllowedFields("groupTwoFields", groupTwoFields);
        createAllowedFields("recommendationsCard", recommendationsCard);
        createAllowedFields("sleepDisturbance", sleepDisturbance);
        createAllowedFields("therapyUsed", therapyUsed);
    };

    const updateConsultationFields = (fields: Consultation) => {
        const createAllowedFields = (field: string, allowedFields: string[]) => {
            if (!fields) {
                return;
            }
            const parsedFields = allowedFields.reduce((obj, key) => ({...obj, [key]: false}), {});
            for (const fieldName of fields[field]) {
                parsedFields[fieldName] = true;
            }
            for (const [field, value] of Object.entries(parsedFields)) {
                fields[field] = value;
            }
        };

        createAllowedFields("conclusionCard", conclusionCard);
        createAllowedFields("groupOneFields", groupOneFields);
        createAllowedFields("groupTwoFields", groupTwoFields);
        createAllowedFields("recommendationsCard", recommendationsCard);
        createAllowedFields("sleepDisturbance", sleepDisturbance);
        createAllowedFields("therapyUsed", therapyUsed);
    };

    React.useEffect(() => {
        if (!id) {
            navigate("/home");
            return;
        }

        const getConsultation = async (id: string) => {
            try {
                changeIsLoading(true);
                await sleep(100);
                const consultation = await consultationsProvider.getConsultation(id);
                parseConsultationFields(consultation);
                form.setFieldsValue(consultation);
                changeConsultationCard(consultation);
                updateInputsFields(consultation);
                await sleep(100);
                changeIsLoading(false);
            } catch {
                navigate("/home");
            }
        };

        getConsultation(id);
    }, [id]);

    React.useEffect(() => {
        if (consultationCard?.statusConsultationActual === "Вторичная") {
            setActiveKeys(activeKeysOnSecondAppointment);
        } else {
            setActiveKeys(activeKeysOnFirstAppointment);
        }
    }, [consultationCard?.statusConsultationActual]);

    const handleCollapseChange = (keys: string | string[]) => {
        if (typeof keys === "string" || keys instanceof String) {
            return;
        }

        setActiveKeys(keys);
    };

    React.useEffect(() => {
        let result = consultationCard;
        formFields?.forEach((item) => {
            result[item.name[0]] = item.value;
        });
        updateConsultationFields(result);
        changeConsultationCard(result);
        updateInputsFields(result);
    }, [formFields]);

    const onFormSubmit = async (values: Consultation) => {
        if (!id || !consultationCard) {
            return;
        }
        try {
            setIsFormSubmitting(true);
            updateConsultationFields(values);
            await consultationsProvider.saveConsultationInfo(id, values);
            setIsFormSubmitting(false);
            openNotification("Консультация завершена", "");
            const consult: Consultation = consultationCard;
            consult.validationStatusActual = "Провалидировано";
            changeConsultationCard(consult);
        } catch (e) {
            console.error("Ocurred error: ", e);
        } finally {
            setIsFormSubmitting(false);
        }
    };

    const updateConsultation = async (needToRestart = true) => {
        const card = consultationCard;

        if (!card || !id) {
            return;
        }

        if (card.validationStatusActual === "Черновик") {
            formCheckboxes.forEach((item) => {
                if (card[item] === null) {
                    card[item] = false;
                }
            });
            try {
                updateConsultationFields(card);
                await consultationsProvider.updateConsultationInfo(id, card);
            } finally {
                if (needToRestart) {
                    setTimeout(async () => await updateConsultation(), consultationUpdateInterval);
                }
            }
        }
    };

    React.useEffect(() => {
        if (!consultationCard) {
            return;
        }
        if (consultationCard.validationStatusActual === "Черновик") {
            setTimeout(async () => await updateConsultation(), consultationUpdateInterval);
        }
    }, [consultationCard?.statusConsultationActual]);

    const saveConsultation = () => {
        try {
            updateConsultation(false);
            openNotification("Консультация сохранена", "");
        } catch (e) {
            console.error("Ocurred error: ", e);
        }
    };

    const downloadConsultation = async () => {
        const fileContent = await consultationsProvider.getConsultationFile(consultationCard?.public_id);
        const fileName = `консультация_${consultationCard?.clientFullName.replace(" ", "_")}.docx`;
        downloadFile(fileContent, fileName);
    };

    const renderPage = () => {
        return isLoading ? null : (
            <>
                {contextHolder}
                <Typography.Title
                    className="consultation_card__question-text"
                    level={4}
                    style={{
                        color: "#464F60",
                        fontSize: "17px",
                        fontWeight: "500",
                        lineHeight: "20px",
                        letterSpacing: "0.02em"
                    }}
                >
                    <Descriptions contentStyle={{fontSize: "16px"}}>
                        <Descriptions.Item
                            span={3}
                            label={<span className="client_card__descriptions_title">Дата приема</span>}
                        >
                            <TimeLabel time={consultationCard.created} />
                        </Descriptions.Item>
                        <Descriptions.Item
                            span={3}
                            label={<span className="client_card__descriptions_title">Имя пациента</span>}
                        >
                            {consultationCard.clientFullName}
                        </Descriptions.Item>
                        <Descriptions.Item
                            span={3}
                            label={<span className="client_card__descriptions_title">Имя специалиста</span>}
                        >
                            {consultationCard.specialistFullName}
                        </Descriptions.Item>
                    </Descriptions>
                </Typography.Title>
                {consultationCard.validationStatusActual === "Провалидировано" && (
                    <Button
                        className="consultation_card__download_btn"
                        onClick={async () => await downloadConsultation()}
                    >
                        Скачать консультацию
                    </Button>
                )}
                <Form<Consultation>
                    form={form}
                    layout="vertical"
                    onFinish={(values) => onFormSubmit(values)}
                    onFieldsChange={(_, allFields) => {
                        changeFormFields(allFields);
                    }}
                    disabled={consultationCard.validationStatusActual !== "Черновик"}
                >
                    <RadioGroupFormComponent
                        name="statusConsultationActual"
                        label="Тип консультации:"
                        items={[
                            {
                                text: "Первичный",
                                value: "Первичная",
                                disabled: true
                            },
                            {
                                text: "Вторичный",
                                value: "Вторичная",
                                disabled: true
                            }
                        ]}
                    />
                    <Typography.Title level={2}>Жалобы пациента:</Typography.Title>
                    <InputFormComponent
                        name="comPsychoEmotionNote"
                        label="Психо-эмоциональные жалобы"
                        errorMessage="Пожалуйста, введите жалобы клиента"
                        isTextArea
                    />
                    <InputFormComponent
                        name="comSocial"
                        label="Социальные жалобы"
                        errorMessage="Пожалуйста, введите жалобы клиента"
                        isTextArea
                    />
                    <InputFormComponent
                        name="comSomatic"
                        label="Соматические жалобы"
                        errorMessage="Пожалуйста, введите жалобы клиента"
                        isTextArea
                    />
                    <Collapse
                        bordered={false}
                        style={{background: "#F5F5F5"}}
                        defaultActiveKey={activeKeysDefaultOpen}
                        onChange={handleCollapseChange}
                        expandIcon={({isActive}) => (
                            <CaretRightOutlined
                                rotate={isActive ? collapseRotateActiveAngle : collapseRotateDisableAngle}
                            />
                        )}
                        activeKey={activeKeys}
                    >
                        <Collapse.Panel header="Анамнез заболевания" key="1">
                            <AnamnesisCard openInput={hasConnectionPsychotrauma} />
                        </Collapse.Panel>
                        <Collapse.Panel header="Объективный статус" key="2">
                            <ObjectiveCard />
                        </Collapse.Panel>
                        <Collapse.Panel header="Внутренняя картина болезни" key="3">
                            <DiseasePictureCard openInput={hasAlexithymiaPresumed} />
                        </Collapse.Panel>
                        <Collapse.Panel header="Нарушение сна" key="4">
                            <SleepDisturbanceCard openInput={isAwakeEarly} />
                        </Collapse.Panel>
                        <Collapse.Panel header="Аппетит" key="5">
                            <AppetiteCard />
                        </Collapse.Panel>
                        <Collapse.Panel header="Когнитивные функции" key="6">
                            <CognitiveFunctions />
                        </Collapse.Panel>
                        <Collapse.Panel header="В беседе использовалась терапия" key="7">
                            <TherapyUsed openInput={useOtherTherapy} />
                        </Collapse.Panel>
                        <Collapse.Panel header="Заключение" key="8">
                            <ConclusionCard openInput={hasConclOther} />
                        </Collapse.Panel>
                        <Collapse.Panel header="Рекомендации" key="9">
                            <RecommendationsCard
                                isAdditionalSelected={isAdditionalSelected}
                                isHomeworkSelected={isHomeworkSelected}
                                isTrainingComplete={isTrainingComplete}
                            />
                        </Collapse.Panel>
                    </Collapse>
                    <Button
                        disabled={consultationCard.validationStatusActual === "Провалидировано" || isFormSubmitting}
                        loading={isFormSubmitting}
                        onClick={() => saveConsultation()}
                        style={{marginRight: 10}}
                    >
                        Сохранить
                    </Button>
                    <Button
                        type="primary"
                        htmlType="submit"
                        disabled={consultationCard.validationStatusActual === "Провалидировано" || isFormSubmitting}
                        loading={isFormSubmitting}
                    >
                        Завершить
                    </Button>
                </Form>
            </>
        );
    };

    return <PageLoadingWithParentComponent isLoading={isLoading} body={renderPage()} />;
};

export default ConsultationCardPage;
