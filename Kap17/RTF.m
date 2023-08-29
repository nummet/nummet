function M=RTF(A)

% Funksjon som rekkereduserer ei matrise til redusert
% trappeform. Funksjonen brukr først funksjonsfila
% Trappeform, som reduserer matrisa til ei trappeform.
% Kvart steg i denne prosessen blir utført i funksjonsfila
% Trappesteg. Når matrisa er redusert til trappeform,
% går vi vidare til redusert trappeform med funksjonen
% Bakoverfase. Fleire av desse funksjonsfilene brukar
% funksjonfiler som implementerer dei tre elementære
% rekkeoperasjonane. Desse er:
% ByteRekker
% GongeRekke
% LeggeTilMult

% Får matrisa på trappeform og finn søylene med leiande tal
[M LeiarVektor]=Trappeform(A);

% Finn talet på leiande tal
l=length(LeiarVektor);

% Viss der er leiande tal: Utfører "bakoverfasen",
% som går ut på å sette alle leiande tal til 1 og
% gjere alle tal over desse til null.
if l>0
  M=Bakoverfase(M,LeiarVektor);
end
