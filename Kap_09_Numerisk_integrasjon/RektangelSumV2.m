% Skript som estimerer eit integral på tre måtar:
% Venstre og høgre Riemann-sum og trapesmetoden

% Talet på rektangel
n=input('Kor mange rektangel? ');
% Funksjonen
funk=@(x) x^3;

% Grenser
a=1;
b=3;

% Bestemmer h og initierer summane V og H
h=(b-a)/n;
V=0;
H=0;

% Reknar ut venstresummen
for i=0:(n-1)
    xi=a+i*h;
    V=V+h*funk(xi);
end

% Reknar ut høgresummen
for i=1:n
    xi=a+i*h;
    H=H+h*funk(xi);
end


% Skriv summane V, H og T til skjerm
V
H
T=(V+H)/2                   % Trapessummen
