size(0,100);
path clock=E..N..W..S..cycle;
path hand=(0,0)--(0,0.9);
draw(clock);
draw(rotate(0/-1000)*hand);
draw(rotate(270000/-1000)*hand);
currentpicture=shift(3,0)*currentpicture;
draw(clock);
draw(rotate(180000/-1000)*hand);
draw(rotate(270000/-1000)*hand);