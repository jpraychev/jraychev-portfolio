import { getBaseUrl, getCoockies, addSearchStyle, removeSearchStyle} from './lib.js';

// API URLS
const postsURL = `${getBaseUrl()}/api/v1/posts`
const subscribeURL = `${getBaseUrl()}/api/v1/subscribe`

// All API calls
const getPosts = async (url) => {
    const postsResponse = await fetch(url);
    const postsData = await postsResponse.json();
    return postsData
}

$("#search-bar").on('click', function(){
    const displayData = async () => {
        const postsObject = await getPosts(postsURL)
        const posts = postsObject.posts
        
        $("#search-bar").keyup(function(){
            let searchData = $(this).val().toLowerCase();
            const match = posts.filter(post => {
                const result = post.title.toLowerCase().includes(searchData)
                return result
            })
            // const html = match.map(post =>`
            //     <li><a href="${post.id}">${post.title}</a>
            //     <a class="float-right small text-secondary" href="${post.category__name}"> in ${post.category__name}</a></li>`
            // ).join('');
            const html = match.map(post => 
                "<li>\
                    <a href="+getBaseUrl('posts')+""+post.id+">"+post.title+"</a>\
                    <a class='float-right small text-secondary' href="+getBaseUrl('category')+""+post.category__name+">in "+post.category__name+"</a>\
                </li>").join('')
            $(".dropdown-content").html(html);
        });
    };
    displayData();
});


$(window).on("click", function(event){
    const clickedElemenet = event.target;
    const searchBar = $("#search-bar")[0];
    clickedElemenet == searchBar ? addSearchStyle() : removeSearchStyle();
})

$('#email-button').on('click', function() {
    // Get the value from email-address input
    const userEmail = $('#email-address').val()
    $('#email-address').val('')
    const csrfToken = $("input[name='csrfmiddlewaretoken']").val()
    const cookies = document.cookie

    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/x-www-form-urlencoded");
    myHeaders.append("Cookie", cookies);

    var urlencoded = new URLSearchParams();
    urlencoded.append('email', userEmail);
    urlencoded.append('csrfmiddlewaretoken', csrfToken);
    
    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: urlencoded,
        redirect: 'follow'
    };
    
    fetch(subscribeURL, requestOptions)
      .then(response => response.text())
      .then(result => $('.modal-body').text(`${result}`))
      .catch(error => console.log('error', error));

});