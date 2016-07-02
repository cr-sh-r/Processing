import processing.sound.*;
int menushown = -1;
int buttonsHeight = 60;
boolean mouseWasPressed=false;
int numIcons = 6;
int frame = 0;
int menugap = 10;
SoundFile pushSound;

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

PImage base1 ;
PImage[] flowers ;

PImage texture1 ;
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
  base1 = loadImage("CACTI.png");

  flowers = new PImage[3];
  flowers[0] = loadImage("flower1.png");
  flowers[1] = loadImage("flower2.png");
  flowers[2] = loadImage("flower3.png");

  texture1 = loadImage("texture1.png");

  pots = new PImage[2];
  pots[0] = loadImage("pot1.png");
  pots[1] = loadImage("pot2.png");

  backgrounds = new PImage[2];
  backgrounds[0] = loadImage("background1.png");
  backgrounds[1] = loadImage("background2.png");

  rectMode(CORNER);
  pushSound = new SoundFile(this, "button.wav");
}


void draw() {
  background(10, 60, 10);

  boolean mouseClicked = (mousePressed == true && mouseWasPressed== false);
  boolean mouseUpClicked = (mousePressed == false && mouseWasPressed== true);


  fill(255, 255, 255);
  rect(0, height-buttonsHeight, width, buttonsHeight);

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
    float y = height-buttonsHeight ;
    float w = iconboxWidth;
    float h = buttonsHeight;

    boolean downButton = false;
    if (mouseX < x+w && mouseX > x && mouseY < y+h && mouseY > y ) {
      // hovered
      if (mouseClicked==true) {
        menushown=icon;
      } 
      if (mouseUpClicked == true && menushown==icon) {
        print(icon+"\n");
        pushSound.play();
        if (icon==5) {
          objects.clear();
        } else {
          CactusObject o = new CactusObject();
          
          o.x = 250 ;       //random(0, width);
          o.y = 70 ;        //random(0, height-buttonsHeight-20);
          o.w =300;
          o.h =300;
          
          if (icon==0) {
            int backgroundchooser = (int)random(0, backgrounds.length-0.0000000001);
            o.image = flowers[backgroundchooser];
            o.image = backgrounds[backgroundchooser];
          } else if (icon==1) {
            o.image = base1;
          } else if (icon==2) {
            int potchooser = (int)random(0, pots.length-0.0000000001);
            o.image = pots[potchooser];
          } else if (icon==3) {
            o.image = texture1;
          } else if (icon==4) {
            int flowerchooser = (int)random(0, flowers.length-0.0000000001);
            o.image = flowers[flowerchooser];
          }

          o.id = icon;
          objects.add(o);
        }
      }

      if (mousePressed==true) {
        // mouse down
        if (menushown==icon) {
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

    rect(xi, yi, wi, hi);

    if (menushown==icon) {
      //using menu
      if (icon==4) { // flowers
        float menuButtonHeight = hi;
        float menuButtonY= y-menugap-menuButtonHeight;

        int menuButtonIndex= 0;
        while (menuButtonIndex<flowers.length) {
          rect(xi, menuButtonY, wi, menuButtonHeight);
          image(flowers[menuButtonIndex], xi, menuButtonY, wi, menuButtonHeight);


          // hit test rect with mouse up clicked
          // create correct flower object


          menuButtonY = menuButtonY - menugap - menuButtonHeight;
          menuButtonIndex = menuButtonIndex + 1 ;
        }
      } else {
        float menuheight=300;
        rect(xi, y-menugap-menuheight, wi, menuheight);
      }
    }

    icon = icon + 1;
  }



  frame = frame + 1;
  if (mousePressed==false) {
    menushown=-1;
  }
  mouseWasPressed=mousePressed;
}