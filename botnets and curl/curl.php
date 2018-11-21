<?php
//load google

$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, 'https://www.google.com/');

//instance of the output derectly
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

//set return header to true
curl_setopt($ch, CURLOPT_HEADER, 1);
//echo $ch;

$output = curl_exec($ch);

//check for error
if ($output === FALSE) {
    echo "cURL Error: " . curl_error($ch);
}

//close handler
curl_close($ch);

print_r($output);


//testing



///post data to page

$url = "http://checker.test/output.php";
$post_data = array(
    "query" => 'some stuff',
    "method" => 'post',
    "kittens" => 'are niffty',
);

//always first init the handle lar
$ch = curl_init();

//url to submit to
curl_setopt($ch,CURLOPT_URL, $url);

//url to submit to
curl_setopt($ch,CURLOPT_RETURNTRANSFER, 1);

//url to submit to
curl_setopt($ch,CURLOPT_POST, 1);

//url to submit to
curl_setopt($ch,CURLOPT_POSTFIELDS, $post_data);

//execute the request and fetch the response + check for errors

$output = curl_exec($ch);

if ($output === FALSE) {
    echo "cURL error" . curl_error($ch);
}

//Close and free up the curl handler
curl_close($ch);


//display results
print_r($output);
