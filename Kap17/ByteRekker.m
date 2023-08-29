function M=ByteRekker(A,m,n)

% Funksjon som byter om to rekker i ei matrise
% Input:
% A: Matrisa som skal endrast.
% m og n: Rekkene som skal bytast om.

M=A;
M([m n],:)=A([n m],:);
