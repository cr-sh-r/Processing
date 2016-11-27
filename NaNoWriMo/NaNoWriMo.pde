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
  5708,    //day  14
  6307,    //day  15
  6307,    //day  16
  6874,    //day  17
  6874,    //day  18
  7490,    //day  19
  7490,    //day  20
  8760,    //day  21
  9075,    //day  22
  9491,    //day  23
  9491,    //day  24
  9491,    //day  25
  10374,   //day  26
  
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
  
  int curentWordCount = DailyWordCount[DailyWordCount.length-1];
  String curentcount = "Word Count:"+curentWordCount;
  text(curentcount,50,30);
  
  int wordGoal = int(DailyWordCount.length*GoalWordCount/30);
  String sWordGoal = "Todays Goal:"+wordGoal;
  text(sWordGoal,50,50);
  //how much above? or below
}