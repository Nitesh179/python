
// const fetch=require('node-fetch');

function fetchdata(){
  fetch('./QuoteData.json').then((res)=>res.json()).then((data)=>{ 
        
        var qt1=data[Math.floor(Math.random() * data.length)]
        var qt2=data[Math.floor(Math.random() * data.length)]
        var qt3=data[Math.floor(Math.random() * data.length)]
       
            var quote1=qt1.Quotes[Math.floor(Math.random() * qt1.Quotes.length)]
            var quote2=qt2.Quotes[Math.floor(Math.random() * qt2.Quotes.length)]
            var quote3=qt3.Quotes[Math.floor(Math.random() * qt3.Quotes.length)]

            var authr1=qt1.Author
            var authr2=qt2.Author
            var authr3=qt3.Author

            document.getElementById('quote-1').innerHTML=quote1
            document.getElementById('author-1').innerHTML=authr1

            document.getElementById('quote-2').innerHTML=quote2
            document.getElementById('author-2').innerHTML=authr2

            document.getElementById('quote-3').innerHTML=quote3
            document.getElementById('author-3').innerHTML=authr3
        
  })
}

fetchdata()