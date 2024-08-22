% Skript som plottar to funksjonar

% Vektor med argumentverdiar
x=-5:1e-2:5;
% Vektorar med funksjonsverdiar
y=sin(exp(x));
z=exp(sin(x));

% Plottar funksjonane saman
plot(x,y,'b')
hold on
plot(x,z,'r')
hold off
