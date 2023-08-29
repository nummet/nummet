% Plottar svømmebanen.
% Skriptet TidKrysseElv må køyrast først.

% For strategi 2

yVektor=zeros(1,N);         % Allokerer vektor med y-verdiar
dx=D/(N-1);                 % Oppdelinga i x
xVektor=0:dx:D;             % Vektor med x-verdiar
% Reknar ut kor lang tid ein har brukt fram til kvar x-verdi
for n=1:N;
  yVektor(n)=xVektor(n)*tan(theta)-...
      1/(v*cos(theta))*TrapesFunk(S, 0, xVektor(n), n);
end

% Plottar banen gjennom elva
plot(xVektor,yVektor,'r-','linewidth',2)

% Plottar også tilsvarande plott for strategi 1 (rett linje)
hold on
plot([0 D],[0 0],'b--','linewidth',2)
hold off
set(gca,'fontsize',15)
xlabel('x [m]'), ylabel('y [m]')
legend('Strategi 2','Strategi 1')
