const int OUTPUTS[] = {22, 26, 30, 34, 38, 42, 46, 50};

const char FLAG[] = {'f', 'l', 'a', 'g', '{', 'h', 'a', 'r', 'd', 'w', 'a', 'r', 'e', 's', 'c', 'm', 'a', 'r', 'd', 'w', 'a', 'r', 'e', '}'};
const int flag_len = 24;
int flag_idx = 0;
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(22, OUTPUT);
  pinMode(26, OUTPUT);
  pinMode(30, OUTPUT);
  pinMode(34, OUTPUT);
  pinMode(38, OUTPUT);
  pinMode(42, OUTPUT);
  pinMode(46, OUTPUT);
  pinMode(50, OUTPUT);
}

void writeLetter(char c) {
  for (int i = 22, i < 51; i += 4, j++) {
    char tmp = c >> j;
    tmp &= 1;
    digitalWrite(i, j);
  }
}

// the loop function runs over and over again forever
void loop() {
  delay(70);
  writeLetter(FLAG[flag_idx]);
  flag_idx = (flag_idx + 1) % flag_len;
}
