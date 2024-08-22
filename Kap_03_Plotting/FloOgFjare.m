x=0:0.1:24;
y=3.2*sin(pi/6*(x-3));
plot(x,y,'linewidth',3)
set(gca,'fontsize',15)
xlabel('t [timra]'); ylabel('T [meter]')
hold on
plot([0 24],[-1 -1],'k-')
plot([6 18],[3.2 3.2],'ro','linewidth',2)
plot([2.39 9.61 14.39 21.61],-ones(1,4),'gd','linewidth',2)
legend('T(t)','y=-1','Flo','T(t)=-1')
axis([0 27 -4 4])
hold off
