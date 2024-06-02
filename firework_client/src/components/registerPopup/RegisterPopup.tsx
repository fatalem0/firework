import "./registerPopup.scss";

import * as React from "react";
import {Form, Input, Button, Select, FormInstance, Row, Radio} from "antd";
import ClientTypeItem from "src/components/clientTypeItem/clientTypeItem";
import {UserForm, UserInfoClientInfo, RecomendationType, CureType} from "src/types";
import CheckboxGroupFormComponent from "src/formComponents/checkboxGroupFormComponent/checkboxGroupFormComponent";
import CheckboxFormComponent from "src/formComponents/checkboxFormComponent/checkboxFormComponent";

interface ModalProps {
    onSubmitFunc: (values: UserForm, form: FormInstance<UserForm>) => Promise<void>;
    isFormSubmitting: boolean;
}

const RegisterFormPopup: React.FC<ModalProps> = (props: ModalProps) => {
    const [form] = Form.useForm<UserForm>();
    const [isClient, changeIsClient] = React.useState<boolean>(false);
    const [isStaffClient, changeIsStaffClient] = React.useState<boolean>(false);
    // @ts-ignore
    const [clientInfo, changeClientInfo] = React.useState<UserInfoClientInfo>({});
    const [clientRecommendationOtherSelected, changeClientRecommendationOtherSelected] = React.useState<boolean>(false);

    const [hasMailAggrement, changeHasMailAggrement] = React.useState<boolean>(false);
    const [hasTGAggrement, changeHasTGAggrement] = React.useState<boolean>(false);

    const regUser = async (userForm: UserForm) => {
        if (isClient && clientInfo && !isStaffClient) {
            userForm.clients_info = clientInfo;
        }
        userForm.hasMailAggrement = hasMailAggrement;
        userForm.hasTGAggrement = hasTGAggrement;
        await props.onSubmitFunc(userForm, form);
    };

    const changeClientRecommendations = (recommendationType: RecomendationType[]) => {
        changeClientInfo({...clientInfo, recomendationType: recommendationType});
        changeClientRecommendationOtherSelected(recommendationType.includes("Другое"));
    };

    return (
        <Form<UserForm> onFinish={regUser} form={form} layout="vertical">
            <Form.Item
                label="Тип пользователя"
                name="userTypeActual"
                required
                rules={[
                    {
                        required: true,
                        message: "Выберите тип"
                    }
                ]}
            >
                <Select
                    style={{width: 154}}
                    allowClear
                    options={[
                        {value: "employer", label: <ClientTypeItem clientType="employer" />},
                        {value: "client", label: <ClientTypeItem clientType="client" />}
                    ]}
                    onChange={(e) => changeIsClient(e === "client")}
                />
            </Form.Item>
            <Form.Item
                label="Фамилия"
                name="lastName"
                required
                rules={[{required: true, message: "Пожалуйста, введите вашу фамилию"}]}
            >
                <Input />
            </Form.Item>
            <Form.Item
                label="Имя"
                name="firstName"
                required
                rules={[{required: true, message: "Пожалуйста, введите ваше имя"}]}
            >
                <Input />
            </Form.Item>
            <Form.Item label="Отчество" name="middleName">
                <Input />
            </Form.Item>
            <Form.Item
                label="Пол"
                name="sexActual"
                required
                rules={[{required: true, message: "Пожалуйста, выберите ваш пол"}]}
            >
                <Select
                    style={{width: 60}}
                    options={[
                        {value: "male", label: <span>М</span>},
                        {value: "female", label: <span>Ж</span>}
                    ]}
                />
            </Form.Item>
            <Form.Item
                label="E-mail"
                name="email"
                required
                rules={[
                    {required: true, message: "Пожалуйста, введите вашу электронную почту"},
                    {type: "email", message: "Пожалуйста, введите корректную электронную почту"}
                ]}
            >
                <Input />
            </Form.Item>
            <Form.Item
                label="Номер телефона"
                name="phoneNumber"
                required
                rules={[{required: true, message: "Пожалуйста, введите ваш номер телефона"}]}
            >
                <Input />
            </Form.Item>
            {isClient && (
                <Form.Item
                    label="Тип клиента"
                    required
                    rules={[{required: true, message: "Пожалуйста, выберите тип клиента"}]}
                    name="clientType"
                >
                    <Select
                        style={{width: 110}}
                        options={[
                            {value: "patient", label: <span>Пациент</span>},
                            {value: "staff", label: <span>Стафф</span>},
                            {value: "relatives", label: <span>Близкий</span>}
                        ]}
                        onChange={(e) => {
                            changeClientInfo({...clientInfo, clientTypeActual: e});
                            changeIsStaffClient(e == "staff");
                        }}
                    />
                </Form.Item>
            )}
            {isClient && !isStaffClient && (
                <>
                    <Form.Item
                        label="Локализация заболевания"
                        required
                        rules={[{required: true, message: "Пожалуйста, опишите локализацию заболевания"}]}
                        name="diseaseLocation"
                    >
                        <Input onChange={(e) => changeClientInfo({...clientInfo, diseaseLocation: e.target.value})} />
                    </Form.Item>
                    <Form.Item
                        label="Стадия заболевания"
                        required
                        rules={[{required: true, message: "Пожалуйста, выберите стадию заболевания"}]}
                        name="diseaseStage"
                    >
                        <Select
                            style={{width: 250}}
                            options={[
                                {value: "justDiagnosed", label: <span>Недавно диагностировали</span>},
                                {value: "cure", label: <span>Лечение</span>},
                                {value: "therapy", label: <span>Терапия</span>},
                                {value: "remission", label: <span>Ремиссия</span>},
                                {value: "palliativeCare", label: <span>Палативное лечение</span>}
                            ]}
                            onChange={(e) => changeClientInfo({...clientInfo, stageActual: e})}
                        />
                    </Form.Item>
                    <CheckboxGroupFormComponent
                        name="cureType"
                        label="Вид лечения"
                        items={[
                            {
                                text: "Химеотерапия",
                                value: "Химеотерапия"
                            },
                            {
                                text: "Лучевая терапия",
                                value: "Лучевая терапия"
                            },
                            {
                                text: "Операция",
                                value: "Операция"
                            },
                            {
                                text: "Таргетная терапия",
                                value: "Таргетная терапия"
                            },
                            {
                                text: "Гормонотерапия",
                                value: "Гормонотерапия"
                            },
                            {
                                text: "Паллиативное лечение",
                                value: "Паллиативное лечение"
                            }
                        ]}
                        // @ts-ignore
                        onChange={(e: CureType[]) => changeClientInfo({...clientInfo, cureType: e})}
                    />
                    <Form.Item
                        label="Месяцев после лечения"
                        required
                        rules={[{required: true, message: "Пожалуйста, опишите сколько прошло месяцев после лечения"}]}
                        name="diseaseMonths"
                    >
                        <Input
                            onChange={(e) => changeClientInfo({...clientInfo, monthsAfterTreatment: e.target.value})}
                        />
                    </Form.Item>
                    <Form.Item
                        label="Клиент имел опыт работы с психологом"
                        required
                        rules={[
                            {
                                required: true,
                                message: "Пожалуйста, укажите имел ли клиент опыт работы с психологом"
                            }
                        ]}
                        name="clientHasPsychologistExperience"
                    >
                        <Radio.Group>
                            <Radio
                                value={true}
                                className="consultation_card__checkbox"
                                onChange={() => changeClientInfo({...clientInfo, workWithPsychologist: true})}
                            >
                                Да
                            </Radio>
                            <Radio
                                value={false}
                                className="consultation_card__checkbox"
                                onChange={() => changeClientInfo({...clientInfo, workWithPsychologist: false})}
                            >
                                Нет
                            </Radio>
                        </Radio.Group>
                    </Form.Item>
                    <Form.Item
                        label="Какой был опыт работы с психологом?"
                        required
                        rules={[{required: true, message: "Пожалуйста, выберите опыт работы с психологом"}]}
                        name="clientPsychologistExperience"
                    >
                        <Select
                            style={{width: 250}}
                            options={[
                                {value: "positive", label: <span>Позитивный</span>},
                                {value: "neutral", label: <span>Нейтральный</span>},
                                {value: "negative", label: <span>Негативный</span>}
                            ]}
                            onChange={(e) => changeClientInfo({...clientInfo, experienceTypeActual: e})}
                        />
                    </Form.Item>
                    <Form.Item
                        label="Описание опыта работы с психологом"
                        required
                        rules={[{required: true, message: "Пожалуйста, описание опыта работы с психологом"}]}
                        name="clientPsychologistExperienceText"
                    >
                        <Input
                            onChange={(e) => changeClientInfo({...clientInfo, experienceDescription: e.target.value})}
                        />
                    </Form.Item>
                    <Form.Item label="Длительность лечения" name="careTime">
                        <Input onChange={(e) => changeClientInfo({...clientInfo, duration: e.target.value})} />
                    </Form.Item>
                    <CheckboxGroupFormComponent
                        name="recomendationType"
                        label="Что клиент хочет получить от платформы"
                        items={[
                            {
                                text: "Информацию о том, как справляться с эмоциями",
                                value: "Информацию о том, как справляться с эмоциями"
                            },
                            {
                                text: "Упражнения, чтобы самому приводить себя в норму",
                                value: "Упражнения, чтобы самому приводить себя в норму"
                            },
                            {
                                text: "Группу поддержки",
                                value: "Группу поддержки"
                            },
                            {
                                text: "Индивидуальную работу с психологом",
                                value: "Индивидуальную работу с психологом"
                            },
                            {
                                text: "Другое",
                                value: "Другое",
                                textAreaItem: {
                                    name: "recomendationDescription",
                                    errorMessage: "Пожалуйста, опишите что именно хочет получить клиент от платформы",
                                    onChange: (e: string) =>
                                        changeClientInfo({...clientInfo, recomendationDescription: e})
                                },
                                isAreaItemOpen: clientRecommendationOtherSelected
                            }
                        ]}
                        // @ts-ignore
                        onChange={changeClientRecommendations}
                    />
                </>
            )}
            <Form.Item
                label="Пароль"
                name="password"
                required
                rules={[
                    {
                        required: true,
                        message: "Введите ваш пароль"
                    }
                ]}
            >
                <Input.Password />
            </Form.Item>
            <CheckboxFormComponent
                name="hasMailAggrement"
                text="Пользователь согласен получать уведомления по почте"
                onChange={changeHasMailAggrement}
            />
            <CheckboxFormComponent
                name="hasTGAggrement"
                text="Пользователь согласен получать уведомления в telegram"
                onChange={changeHasTGAggrement}
            />
            <Form.Item wrapperCol={{offset: 8, span: 16}}>
                <Row justify="end">
                    <Button
                        disabled={props.isFormSubmitting}
                        loading={props.isFormSubmitting}
                        type="primary"
                        htmlType="submit"
                        className="register-form__btn-text"
                    >
                        Зарегистрировать
                    </Button>
                </Row>
            </Form.Item>
        </Form>
    );
};

export default RegisterFormPopup;
