int[] DailyWordCount = {
  469, 
  1322, 
  1589,
  
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
    float rectWidth = width/30;
    float h = scale*DailyWordCount[i];
    fill(#DEA56B);
    rect(i*rectWidth, height-h, rectWidth, h);
    i=i+1;
  }
  line(0, height, width, 0);
}