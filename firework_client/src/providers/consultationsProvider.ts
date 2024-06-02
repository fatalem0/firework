import {apiRequest, apiRequestBlob} from "src/utils/apiRequest";
import {Consultation, ConsultationForm} from "src/types";
import withApiPath from "src/utils/withApiPath";

const consultationsProvider = {
    async listConsultations(): Promise<Consultation[]> {
        const response = await apiRequest.get(withApiPath("card/"));
        return response.data?.data;
    },
    async createConsultation(params: ConsultationForm): Promise<Consultation> {
        const response = await apiRequest.post(withApiPath("card/create"), params);
        return response.data;
    },
    async getConsultation(consultationId: string): Promise<Consultation> {
        const response = await apiRequest.get(withApiPath(`card/${consultationId}`));
        return response.data;
    },
    async updateConsultationInfo(consultationId: string, data: Consultation): Promise<void> {
        await apiRequest.put(withApiPath(`card/save/blueprint/${consultationId}`), data);
    },
    async saveConsultationInfo(consultationId: string, data: Consultation): Promise<void> {
        await apiRequest.put(withApiPath(`card/save/card/${consultationId}`), data);
    },
    async getConsultationFile(consultationId: string): Promise<string> {
        const response = await apiRequestBlob.get(withApiPath(`card/upload/${consultationId}`));
        return response.data;
    }
};

export default consultationsProvider;
