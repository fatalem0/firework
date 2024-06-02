import {apiRequest, apiRequestBlob} from "src/utils/apiRequest";
import {Login} from "src/types";
import {getCookie, setCookie} from "typescript-cookie";
import withApiPath from "src/utils/withApiPath";

const authProvider = {
    async getCookie(params?: Login): Promise<void> {
        const token = getCookie("token");
        if (!token) {
            const response = await apiRequest.post(withApiPath("auth/login"), params ?? {email: "", password: ""});
            const millisecondInMinute = 60000;
            const expirationTimeInMinutes = 24 * 60;
            const tokenExpiresIn = expirationTimeInMinutes * millisecondInMinute - 5 * millisecondInMinute;

            apiRequest.defaults.headers.common = {Authorization: `${response.data.Authorization}`};
            apiRequestBlob.defaults.headers.common = {Authorization: `${response.data.Authorization}`};

            setCookie("token", response.data.Authorization, {
                expires: new Date(new Date().getTime() + tokenExpiresIn),
                sameSite: "Lax"
            });
        } else {
            apiRequest.defaults.headers.common = {Authorization: `${token}`};
            apiRequestBlob.defaults.headers.common = {Authorization: `${token}`};
        }

        return;
    },
    isUserCanBeAuthorized(): boolean {
        return Boolean(getCookie("token"));
    }
};

export default authProvider;
