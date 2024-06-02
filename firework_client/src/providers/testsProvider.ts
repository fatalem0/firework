import {apiRequest} from "src/utils/apiRequest";
import {
    TestResult,
    TestQuestion,
    TestQuestionsResult,
    GetQuestionParams,
    PostQuestionAnswerParams,
    TestInfo,
    TestEditForm
} from "src/types";
import withApiPath from "src/utils/withApiPath";

const testsProvider = {
    async listTests(): Promise<TestResult[]> {
        const response = await apiRequest.get(withApiPath("test/result"));
        return response.data?.data;
    },
    async getTestQuestion(pararms: GetQuestionParams): Promise<TestQuestion> {
        const response = await apiRequest.post(withApiPath("test/open"), pararms);
        return response.data?.data;
    },
    async submitTestQuestion(pararms: PostQuestionAnswerParams): Promise<TestQuestion> {
        const response = await apiRequest.post(withApiPath("test/answer"), pararms);
        return response.data?.data;
    },
    async getResult(public_id: string): Promise<TestQuestionsResult> {
        const response = await apiRequest.post(withApiPath(`test/end/${public_id}`));
        return response.data?.data;
    },
    async getAvailTests(): Promise<TestInfo[]> {
        const response = await apiRequest.get(withApiPath("test/list"));
        return response.data?.data;
    },
    async createTest(data: TestEditForm): Promise<TestInfo[]> {
        const response = await apiRequest.post(withApiPath("test/createtest"), data);
        return response.data;
    },
    async getTest(testId: string): Promise<TestEditForm> {
        const response = await apiRequest.get(withApiPath(`test/info/${testId}`));
        return response.data;
    }
};

export default testsProvider;
