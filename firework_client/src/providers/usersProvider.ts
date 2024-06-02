import {apiRequest} from "src/utils/apiRequest";
import {User, UserForm} from "src/types";
import withApiPath from "src/utils/withApiPath";

const usersProvider = {
    async getUser(userId: string): Promise<User> {
        const response = await apiRequest.get(withApiPath(`user/${userId}`));
        return response.data;
    },

    async createUser(user: UserForm): Promise<User> {
        const response = await apiRequest.post(withApiPath("user/"), user);
        return response.data;
    },

    async listUsers(): Promise<User[]> {
        const response = await apiRequest.get(withApiPath("user/"));
        return response.data?.data;
    }
};

export default usersProvider;
