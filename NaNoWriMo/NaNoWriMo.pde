float GoalWordCount=12000;

int[] DailyWordCount = {
  //int(GoalWordCount/30),int(2*GoalWordCount/30),int(3*GoalWordCount/30),int(4*GoalWordCount/30),
  469,     //day  1
  1322,    //day  2
  1589,    //day  3
  2075,    //day  4
  2075,    //day  5
  2527,    //day  6
  2898,    //day  7
  3085,    //day  8
  3605,    //day  9
  3730,    //day  10
  4347,    //day  11
  5041,    //day  12
  5498,    //day  13
  
  
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