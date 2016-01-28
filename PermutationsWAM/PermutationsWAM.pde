int countd;
void permute2 (String prefix, String first, String second) {
  print(countd + ": " + prefix);
  print(first) ;
  print(second);
  countd = countd + 1;
  print("\n");
  print(countd + ": " + prefix);
  print(second);
  print(first) ;
  countd = countd + 1;
  print("\n");
}


void permute3 (String prefix, String first, String second, String third) {
  permute2(prefix+first, second, third);
  permute2(prefix+second, first, third);
  permute2(prefix+third, first, second);
}

void permute4 (String prefix, String first, String second, String third, String fourth) {
  permute3(prefix+first, second, third, fourth);
  permute3(prefix+second, first, third, fourth);
  permute3(prefix+third, first, second, fourth);
  permute3(prefix+fourth, first, second, third);
}

void permute5 ( String first, String second, String third, String fourth, String fifth) {
  permute4(first,second,third,fourth,fifth);
  permute4(second,first,third,fourth,fifth);
  permute4(third,first,second,fourth,fifth);
  permute4(fourth,first,second,third,fifth);
  permute4(fifth,first,second,third,fourth);
}

void setup () { 
  countd = 1;
  permute2 ("", "a", "b") ;                                  //I know what ! means!
  print("\n\n");
  countd = 1;
  permute3 ("", "a", "b", "c");
  print("\n\n");
  countd = 1;
  permute4("", "a", "b", "c", "d");
  print("\n\n");
  countd = 1;
  permute5("a", "b", "c", "d", "e");

  exit();
}

