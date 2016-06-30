import processing.sound.*;

int menuHeight = 60;
boolean mouseWasPressed=false;
int numIcons = 6;
int frame = 0;
SoundFile pushSound;

color[] iconNotHoveredColors = { 
  color(255, 40, 30), // icon 0
  color(255, 81, 20), // icon 1
  color(255, 234, 45), // icon 2
  color(118, 255, 60), // icon 3
  color(48, 249, 255), // icon 4
  color(255, 255, 255), // icon 5
};
color[] iconMouseDownColors = {
  color(255, 0, 0), 
  color(255, 81, 0), 
  color(255, 234, 0), 
  color(118, 255, 0), 
  color(0, 249, 255), 
  color(0, 0, 0), 
};
color[] iconMouseUpColors = {
  color(55, 0, 0), 
  color(255, 1, 0), 
  color(55, 34, 0), 
  color(18, 255, 0), 
  color(28, 29, 60), 
  color(100, 100, 100), 
};

PImage base1 ;
PImage flower1 ;
PImage flower2;
PImage flower3;
PImage texture1 ;
PImage pot1 ;
PImage background1 ;


class CactusObject {
  float x;
  float y;
  float w;
  float h;
  int id;
  PImage image;
}

ArrayList<CactusObject> objects = new ArrayList<CactusObject>();

void setup() {
  size(800, 600);
  ellipseMode(CENTER);
  base1 = loadImage("CACTI.png");
  flower1 = loadImage("flower1.png");
  flower2 = loadImage("flower2.png");
  flower3 = loadImage("flower3.png");
  texture1 = loadImage("texture1.png");
  pot1 = loadImage("pot1.png");
  background1 = loadImage("background1.png");
  rectMode(CORNER);
  pushSound = new SoundFile(this, "button.wav");
}


void draw() {
  background(10, 60, 10);

  boolean mouseClicked = (mousePressed == true && mouseWasPressed== false);
  boolean mouseUpClicked = (mousePressed == false && mouseWasPressed== true);


  fill(255, 255, 255);
  rect(0, height-menuHeight, width, menuHeight);

  // main objects loop
  int layer =0;
  while (layer< numIcons) {

    int i = 0;
    while (i < objects.size ()) {
      CactusObject obj = objects.get(i);
      if (layer == obj.id) {
        image(obj.image, obj.x, obj.y, obj.w, obj.h );

        //String s = "hi" + obj.id;
        //text(s, obj.x, obj.y);
      }

      i = i + 1;
    }

    layer = layer + 1;
  }
  // buttons loop

  float iconboxWidth = ((float)width)/numIcons ;
  int icon = 0 ;
  while (icon < numIcons ) {
    float x = iconboxWidth*icon ;
    float y = height-menuHeight ;
    float w = iconboxWidth;
    float h = menuHeight;

    boolean downButton = false;
    if (mouseX < x+w && mouseX > x && mouseY < y+h && mouseY > y ) {
      // hovered
      if (mouseUpClicked == true) {
        print(icon+"\n");
        pushSound.play();
        if (icon==5) {
          objects.clear();
        } else {
          CactusObject o = new CactusObject();
          o.x = 250 ;       //random(0, width);
          o.y = 70 ;        //random(0, height-menuHeight-20);
          if (icon==0) {
            o.image = background1;
          } else if (icon==1) {
            o.image = base1;
          } else if (icon==2) {
            o.image = pot1;
          } else if (icon==3) {
            o.image = texture1;
          } else if (icon==4) {
            int flowerchooser = (int)random(1,3.999999999999999999999999);
            if (flowerchooser==1) {
              o.image = flower1;
            } else if (flowerchooser==2) {
              o.image = flower2;
            } else if (flowerchooser==3) {
              o.image = flower3;
            }
          }

          o.w =300;
          o.h =300;

          o.id = icon;
          objects.add(o);
        }
      }

      if (mousePressed==true) {
        // mouse down
        //fill(53, 98, 17);
        downButton = true;

        fill(iconMouseDownColors[icon]);
      } else {
        // mouse up
        fill(iconMouseUpColors[icon]);
      }
    } else {
      // not hovered
      fill(iconNotHoveredColors[icon]);
    }

    float buttonYOffset = 0;
    if (downButton==true) {
      buttonYOffset=2;
    }
    float bw = w/6;
    float bh =h/6;
    float xi = x+bw;
    float yi= y+bh+buttonYOffset;
    float wi = w-2*bw;
    float hi = h-2*bh;

    rect(xi, yi, wi, hi);

    icon = icon + 1;
  }

  //text(frame,mouseX,mouseY);
  //frame = frame + 1;

  mouseWasPressed=mousePressed;
}