// import React from "react";
import ReactDOM from "react-dom/client";
import {BrowserRouter} from "react-router-dom";
import {QueryClient, QueryClientProvider} from "@tanstack/react-query";
import App from "./App";
import "src/assets/fonts/fonts.scss";

const queryClient = new QueryClient();

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
    // TODO: Return when https://github.com/ant-design/pro-components/issues/6264 will be fixed
    // <React.StrictMode>
    <BrowserRouter>
        <QueryClientProvider client={queryClient}>
            <App />
        </QueryClientProvider>
    </BrowserRouter>
    // </React.StrictMode>
);
