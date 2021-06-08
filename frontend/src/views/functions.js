import axios from 'axios'

export async function sendRequest(url, data) {
    try {
        url = 'http://127.0.0.1:8000/' + url
        const response = await axios.post(
            url,
            data
        )
        return response
    } catch (error) {
        console.error(error);
    }
}

export function createCookie(cookieName,cookieValue,daysToExpire) {
    var date = new Date();
    date.setTime(date.getTime()+(daysToExpire*24*60*60*1000));
    document.cookie = cookieName + "=" + cookieValue + "; expires=" + date.toGMTString();
}

export function accessCookie(cookieName) {
    var name = cookieName + "=";
    var allCookieArray = document.cookie.split(';');
    for(var i=0; i<allCookieArray.length; i++)
    {
        var temp = allCookieArray[i].trim();
        if (temp.indexOf(name)==0)
            return temp.substring(name.length,temp.length);
        }
    return "";
}

// Clear all the keys of a dictionary
export function clearKeys(dictionary) {
    for (const key in dictionary) {
        dictionary[key] = ""
    }
    return dictionary
}


// Show and Hide utility function
export function showOrHide(component, show) {
    const classList = component.classList

    if (show) {
        classList.add('show')
        component.style.display = "block"
    } else {
        classList.remove('show')
        component.style.display = "none"
    }
}