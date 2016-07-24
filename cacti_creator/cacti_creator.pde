import processing.sound.*;
int menuShown = -1;
int dockHeight = 60;
boolean mouseWasPressed=false;
int numButtons = 6;
int frame = 0;
int menuGap = 10;
boolean mouseClicked = false;
boolean mouseUpClicked = false;
SoundFile pushSound;
SoundFile clearSound;

color[] iconNotHoveredColors = { 
  color(255, 40, 30), // icon 0 background
  color(255, 81, 20), // icon 1 body
  color(255, 234, 45), // icon 2 pot
  color(118, 255, 60), // icon 3 texture
  color(48, 249, 255), // icon 4 flowers
  color(255, 255, 255), // icon 5 tools
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

PImage[] bases ;

PImage[] flowers ;

PImage[] textures ;
PImage[] pots ;

PImage[] backgrounds ;


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

  bases = new PImage[2];
  bases[0] = loadImage("base1.png");
  bases[1] = loadImage("base2.png");

  flowers = new PImage[3];
  flowers[0] = loadImage("flower1.png");
  flowers[1] = loadImage("flower2.png");
  flowers[2] = loadImage("flower3.png");

  textures = new PImage[2];
  textures[0]=loadImage("texture1.png");
  textures[1]=loadImage("texture1.2.png");

  pots = new PImage[2];
  pots[0] = loadImage("pot1.png");
  pots[1] = loadImage("pot2.png");

  backgrounds = new PImage[2];
  backgrounds[0] = loadImage("background1.png");
  backgrounds[1] = loadImage("background2.png");

  rectMode(CORNER);
  pushSound = new SoundFile(this, "button.wav");
  clearSound = new SoundFile(this, "clearButtonSound.mp3");
}

void handleIconMenu(int icon, float x, float y, float menuButtonWidth, float menuButtonHeight, PImage[] images) {
  float menuButtonY= y-menuGap-menuButtonHeight;
  int menuButtonIndex= 0;
  while (menuButtonIndex<images.length) {
    if (mouseX>x && mouseX<x+menuButtonWidth && mouseY>menuButtonY && mouseY< menuButtonY+menuButtonHeight) {
      stroke(255, 255, 255);
      if (mouseUpClicked==true) {
        // print(menuButtonIndex+"\n");
        CactusObject o = new CactusObject();
        pushSound.play();
        o.w = 300;
        o.x = width/2-o.w/2 ;    //random(0, width);
        o.h =300;
        o.y = (height-dockHeight)/2-o.h/2 ;   //random(0, height-dockHeight-20);
        o.image = images[menuButtonIndex];
        o.id = icon;
        objects.add(o);
      }
    } else {
      stroke(0, 0, 0);
    }
    rect(x, menuButtonY, menuButtonWidth, menuButtonHeight);
    image(images[menuButtonIndex], x, menuButtonY, menuButtonWidth, menuButtonHeight);
    menuButtonY = menuButtonY - menuGap - menuButtonHeight;
    menuButtonIndex = menuButtonIndex + 1 ;
  }
}

void draw() {
  background(10, 60, 10);

  mouseClicked = (mousePressed == true && mouseWasPressed== false);
  mouseUpClicked = (mousePressed == false && mouseWasPressed== true);

  //dock
  fill(255, 255, 255);
  rect(0, height-dockHeight, width, dockHeight);

  // main objects loop
  int layer =0;
  while (layer< numButtons) {

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

  float iconBoxWidth = ((float)width)/numButtons ;
  int icon = 0 ;
  while (icon < numButtons ) {
    float x = iconBoxWidth*icon ;
    float y = height-dockHeight ;
    float w = iconBoxWidth;
    float h = dockHeight;

    boolean downButton = false;
    if (mouseX < x+w && mouseX > x && mouseY < y+h && mouseY > y ) {
      // hovered
      if (mouseClicked==true) {
        menuShown=icon;
      } 
      if (mouseUpClicked == true && menuShown==icon) {
        print(icon+"\n");

        if (icon==5) {
          objects.clear();
          clearSound.play();
        }
      }

      if (mousePressed==true) {
        // mouse down
        if (menuShown==icon) {
          downButton = true;
          fill(iconMouseDownColors[icon]);
        } else {
          fill(iconNotHoveredColors[icon]);
        }
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
    stroke(0, 0, 0);
    rect(xi, yi, wi, hi);

    if (menuShown==icon) {
      //using menu
      if (icon==0) { 
        handleIconMenu( icon, xi, y, wi, hi, backgrounds);
      } else  if (icon==1) { 
        handleIconMenu( icon, xi, y, wi, hi, bases);
      } else  if (icon==2) { 
        handleIconMenu( icon, xi, y, wi, hi, pots);
      } else  if (icon==3) { 
        handleIconMenu( icon, xi, y, wi, hi, textures);
      } else  if (icon==4) { 
        handleIconMenu( icon, xi, y, wi, hi, flowers);
      } else {
        float menuheight=300;
        rect(xi, y-menuGap-menuheight, wi, menuheight);
      }
    }

    icon = icon + 1;
  }



  frame = frame + 1;
  if (mousePressed==false) {
    menuShown=-1;
  }
  mouseWasPressed=mousePressed;
}