int menuHeight = 60;
boolean mouseWasPressed=false;

void setup() {
  size(800, 600);

  rectMode(CORNER);
}


void draw() {
  background(10, 60, 10);
  boolean mouseClicked = (mousePressed == true && mouseWasPressed== false);
  boolean mouseUpClicked = (mousePressed == false && mouseWasPressed== true);

  int hotbarColor = 0;

  if (mouseX< width && mouseX >0 && mouseY < height && mouseY > height-menuHeight ) {
    if (mousePressed == true) {
      hotbarColor=2;
    } else {
      hotbarColor=1;
    }      



    if (mouseUpClicked == true) {
      print("yo");
    }
  } 

  if (hotbarColor== 0) {
    fill(255, 255, 255);
  } else if (hotbarColor == 1) {
    fill(83, 103, 67);
  } else if (hotbarColor== 2) {
    fill(53, 98, 17);
  }

  rect(0, height-menuHeight, width, menuHeight);

  float numIcons = 7;
  float iconWidth = width/numIcons ;
  int icon = 0 ;
  while(icon < numIcons ) {
    float x = iconWidth*icon ;
    float y = height-menuHeight ;
    
    rect(x,y,iconWidth,menuHeight);
    
    icon = icon + 1;
  }








  mouseWasPressed=mousePressed;
}

