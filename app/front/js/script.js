// Source - https://stackoverflow.com/a

var url = "https://raw.githubusercontent.com/dev-byTN/Web-Scrapping/refs/heads/twitter/ressource/cleanedTweets.json";

/* this tells the page to wait until jQuery has loaded, so you can use the Ajax call */

$(document).ready(function(){
  $.ajax({
    url: url,
    dataType: 'json',
      error: function(){
        console.log('JSON FAILED for data');
      },
    success:function(results){
      console.log(results);
  
      var tweetsList = document.getElementById("tweetsList");

      results.forEach(function(element) {
        tweetsList.insertAdjacentHTML(
        "beforeend",
        `
        <div class="tweet">
            <img src="${element.photo}" alt="">
            <h3>${element.username}</h3>
            <p>Depression : ${element.depression}</p>
            <p>Followers : ${element.followers}</p>
            <p>Following : ${element.following}</p>
            <a href="${element.url}" target="_blank">Link</a>
        </div>
        `
        );
      }); 
    }  
   })
 })   