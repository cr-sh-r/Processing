float GoalWordCount=12000;

int[] DailyWordCount = {
  //int(GoalWordCount/30),int(2*GoalWordCount/30),int(3*GoalWordCount/30),int(4*GoalWordCount/30),
  469, 
  1322, 
  1589,
  2075,
  2075,
  2527,
  2898,
  3085,
  3605,
  3730,
  4347,
  5041,
  
  
};

void setup() {
  size(700, 400);
}

void draw() {
  background(255, 255, 255);
  float stepWidth = width/30;
  float scale =height/GoalWordCount;
  int i =0;
  while (i<DailyWordCount.length) {
    float rectWidth = 0.1*stepWidth;
    float h = scale*DailyWordCount[i];
    fill(#DEA56B);
    rect(i*stepWidth+stepWidth/2-rectWidth/2, height-h, rectWidth, h);
    i=i+1;
  }
  line(stepWidth/2,height-scale*GoalWordCount/30, 29.5*stepWidth, height-scale*GoalWordCount);
}