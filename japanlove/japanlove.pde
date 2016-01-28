/**
 * Blur Filter
 * 
 * Change the default shader to apply a simple, custom blur filter.
 * 
 * Press the mouse to switch between the custom and default shader.
 */

PShader blur;

void setup() {
  size(640, 360, P2D);
  blur = loadShader("blur.glsl"); 
  //stroke(0, 0, 0);
  noStroke();
  rectMode(CENTER);
}

void draw() {
  filter(blur);  
  fill(255,255,255);
  rect(mouseX, mouseY, 30, 20);
  fill (255, 0, 0);
  ellipse(mouseX, mouseY, 10, 10);
}

