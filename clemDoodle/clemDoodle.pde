
void setup() {
  size(800, 800);
  smooth();
  noStroke();
}

void draw() {
  if (mousePressed) {
    if (keyPressed) {
      if (key == 'q') {
        fill(156, 4, 9 );
      } else if (key== 'w') {
        fill(232, 154, 28);
      } else if (key== 'e') {
        fill(255, 215, 50);
      } else if (key== 'r') {
        fill(142, 209, 19);
      }
    } else {
      fill(0);
    }

    ellipse(mouseX, mouseY, 80, 80);
  }
  saveFrame("#betterthanphotoshop-######.png");
}

