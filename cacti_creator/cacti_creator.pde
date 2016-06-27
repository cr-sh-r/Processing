int menuHeight = 60;
boolean mouseWasPressed=false;

PImage base1 ;
PImage flower1 ;
PImage texture1 ;
PImage pot1 ;
PImage background1 ;
class CactusObject {
  float x;
  float y;
  float w;
  float h;
  int id;
}

ArrayList<CactusObject> objects = new ArrayList<CactusObject>();

void setup() {

  size(600, 600);
  ellipseMode(CENTER);
  base1 = loadImage("CACTI.png");
  flower1 = loadImage("flower1.png");
  texture1 = loadImage("texture1.png");
  pot1 = loadImage("pot1.png");
  background1 = loadImage("background1.png");
  size(800, 600);
  rectMode(CORNER);
}


void draw() {
  background(10, 60, 10);

  boolean mouseClicked = (mousePressed == true && mouseWasPressed== false);
  boolean mouseUpClicked = (mousePressed == false && mouseWasPressed== true);


  fill(255, 255, 255);
  rect(0, height-menuHeight, width, menuHeight);

  // main objects loop
  int i = 0;
  while (i < objects.size ()) {
    CactusObject obj = objects.get(i);
    int cactiplace =300;

    if (obj.id==0) {
      fill(255, 0, 0);
      image(background1, obj.x, obj.y, cactiplace, cactiplace);
    } else if (obj.id==1) {
      fill(255, 81, 0);
      image(base1, obj.x, obj.y, cactiplace, cactiplace );
    } else if (obj.id==2) {
      fill(255, 234, 0);
      image(pot1, obj.x, obj.y, cactiplace, cactiplace );
    } else if (obj.id==3) {
      fill(118, 255, 0);
      image(texture1, obj.x, obj.y, cactiplace, cactiplace );
    } else if (obj.id==4) {
      fill(0, 249, 255);
      image(flower1, obj.x, obj.y, cactiplace, cactiplace );
    } else if (obj.id==5) {
      //fill(0, 30, 255);
    } else if (obj.id==6) {
      //fill(207, 0, 255);
    } else {
      rect(obj.x, obj.y, obj.w, obj.h);
    }
    String s = "hi" + obj.id;
    text(s, obj.x, obj.y);

    i = i + 1;
  }

  // buttons loop
  int numIcons = 5;
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

        CactusObject o = new CactusObject();
        o.x = 250;       //random(0, width);
        o.y = 70;        //random(0, height-menuHeight-20);
        if (icon==0) {
          o.w = 20;
          o.h = 20;
        } else if (icon==1) {
          o.w = 30;
          o.h = 30;
        } else if (icon==2) {
          o.w = 40;
          o.h = 60;
        } else {
          o.w = 200;
          o.h = 200;
        }

        o.id = icon;
        objects.add(o);
      }
      if (mousePressed==true) {
        //fill(53, 98, 17);
        downButton = true;

        if (icon==0) {
          fill(255, 0, 0);
        } else if (icon==1) {
          fill(255, 81, 0);
        } else if (icon==2) {
          fill(255, 234, 0);
        } else if (icon==3) {
          fill(118, 255, 0);
        } else if (icon==4) {
          fill(0, 249, 255);
        } else if (icon==5) {
          fill(0, 30, 255);
        } else if (icon==6) {
          fill(207, 0, 255);
        }
      } else {
        if (icon==0) {
          fill(55, 0, 0);
        } else if (icon==1) {
          fill(255, 1, 0);
        } else if (icon==2) {
          fill(55, 34, 0);
        } else if (icon==3) {
          fill(18, 255, 0);
        } else if (icon==4) {
          fill(28, 29, 60);
        } else if (icon==5) {
          fill(0, 30, 55);
        } else if (icon==6) {
          fill(27, 0, 55);
        }
      }
    } else {
      // not hovered
      if (icon==0) {
        fill(255, 40, 30);
      } else if (icon==1) {
        fill(255, 81, 20);
      } else if (icon==2) {
        fill(255, 234, 45);
      } else if (icon==3) {
        fill(118, 255, 60);
      } else if (icon==4) {
        fill(48, 249, 255);
      } else if (icon==5) {
        fill(56, 30, 255);
      } else if (icon==6) {
        fill(207, 57, 255);
      }
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

  mouseWasPressed=mousePressed;
}

