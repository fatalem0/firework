function sleep(ms: number): Promise<void> {
    return new Promise((res) => setTimeout(res, ms));
}
const downloadFile = (blob: string, fileName: string) => {
    const url = window.URL.createObjectURL(new Blob([blob]));
    const link = document.createElement("a");
    link.href = url;
    link.download = fileName;

    document.body.appendChild(link);

    link.click();

    link.parentNode?.removeChild(link);
};

export {sleep, downloadFile};
