int menuHeight = 60;
boolean hotbarColor = false;
boolean mouseWasPressed=false;

void setup() {
  size(800, 600);

  rectMode(CORNER);
}


void draw() {
  background(10, 60, 10);

  if (mouseX< width && mouseX >0 && mouseY < height && mouseY > height-menuHeight ) {
    hotbarColor=true;
    if (mousePressed == true && mouseWasPressed== false) {
      print("yo");
    }
  } else {
    hotbarColor=false;
  }

  if (hotbarColor== true) {
    fill(83, 103, 67);
  } else {
    fill(255, 255, 255);
  }

  rect(0, height-menuHeight, width, menuHeight);
  
  mouseWasPressed=mousePressed;
}

