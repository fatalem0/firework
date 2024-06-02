import config from "src/config.json";

const withApiPath = (str: string): string => {
    return config.dashboardApi + str;
};

export default withApiPath;
