import axios, {AxiosError} from "axios";
import {notification} from "antd";
import {ErrorResponse} from "src/types";

const apiRequest = axios.create({
    baseURL: import.meta.env.VITE_BACKEND_HOST,
    headers: {
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
        Accept: "application/json"
    }
});

const apiRequestBlob = axios.create({
    baseURL: import.meta.env.VITE_BACKEND_HOST,
    headers: {
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
        Accept: "application/json"
    },
    responseType: "blob"
});

const requestsCallback = async (error: AxiosError) => {
    if (!error.response) {
        return;
    }

    if (error.response.status === 400) {
        const response: ErrorResponse = error.response.data as ErrorResponse;

        notification.error({
            message: "Ошибка валидации",
            description: response.message,
            placement: "bottomRight"
        });
    } else if (error.response.status !== 403 && error.response.status !== 404) {
        const response: ErrorResponse = error.response.data as ErrorResponse;

        if (response.message && response.message != "Отсутствует фактор аутентификации.") {
            notification.error({
                message: "Что-то пошло не так",
                description: response.message,
                placement: "bottomRight"
            });
        }
    }

    return Promise.reject(error);
};

apiRequest.interceptors.response.use(undefined, requestsCallback);
apiRequestBlob.interceptors.response.use(undefined, requestsCallback);

export {apiRequest, apiRequestBlob};
