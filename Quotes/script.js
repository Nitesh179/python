
// const emoji=require('./emoji.json');

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

            fetch("./emoji.json").then(res=> res.json()).then(emoji=>{
              document.getElementById('img-1').src=emoji[Math.floor(Math.random() * emoji.length)]
              document.getElementById('img-2').src=emoji[Math.floor(Math.random() * emoji.length)]
              document.getElementById('img-3').src=emoji[Math.floor(Math.random() * emoji.length)]
            })

            document.getElementById('quote-1').innerHTML=quote1
            document.getElementById('author-1').innerHTML=authr1
            // document.getElementById('img-1').src=authr1

            document.getElementById('quote-2').innerHTML=quote2
            document.getElementById('author-2').innerHTML=authr2
            // document.getElementById('img-2').src=authr1

            document.getElementById('quote-3').innerHTML=quote3
            document.getElementById('author-3').innerHTML=authr3
            // document.getElementById('img-3').src=authr1
        
  })
}

fetchdata()