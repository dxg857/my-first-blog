// document.addEventListener('trix-file-accept', function(ev) {
//   ev.preventDefault();
// });


document.addEventListener('trix-attachment-add', function(ev) {

    let data = {};

    let request = new XMLHttpRequest();
    request.open('POST', '/trix/attachment/', true);
    request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
    request.send(data);

});

