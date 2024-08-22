function F=DeltForskrift(x)

% Funsjonen f(x) der f=cos(pi*x) + 2 når x<0 og
% x^2-2 når x er større eller lik 2.
% Funksjonen tar berre skalarar som input.

if x<2
  F=cos(pi*x)+2;
else
  F=x^2-2;
end
