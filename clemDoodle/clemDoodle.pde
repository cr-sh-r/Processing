
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

    if (key == '1') {
      fill(255, 0, 0);
      ellipse(mouseX, mouseY, 10, 10);
    } else if (key == '2') {
      ellipse(mouseX, mouseY, 40, 40);
    } else if (key == '3') {
      ellipse(mouseX, mouseY, 60, 60);
    } else if (key == '4') {
      ellipse(mouseX, mouseY, 80, 80);
    } else if (mousePressed) {
      fill(0, 255, 0);
      ellipse(mouseX, mouseY, 40, 40);
    }
  }

  String message = "key: " + key;
  fill(255, 255, 255);
  text(message, mouseX, mouseY);

  //saveFrame("betterthanphotoshop-######.png");
}

