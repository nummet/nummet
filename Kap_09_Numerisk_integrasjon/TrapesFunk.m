function T=TrapesFunk(funk,a,b,n)

% Implementering av trapesmetoden for numerisk integrasjon.
% Integranden funk, grensene a og b, og oppdelinga n
% blir gitt som input.

% Steglengda
h=(b-a)/n;

% Bidrag frå endane
T=h/2*(funk(a)+funk(b));

% Resten av bidraga
for i=1:(n-1)
    xi=a+i*h;
    T=T+h*funk(xi);
end
