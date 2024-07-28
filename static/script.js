let submit = document.getElementById("submit");

// create a submmit function
const submitQuery = (query)=>{
    window.location.href = '/search?q=' + query;
}

submit.addEventListener("click",(evt)=>{
    console.log("clicked");
    evt.preventDefault();
    let query = document.getElementById("search").value;
    if (query!=null || query!=""){
        submitQuery(query);
    }  
})
