function S=SimpsonFunk(x,y)

% Funksjon som beregner integral ved Simpsons metode 
% for gitte x- og y-vektorer
% Partisjonen, gitt ved x-vektoren, må være regulær.

% Bestemmer steglengda og antall steg
h=x(2)-x(1);
n=length(x);

% Ende-bidrag:
S=h/3*(y(1)+y(n));

% Partalls-bidrag
for i=2:2:(n-1)
    S=S+h/3*4*y(i);
end

% Oddetalls-bidrag
for i=3:2:(n-2)
    S=S+h/3*2*y(i);
end


