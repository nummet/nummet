% Skript som reknar ut ein sum av areal av rektangel

% Talet på rektangel
n=input('Kor mange rektangel? ');
% Funksjonen
funk=@(x) x^3;

% Grenser
a=1;
b=3;

% Bestemmer h og initierer summen V
h=(b-a)/n;
V=0;

for i=0:(n-1)
    xi=a+i*h;
    V=V+h*funk(xi);
end

% Skriv summen V til skjerm
V
