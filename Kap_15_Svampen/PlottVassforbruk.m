% Skript som reknar ut vassforbruket som funksjon av tid for ein
% tank som blir tømd. 
% Profilen til tanken er gitt ved R(x) under.
% Vi tar utgongspunkt i Torrichellis lov, V'(t) = -k sqrt(h), for
% å bestemme høgda som funksjona av tid, som vi i sin tur brukar
% til å bestemme volumet av det som har runne ut ved integrasjon.

% Startkrav:
t0=0;
tf=1.9160;
h0=60;
t=t0; h=h0; Volum=0;

% Parametrar
Vtot=2.0547e+04;
% Konstanten k:
k=2*Vtot/(3*sqrt(h0));

% Profil-funksjon
R=@(x) 5+4/(1+exp((35-x)/1.5))*(sqrt(x)-sqrt(30))^2;
% Høgresida i differensaillikninga h'=F(h)
F=@(x) -k*sqrt(x)/(pi*R(x)^2);

% Oppdeling i Eulers-metode og Riemann-integrasjon
N=input('Oppdelinga: ');
dt=(tf-t0)/N;

% Vektorar til plotting
tVektor=t0:dt:tf;
hVektor=zeros(1,N+1); hVektor(1)=h0;
VolumVektor=zeros(1,N+1); VolumVektor(1)=h0;

for n=1:N
  h=h+F(h)*dt;                  % Eulers meotde
  hVektor(n+1)=h;
  Volum=Volum+k*sqrt(h)*dt;     % Oppdaterar volum ved eit Riemann-integral
  VolumVektor(n+1)=Volum;
end

% Plottar resultatet
plot(tVektor,real(VolumVektor)/1e4,'b-','linewidth',2)


% Plottar tilsvarende funksjon for sylindertårnet
H=60;                           % Høgde
% Funksjon for vasshøgda i sylindertårn
SylFunk=@(t) (sqrt(H)-k*H/2/Vtot*t).^2;
xx=0:1e-2:3;                    % Tids-vektor
hold on
% Volum: Høgd gange grunnflate, grunnflata er totalvolum delt å høgda
plot(xx,(Vtot-SylFunk(xx)*Vtot/H)/1e4,'r-','linewidth',2)

% Linje som markerar totalvolumet
plot([0 3], [Vtot Vtot]/1e4, 'k--','linewidth',1.2)
% Forklarar grafane
legend('Svampen','Sylinder','Totalt volum','location','southeast')
% Tekst på aksane
xlabel('Tid [døgn]'); ylabel('Volum [10^4 m^3]')
% Justerar aksane
axis([0 3 0 1.1*Vtot/1e4])
% Justerar skriftstorleiken
set(gca,'fontsize',15)
hold off

