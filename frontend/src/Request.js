import axios from "axios";
import {config} from './config';

class Request {

    async get(url) {
        let response = await axios.get(`${config.backendURL}${url}`)
        return response.data;
    }

    async post(url, data) {
        let response = await axios.post(`${config.backendURL}${url}`,data)
        return response.data;
    }

}

export default Request;