type ClientExperience = "positive" | "neutral" | "negative";
type ClientStage = "justDiagnosed" | "cure" | "therapy" | "remission" | "palliativeCare" | "staff";
type ClientType = "patient" | "staff" | "relatives";
type ClientTypeName = "client" | "employer" | "close";
type UserSex = "male" | "female";
type CureType =
    | "Химеотерапия"
    | "Лучевая терапия"
    | "Операция"
    | "Таргетная терапия"
    | "Гормонотерапия"
    | "Паллиативное лечение";
type RecomendationType =
    | "Информацию о том, как справляться с эмоциями"
    | "Упражнения, чтобы самому приводить себя в норму"
    | "Группу поддержки"
    | "Индивидуальную работу с психологом"
    | "Другое";
type InputNameType = string | number;

interface UserInfoClientInfo {
    clientTypeActual: ClientType;
    diseaseLocation: string;
    stageActual: ClientStage;
    monthsAfterTreatment: string;
    workWithPsychologist: boolean;
    experienceTypeActual: ClientExperience;
    experienceDescription: string;
    duration?: string;
    cureType: CureType[];
    recomendationType: RecomendationType[];
    recomendationDescription: string;
}

interface UserForm {
    firstName: string;
    lastName: string;
    middleName?: string;
    email: string;
    phoneNumber: string;
    userTypeActual: ClientTypeName;
    sexActual: UserSex;
    password: string;
    clients_info: UserInfoClientInfo;
    hasMailAggrement: boolean;
    hasTGAggrement: boolean;
}

interface User {
    public_id: number;
    firstName: string;
    lastName: string;
    middleName?: string;
    userTypeActual: "Клиент" | "Сотрудник" | "Родственник";
    email: string;
    phoneNumber: string;
    sexActual: "Мужской" | "Женский";
    password: string;
    created: string;
    updated: string;
}

interface Login {
    email: string;
    password: string;
}

interface Client {
    public_id: string;
    public_user_id: string;
    clientFullName: string;
    userTypeActual: ClientTypeName;
    clientEmail: string;
    phoneNumber: string;
    sexActual: UserSex;
    stageActual: string;
    clientTypeActual: string;
    country: string;
    city: string;
    blocked: boolean;
    clientCreated: string;
    updated: string;
    password: string;
    description: string;
    photo: string;
}

interface ClientsCard {
    firstName: string;
    lastName: string;
    middleName: string;
    typeName: string;
    typeDisease: string;
    stageTreatment: string;
    skillPsycholog: string;
    dataReg: string;
    monthAfter: string;
}

interface ClientInfo {
    public_id: string;
    public_user_id: string;
    clientFullName: string;
    clientTypeName: ClientTypeName;
    clientEmail: string;
    diseaseLocation: string;
    stageActual: string;
    psychologist: boolean;
    workWithPsychologist: string;
    clientCreated: string;
    monthsAfterTreatment: string;
    treatments: string[];
    platformWishes: string[];
    clientTypeActual: string;
    cureType: CureType[];
    recomendationType: RecomendationType[];
}

type ConsultationFormType = "first" | "second";
type ConsultationType = "Первичная" | "Вторичная";

interface Consultation {
    alexithymiaNoPresumedNote: string;
    alexithymiaNote: string;
    alexithymiaPresumedNote: string;
    appetiteDisordersActual: "string";
    appetiteRegulationActionNote: string;
    clientEmail: string;
    clientFullName: string;
    cognMemoizationOfInfoNote: string;
    cognPraxisNote: string;
    cognSocIntelligenceNote: string;
    cognUnderstandingOfInfoNote: string;
    conclFirstPlanNote: string;
    conclNotes: string;
    conclOnBackgroundNote: string;
    conclOtherNote: string;
    conclTargetNote: string;
    congSpeechNote: string;
    connectionPsychotraumaNote: string;
    copingHostsNote: string;
    copingNote: string;
    created: string;
    earlyAwakeningNote: string;
    emotionReactOnco: string;
    experiencingEmotion: string;
    featuresConversationsNote: string;
    hasActiveCopingSpecies: boolean;
    hasAcutePsyReact: boolean;
    hasAdaptationDisorder: boolean;
    hasAlexithymiaPresumed: boolean;
    hasAnxiety: boolean;
    hasAnxietyDisorder: boolean;
    hasAppetiteChange: boolean;
    hasConclOther: boolean;
    hasConnectionPsychotrauma: boolean;
    hasContinuousDuration: boolean;
    hasDecliningAttention: boolean;
    hasDepressionClinical: boolean;
    hasEnergyDecline: boolean;
    hasFrequentWaking: boolean;
    hasGoodDevelopedCoping: boolean;
    hasGuilt: boolean;
    hasHopelessness: boolean;
    hasIncreasedDrowsiness: boolean;
    hasInnerPicture: boolean;
    hasLossInterest: boolean;
    hasLowerSelfesteem: boolean;
    hasPersistentLowMood: boolean;
    hasPessimisticThoughts: boolean;
    hasPostDisorder: boolean;
    hasSleepDeprivation: boolean;
    hasSleepDisturbance: boolean;
    hasSuicidalThoughts: boolean;
    isAwakeEarly: boolean;
    isCopeWithSleepDisturbancesActual: "string";
    isHardToFallAsleep: boolean;
    oncologyTime: string;
    opinionFutureNote: string;
    opinionOnsetOfDiseaseNote: string;
    opinionPersonIllnessNote: string;
    opinionTreatmentNote: string;
    publicUserClientId: number;
    public_id: string;
    recomAdditionalPsychometry: boolean;
    recomAdditionalPsychometryNote: string;
    recomContactSpecialist: boolean;
    recomHomework: boolean;
    recomHomeworkNote: string;
    recomNeuroStudy: boolean;
    recomPassTraining: boolean;
    recomPassTrainingNote: string;
    recomPathoStudy: boolean;
    recomPsychocorrection: boolean;
    sleepNote: string;
    specialistFullName: string;
    statusConsultationActual: ConsultationType;
    suicidalThoughtsNote: string;
    symptomAtRelationshipNote: string;
    useAcceptanceTherapy: boolean;
    useArtTherapy: boolean;
    useBodilyOrientedTherapy: boolean;
    useCognBehavTherapy: boolean;
    useDecisionTherapy: boolean;
    useExistentialTherapy: boolean;
    useOtherTherapy: boolean;
    useOtherTherapyNote: string;
    useWorkImagesTherapy: boolean;
    usuallyHelpEmotion: string;
    usuallyNoHelpEmotion: string;
    validationStatusActual: "Черновик" | "Провалидировано";
}

interface ConsultationMainDetailsForm {
    isFirstAppointment?: boolean;
    psychoProblem?: string;
    somaticProblems?: string;
    socialProblems?: string;
}

interface ConsultationForm {
    publicUserClientId: string;
    statusConsultationActual: ConsultationFormType;
}

type TestType = "Radio Button" | "Checkbox" | "Selector" | "Text";

interface TestResult {
    clientFullName: string;
    email: string;
    name: string;
    public_id: string;
    user_id: string;
    test_id: string;
    startDate: string;
    spendTime: string;
    total: number;
}

interface TestResultSettings {
    resultText: string;
    from: number;
    to: number;
    resultDesc: string;
    stressLevelActual: "red" | "yellow" | "green";
}

interface QuestionAnswer {
    value: string;
    score: number;
}

interface TestQuestionSettings {
    question: string;
    questionType: "radio" | "checkbox" | "select" | "text";
    questionAnswers: QuestionAnswer[];
}

interface TestEditForm {
    title: string;
    resultSettings: TestResultSettings[];
    questionSettings: TestQuestionSettings[];
    clientTypeActual: "patient" | "staff" | "relatives";
    interval: number;
    stageActual: ClientStage;
}

interface GetQuestionParams {
    email: string;
    test_id: string;
}

interface PostQuestionAnswerParams {
    user_id: string;
    test_id: string;
    test_question_id: string;
    answerNumber: number[];
}

interface TestAnswer {
    answerNumber: number;
    answerText: string;
}

interface TestQuestion {
    public_id: string;
    user_id: string;
    test_id: string;
    questionNumber: number;
    numberOfQuestions: number;
    test_question_id: string;
    title: string;
    name: string;
    questionTypeActual: TestType;
    test_answers: TestAnswer[];
    result_id?: string;
}

interface TestQuestionsResult {
    description: string;
    recommendation: string;
}

interface Test {
    title: string;
    questionCount: number;
    question: string;
    type: TestType;
    options: string[];
}

interface TestInfo {
    public_id: string;
    name: string;
    minScore: number;
    maxScore: number;
    numberOfQuestions: number;
}

interface ErrorResponseItem {
    field: string;
    message: string;
}

interface ErrorResponse {
    errors: ErrorResponseItem[];
    message: string;
    status: string;
}

interface TextInputFormItem {
    name: string | InputNameType[];
    label?: string;
    errorMessage?: string;
    style?: React.CSSProperties;
    isTextArea?: boolean;
    onChange?: (value: string) => void;
    disabled?: boolean;
}

interface RadioGroupItem {
    value: string | boolean;
    text: string;
    disabled?: boolean;
    textAreaItem?: TextInputFormItem;
    isAreaItemOpen?: boolean;
}

export type {
    Client,
    ClientInfo,
    ClientTypeName,
    ClientsCard,
    Consultation,
    ConsultationForm,
    ConsultationMainDetailsForm,
    ConsultationType,
    CureType,
    ErrorResponse,
    GetQuestionParams,
    Login,
    PostQuestionAnswerParams,
    RadioGroupItem,
    RecomendationType,
    Test,
    TestAnswer,
    TestEditForm,
    TestInfo,
    TestQuestion,
    TestQuestionsResult,
    TestResult,
    TestType,
    TextInputFormItem,
    User,
    UserForm,
    UserInfoClientInfo
};
