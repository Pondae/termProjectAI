import apiClient from "./AxiosClient.js";

export default {
  searcWebsite(query) {
    return apiClient.post("/search", {
      query: query,
    });
  },
  storage() {
    return apiClient.get("/storage");
  }
};
