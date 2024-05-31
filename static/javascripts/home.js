const form = document.querySelector("#searchForm");
form.addEventListener("submit", function (e) {
    e.preventDefault();
  
    if (form.elements.q) {
      const searchTerm = form.elements.q.value;
  
      if (searchTerm.trim().length !== 0) {
        const params = new URLSearchParams();
        params.append("q", searchTerm);
  
        const baseUrl = "http://127.0.0.1:8000/search/";
  
        const url = baseUrl + "?" + params.toString();
  
        window.location.href = url;
      } else {
        console.error("Search term is empty.");
      }
    } else {
      console.error("Form element with name 'q' not found.");
    }
  });
