function M=GongeRekke(A,k,m)

% Funksjon som gongar ei rekke i ei matrise
% med eit tal ulik null
% Input:
% A: Matrisa som skal endrast.
% k: Talet det skal gongast med.
% m: Rekka som skal gongast med dette talet.

if abs(k)<1e-14
  disp('Talet får ikkje vere null.')
  return
end

M=A;
M(m,:)=k*A(m,:);
