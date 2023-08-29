function M=MaksFunk(x)

% Funksjon som finn det største elementet i vektoren x

% tilordnar M - det foreløpig største elementet
M=x(1);

% for-løkke som går gjennom x
for xElement=x
  if xElement>M
% om elementet er større enn M, oppdaterer vi M
    M=xElement;
  end
end
