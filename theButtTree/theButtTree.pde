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

//  if (level%2 == 1) {
//    stroke(255) ;
//  } else {
//    stroke(0);

//  }
  
  int index = level;//min(level,colors.length-1);
  if (index >= colors.length ){
    index= colors.length-1;
  }
  int c = colors[index];
  stroke(c);
  line(xstart, ystart, xend, yend);

  if (w >= 1) {
    float branch_angle = 30;
    float length_scale = 0.7;
    float width_scale = mouseX/(float)width;
    float max_width_scale = 0.775 ;
    if (width_scale >= max_width_scale) {
      width_scale = max_width_scale;
    }
    branch(level +1, xend, yend, l*length_scale, w*width_scale, degrees+branch_angle);  
    branch(level+1, xend, yend, l*length_scale, w*width_scale, degrees-branch_angle);
  }
}

void draw() {
  background(77, 89, 23); 
 stroke(77, 89, 23);
  fill(106,69,1);
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

