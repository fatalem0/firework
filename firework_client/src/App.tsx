import "./app.scss";

import * as React from "react";
import {ProLayout} from "@ant-design/pro-components";
import {Routes, Route, useLocation, useNavigate} from "react-router-dom";
import {useMount} from "react-use";
import ClientCardPage from "src/pages/clientCardPage/clientCardPage";
import ClientsPage from "src/pages/clientsPage/clientsPage";
import ConsultationCardPage from "src/pages/consultationsCardPage/consultationsCardPage";
import ConsultationsPage from "src/pages/consultationJournalPage/consultationJournalPage";
import HomePage from "src/pages/homePage/homePage";
import LoginPage from "src/pages/loginPage/loginPage";
import TestPage from "src/pages/testPage/testPage";
import TestsEditing from "src/pages/testsEditing/testsEditing";
import TestsPage from "src/pages/testsPage/testsPage";
import TestsViewPage from "src/pages/testsViewPage/testsViewPage";
import UsersPage from "src/pages/usersPage/usersPage";
import authProvider from "src/providers/authProvider";
import logoImg from "/fav/logo.png";

const defaultMenus = [
    {
        path: "/home",
        name: "Домашняя страница"
    },
    {
        path: "/clients",
        name: "Клиенты"
    },
    {
        path: "/consultations",
        name: "Журнал консультаций"
    },
    {
        path: "/testView",
        name: "Каталог тестов"
    },
    {
        path: "/tests",
        name: "Пройденые тесты"
    },
    {
        path: "/users",
        name: "Пользователи"
    },
    {
        path: "/test",
        name: "Пройти тест"
    }
];

const App: React.FC = () => {
    const location = useLocation();
    const navigate = useNavigate();

    useMount(async () => {
        if (!defaultMenus.find((elem) => location.pathname.startsWith(elem.path)) && location.pathname != "/login") {
            navigate("/home");
        }
        if (authProvider.isUserCanBeAuthorized()) {
            try {
                await authProvider.getCookie();
            } catch (e) {
                if (location.pathname !== "/login") {
                    navigate("/login");
                }
            }
        } else if (location.pathname !== "/login") {
            navigate("/login");
        }
    });

    return (
        <Routes>
            <Route path="login" element={<LoginPage />} />
            <Route path="test" element={<TestPage />} />
            <Route
                path="*"
                element={
                    <>
                        <ProLayout
                            fixSiderbar
                            location={{
                                pathname: location.pathname
                            }}
                            route={{
                                routes: defaultMenus
                            }}
                            logo={<img src={logoImg} className="app__logo" alt="logo" />}
                            menuItemRender={(item, dom) => (
                                <div
                                    onClick={() => {
                                        navigate(item.path || "/");
                                    }}
                                >
                                    {dom}
                                </div>
                            )}
                            title={false}
                            collapsed={false}
                            collapsedButtonRender={false}
                            layout="mix"
                        >
                            <Routes>
                                <Route path="users" element={<UsersPage />} />
                                <Route path="clients" element={<ClientsPage />} />
                                <Route path="clientsCard/:id" element={<ClientCardPage />} />
                                <Route path="consultationsCardPage/:id" element={<ConsultationCardPage />} />
                                <Route path="consultations" element={<ConsultationsPage />} />
                                <Route path="tests" element={<TestsPage />} />
                                <Route path="testView" element={<TestsViewPage />} />
                                <Route path="testsEditing" element={<TestsEditing />} />
                                <Route path="testsEditing/:id" element={<TestsEditing />} />
                                <Route path="home" element={<HomePage />} />
                                <Route path="*" element={<HomePage />} />
                            </Routes>
                        </ProLayout>
                    </>
                }
            />
        </Routes>
    );
};

export default App;
