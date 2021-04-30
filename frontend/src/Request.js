import axios from "axios";
import {config} from './config';

class Request {

    async get(url) {
        let response = await axios.get(`${config.backendURL}${url}`,{
            headers: {
                'Authorization': `Token ${localStorage.getItem('token')}`
            }
        })
        return response.data;
    }

    async post(url, data) {
        let response = await axios.post(`${config.backendURL}${url}`,data,{
            headers: {
                'Authorization': `Token ${localStorage.getItem('token')}`
            }
        })
        return response.data;
    }

}

export default Request;