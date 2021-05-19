import axios from 'axios'

export async function sendRequest(url, data) {
    try {
        const response = await axios.post(
            url,
            data
        )
        return response
    } catch (error) {
        console.error(error);
    }
}