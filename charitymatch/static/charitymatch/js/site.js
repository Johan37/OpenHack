$( document ).ready(function() {
    // using jQuery
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var answers = {'subject': []};


    $('.answer').click(function(){
        //Answer was clicked.
        var value = $(this).data('value');
        var question = $(this).data('question');


        if (question != 'subject') {
            //Change active states accordingly
            $('[data-question="' + question +'"]').removeClass('active btn-warning');
            //Delete value if it was previously there, otherwise set it.
            if (answers[question] == value) {
                delete answers[question]
            } else {
                answers[question] = value;
                $(this).addClass('active btn-warning');
            }
        } else {
            //subject behaves as a list and items can be added or removed.
            $(this).toggleClass('active btn-warning');
            var index = answers[question].indexOf(value);
            if (index < 0) {
                answers[question].push(value);
            } else {
                answers[question].splice(index, 1);
            }
        }
        console.log(question);
        console.log(value);
        console.log(answers);
        //answers.push(value);
        //Ajax request
        $.ajax({
          method: 'POST',
          url: "searchQuery",
          dataType: 'json',
          contentType: 'application/json; charset=utf-8',
          data: JSON.stringify({ answers: answers })
        })
                .done(function( msg ) {
                    console.log("Data Saved: " + msg.data);

//                    var dummy_json = get_dummy_json();
                    show_relevant_thumbs(msg);
                })
                .fail(function(e) {
                    console.log("Fail!");

                    console.log(e);
                });
    })
});


var get_dummy_json = function() {

    var dummy_text = '{ "organisations" : [' +
            '{ "name":"Amnesty" , "id":"1", "pic":"/static/charitymatch/organisations/image/amnesty.jpg" },' +
            '{ "name":"WWF", "id":"2", "pic":"/static/charitymatch/organisations/image/wwf.png" },' +
            '{ "firstName":"SIDA" , "id":"10", "pic":"/static/charitymatch/organisations/image/sida.png" } ]}';

    return JSON.parse(dummy_text);
};

var show_relevant_thumbs = function(target_json) {

    console.log("show relevant thumbs");
    console.log(target_json);

//    var target_json = JSON.parse(target_json_string);

//    console.log(target_json);

    var orgs = target_json.data;
    var active_orgs = [];

    for (var i = 0; i < orgs.length; i++) {
        active_orgs.push("org" + orgs[i]);
    }

    $('.org_thumb').each(function(i, obj) {

        var element_id = obj.id;
        var dom_id = "#" + element_id;

        if (arrayContains(element_id, active_orgs)) {
            $(dom_id).fadeIn(400);
        }
        else {
            $(dom_id).fadeOut(400);
//            $(dom_id).parent().css("display", "none");
//            $(dom_id).parent().parent().css("overflow", "hidden");
        }
    });


};


function arrayContains(needle, arrhaystack) {
    return (arrhaystack.indexOf(needle) > -1);
}