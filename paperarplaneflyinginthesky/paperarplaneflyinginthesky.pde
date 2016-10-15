float glideRatio =2;
float paperx =130;
float papery =130;
PImage paperPlane ;

void setup() {
  size(600, 700);
  paperPlane = loadImage("plane2.png");
}

void draw() {
  background(#A3EDF5);
  paperx=paperx+glideRatio;
  papery=papery+1;
  stroke(0,0,0);
  fill(255,255,255);
  ellipse(paperx,papery, 11,11);
  image(paperPlane, paperx , papery, 100,100);
}