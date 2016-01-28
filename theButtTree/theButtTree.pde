void setup() {
  size(600, 600) ;
}

void branch(float xstart, float ystart, float l, float w ,float degrees) {
  strokeWeight(w);
  
  
  float radians = (degrees/180) * PI;
  float xend = xstart + l*cos(radians);
  float yend = ystart + l*sin(radians);

  line(xstart, ystart, xend, yend);

  if (w >= 1) {
    float branch_angle = 30;
    float length_scale = 0.7;
    float width_scale = mouseX/600.0;
    branch(xend, yend, l*length_scale, w*width_scale, degrees+branch_angle);  
    branch(xend, yend, l*length_scale, w*width_scale, degrees-branch_angle);
  }
}

void draw() {
  background(77, 89, 23); 

  branch(300, 600, mouseY, 30, -90);

  strokeWeight(1);
  //line(0, 600, 600, 0);

  

  
   //ellipse(width/2, height/2, mouseX, mouseY);
}

