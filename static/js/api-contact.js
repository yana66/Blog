var log = function() {
    console.log.apply(console, arguments)
}

var e = function(sel) {
    return document.querySelector(sel)
}

var ajax = function(method, path, data, responseCallback) {
    var r = new XMLHttpRequest()
    r.open(method, path, true)
    r.setRequestHeader('Content-Type', 'application/json')
    log('1')
    r.onreadystatechange = function() {
    log('4')
        if(r.readyState === 4) {
        log('5')
            responseCallback(r.response)
        }
        log('6')
    }
    log('2')
    data = JSON.stringify(data)
    r.send(data)
    log('3')
}

var apiSendMail = function(form, callback) {
    var path = '/mail'
    ajax('POST', path, form, callback)
}

var bindEventSend = function() {
    var b = e('#sendMessageButton')
    b.addEventListener('click', function() {
        var name = e('#name').value
        var email = e('#email').value
        var phone = e('#phone').value
        var message = e('#message').value
        var form = {
            name: name,
            email: email,
            phone: phone,
            message: message
        }
        swal({
            title: "正在发送...",
            showConfirmButton: false
        })
        apiSendMail(form, function(r) {
            swal({
                title: '成功发送',
                text: '来信已收到,我将尽快回复您!',
                type: 'success'
            },
            function() {
                setTimeout(
                    function() {
                        window.location.href='/'
                    }, 2000)}
            )
        })
    })
}


var __main = function() {
    bindEventSend()
}

__main()

