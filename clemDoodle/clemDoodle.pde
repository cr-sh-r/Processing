int BrushSize = 50 ;
int ColorR  =  0 ;
int ColorG  =  0 ;
int ColorB  =  0 ;
int BackgroundColorR  =  255 ;
int BackgroundColorG  =  255 ;
int BackgroundColorB  =  255 ;
void setup() {
  size(800, 800);
  smooth();
  noStroke();
  background(BackgroundColorR, BackgroundColorG, BackgroundColorB);
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
    ColorR = 156 ;
    ColorG = 4 ;
    ColorB = 9 ;
  } else if (key== 'w') {
    ColorR = 232 ;
    ColorG = 154 ;
    ColorB = 28 ;
  } else if (key== 'e') {
    ColorR = 255 ;
    ColorG = 215 ;
    ColorB = 50 ;
  } else if (key== 'r') {
    ColorR = 142 ;
    ColorG = 209 ;
    ColorB = 19 ;
  } else if (key == 's') {
    saveFrame("clemDoodle saves/betterthanphotoshop-######.png");
  } else if (key== 'd') {
    ColorR =BackgroundColorR  ;
    ColorG =BackgroundColorG  ;
    ColorB =BackgroundColorB  ;
  }
}
void draw() {
  if (mousePressed) {
    fill(ColorR, ColorG, ColorB );
    ellipse(mouseX, mouseY, BrushSize, BrushSize);
  }

  //fill(0, 0, 0);
  //rect(40, 40, 50, 20);
  //String message = "key: " + key;
  //fill(255, 255, 255);
  //text(message, 50, 50);

  //saveFrame("betterthanphotoshop-######.png");
}

