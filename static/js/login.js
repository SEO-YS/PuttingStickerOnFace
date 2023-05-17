  const images = document.querySelectorAll('.subimg img');
    let currentImage = 0;

    function showNextImage() {
      images[currentImage].classList.remove('active');
      currentImage = (currentImage + 1) % images.length;
      images[currentImage].classList.add('active');
    }

    setInterval(showNextImage, 3000);

function hideLogin() {
        var loginForm = document.getElementById("login-form");
        loginForm.style.display = "none";
    }

function handleLoginResponse(response) {
        if (response.success) {
            hideLogin();
        } else {
            // Handle login failure
        }
    }