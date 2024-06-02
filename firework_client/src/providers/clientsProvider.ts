import {apiRequest} from "src/utils/apiRequest";
import {Client, ClientInfo} from "src/types";
import withApiPath from "src/utils/withApiPath";

const clientsProvider = {
    async listClients(): Promise<Client[]> {
        const response = await apiRequest.get(withApiPath("client/"));
        return response.data?.data;
    },

    async getClient(clientId: string): Promise<ClientInfo> {
        const response = await apiRequest.get(withApiPath(`client/${clientId}`));
        return response.data;
    }
};

export default clientsProvider;
