// CLEMENTINES 1st PROGRAM
//Tree Mountain place of GLORY
int season=0;
float time=0;
float last_time=0;





void keyPressed()
{
  if (key == '8') {
    season = season+1;
    if (season==4) {
      season=0;
    }
  }
}

void setup() 
{

  // strokeWeight(0); 

  size(600, 600); 
  rectMode(CENTER);
  ellipseMode(CENTER);                    //comments
}                                                //function

void rotrect( float angle, float x, float y, float w, float h )
{
  pushMatrix();
  translate(x, y);
  rotate(-(angle/360)*2*PI);   //pie is yummy!
  rect(0, 0, w, h);
  popMatrix();
}


void tree(float x, float y)             //parameter
{

  // trunky
  fill(116, 86, 57);
  rect (x, y+ 28, 12, 21);

  //branch2s
  rotrect(30, x-5, y+7, 6, 30);
  rotrect(-22.5, x+5, y+7, 6, 30);


  // mini branch
  rotrect(-40, x+15, y-10, 3, 10);

  // mini branch2
  rotrect(3, x+5, y-10, 3, 20);
  //  -----------------------------
  // mini branch3
  rotrect(40, x-15, y-10, 3, 20);

  // mini branch4
  rotrect(-5, x-5, y-10, 3, 20);



  //leaves

  if (season ==0) {
    fill(227, 112, 189 ); //spring
  } else if (season==1) {
    fill(100, 100, 10 ); // summer
  } else if (season==2) {
    fill(252, 188, 59 ); // fall
  }

  if (season !=3) {
    rect(x-15, y-10, 17, 17);          

    rect(x+8, y-13, 17, 17);          

    rect(x+15, y-5, 17, 17);          

    rect(x-5, y-15, 17, 17);
  }
}



void draw() 
{   

  time=millis()/1000.0;
  //sky
  background(11, 142, 188);


  // hill
  if (season ==3) {
    fill (255, 255, 255);
    } else {
    fill(38, 103, 1 );
  }
  ellipse(300, 600, 800, 200 );


  //sun
  fill(255, 196, 0);
  ellipse(500, 60, 90, 90  );     

  fill(0, 0, 0);
  ellipse(470, 54, 11, 11 );
  ellipse(530, 54, 11, 11);
  arc(500, 80, 40, 40, 0, PI, CHORD);
  //sun rays
  //fill(255,200,0);
  // rect(400,400, 100, 10);

  //spinnie
  //fill(mouseX, mouseY,128 );
  //rotrect(mouseX, 400,400, 100, 10);



  // ........trees.......                          


  tree(171, 541);





  tree(132, 510);


  tree(246, 573);


  tree(352, 547);

  tree(387, 472);

  tree(287, 496);

  tree(440, 543);

  tree(575, 541);

  tree(30, 575);     

  tree(500, 565);

  tree(99, 563);

  String message = "clem(; "+ mouseX +", "+ mouseY + "  " + time ;
  fill(70, 0, 70);
  text(message, mouseX-100, mouseY);

  // seasons text
  fill(0, 50, 100);
  ellipse(mouseX, mouseY, 10, 10);
  //spring
  if (season ==0) {        
    String spring = "spring" ;
    fill( 70, 0, 70);
    text(spring, 182, 83);
  } //summer
  else if (season ==1) {       
    String summer = "summer" ;
    fill( 70, 0, 70);
    text(summer, 182, 83);
  } //fall
  else if (season ==2) {
    String fall = "fall" ;
    fill( 70, 0, 70);
    text(fall, 182, 83);
  } //winter
  else if (season ==3) {
    String winter = "winter" ;
    fill( 70, 0, 70);
    text(winter, 182, 83);
  }
}
//if (season ==3)

