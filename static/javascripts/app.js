const form = document.querySelector("#searchForm");
form.addEventListener("submit", function (e) {
    e.preventDefault();
  
    if (form.elements.q) {
      const searchTerm = form.elements.q.value;
      const searchOption = form.elements.opt.value;
  
      if (searchTerm.trim().length !== 0) {
        const params = new URLSearchParams();
        params.append("q", searchTerm);
        if (searchOption) {
            params.append("opt", searchOption);
        }
        const url = baseUrl + "?" + params.toString();
  
        window.location.href = url;
      } else {
        console.error("Search term is empty.");
      }
    }
});
