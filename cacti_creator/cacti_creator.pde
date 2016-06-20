int menuHeight = 60;
boolean mouseWasPressed=false;

class CactusObject {
  float x;
  float y;
  float w;
  float h;
  int id;
}

ArrayList<CactusObject> objects = new ArrayList<CactusObject>();

void setup() {
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

    rect(obj.x, obj.y, obj.w, obj.h);

    String s = "hi" + obj.id;
    text(s, obj.x, obj.y);

    i = i + 1;
  }

  // buttons loop
  float numIcons = 7;
  float iconboxWidth = width/numIcons ;
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
        o.x = random(0, width);
        o.y = random(0, height-menuHeight-20);
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
        fill(53, 98, 17);
        downButton = true;
      } else {
        fill(83, 103, 67);
      }
    } else {
      // not hovered
      fill(255, 255, 255);
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

