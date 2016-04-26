int BrushSize = 50 ;
color BrushColor = color(0, 0, 0);
color BackgroundColor  = color(255, 255, 255) ;
int mouseWasX = 0 ;
int mouseWasY = 0 ;
boolean WasFocused = false;
boolean WasWasFocused = false ;

void setup() {
  size(700, 700);
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
  //print(focused + " " + mouseX + " " + mouseY + "\n");

  if (mousePressed && WasFocused == true && focused == true && WasWasFocused == true) {
    stroke(BrushColor);
    strokeWeight(BrushSize);
    line(mouseWasX, mouseWasY, mouseX, mouseY);

    //ellipse(mouseX, mouseY, BrushSize, BrushSize);
  }



  //rainbow
  noStroke();
  int rainbowheight= 60;
  int brushselectorwidth= 100;
  float numcolors = 255;
  colorMode(HSB, numcolors, 100, 100);
  float rectwidth = (width-brushselectorwidth)/numcolors ;
  int i = 0 ;
  while (i < numcolors) {
    color c = color(i, 99, 99);
    //if mousePressed && mouseX ==
    fill(c);                   
    rect(rectwidth*i, 0, rectwidth, rainbowheight );
    if (mouseX >= rectwidth*i && mouseX <= rectwidth*i + rectwidth && 
      mouseY >= 0 && mouseY <= rainbowheight) {
      BrushColor = c ;
    }
    i=i+1 ;
  }
  if ( mousePressed && mouseX > (width - brushselectorwidth) && mouseX < width && mouseY < rainbowheight) {
   float Xm=mouseX ;
   float Xc=width - brushselectorwidth/2;
   float Ym=mouseY;
   float Yc=rainbowheight/2;
   
    float a= abs(Xm-Xc);
    float b= abs(Ym-Yc);
    float c= sqrt(a*a+b*b);
    
    BrushSize =  round(2*c) ;
    
    
  }
  // brush sample
  fill(0, 0, 99); //white in hsb
  rect(width - brushselectorwidth, 0, brushselectorwidth, rainbowheight);
  fill(BrushColor);
  ellipse(width - brushselectorwidth/2, rainbowheight/2, BrushSize, BrushSize);

  colorMode(RGB, 255);


  mouseWasX = mouseX ;
  mouseWasY = mouseY ;
  WasWasFocused = WasFocused ;
  WasFocused = focused ;

  //saveFrame("betterthanphotoshop-######.png");
}

