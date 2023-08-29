% Skript som løyser likninga a x^2 + b x + c = 0.
% Vi er her berre interesserte i reelle løysingar.

% Les inn verdiane for a, b og c:
a=input('Gi verdien for a: ');
b=input('Gi verdien for b: ');
c=input('Gi verdien for c: ');

% Ser om det er ei førstegradslikning
if a==0
    x=-c/b
% Undersøker om vi har to, ei eller ingen reelle løysingar
elseif b^2-4*a*c<0              % Inga reell løysing
    disp('Inga reell løysing')
elseif b^2-4*a*c==0             % Ei løysing
    x=-b/(2*a)
else                            % To løysingar
    x1=(-b-sqrt(b^2-4*a*c))/(2*a)
    x2=(-b+sqrt(b^2-4*a*c))/(2*a)
end
