% Skript som lagar plott av folkeveksten på 1900-talet

% Gir vektorar med år og folketal (i milliardar):
h=10;
Aar=1900:h:2000;
Folk=[1.65 1.75 1.86 2.07 2.30 2.52 3.02 3.70 4.45 5.30 6.12];

% Plottar folketal
figure(1)
plot(Aar,Folk,'k-','linewidth',2)
set(gca,'fontsize',15)
xlabel('År')
ylabel('Folketal [i milliardar]')

% Reknar ut dei deriverte
% For år 1900
FolkDeriv(1)=(Folk(2)-Folk(1))/h;
% For åra 1910-1990
for n=2:10
  FolkDeriv(n)=(Folk(n+1)-Folk(n-1))/(2*h);
end
% For år 2000
FolkDeriv(11)=(Folk(11)-Folk(10))/h;

% Plottar vekstfarten
figure(2)
% Reknar om til millionar/år
plot(Aar,FolkDeriv*1e3,'k-','linewidth',2)
set(gca,'fontsize',15)
xlabel('År')
ylabel('Vekst i folketal [i millionar per år]')

% Plottar relativ vekstfart
figure(3)
plot(Aar,FolkDeriv./Folk*100,'k-','linewidth',2)
set(gca,'fontsize',15)
xlabel('År')
ylabel('Relativ vekst [i prosent per år]')
