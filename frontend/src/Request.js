import axios from "axios";


class Request {

    async get(url) {
        let response = await axios.get(`${url}`)
        return response.data;
    }

}

export default Request;