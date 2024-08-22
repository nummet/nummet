% Gir parametrar
v=1;                % Fart
D=20;               % Breidda
Smax=.9;            % Maksimal straum

% Oppdelinga brukt i integrala
N=input('Oppdeling for integrala: ');

% Modell for straumen
S=@(x) Smax*exp(-(x-D/2).^4/5000);

% Integranden i T1-integralet
T1Int=@(x) 1/sqrt(v^2-(S(x))^2);
% Bestemmer tida T1
T1=TrapesFunk(T1Int, 0, D, N);
% Skriv svaret til skjerm
if abs(imag(T1))>1e-8
  disp('Strategi 1 vil ikkje fungere')
else
  disp(['Strategi 1 tar ',num2str(T1),' sekund.'])
end

I=TrapesFunk(S,0,D,N);
theta=asin(I/(v*D));
% Bestemmer tida T2 og skriv svaret til skjerm
T2=D^2/(sqrt((v*D)^2-I^2));
disp(['Strategi 2 tar ',num2str(T2),' sekund.'])
% Skriv retninga theta, gitt i grader, til skjerm
disp(['Svømmeretninga blir ',num2str(theta*180/pi),...
' grader.'])
