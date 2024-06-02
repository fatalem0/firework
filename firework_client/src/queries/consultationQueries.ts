import {useMutation, useQuery, useQueryClient, UseQueryResult} from "@tanstack/react-query";
import consultationsProvider from "src/providers/consultationsProvider";
import {Consultation, ConsultationForm} from "src/types";
import {sleep} from "src/utils";

const consultationQueries = {
    listConsultations: (): UseQueryResult<Consultation[]> => {
        return useQuery(
            ["listConsultations"],
            () => {
                return consultationsProvider.listConsultations();
            },
            {
                staleTime: Infinity,
                enabled: true,
                retry: 2
            }
        );
    },

    createConsultation: () => {
        const queryClient = useQueryClient();

        return useMutation(
            (params: ConsultationForm) => {
                return consultationsProvider.createConsultation(params);
            },
            {
                onSuccess: async () => {
                    await sleep(1000);
                    queryClient.invalidateQueries(["listConsultations"], {
                        refetchPage: (_page, index, allPages) => index === allPages.length - 1
                    });
                }
            }
        );
    },

    getConsultation: () => {
        return useMutation((consultationId: string) => {
            return consultationsProvider.getConsultation(consultationId);
        });
    }
};

export default consultationQueries;
