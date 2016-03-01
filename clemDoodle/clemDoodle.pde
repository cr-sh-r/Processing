int BrushSize = 50 ;
void setup() {
  size(800, 800);
  smooth();
  noStroke();
}

void keyPressed()
{
  if (key == '1') {
    BrushSize = 10 ;
  } else if (key == '2') {
    BrushSize = 40 ;
  } else if (key == '3') {
    BrushSize = 60;
  } else if (key == '4') {
    BrushSize = 80;
  } else if (key == '5') {
    BrushSize = 100;
  }
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

    ellipse(mouseX, mouseY, BrushSize, BrushSize);
  }

  fill(0, 0, 0);
  rect(40, 40, 50, 20);
  String message = "key: " + key;
  fill(255, 255, 255);
  text(message, 50, 50);

  //saveFrame("betterthanphotoshop-######.png");
}

