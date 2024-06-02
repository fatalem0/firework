import "./loginPage.scss";

import * as React from "react";
import {useNavigate} from "react-router-dom";
import {Modal, Button, Form, Input, Typography} from "antd";
import {useMount} from "react-use";
import authProvider from "src/providers/authProvider";
import {Login} from "src/types";
import {removeCookie} from "typescript-cookie";

const LoginPage: React.FC = () => {
    const navigate = useNavigate();

    const [form] = Form.useForm<Login>();

    useMount(() => {
        removeCookie("token");
    });

    const loginMe = async (params: Login) => {
        try {
            await authProvider.getCookie(params);
            navigate("/users");
        } catch (e) {
            console.error("error occurred: ", e);
        }
    };

    return (
        <Modal
            className="loginPage__modal"
            wrapClassName="loginPage__modal-wrap"
            title={
                <>
                    <Form<Login> className="loginPage__form" onFinish={loginMe} form={form} layout="vertical">
                        <Typography.Title level={2} className="loginPage__title">
                            ВХОД
                        </Typography.Title>
                        <Form.Item
                            label="Email"
                            name="email"
                            required
                            rules={[{required: true, message: "Пожалуйста, введите вашу почту"}]}
                        >
                            <Input />
                        </Form.Item>
                        <Form.Item
                            label="Пароль"
                            name="password"
                            required
                            rules={[{required: true, message: "Пожалуйста, введите ваш пароль"}]}
                        >
                            <Input.Password />
                        </Form.Item>
                        <Button className="loginPage__button" type="primary" htmlType="submit">
                            Вход
                        </Button>
                    </Form>
                </>
            }
            style={{maxWidth: "350px"}}
            centered
            open
            closable={false}
            footer={null}
        />
    );
};

export default LoginPage;
