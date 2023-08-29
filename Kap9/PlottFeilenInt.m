% Skript som plottar feilen i eit estimat for ein
% Riemann-sum, trapesmetoden og Simpsons metode.

% Spesifiserer integrand, grenser og eksakt svar
funk=@(x) x*sin(x^2);
a=-1; b=3;
Fasit=(cos(1)-cos(9))/2;

% Lagar vektor med n-verdiar
nStart=2;
nSteg=10;
nSlutt=100000;
nVektor=nStart:nSteg:nSlutt;
hVektor=(b-a)./nVektor;

% Lagar vektorar med estimat
indeks=1;
for n=nVektor
  Vvektor(indeks)=RiemannFunk(funk,a,b,n);
  Tvektor(indeks)=TrapesFunk(funk,a,b,n);
  Svektor(indeks)=SimpsonFunk(funk,a,b,n);
  indeks=indeks+1;
end

% Plottar feilen
loglog(hVektor,abs(Vvektor-Fasit),'b-','linewidth',2)
hold on
loglog(hVektor,abs(Tvektor-Fasit),'r--','linewidth',2)
loglog(hVektor,abs(Svektor-Fasit),'k-.','linewidth',2)
hold off
set(gca,'fontsize',15)
legend('Venstre Riemann-sum','Trapesmetoden','Simpsons metode')
