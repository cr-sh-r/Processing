
void setup() {
  size(800, 800);
  smooth();
  noStroke();
}

void draw() {
  if (mousePressed) {
    if (keyPressed) {
      fill(156, 4, 9 );
    } else {
      fill(0);
    }
    ellipse(mouseX, mouseY, 80, 80);
  }
}

