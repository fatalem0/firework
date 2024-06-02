import * as React from "react";
import {useNavigate} from "react-router-dom";
import {useMount} from "react-use";
import {Form, Button, Select, FormInstance} from "antd";
import clientQueries from "src/queries/clientQueries";
import {ConsultationForm, Client} from "src/types";
import {sleep} from "src/utils";

interface ModalProps {
    onSubmitFunc: (values: ConsultationForm, form: FormInstance<ConsultationForm>) => Promise<string>;
    isFormSubmitting: boolean;
    clientEmail?: string;
}

const ConsultationFormPopup: React.FC<ModalProps> = (props: ModalProps) => {
    const navigate = useNavigate();
    const [form] = Form.useForm<ConsultationForm>();
    const listClients = clientQueries.listClients();
    const [availClients, changeAvailClients] = React.useState<Client[]>(listClients.data || []);

    useMount(async () => {
        await sleep(100);
        await listClients.refetch();
    });

    React.useEffect(() => {
        const clientData = listClients.data || [];
        changeAvailClients(
            props.clientEmail ? clientData.filter((client) => client.clientEmail === props?.clientEmail) : clientData
        );
    }, [listClients.data]);

    const regConsultation = async (consultationForm: ConsultationForm) => {
        if (props.clientEmail) {
            consultationForm.publicUserClientId = availClients[0].public_user_id ?? "";
        }
        const cardId = await props.onSubmitFunc(consultationForm, form);
        navigate(`/consultationsCardPage/${cardId}`);
    };

    return (
        <Form<ConsultationForm> style={{width: 300}} onFinish={regConsultation} form={form} layout="vertical">
            {availClients.length === 0 && <span>Для создания консультации должен существовать хотя бы 1 клиент</span>}
            {availClients.length > 0 && (
                <>
                    {props.clientEmail ? (
                        <Form.Item label="ФИО Клиента" name="publicUserClientId">
                            <span>{availClients[0].clientFullName}</span>
                        </Form.Item>
                    ) : null}
                    {!props.clientEmail ? (
                        <Form.Item
                            label="ФИО Клиента"
                            name="publicUserClientId"
                            required
                            rules={[{required: true, message: "Пожалуйста, выберите клиента"}]}
                        >
                            <Select
                                options={availClients?.map((client) => ({
                                    value: client.public_user_id,
                                    label: client.clientFullName
                                }))}
                            />
                        </Form.Item>
                    ) : null}
                    <Form.Item
                        label="Тип консультации"
                        name="statusConsultationActual"
                        required
                        rules={[{required: true, message: "Пожалуйста, выберите клиента"}]}
                    >
                        <Select
                            options={[
                                {
                                    value: "first",
                                    label: "Первичная"
                                },
                                {
                                    value: "second",
                                    label: "Вторичная"
                                }
                            ]}
                        />
                    </Form.Item>
                    <Button
                        type="primary"
                        htmlType="submit"
                        disabled={props.isFormSubmitting}
                        loading={props.isFormSubmitting}
                    >
                        Сохранить
                    </Button>
                </>
            )}
        </Form>
    );
};

export default ConsultationFormPopup;
