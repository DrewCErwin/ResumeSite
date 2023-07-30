var Linkedin = "Linkedin";
var Github = "Github";
var Blog = "Blog";


function UpdateClick(obj) {
    const url = "**********************";
    const bodyinfo = JSON.stringify({"name": obj});
    const options = {
      method: "POST",
      headers: {
        "Access-Control-Allow-Origin": url,
        "Content-Type": "application/json"
      },
      body: JSON.stringify({"name": obj}),  
      mode: "cors"
    };
    fetch(url, options)
      .then(response => {
        if (response.ok) {
          console.log(bodyinfo+" was successfully stored in the database.");
        } else {
          console.error("An error occurred while storing the object in the database.");
        }
      })
      .catch(error => {
        console.error(error);
      });
  };

function LinkToLinkedin(){
    UpdateClick(Linkedin);
    window.location.href = ("https://www.linkedin.com/in/drew-erwin-265256119/");
};

function LinkToGithub(){
    UpdateClick(Github);
    window.location.href = "https://github.com/DrewCErwin?tab=repositories";
};

function LinkToBlog(){
    UpdateClick(Blog);
    window.location.href = "https://drewerwin.hashnode.dev/cloud-resume-challenge";
};

//var visitCount = localStorage.getItem("page_view");
//if (visitCount) {
//    visitCount = Number(visitCount) + 1;
//    localStorage.setItem("page_view", visitCount);
//} else {
//    visitCount = 1;
//    localStorage.setItem("page_view", 1);
//  }
