nata=input('ingrese tiempo de natacion')
atle=input('ingrese tiempo que corrió')
cicli=input('ingrse tiempo de ciclismo')
natacion=int((nata[0]+nata[1])*60+int(nata[3]+nata[4]))
atletismo=int((atle[0]+atle[1])*60+int(atle[3]+atle[4]))
ciclismo=int((cicli[0]+cicli[1])*60+int(cicli[3]+cilci[4]))
total=natacion+ciclismo+atletismo
x=diumod(total,3600)
total_hh=x[0]
y=diumod(x[1],60)
total_mm=y[0]
total_ss=y[1]
tiempo_max=max(natacion,ciclismo,atletismo)
tiempo_min=min(natacion,ciclismo,atletismo)
tiempo_prom=total/3
tiempo_prom=roun(tiempo_prom,2)
#falta el print
