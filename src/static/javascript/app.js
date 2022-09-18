window.addEventListener("load", () => {
  const Password = document.getElementById("password");

  const Eye = document.getElementById("eye");

  console.log(Password, Eye);

  Eye.addEventListener("click", () => {
    if (Password.type === "password") {
      Password.type = "text";
      Eye.classList.add("focused");
    } else {
      Password.type = "password";
      Eye.classList.remove("focused");
    }
  });
});
