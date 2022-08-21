/** 
* Function returns base url for post or category view
* @param {string} url - Function accepts a string URL for paramter. If none is specified, base url for posts is used.\
Note that the parameter for this function has to be identical to the one in posts/urls.py in order for the function to work properly.
* @return {string} Returns the base url for a specified parameter
*
* Basic usage:
* getBaseUrl() => Base URL for posts view
* getBaseUrl('category') => Base URL for category view. 
*/
export const getBaseUrl = (url = '') => {
    const httpBaseUrl = $(".dropdown-content").attr("data-url");
    const httpPostsPath = $(".dropdown-content").attr("data-posts-href")
    const httpCatPath = $(".dropdown-content").attr("data-cat-href")
    const categoryUrl = httpCatPath.substring(0,httpCatPath.length-2)
    var baseUrl = `${httpBaseUrl}`
    
    if (url === 'posts') {
        baseUrl = `${httpBaseUrl}${httpPostsPath}`
    }
    if (url === 'category') {
        baseUrl = `${httpBaseUrl}${categoryUrl}`
    }
    return baseUrl
}


/** 
* Returns browser cookies
* @summary Return browser cookies in form of an object if function parameters is not specified or returns a single entry from that object
* @param {string} cookie - Specify a cookie to be returned or leave empty /function call/ to get all cookies in form of object
* @return {object or string} Returns object or individual cookies
*/

export function getCoockies(cookie='') {
    const cookies = document.cookie.split(';')
    var cookieObj = {};

    cookies.forEach(cookie => {
        var keyValuePair = cookie.split('=')
        var key = keyValuePair[0].trim()
        var value = keyValuePair[1].trim()
        cookieObj[key] = value
    });

    if (cookie === '') { return cookieObj }
    if (cookie in cookieObj) { return cookieObj[cookie]}
    
    return new Error('There is no such cookies stored in the browser')
}


/** 
* Remove styles to search bar
*/

export function removeSearchStyle() {
    $(".dropdown-content").removeClass('show');
    $("#search-bar").removeClass('style-search-bar');
};


/** 
* Add styles to search bar
*/
export function addSearchStyle() {
    $(".dropdown-content").toggleClass('show');
    $("#search-bar").toggleClass('style-search-bar');
};
