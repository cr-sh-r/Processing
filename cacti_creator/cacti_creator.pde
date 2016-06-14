int menuHeight = 60;
boolean hotbarColor = false;

void setup() {
  size(800, 600);

  rectMode(CORNER);
}


void draw() {
  background(10, 60, 10);

  if (mouseX< width && mouseX >0 && mouseY < height && mouseY > height-menuHeight ) {
    hotbarColor=true;
  } else {
    hotbarColor=false;
  }

  if (hotbarColor== true) {
    fill(50, 50, 2);
  } else {
    fill(255,255,255);
  }

  rect(0, height-menuHeight, width, menuHeight);
}

