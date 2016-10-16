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
  //imageMode(CENTER);
  image(paperPlane,paperx-paperPlane.width/2,papery-paperPlane.height/2, paperPlane.width,paperPlane.height );

  //rect(paperx-paperPlane.width/2,papery-paperPlane.height/2, paperPlane.width,paperPlane.height );
  ellipse(paperx,papery, 11,11);
}