// This script is optional and is used to randomly display the front or the back of the card
var card = document.querySelector('.card');
card.addEventListener('click', function () {
  card.classList.toggle('is-flipped');
});
