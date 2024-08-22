% Skript som les inn eit tal og avgjer om talet er
% positivt eller negativt, om det er eit heiltal eller
% ikkje og - dersom det er eit heiltal - om det er eit
% partal eller eit oddetal

% Les inn tal frå kommandovindauga
x=input('Gi eit tal: ');

% Avgjer om talet er positivt eller negativt
if x<0
  disp('Talet er negativt')
else
  disp('Talet er positivt eller null')
end

% Avgjer om talet er eit heiltal
if round(x)~=x
  disp('Talet er ikkje eit heiltal')
else
% Avgjer om talet er eit partal
  if round(x/2)==x/2
    disp('Talet er eit partal')
  else
    disp('Talet er eit oddetal')
  end
end
