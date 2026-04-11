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
  const loadingContainer = document.getElementById("loading-container");
  const mainContent = document.getElementById("main-content");
  const toggleBtn = document.getElementById("toggleViewBtn");
  const countryImg = document.getElementById("countryGraph");
  const causeImg = document.getElementById("causeGraph");

  // 1. Session Check
  const email = localStorage.getItem("email");
  if (!email && mainContent) {
    // Only redirect if we are actually on the Home page (where main-content exists)
    alert("Please log in to view analysis.");
    window.location.href = "LogIn.html";
    return;
  }

  // 2. Loading Logic
  if (loadingContainer && mainContent) {
    // Show loader, hide content
    loadingContainer.classList.remove("hidden");
    mainContent.classList.add("hidden");

    setTimeout(() => {
      loadingContainer.classList.add("hidden");
      mainContent.classList.remove("hidden"); // Show content
    }, 2500); // 2.5-second delay
  }

  // 4. Country Dropdown Selection
  const countrySelect = document.getElementById("countrySelect");
  const detailedSection = document.getElementById("country-detailed-section");
  const causeWrapper = document.getElementById("causeWrapper");
  const subCauseWrapper = document.getElementById("subCauseWrapper");
  const causeLoader = document.getElementById("causeLoader");
  const subCauseLoader = document.getElementById("subCauseLoader");
  const countryTitle = document.getElementById("selectedCountryTitle");
  const countryCauseImg = document.getElementById("countryCauseGraph");
  const countrySubCauseImg = document.getElementById("countrySubCauseGraph");

  if (countrySelect && detailedSection) {
    countrySelect.addEventListener("change", (e) => {
      const selectedCountry = e.target.value;
      if (selectedCountry) {
        // Update Title
        countryTitle.textContent = `Detailed Analysis: ${selectedCountry}`;

        // Sanitize for paths (matches sanitization in dataProcessing2.py)
        const safeName = selectedCountry
          .replace("/", "_")
          .replace("\\", "_")
          .trim();

        // Update Image Paths
        countryCauseImg.src = `/Graphs/Graphs2/${safeName}/${safeName}_cause_frequency.png`;
        countrySubCauseImg.src = `/Graphs/Graphs2/${safeName}/${safeName}_sub_cause_frequency.png`;

        // Reveal Section and show loaders inside the wrappers
        detailedSection.classList.remove("hidden");
        causeLoader.classList.remove("hidden");
        subCauseLoader.classList.remove("hidden");
        causeWrapper.classList.add("loading");
        subCauseWrapper.classList.add("loading");

        detailedSection.scrollIntoView({ behavior: "smooth" });

        // Switch from loader to content after 2.5 seconds
        setTimeout(() => {
          causeLoader.classList.add("hidden");
          subCauseLoader.classList.add("hidden");
          causeWrapper.classList.remove("loading");
          subCauseWrapper.classList.remove("loading");
        }, 2500);
      } else {
        detailedSection.classList.add("hidden");
      }
    });
  }

  // 3. Graph Toggle Logic
  if (toggleBtn && countryImg && causeImg) {
    let currentMode = "bar";

    toggleBtn.addEventListener("click", () => {
      // Logic for switching paths
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

      console.log(
        `Switched to ${currentMode}. Country path: ${countryImg.src}`,
      );
    });

    // Error handling: If the image fails to load, log it
    countryImg.onerror = () =>
      console.error("Failed to load: " + countryImg.src);
    causeImg.onerror = () => console.error("Failed to load: " + causeImg.src);
  }

  // 5. Upload Dataset Redirection (Home Page)
  const goToUploadBtn = document.getElementById("goToUploadBtn");
  if (goToUploadBtn) {
    goToUploadBtn.addEventListener("click", () => {
      window.location.href = "customData.html";
    });
  }

  // 6. Custom Data Page Upload Logic
  const customDatasetInput = document.getElementById("customDatasetUpload");
  if (customDatasetInput) {
    customDatasetInput.addEventListener("change", async (e) => {
      const file = e.target.files[0];
      const statusText = document.getElementById("fileStatus");
      const email = localStorage.getItem("email");

      if (!email) {
        alert("Session expired. Please log in.");
        window.location.href = "LogIn.html";
        return;
      }

      if (file) {
        if (!file.name.endsWith(".xlsx")) {
          alert("Error: Only .xlsx format is accepted.");
          customDatasetInput.value = "";
          return;
        }

        if (statusText) {
          statusText.textContent = `Uploading: ${file.name}...`;
        }

        const formData = new FormData();
        formData.append("file", file);
        formData.append("email", email);

        try {
          const response = await fetch(
            "http://127.0.0.1:8000/upload-custom-dataset",
            {
              method: "POST",
              body: formData,
            },
          );

          const data = await response.json();

          if (response.ok) {
            if (statusText) {
              statusText.textContent = "Data processed successfully!";
            }
            alert("Success: Graphs have been generated for your dataset.");

            // Store session data for results rendering
            localStorage.setItem(
              "customCountries",
              JSON.stringify(data.countries),
            );
            localStorage.setItem("customEmailPrefix", data.emailPrefix);

            // Trigger UI update for results (logic to be added to customData.html)
            location.reload();
          } else {
            alert("Upload failed: " + data.detail);
            if (statusText) statusText.textContent = "Error occurred.";
          }
        } catch (error) {
          console.error("Upload error:", error);
          alert("Could not connect to the server.");
        }
      }
    });
  }

  // 7. Custom Results Logic (On page load)
  const resultsSection = document.getElementById("customResultsSection");
  const customSelector = document.getElementById("customCountrySelect");
  const savedCountries = localStorage.getItem("customCountries");
  const emailPrefix = localStorage.getItem("customEmailPrefix");

  if (resultsSection && savedCountries && emailPrefix) {
    resultsSection.classList.remove("hidden");
    const countries = JSON.parse(savedCountries);

    // Filter out duplicates and empty
    const uniqueCountries = [...new Set(countries)].filter((c) => c);

    uniqueCountries.forEach((country) => {
      const opt = document.createElement("option");
      opt.value = country;
      opt.textContent = country;
      customSelector.appendChild(opt);
    });

    customSelector.addEventListener("change", (e) => {
      const selected = e.target.value;
      if (selected) {
        const safeCountry = selected
          .replace("/", "_")
          .replace("\\", "_")
          .trim();
        const mainImg = document.getElementById("customCauseGraph");
        const subImg = document.getElementById("customSubCauseGraph");
        const mainLoader = document.getElementById("customCauseLoader");
        const subLoader = document.getElementById("customSubCauseLoader");

        // We are in FrontEnd/ folder.
        // Paths relative to FrontEnd/ index.html or Home.html:
        // Graphs are in ../Graphs/CustomGraphs/
        mainImg.src = `../Graphs/CustomGraphs/${emailPrefix}_${safeCountry}/${safeCountry}_main_cause.png?t=${new Date().getTime()}`;
        subImg.src = `../Graphs/CustomGraphs/${emailPrefix}_${safeCountry}/${safeCountry}_sub_cause.png?t=${new Date().getTime()}`;

        console.log("Loading Main Graph:", mainImg.src);
        console.log("Loading Sub Graph:", subImg.src);

        mainLoader.classList.remove("hidden");
        subLoader.classList.remove("hidden");
        mainImg.classList.add("hidden");
        subImg.classList.add("hidden");

        // Error detection for images
        mainImg.onerror = () => {
          console.error("404: Main Graph not found at " + mainImg.src);
          mainLoader.textContent = "Failed to load graph.";
        };
        subImg.onerror = () => {
          console.error("404: Sub Graph not found at " + subImg.src);
          subLoader.textContent = "Failed to load graph.";
        };

        // Reset display after a small delay to ensure loading state shows
        setTimeout(() => {
          mainLoader.classList.add("hidden");
          subLoader.classList.add("hidden");
          mainImg.classList.remove("hidden");
          subImg.classList.remove("hidden");
        }, 1500);
      }
    });
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
