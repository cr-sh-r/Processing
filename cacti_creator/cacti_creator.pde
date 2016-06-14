int menuHeight = 50;


void setup() {
  size(900, 600);
  
  rectMode(CORNER);
}


void draw() {
  background(10,60,10);
  fill(255,255,255);
  rect(0,height-menuHeight,width,menuHeight);
  
  rect(mouseX, mouseY, 10,10);
  
}
