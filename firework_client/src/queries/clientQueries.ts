import {useMutation, useQuery, UseQueryResult} from "@tanstack/react-query";
import clientsProvider from "src/providers/clientsProvider";
import {Client} from "src/types";

const clientQueries = {
    listClients: (): UseQueryResult<Client[]> => {
        return useQuery(
            ["listClients"],
            () => {
                return clientsProvider.listClients();
            },
            {
                staleTime: Infinity,
                enabled: true,
                retry: 2
            }
        );
    },
    listClientsWithoutRetry: () => {
        return useMutation(() => {
            return clientsProvider.listClients();
        });
    },

    getClient: () => {
        return useMutation((clientId: string) => {
            return clientsProvider.getClient(clientId);
        });
    }
};

export default clientQueries;
