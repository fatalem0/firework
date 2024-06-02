import {useMutation, useQuery, UseQueryResult} from "@tanstack/react-query";
import testsProvider from "src/providers/testsProvider";
import {TestResult, GetQuestionParams, PostQuestionAnswerParams, TestInfo} from "src/types";

const testQueries = {
    listTests: (): UseQueryResult<TestResult[]> => {
        return useQuery(
            ["listTests"],
            () => {
                return testsProvider.listTests();
            },
            {
                staleTime: Infinity,
                enabled: true,
                retry: 2
            }
        );
    },
    listAvailTests: (): UseQueryResult<TestInfo[]> => {
        return useQuery(
            ["availListTests"],
            () => {
                return testsProvider.getAvailTests();
            },
            {
                staleTime: Infinity,
                enabled: true,
                retry: 2
            }
        );
    },
    getQuestion: () => {
        return useMutation((pararms: GetQuestionParams) => {
            return testsProvider.getTestQuestion(pararms);
        });
    },
    postAnswer: () => {
        return useMutation((pararms: PostQuestionAnswerParams) => {
            return testsProvider.submitTestQuestion(pararms);
        });
    },
    getQuestionsResult: () => {
        return useMutation((test_id: string) => {
            return testsProvider.getResult(test_id);
        });
    },
    getAvailTests: () => {
        return useMutation(() => {
            return testsProvider.getAvailTests();
        });
    }
};

export default testQueries;
