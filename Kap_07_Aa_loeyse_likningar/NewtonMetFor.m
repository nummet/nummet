% Skript som implementerer Newtons metode
2
3
4
% Bestemmer x_0
x=1;
5
6
7
8
9
for i=1:5
% Iterasjonsformel
x=x-(sqrt(x)-cos(x))/(1/(2*sqrt(x))+sin(x))
end