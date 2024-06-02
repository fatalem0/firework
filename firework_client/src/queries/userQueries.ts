import {useMutation, useQuery, useQueryClient, UseQueryResult} from "@tanstack/react-query";
import usersProvider from "src/providers/usersProvider";
import {User, UserForm} from "src/types";
import {sleep} from "src/utils";

const userQueries = {
    listUsers: (): UseQueryResult<User[]> => {
        return useQuery(
            ["listUsers"],
            () => {
                return usersProvider.listUsers();
            },
            {
                staleTime: Infinity,
                enabled: true,
                retry: 2
            }
        );
    },

    createUser: () => {
        const queryClient = useQueryClient();

        return useMutation(
            (params: UserForm) => {
                return usersProvider.createUser(params);
            },
            {
                onSuccess: async () => {
                    await sleep(1000);
                    queryClient.invalidateQueries(["listUsers"], {
                        refetchPage: (_page, index, allPages) => index === allPages.length - 1
                    });
                }
            }
        );
    }
};

export default userQueries;
