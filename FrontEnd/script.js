// Function to handle navigation between pages
function navigateTo(page) {
  if (page === "signup") {
    window.location.href = "signup.html";
  } else if (page === "login") {
    window.location.href = "login.html";
  }
}

window.addEventListener("scroll", () => {
  const nav = document.querySelector(".navbar");
  if (window.scrollY > 50) {
    nav.style.background = "rgba(26, 26, 46, 0.9)";
    nav.style.backdropFilter = "blur(10px)";
  } else {
    nav.style.background = "transparent";
    nav.style.backdropFilter = "none";
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const signupForm = document.getElementById("signupForm");
  const loginForm = document.getElementById("loginForm");

  if (signupForm) {
    signupForm.addEventListener("submit", (e) => handleAuth(e, "signup"));
  }

  if (loginForm) {
    loginForm.addEventListener("submit", (e) => handleAuth(e, "login"));
  }
});

async function handleAuth(event, type) {
  event.preventDefault();

  const email = event.target.querySelector("#email").value;
  const password = event.target.querySelector("#password").value;

  try {
    const response = await fetch(`http://127.0.0.1:8000/${type}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });

    const data = await response.json();

    if (response.ok) {
      alert(data.message);
      if (type === "signup") {
        window.location.href = "Home.html";
        localStorage.setItem("email", email);
      } else {
        window.location.href = "Home.html";
        localStorage.setItem("email", email);
      }
    } else {
      alert("Error: " + data.detail);
    }
  } catch (error) {
    console.error("Connection failed:", error);
    alert("Could not connect to the server. Make sure FastAPI is running.");
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const mainContent = document.getElementById("main-content");
  const toggleBtn = document.getElementById("toggleViewBtn");
  const countryImg = document.getElementById("countryGraph");
  const causeImg = document.getElementById("causeGraph");

  // 1. Session Check
  const email = localStorage.getItem("email");
  if (!email && mainContent) {
    // Only redirect if we are actually on the Home page (where main-content exists)
    alert("Please log in to view analysis.");
    window.location.href = "signIn.html";
    return;
  } else if (mainContent) {
    mainContent.classList.remove("hidden");
  }

  // 2. Graph Toggle Logic
  if (toggleBtn && countryImg && causeImg) {
    let currentMode = "bar";

    toggleBtn.addEventListener("click", () => {
      // Logic for switching paths
      // Note: Removed the leading '/' to ensure consistency with your folder structure
      if (currentMode === "bar") {
        countryImg.src = "/Graphs/country_frequency_pie.png";
        causeImg.src = "/Graphs/main_cause_frequency_pie.png";
        toggleBtn.textContent = "Switch to Bar Graphs";
        currentMode = "pie";
      } else {
        countryImg.src = "/Graphs/country_frequency_bar.png";
        causeImg.src = "/Graphs/main_cause_frequency_bar.png";
        toggleBtn.textContent = "Switch to Pie Charts";
        currentMode = "bar";
      }

      // Console log to help you debug in the browser (F12 > Console)
      console.log(
        `Switched to ${currentMode}. Country path: ${countryImg.src}`,
      );
    });

    // Error handling: If the image fails to load, log it
    countryImg.onerror = () =>
      console.error("Failed to load: " + countryImg.src);
    causeImg.onerror = () => console.error("Failed to load: " + causeImg.src);
  }
});

// Function to load components (Nav/Footer)
async function loadComponents() {
  try {
    // Load Navbar
    const navResponse = await fetch("Nav.html");
    const navHtml = await navResponse.text();
    document.getElementById("nav-placeholder").innerHTML = navHtml;

    // Load Footer
    const footerResponse = await fetch("Footer.html");
    const footerHtml = await footerResponse.text();
    document.getElementById("footer-placeholder").innerHTML = footerHtml;

    // Update the Email in Navbar after it loads
    const email = localStorage.getItem("email");
    const emailSpan = document.getElementById("user-email");
    if (email && emailSpan) {
      emailSpan.textContent = email;
    }
  } catch (error) {
    console.error("Error loading components:", error);
  }
}

// Function to handle Logout
function logout() {
  localStorage.removeItem("email");
  window.location.href = "LogIn.html";
}

// Ensure components load on every page
document.addEventListener("DOMContentLoaded", loadComponents);

// Function to open image in a new tab
function openImage(imgId) {
  const img = document.getElementById(imgId);
  if (img && img.src) {
    window.open(img.src, "_blank");
  }
}

// Ensure the Toggle Logic from before is updated to match new IDs if necessary
// (Your existing toggle logic will work fine with this HTML)
