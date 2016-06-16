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

  

  

  
fill(255,255,255);
  rect(0, height-menuHeight, width, menuHeight);

  float numIcons = 7;
  float iconboxWidth = width/numIcons ;
  int icon = 0 ;
  while (icon < numIcons ) {
    float x = iconboxWidth*icon ;
    float y = height-menuHeight ;
    float w = iconboxWidth;
    float h = menuHeight;

    if (mouseX < x+w && mouseX > x && mouseY < y+h && mouseY > y ) {
      // hovered
      if (mouseUpClicked == true) {
        print(icon+"\n");
      }
      if (mousePressed==true) {
        fill(53, 98, 17);
      } else {
        fill(83, 103, 67);
      }
    } else {
      // not hovered
      fill(255, 255, 255);
    }

    rect(x, y, w, h);

    icon = icon + 1;
  }








  mouseWasPressed=mousePressed;
}

