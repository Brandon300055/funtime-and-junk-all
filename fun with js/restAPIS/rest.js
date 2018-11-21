var getJSON = function(url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.responseType = 'json';
    xhr.onload = function() {
        var status = xhr.status;
        if (status == 200) {
            callback(null, xhr.response);
        } else {
            callback(status);
        }
    };
    xhr.send();
};

getJSON('https://maps.googleapis.com/maps/api/place/textsearch/json?query=sillicon_valley&key=AIzaSyD_9VyLJ01BNKW2oIB6CEXIqU9sHYhKKBs',  function(err, data) {

    if (err != null) {
        console.error(err);
    } else {

        var text = `Date: ${data.date}
Time: ${data.time}
Unix time: ${data.milliseconds_since_epoch}`

        console.log(text);
    }
});
