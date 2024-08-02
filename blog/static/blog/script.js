// document.querySelector("body").style.backgroundColor = "red";

function showdiv(divclass){
  document.querySelector("div").style.display="none";
  document.querySelector(`.${divclass}`).style.display="block";
}



localStorage.setItem('pokemon', 'pikachu' );

if(localStorage.getItem("token")!= null){
  url="https://5fd6284a-af3a-4fdf-8994-cf7705c84000-00-3u2qot3wbb3p7.sisko.replit.dev/allblog";
  need={
    method: "get",
    headers: {
      "Authorization": "Token 3d83db67fcbf63f086fea63a38a0bb8b4f1f1f62",
      "Content-Type": "application/json",
      "X-CSRFToken": "{{csrf_token}}"
    }
  }
  
  fetch(url, need)
  .then((response)=>{return response.json()})
  .then((value)=>{console.log(value)})

  showdiv(allblogs)
}
else{
  showdiv(login)
}


// let myBlogs=document.querySelector("#my_blogs");

// myBlogs.addEventListener("click", ()=>{

//   data={
//     method: "get",
//     headers: {
//       "Authorization": "Token 3d83db67fcbf63f086fea63a38a0bb8b4f1f1f62",
//       "Content-Type": "application/json",
//       "X-CSRFToken": "{{csrf_token}}"
//     }
//   }
  
//   fetch("https://5fd6284a-af3a-4fdf-8994-cf7705c84000-00-3u2qot3wbb3p7.sisko.replit.dev/myblogs", data)
// .then((response)=>{return response.json()})
// .then((value)=>{console.log(value)})
  
// })