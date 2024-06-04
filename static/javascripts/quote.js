document.addEventListener("DOMContentLoaded", function () {
  fetch("https://api.quotable.io/random")
    .then((response) => response.json())
    .then((data) => {
      const quoteContainer = document.getElementById("quoteContainer");
      quoteContainer.innerHTML = `
                <p class="quote text-white text-center">
                    "${data.content}"
                </p>
                <p class="author text-white text-center">- <em>${data.author}</em></p>`;
    })
    .catch((error) => console.error("Error fetching the quote:", error));
});
