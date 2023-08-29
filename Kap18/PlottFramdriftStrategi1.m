% Plottar framdrifta som funksjon av tid.
% Skriptet TidKrysseElv må køyrast først.

% For strategi 1

tVektor=zeros(1,N);         % Allokerer vektor med t-verdiar
dx=D/(N-1);                 % Oppdelinga i x
xVektor=0:dx:D;             % Vektor med x-verdiar
% Reknar ut kor lang tid ein har brukt fram til kvar x-verdi
for n=1:N;
  tVektor(n)=TrapesFunk(T1Int, 0, xVektor(n), n);
end

% Plottar framdrifta mot tida
plot(tVektor,xVektor,'b-','linewidth',2)

% Plottar også tilsvarande plott for strategi 2 (rett linje)
hold on
t2Vektor=[0 T2];
plot(t2Vektor,v0*cos(theta)*t2Vektor,'r--','linewidth',2)
plot(T1,0,'bs')             % Markerar tida for strategi 1
plot(T2,0,'ro')             % Markerar tida for strategi 2
hold off
set(gca,'fontsize',15)
% Tekst på aksar og plott
xlabel('t [s]'), ylabel('x [m]')
legend('Strategi 1','Strategi 2')
