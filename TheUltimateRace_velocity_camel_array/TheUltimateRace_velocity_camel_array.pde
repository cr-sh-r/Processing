int frame = 0;
float ballSize = 14;
PImage tyler ;
float[] p = { 
  0, 0, 0, 0, 0, 0
};
float[] pinit = {
  6, 6, 6, 6, 6, 300,
}; 

float[] y = {
  300, 250, 200, 150, 100, 50
};

float[] v = { 
  0, 0, 0, 0, 0, 0
};
float[] vinit = {
  0.01, 1.72, 3.46, 5, 0, -400
};
float[] vs = { 
  0, 0, 0, 0, 0, 0
}; 

float[] a = { 
  0, 0, 0, 0, 0, 0
};
float[] ainit = {
  0.01, 0.0, -0.01, -0.03, 0, 0
};
float[] as = { 
  0, 0, 0, 0, 0, 0
};


void SetValues() {
  int i=0; 
  while (i < p.length) {
    p[i] = pinit[i];
    v[i] = vinit[i];
    a[i] = ainit[i];
    i=i+1;
  }

  frame = 0;
}

void keyPressed()
{
  if (key == '8') {
    SetValues();
  } else if (key== '9') {
    // saves and stops
    int i=0;
    while (i < v.length) {
      vs[i] = v[i];
      as[i] = a[i];
      v[i]=0;
      a[i]=0;
      i=i+1;
    }
  } else if (key == '7') {
    // restore from save
    int i=0;
    while (i < v.length) {
      v[i]=vs[i];
      a[i]=as[i];
      i=i+1;
    }
  } else if (key == 'q') {
    exit();
  }
}



void setup()
{
  SetValues();
  size(600, 600);
  ellipseMode(CENTER);
  tyler = loadImage("CACTI.png");
}

void draw()
{
  background(11, 142, 188);
  image(tyler, 0, 0, mouseX, mouseY);

  int i=0;
  while (i < p.length) {
    if ((p[i] <= ballSize/2 ) && (v[i]<0)) {
      //do nothing
    } else {
      float np =p[i]+v[i];
      if (np < ballSize/2 ) {
        np =ballSize/2;
      }
      p[i]= np;

      v[i]=v[i]+a[i];
    }
     ellipse(p[i], y[i], ballSize, ballSize);
    i=i+1;
  }

  line(590, 0, 590, 600);

  String message = "" + frame;
  fill(70, 0, 70); 
  textSize(13);
  float w= textWidth(message);
  text(message, mouseX-w/2, mouseY-5);
  frame = frame + 1;
  //ellipse(mouseX , mouseY , 20, 20);
}

