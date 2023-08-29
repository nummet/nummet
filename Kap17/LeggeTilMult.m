function M=LeggeTilMult(A,k,m,n)

% Funksjon som legg eit multiplum av
% ei rekke til ei anna rekke i ei matrise.
% Input:
% A: Matrisa som skal endrast.
% k: Talet det skal gongast med.
% m: Rekka som skal gongast med k og leggast til n.
% n: Rekka som vi skal legge til k gongar rekke m.

M=A;
M(n,:)=A(n,:)+k*A(m,:);
