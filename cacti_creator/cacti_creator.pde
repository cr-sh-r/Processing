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

  fill(255, 255, 255);
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
   
    
    
    float bw = w/6;
    float bh =h/6;
    float xi = x+bw;
    float yi= y+bh;
    float wi = w-2*bw;
    float hi = h-2*bh;
    
    rect(xi, yi, wi, hi);

    icon = icon + 1;
  }








  mouseWasPressed=mousePressed;
}

