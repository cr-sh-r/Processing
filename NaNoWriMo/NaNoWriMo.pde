int[] DailyWordCount = {
  //400,800,1200,1600,
  469, 
  1322, 
  1589,
  2075,
  
};
float GoalWordCount=12000;
void setup() {
  size(700, 400);
}

void draw() {
  background(255, 255, 255);
  float scale =height/GoalWordCount;
  int i =0;
  while (i<DailyWordCount.length) {
    float stepWidth = width/30;
    float rectWidth = 0.5*stepWidth;
    float h = scale*DailyWordCount[i];
    fill(#DEA56B);
    rect(i*stepWidth+stepWidth/2-rectWidth/2, height-h, rectWidth, h);
    i=i+1;
  }
  line(0, height, width, 0);
}