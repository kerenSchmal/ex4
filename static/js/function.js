const activePage= window.location.pathname;

const navlinks= document.querySelectorAll('nav a').forEach(link => {
    if (link.href.includes(`${activePage}`)) {
        link.classList.add('active');
    }
});



var i = 0;
var txt = 'Thank you. Our phone number is 052-4829014';
var speed = 50;
      
function typeWriter() {
    if (i < txt.length) {
        document.getElementById("ourPhoneNumber").innerHTML += txt.charAt(i);
        i++;
        setTimeout(typeWriter, speed);
        }
      }


function change() {
    const  doc = document.getElementsByClassName('imagesIce');
    var randomColor = Math.floor(Math.random() * 16777215).toString(16);
    doc[0].style.borderColor  = "#" + randomColor;
    }
setInterval(change, 1000);




function getUserBy_id(user_id){
    fetch('https://reqres.in/api/users/'+user_id).then(
        response => response.json()
    ).then(
        responseOBJECT => createUser(responseOBJECT.data)
    ).catch(
        err => console.log(err)
    );
}

function createUser(response){
    let user = response;
    const currMain = document.querySelector("main")

    const section = document.createElement('section')
    section.innerHTML = `
        <img src="${user.avatar}" alt="Profile Picture"/>
        <div>
         <span>${user.first_name} ${user.last_name}</span>
         <br>
         <a href="mailto:${user.email}">Send Email</a>
        </div> 
        `
    currMain.appendChild(section)
}