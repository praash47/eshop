import axios from 'axios'

export function sendRequest(method, url, data) {
    return axios({
        method,
        url,
        xsrfCookieName: 'csrftoken',
        xsrfHeaderName: 'X-CSRFToken',
        data
    });
}