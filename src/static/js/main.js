// TO DO - Move these functions to a separate file and import them when needed
const removeActive = () => {
    $('#sidebar').removeClass('active')
    $('.arrow').removeClass('left').addClass('right')
}

const addActive = () => {
    $('#sidebar').addClass('active')
    $('.arrow').removeClass('right').addClass('left')
}

const checkWidth = (width) => {
    return width > 768 ? true : false;
}

$(document).ready(function () {

    // Toggles sidebar
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
        $('.arrow').toggleClass('left right');
    });
    
    // Checks if width is bigger than 768 px
    checkWidth($(document).width()) ? '' : removeActive();

    // Renders social box on contact page
    $('.social-box-animate').animate({ 
        left: '0%',
        opacity: '1'
    }, 1000 );

    // Renders contact form on contact page
    $('.contact-form-animate').animate({ 
        right: '0%',
        opacity: '1',
        'margin-left' : '-15px'
    }, 1000 );

    // Get number of experience objects from DB
    const timelineLength = $('.timeline-box').parent().length + 1 
    
    for (let i = 1; i < timelineLength; i++) {
        var delaySeconds = 750+i*450;

        $('.fadeInUp-'+ i +'').animate({
            'bottom': '0'
        }, delaySeconds );

        $('.fadeInRight-'+ i +'').animate({ 
            'margin-left': '0%',
            'opacity': '1'
        }, delaySeconds );
    };

    // Dynamically render progress on skill bar
    $.each( $('.progress-box'), function() {
        skillPercent = $(this).find('.skill-percent').text();
        $(this).find('.progress-active').css("width", skillPercent)
    });

    $('.experience').on('click', function () {
        $(this).toggleClass('updown');
    });

    $( '.work-box' ).hover(function() {
        $( this ).addClass( "disable-select" );
    });

    $('.work-box, .blog-box, .service-box, .timeline-box, .quote-box').animate({ 
        opacity: '1'
    }, 1000 );
    
    // Key combination to show/hide sidebar CTRL + ALT + B
    $(document).keydown(function(e){
        if( e.ctrlKey  &&  e.altKey  &&  e.which === 66) {
            $('#sidebar').toggleClass('active');
            $('.arrow').toggleClass('left right');
        }        
    });

});

// Hides or shows the sidebar based on size of window
$(window).on('resize', function() {
    width = $(this).width();
    checkWidth(width) ? addActive() : removeActive();
});

// // Handles Google ReCaptcha logic
// btn = document.getElementsByTagName("button")[0]
// form = btn.closest("form")
// console.log(btn)
// // formBtn = document.getElementById('form-btn')
// btn.addEventListener("click", function(e){ 
//     e.preventDefault();
//     grecaptcha.ready(function() {
//         grecaptcha.execute("6LcevbYhAAAAADgeMdbvfQtFpOBgklwcIS-fCUpS", {action: "submit"}).then(function(token) {
//             document.getElementById("recaptcha").value = token
//             form.submit()
//         });
//     });
// });


// Handles active class and adds line below the item
currentPath = $("#request-path").data("requestPath").split("/")[1]
if (!currentPath) {
    currentLink = $("#home")
} else {
    currentLink = $("#" + currentPath)
}
currentLink.addClass("active")