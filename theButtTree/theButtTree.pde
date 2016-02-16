int[] colors = {
  0, 16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192
};


void setup() {
  size(600, 600 ) ;
}

void branch(int level, float xstart, float ystart, float l, float w, float degrees) {
  strokeWeight(w);
  float radians = (degrees/180) * PI;
  float xend = xstart + l*cos(radians);
  float yend = ystart + l*sin(radians);

  int index = level;//min(level,colors.length-1);
  if (index >= colors.length ) {
    index= colors.length-1;
  }
  int c = colors[index];
  stroke(c);
  line(xstart, ystart, xend, yend);

  if (w >= 1) {
    float branch_angle = 30;
    float length_scale = 0.7;
    float width_scale = (float)mouseX/width;
    float max_width_scale = 0.666 ;
    if (width_scale >= max_width_scale) {
      width_scale = max_width_scale;
    }
    branch(level+1, 
           xend, yend, 
           l*length_scale, 
           w*width_scale, 
           degrees+branch_angle);  
    branch(level+1, xend, yend, l*length_scale, w*width_scale, degrees-branch_angle);
  }
  
 // if (level > 2 ){
   if (w < 10 ){
    stroke(65,129,38);
    int g = (int)random(255);
    int r = (int)random(255);
     fill(r,g,38);  // g = 129 r=65
    ellipse(xend, yend, 10, 10);
  }
}

void draw() {
  randomSeed(0); 
  background(38, 116, 139); 
  stroke(77, 89, 23);
  fill(62, 46, 4);
  ellipse(width/2, height, 1.333*width, 0.333*width);
  float safey=mouseY;
  float max_safey= 0.37 * height;
  if (safey >= max_safey) {
    safey= max_safey;
  }
  float w = (30.0 / 500)* width ;
  branch( 0, width/2, height, safey, w, -90);

  strokeWeight(1);
  //line(0, 600, 600, 0);




  //ellipse(width/2, height/2, mouseX, mouseY);
}

