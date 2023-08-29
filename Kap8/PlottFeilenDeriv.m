% Skript som plottar feilen i ulike estimat for
% den deriverte.
% Plottet blir laga med logaritmiske aksar.

% Funksjonen som skal deriverast
f=@(x) sin(x.^2);
% Den deriverte
fD=@(x) 2*x.*cos(x.^2);

% Argument-verdi
a=5;

% Eksakt svar
Derivert=fD(a);

% Vektor med ulike steglengder
%h=10.^[0:-1:-17];               % Grov oppdeling
h=.9.^[0:350];                   % Fin oppdeling

% Tre estimat: framover-, bakover- og midtpunktsformel
FramFormel=abs((f(a+h)-f(a))./h-Derivert);
BakFormel=abs((f(a)-f(a-h))./h-Derivert);
MidtFormel=abs((f(a+h)-f(a-h))./(2*h)-Derivert);

% Plottar feilen med logaritmiske aksar
loglog(h,FramFormel,'b-','linewidth',2)
hold on
loglog(h,BakFormel,'g--','linewidth',2)
loglog(h,MidtFormel,'m-.','linewidth',2)
hold off
set(gca,'fontsize',15)
set(gcf,'paperpositionmode','auto')