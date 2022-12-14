const Password = document.getElementById("password");
const Eye = document.querySelector(".pass-show-eye");

Eye &&
  Eye.addEventListener("click", () => {
    if (Password.type === "password") {
      Password.type = "text";
      Eye.classList.add("focused");
    } else {
      Password.type = "password";
      Eye.classList.remove("focused");
    }
  });

// error message

const error = document.querySelector(".error");

error &&
  setTimeout(() => {
    error.style.display = "none";
  }, 3000);

// form

const Input = document.querySelectorAll("input");

Input.forEach((input) => {
  input.addEventListener("input", function (evt) {
    if (this.value.length > 0) {
      this.classList.add("active");
    } else {
      this.classList.remove("active");
    }
  });
});

// notification

// sidebar

const menuIcon = document.querySelector(".menu-toggle");
const sideBar = document.querySelector(".side-menu");

sideBar &&
  menuIcon.addEventListener("click", () => {
    console.log("hehe");
    sideBar.classList.toggle("active");
  });
