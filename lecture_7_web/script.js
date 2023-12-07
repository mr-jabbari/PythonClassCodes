function changeColor() {
  const heading = document.getElementById('heading');
  // Random color generator
  const randomColor = '#' + Math.floor(Math.random()*16777215).toString(16);
  heading.style.color = randomColor;
}