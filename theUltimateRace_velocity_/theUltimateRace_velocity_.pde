
int frame = 0;

float p1;
float v1 ,v1s;
float a1, a1s;

float p2;
float v2, v2s;
float a2, a2s;

float p3;
float v3, v3s;
float a3, a3s;

void SetValues() {
  p1=0;
  v1=0.01;
  a1=0.01;

  p2=0;
  v2=1.72;
  a2= 0.0;

  p3=0;
  v3=3.46;
  a3=-0.01;
  
  frame = 0;
}

void keyPressed()
{
  if (key == '8') {
    SetValues();
  } else if (key== '9') {

    v1s = v1;
    a1s = a1;

    v2s = v2;
    a2s = a2;

    v3s = v3;
    a3s = a3;
    
    v1=0;
    a1=0;

    v2=0;
    a2= 0.0;

    v3=0;
    a3=0;
  } else if (key == '7') {

    v1=v1s;
    a1=a1s;

    v2=v2s;
    a2= a2s;

    v3=v3s;
    a3=a3s;
  }
}



void setup()
{
  SetValues();
  size(600, 600);
  ellipseMode(CENTER);
}

void draw()
{
  background(11, 142, 188);

  ellipse(p1, 300, 12, 12);

  p1=p1+v1;
  v1=v1+a1;


  ellipse(p2, 260, 12, 12);

  p2=p2+v2;
  v2=v2+a2;


  ellipse(p3, 200, 12, 12);

  p3=p3+v3;
  v3=v3+a3;

  line(590,0,590,600);

  String message = "my dad is a jerk and a dog murderer! " + frame;
  fill(70, 0, 70);
  text(message, mouseX-100, mouseY);
  frame = frame + 1;
}

