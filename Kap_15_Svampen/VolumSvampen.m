% Skript som brukar trapesmetoden til å rekne ut volumet
% av eit vasstårn ut frå ein gitt modell for profilen

% Grenser (høgda)
a=0;b=60;

% Profil på tårn
R=@(x) 5+4./(1+exp((35-x)/1.5)).*(sqrt(x)-sqrt(30)).^2;
% Integrand
f=@(x) R(x).^2;

% Oppdeling
n=input('Gi oppdelinga n: ');
h=(b-a)/n;                  % Steglengda

% Bidrag frå endane
T=h/2*(f(a)+f(b));

% Resten av bidraga
for i=1:(n-1)
    xi=a+i*h;
    T=T+h*f(xi);
end

% Skriv volumet til skjerm
Volum=pi*T