function X=TredjeGradFunk(a,b,c,d)

% Funksjon som løyser tredjegradslikninga
% ax^3+bx^2+cx+d=0.
% Input er koeffisientane a, b, c, d.
% Funksjonen gir dei tre løysingane x_1, x_2 og x_3
% som output.

% Kontrollerer at det faktisk er ei tredjegradslikning
if a==0
   disp('Dette er ikkje ei tredjegradslikning')
   return
end

% Tilordnar parametrar som inngår i løysingsformelen
% Vektor med u_1, u_2 og u_3:
u=[1 (-1+sqrt(3)*i)/2 (-1-sqrt(3)*i)/2];
Delta0=b^2-3*a*c;
Delta1=2*b^3-9*a*b*c+27*a^2*d;
% Stor C. NB! Ulik input-variabelen c.
C=((Delta1+sqrt(Delta1^2-4*Delta0^3))/2)^(1/3);

% Løysinga
if abs(Delta0)<1e-14 & abs(Delta1)<1e-14
% Spesialtilfelle: 3 like røter
  X=-b/(3*a);
elseif abs(Delta0)<1e-14 & Delta1<0
% Endrar C i dette tilfellet
  C=Delta1^(1/3);
  X=-1/(3*a)*(b+u*C+Delta0./(u*C));
else
  X=-1/(3*a)*(b+u*C+Delta0./(u*C));
end
