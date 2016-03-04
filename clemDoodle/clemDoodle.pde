int BrushSize = 50 ;
color BrushColor = color(0, 0, 0);
color BackgroundColor  = color(255, 255, 255) ;
int mouseWasX = 0 ;
int mouseWasY = 0 ;

void setup() {
  size(800, 800);
  smooth();
  //noStroke();
  background(BackgroundColor);
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
  } else if (key == 'q') {
    BrushColor = color(156, 4, 9 );
  } else if (key== 'w') {
    BrushColor = color(232, 154, 28 );
  } else if (key== 'e') {
    BrushColor = color(255, 215, 50);
  } else if (key== 'r') {
    BrushColor = color(142, 209, 19 );
  } else if (key == 's') {
    saveFrame("clemDoodle saves/betterthanphotoshop-######.png");
  } else if (key== 'd') {
    BrushColor = BackgroundColor  ;
  }
}
void draw() {
  if (mousePressed) {
    stroke(BrushColor);
    strokeWeight(BrushSize);
    line(mouseWasX, mouseWasY, mouseX, mouseY);

    //ellipse(mouseX, mouseY, BrushSize, BrushSize);
  }
  mouseWasX = mouseX ;
  mouseWasY = mouseY ;

  colorMode(HSB,360,100,100);
  color c = color(180,100,100);
  fill(c);
  rect(40, 40, 50, 20);
  colorMode(RGB,255);
  //String message = "key: " + key;
  //fill(255, 255, 255);
  //text(message, 50, 50);


  //saveFrame("betterthanphotoshop-######.png");
}

