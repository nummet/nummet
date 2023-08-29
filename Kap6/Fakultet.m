function F=Fakultet(n)

% Funksjon som reknar ut n! - n fakultet
% n må vere eit naturleg tal

F=1;        % Set startverdien til 1

for i=1:n
  F=F*i;    % Gongar med neste faktor
end
