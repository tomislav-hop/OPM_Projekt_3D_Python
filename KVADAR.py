from visual import*

scene = display(title='F1 - Prikazi pomoc || F2 - Sakrij pomoc', width=900, height=900)

#koordinatni sustav
curve(pos=[(-10,0,0),(10,0,0)],radius = 0.05, color=color.white)
curve(pos=[(0,-10,0),(0,10,0)],radius = 0.05, color=color.white)
curve(pos=[(0,0,-10),(0,0,10)],radius = 0.05, color=color.white)

#tocke
for x in range(1,10):
    sphere(pos=vector(x,0,0),radius=0.06, color=color.red)
    sphere(pos=vector(0,x,0),radius=0.06, color=color.red)
    sphere(pos=vector(0,0,x),radius=0.06, color=color.red)
    sphere(pos=vector(-x,0,0),radius=0.06, color=color.red)
    sphere(pos=vector(0,-x,0),radius=0.06, color=color.red)
    sphere(pos=vector(0,0,-x),radius=0.06, color=color.red)

#oznake tocaka
label(pos=(10.3,0,0), text = 'X',box = 0,height=30,color=color.red)
label(pos=(1,0,-0.3),text="1",opacity=0,box=0,height=20 ,color=color.red)

label(pos=(0,10.3,0), text = 'Y',box = 0,height=30,color=color.red)
label(pos=(0,1,-0.3),text="1",opacity=0,box=0,height=20 ,color=color.red)

label(pos=(0,0,10.3), text = 'Z',box = 0,height=30,color=color.red)
label(pos=(0,-0.3,1),text="1",opacity=0,box=0,height=20 ,color=color.red)

#kvadar
convex(pos=[(1,1,1), (1,3,1), (4,1,1),(1,1,0),(4,3,0),(4,1,0),(1,3,0),(4,3,1)], color=color.green)
label(pos=(1,1,1.2),text="(1,1,1)",box=0,opacity=0,color=color.yellow)
label(pos=(1,3,1.2),text="(1,3,1)",box=0,opacity=0,color=color.yellow)
label(pos=(4,1,1.2),text="(4,1,1)",box=0,opacity=0,color=color.yellow)
label(pos=(4,3,1.2),text="(4,3,1)",box=0, opacity=0,color=color.yellow)
label(pos=(1,1,-0.2),text="(1,1,0)",box=0,opacity=0,color=color.yellow)
label(pos=(4,3,-0.2),text="(4,3,0)",box=0,opacity=0,color=color.yellow)
label(pos=(4,1,-0.2),text="(4,1,0)",box=0,opacity=0,color=color.yellow)
label(pos=(1,3,-0.2),text="(1,3,0)",box=0,opacity=0,color=color.yellow)
points(pos=[(1,1,1), (1,3,1), (4,1,1),(1,1,0),(4,3,0),(4,1,0),(1,3,0),(4,3,1)],size=6, color=color.yellow)

#1) Translacija za vektor v = (-3, -2, 1)
kvadar1 = convex(pos=[(-2,-1,2), (-2,1,2), (1,-1,2),(-2,-1,1),(1,1,1),(1,-1,1),(-2,1,1),(1,1,2)], color=color.blue, visible=0)
k1=label(pos=(-2,-1,2.2),text="(-2,-1,2)",box=0,opacity=0,color=color.cyan, visible=0)
k11=label(pos=(-2,1,2.2),text="(-2,1,2)",box=0,opacity=0,color=color.cyan, visible=0)
k111=label(pos=(1,-1,2.2),text="(1,-1,2)",box=0,opacity=0,color=color.cyan, visible=0)
k1111=label(pos=(1,1,2.2),text="(1,1,2)",box=0, opacity=0,color=color.cyan, visible=0)
k11111=label(pos=(-2,-1,1.2),text="(-2,-1,1)",box=0,opacity=0,color=color.cyan, visible=0)
k111111=label(pos=(1,1,1.5),text="(1,1,1)",box=0,opacity=0,color=color.cyan, visible=0)
k1111111=label(pos=(1,-1,1.2),text="(1,-1,1)",box=0,opacity=0,color=color.cyan, visible=0)
k11111111=label(pos=(-2,1,1.2),text="(-2,1,1)",box=0,opacity=0,color=color.cyan, visible=0)
k111111111=points(pos=[(-2,-1,2), (-2,1,2), (1,-1,2),(-2,-1,1),(1,1,1),(1,-1,1),(-2,1,1),(1,1,2)],size=6, color=color.cyan, visible=0)
k1111111111=label(pos=(-3, -3, 1),text="Translacija za vektor v = (-3, -2, 1)",box=0,opacity=0,color=color.yellow, visible=0)

#2) Rotacija oko osi x za 180 stupnjeva
#Q) Zrcaljenje s obzirom na os x
kvadar2 = convex(pos=[(1,-1,-1), (1,-3,-1), (4,-1,-1),(1,-1,-0),(4,-3,-0),(4,-1,-0),(1,-3,-0),(4,-3,-1)], color=color.blue, visible=0)
k2=label(pos=(1,-1,-1.2),text="(1,-1,-1)",box=0,opacity=0,color=color.cyan, visible=0)
k22=label(pos=(1,-3,-1.2),text="(1,-3,-1)",box=0,opacity=0,color=color.cyan, visible=0)
k222=label(pos=(4,-1,-1.2),text="(4,-1,-1)",box=0,opacity=0,color=color.cyan, visible=0)
k2222=label(pos=(4,-3,-1.2),text="(4,-3,-1)",box=0, opacity=0,color=color.cyan, visible=0)
k22222=label(pos=(1,-1,0.2),text="(1,-1,-0)",box=0,opacity=0,color=color.cyan, visible=0)
k222222=label(pos=(4,-3,0.2),text="(4,-3,-0)",box=0,opacity=0,color=color.cyan, visible=0)
k2222222=label(pos=(4,-1,0.2),text="(4,-1,-0)",box=0,opacity=0,color=color.cyan, visible=0)
k22222222=label(pos=(1,-3,0.2),text="(1,-3,-0)",box=0,opacity=0,color=color.cyan, visible=0)
k222222222=points(pos=[(1,-1,-1), (1,-3,-1), (4,-1,-1),(1,-1,-0),(4,-3,-0),(4,-1,-0),(1,-3,-0),(4,-3,-1)],size=6, color=color.cyan, visible=0)

#3) Rotacija oko osi y za 180 stupnjeva
#W) Zrcaljenje s obzirom na os y
kvadar3 = convex(pos=[(-1,1,-1), (-1,3,-1), (-4,1,-1),(-1,1,-0),(-4,3,-0),(-4,1,-0),(-1,3,-0),(-4,3,-1)], color=color.blue, visible=0)
k3=label(pos=(-1,1,-1.2),text="(-1,1,-1)",box=0,opacity=0,color=color.cyan, visible=0)
k33=label(pos=(-1,3,-1.2),text="(-1,3,-1)",box=0,opacity=0,color=color.cyan, visible=0)
k333=label(pos=(-4,1,-1.2),text="(-4,1,-1)",box=0,opacity=0,color=color.cyan, visible=0)
k3333=label(pos=(-4,3,-1.2),text="(-4,3,-1)",box=0, opacity=0,color=color.cyan, visible=0)
k33333=label(pos=(-1,1,-0.2),text="(-1,1,-0)",box=0,opacity=0,color=color.cyan, visible=0)
k333333=label(pos=(-4,3,-0.2),text="(-4,3,-0)",box=0,opacity=0,color=color.cyan, visible=0)
k3333333=label(pos=(-4,1,-0.2),text="(-4,1,-0)",box=0,opacity=0,color=color.cyan, visible=0)
k33333333=label(pos=(-1,3,-0.2),text="(-1,3,-0)",box=0,opacity=0,color=color.cyan, visible=0)
k333333333=points(pos=[(-1,1,-1), (-1,3,-1), (-4,1,-1),(-1,1,-0),(-4,3,-0),(-4,1,-0),(-1,3,-0),(-4,3,-1)],size=6, color=color.cyan, visible=0)

#4) Rotacija oko osi z za 180 stupnjeva
#E) Zrcaljenje s obzirom na os z
kvadar4 = convex(pos=[(-1,-1,1), (-1,-3,1), (-4,-1,1),(-1,-1,0),(-4,-3,0),(-4,-1,0),(-1,-3,0),(-4,-3,1)], color=color.blue, visible=0)
k4=label(pos=(-1,-1,1.2),text="(-1,-1,1)",box=0,opacity=0,color=color.cyan, visible=0)
k44=label(pos=(-1,-3,1.2),text="(-1,-3,1)",box=0,opacity=0,color=color.cyan, visible=0)
k444=label(pos=(-4,-1,1.2),text="(-4,-1,1)",box=0,opacity=0,color=color.cyan, visible=0)
k4444=label(pos=(-4,-3,1.2),text="(-4,-3,1)",box=0, opacity=0,color=color.cyan, visible=0)
k44444=label(pos=(-1,-1,0.2),text="(-1,-1,0)",box=0,opacity=0,color=color.cyan, visible=0)
k444444=label(pos=(-4,-3,0.2),text="(-4,-3,0)",box=0,opacity=0,color=color.cyan, visible=0)
k4444444=label(pos=(-4,-1,0.2),text="(-4,-1,0)",box=0,opacity=0,color=color.cyan, visible=0)
k44444444=label(pos=(-1,-3,0.2),text="(-1,-3,0)",box=0,opacity=0,color=color.cyan, visible=0)
k444444444=points(pos=[(-1,-1,1), (-1,-3,1), (-4,-1,1),(-1,-1,0),(-4,-3,0),(-4,-1,0),(-1,-3,0),(-4,-3,1)],size=6, color=color.cyan, visible=0)

#5) Homotetija za faktor k=-2 sa centrom u ishodistu
kvadar5 = convex(pos=[(-2,-2,-2), (-2,-6,-2), (-8,-2,-2),(-2,-2,0),(-8,-6,0),(-8,-2,0),(-2,-6,0),(-8,-6,-2)], color=color.blue, visible=0)
k5=label(pos=(-2,-2,-2.2),text="(-2,-2,-2)",box=0,opacity=0,color=color.cyan, visible=0)
k55=label(pos=(-2,-6,-2.2),text="(-2,-6,-2)",box=0,opacity=0,color=color.cyan, visible=0)
k555=label(pos=(-8,-2,-2.2),text="(-8,-2,-2)",box=0,opacity=0,color=color.cyan, visible=0)
k5555=label(pos=(-8,-6,-0.2),text="(-2,-2,0)",box=0, opacity=0,color=color.cyan, visible=0)
k55555=label(pos=(-8,-2,-0.2),text="(-8,-2,0)",box=0,opacity=0,color=color.cyan, visible=0)
k555555=label(pos=(-2,-6,-0.2),text="(-2,-6,0)",box=0,opacity=0,color=color.cyan, visible=0)
k5555555=label(pos=(-2,-2,0),text="(-2,-2,0)",box=0,opacity=0,color=color.cyan, visible=0)
k55555555=label(pos=(-8,-6,-2.2),text="(-8,-6,-2)",box=0,opacity=0,color=color.cyan, visible=0)
k555555555=points(pos=[(-2,-2,-2), (-2,-6,-2), (-8,-2,-2),(-2,-2,0),(-8,-6,0),(-8,-2,0),(-2,-6,0),(-8,-6,-2)],size=6, color=color.cyan, visible=0)

#6) Rotacija oko proizvoljnog pravca v=i+j+k
kvadar6 = convex(pos=[(1,1,1), (2.33, 0.33,2.33), (0.11, 3, 3),(0.33, 0.33, 1.33),(0.66, 1.66, 4.66),(-0.66, 2.33, 3.33),(1.66, -0.33, 2.66),(1.33, 2.33, 4.33)], color=color.blue, visible=0)

k6=label(pos=(1,1,1),text="(1,1,1)",box=0,opacity=0,color=color.cyan, visible=0)
k66=label(pos=(2.33, 0.33,2.33),text="(2.33, 0.33,2.33)",box=0,opacity=0,color=color.cyan, visible=0)
k666=label(pos=(0.11, 3, 3),text="(0.11, 3, 3)",box=0,opacity=0,color=color.cyan, visible=0)
k6666=label(pos=(0.33, 0.33, 1.33),text="(0.33, 0.33, 1.33)",box=0, opacity=0,color=color.cyan, visible=0)
k66666=label(pos=(0.66, 1.66, 4.66),text="(0.66, 1.66, 4.66)",box=0,opacity=0,color=color.cyan, visible=0)
k666666=label(pos=(-0.66, 2.33, 3.33),text="(-0.66, 2.33, 3.33)",box=0,opacity=0,color=color.cyan, visible=0)
k6666666=label(pos=(1.66, -0.33, 2.66),text="(1.66, -0.33, 2.66)",box=0,opacity=0,color=color.cyan, visible=0)
k66666666=label(pos=(1.33, 2.33, 4.33),text="(1.33, 2.33, 4.33)",box=0,opacity=0,color=color.cyan, visible=0)
k666666666=points(pos=[(1,1,1), (2.33, 0.33,2.33), (0.11, 3, 3),(0.33, 0.33, 1.33),(0.66, 1.66, 4.66),(-0.66, 2.33, 3.33),(1.66, -0.33, 2.66),(1.33, 2.33, 4.33)],size=6, color=color.cyan, visible=0)
k6666666666=label(pos=(-1,-1,2),text="v = (1,1,1) \nkut = 180",box=0, opacity=0,color=color.yellow, visible=0)

#7) Homotetija za faktor k=-2 sa centrom u tocki (-2,-2,-2)
kvadar7 = convex(pos=[(-8,-8,-8), (-8,-12,-8), (-14,-8,-8),(-8,-8,-6),(-14,-12,-6),(-14,-8,-6),(-8,-12,-6),(-14,-12,-8)], color=color.blue, visible=0)
k7=label(pos=(-8,-8,-8.2),text="(-8,-8,-8)",box=0,opacity=0,color=color.cyan, visible=0)
k77=label(pos=(-8,-12,-8.2),text="(-8,-12,-8)",box=0,opacity=0,color=color.cyan, visible=0)
k777=label(pos=(-14,-8,-8.2),text="(-14,-8,-8)",box=0,opacity=0,color=color.cyan, visible=0)
k7777=label(pos=(-8,-8,-6.2),text="(-8,-8,-6)",box=0, opacity=0,color=color.cyan, visible=0)
k77777=label(pos=(-14,-12,-6.2),text="(-14,-12,-6)",box=0,opacity=0,color=color.cyan, visible=0)
k777777=label(pos=(-14,-8,-6.2),text="(-14,-8,-6)",box=0,opacity=0,color=color.cyan, visible=0)
k7777777=label(pos=(-8,-12,-6.2),text="(-8,-12,-6)",box=0,opacity=0,color=color.cyan, visible=0)
k77777777=label(pos=(-14,-12,-8.2),text="(-14,-12,-8)",box=0,opacity=0,color=color.cyan, visible=0)
k777777777=label(pos=(-2,-2,-2),text="(-2,-2,-2)",box=0,opacity=0,color=color.cyan, visible=0)
k7777777777=points(pos=[(-2,-2,-2), (-8,-8,-8), (-8,-12,-8), (-14,-8,-8),(-8,-8,-6),(-14,-12,-6),(-14,-8,-6),(-8,-12,-6),(-14,-12,-8)],size=6, color=color.cyan, visible=0)

#8) Zrcaljenje s obzirom na xy-ravninu
kvadar8 = convex(pos=[(1,1,-1), (1,3,-1), (4,1,-1),(1,1,-0),(4,3,-0),(4,1,-0),(1,3,-0),(4,3,-1)], color=color.blue, visible=0)
k8=label(pos=(1,1,-1.2),text="(1,1,-1)",box=0,opacity=0,color=color.cyan, visible=0)
k88=label(pos=(1,3,-1.2),text="(1,3,-1)",box=0,opacity=0,color=color.cyan, visible=0)
k888=label(pos=(4,1,-1.2),text="(4,1,-1)",box=0,opacity=0,color=color.cyan, visible=0)
k8888=label(pos=(4,3,-1.2),text="(4,3,-1)",box=0, opacity=0,color=color.cyan, visible=0)
k88888=label(pos=(1,1,-0.2),text="(1,1,-0)",box=0,opacity=0,color=color.cyan, visible=0)
k888888=label(pos=(4,3,-0.2),text="(4,3,-0)",box=0,opacity=0,color=color.cyan, visible=0)
k8888888=label(pos=(4,1,-0.2),text="(4,1,-0)",box=0,opacity=0,color=color.cyan, visible=0)
k88888888=label(pos=(1,3,-0.2),text="(1,3,-0)",box=0,opacity=0,color=color.cyan, visible=0)
k888888888=points(pos=[(1,1,-1), (1,3,-1), (4,1,-1),(1,1,-0),(4,3,-0),(4,1,-0),(1,3,-0),(4,3,-1)],size=6, color=color.cyan, visible=0)

#9) Zrcaljenje s obzirom na xz-ravninu
kvadar9 = convex(pos=[(1,-1,1), (1,-3,1), (4,-1,1),(1,-1,0),(4,-3,0),(4,-1,0),(1,-3,0),(4,-3,1)], color=color.blue, visible=0)
k9=label(pos=(1,-1,1.2),text="(1,-1,1)",box=0,opacity=0,color=color.cyan, visible=0)
k99=label(pos=(1,-3,1.2),text="(1,-3,1)",box=0,opacity=0,color=color.cyan, visible=0)
k999=label(pos=(4,-1,1.2),text="(4,-1,1)",box=0,opacity=0,color=color.cyan, visible=0)
k9999=label(pos=(4,-3,1.2),text="(4,-3,1)",box=0, opacity=0,color=color.cyan, visible=0)
k99999=label(pos=(1,-1,0.2),text="(1,-1,0)",box=0,opacity=0,color=color.cyan, visible=0)
k999999=label(pos=(4,-3,0.2),text="(4,-3,0)",box=0,opacity=0,color=color.cyan, visible=0)
k9999999=label(pos=(4,-1,0.2),text="(4,-1,0)",box=0,opacity=0,color=color.cyan, visible=0)
k99999999=label(pos=(1,-3,0.2),text="(1,-3,0)",box=0,opacity=0,color=color.cyan, visible=0)
k999999999=points(pos=[(1,-1,1), (1,-3,1), (4,-1,1),(1,-1,0),(4,-3,0),(4,-1,0),(1,-3,0),(4,-3,1)],size=6, color=color.cyan, visible=0)

#0) Zrcaljenje s obzirom na yz-ravninu
kvadar0 = convex(pos=[(-1,1,1), (-1,3,1), (-4,1,1),(-1,1,0),(-4,3,0),(-4,1,0),(-1,3,0),(-4,3,1)], color=color.blue, visible=0)
k0=label(pos=(-1,1,1.2),text="(-1,1,1)",box=0,opacity=0,color=color.cyan, visible=0)
k00=label(pos=(-1,3,1.2),text="(-1,3,1)",box=0,opacity=0,color=color.cyan, visible=0)
k000=label(pos=(-4,1,1.2),text="(-4,1,1)",box=0,opacity=0,color=color.cyan, visible=0)
k0000=label(pos=(-4,3,1.2),text="(-4,3,1)",box=0, opacity=0,color=color.cyan, visible=0)
k00000=label(pos=(-1,1,0.2),text="(-1,1,0)",box=0,opacity=0,color=color.cyan, visible=0)
k000000=label(pos=(-4,3,0.2),text="(-4,3,0)",box=0,opacity=0,color=color.cyan, visible=0)
k0000000=label(pos=(-4,1,0.2),text="(-4,1,0)",box=0,opacity=0,color=color.cyan, visible=0)
k00000000=label(pos=(-1,3,0.2),text="(-1,3,0)",box=0,opacity=0,color=color.cyan, visible=0)
k000000000=points(pos=[(-1,1,1), (-1,3,1), (-4,1,1),(-1,1,0),(-4,3,0),(-4,1,0),(-1,3,0),(-4,3,1)],size=6, color=color.cyan, visible=0)

#R) Rastezanje duz koordinatnih osi sa faktorima=1.5
kvadarr = convex(pos=[(1.5,1.5,1.5),(1.5,4.5,1.5),(6,1.5,1.5),(1.5,1.5,0),(6,4.5,0),(6,1.5,0),(1.5,4.5,0),(6,4.5,1.5)], color=color.blue, visible=0)
kr=label(pos=(1.5,1.5,1.7),text="(1.5,1.5,1.5)",box=0,opacity=0,color=color.cyan, visible=0)
krr=label(pos=(1.5,4.5,1.5),text="(1.5,4.5,1.5)",box=0,opacity=0,color=color.cyan, visible=0)
krrr=label(pos=(6,1.5,1.5),text="(6,1.5,1.5)",box=0,opacity=0,color=color.cyan, visible=0)
krrrr=label(pos=(1.5,1.5,0),text="(1.5,1.5,0)",box=0, opacity=0,color=color.cyan, visible=0)
krrrrr=label(pos=(6,4.5,0),text="(6,4.5,0)",box=0,opacity=0,color=color.cyan, visible=0)
krrrrrr=label(pos=(6,1.5,0),text="(6,1.5,0)",box=0,opacity=0,color=color.cyan, visible=0)
krrrrrrr=label(pos=(1.5,4.5,0),text="(1.5,4.5,0)",box=0,opacity=0,color=color.cyan, visible=0)
krrrrrrrr=label(pos=(6,4.5,1.5),text="(6,4.5,1.5)",box=0,opacity=0,color=color.cyan, visible=0)
krrrrrrrrr=points(pos=[(1.5,1.5,1.5),(1.5,4.5,1.5),(6,1.5,1.5),(1.5,1.5,0),(6,4.5,0),(6,1.5,0),(1.5,4.5,0),(6,4.5,1.5)],size=6, color=color.cyan, visible=0)
krrrrrrrrrr=label(pos=(-1,-1,2),text="faktori = 1.5",box=0,opacity=0,color=color.red, visible=0)


#T) Centralna simetrija sa centrom u ishodistu
kvadart = convex(pos=[(-1,-1,-1), (-1,-3,-1), (-4,-1,-1),(-1,-1,-0),(-4,-3,-0),(-4,-1,-0),(-1,-3,-0),(-4,-3,-1)], color=color.blue, visible=0)
kt=label(pos=(-1,-1,-1.2),text="(-1,-1,-1)",box=0,opacity=0,color=color.cyan, visible=0)
ktt=label(pos=(-1,-3,-1.2),text="(-1,-3,-1)",box=0,opacity=0,color=color.cyan, visible=0)
kttt=label(pos=(-4,-1,-1.2),text="(-4,-1,-1)",box=0,opacity=0,color=color.cyan, visible=0)
ktttt=label(pos=(-4,-3,-1.2),text="(-4,-3,-1)",box=0, opacity=0,color=color.cyan, visible=0)
kttttt=label(pos=(-1,-1,-0.2),text="(-1,-1,-0)",box=0,opacity=0,color=color.cyan, visible=0)
ktttttt=label(pos=(-4,-3,-0.2),text="(-4,-3,-0)",box=0,opacity=0,color=color.cyan, visible=0)
kttttttt=label(pos=(-4,-1,-0.2),text="(-4,-1,-0)",box=0,opacity=0,color=color.cyan, visible=0)
ktttttttt=label(pos=(-1,-3,-0.2),text="(-1,-3,-0)",box=0,opacity=0,color=color.cyan, visible=0)
kttttttttt=points(pos=[(-1,-1,-1), (-1,-3,-1), (-4,-1,-1),(-1,-1,-0),(-4,-3,-0),(-4,-1,-0),(-1,-3,-0),(-4,-3,-1)],size=6, color=color.cyan, visible=0)

#Z) Centralna simetrija sa centrom u tocku (-1 ,-1 ,-1 )
kvadarz = convex(pos=[(-3,-3,-3), (-3,-5,-3), (-6,-3,-3),(-3,-3,-2),(-6,-5,-2),(-6,-3,-2),(-3,-5,-2),(-6,-5,-3)], color=color.blue, visible=0)
kz=label(pos=(-3,-3,-3.2),text="(-3,-3,-3)",box=0,opacity=0,color=color.cyan, visible=0)
kzz=label(pos=(-3,-5,-3.2),text="(-3,-5,-3)",box=0,opacity=0,color=color.cyan, visible=0)
kzzz=label(pos=(-6,-3,-3.2),text="(-6,-3,-3)",box=0,opacity=0,color=color.cyan, visible=0)
kzzzz=label(pos=(-6,-5,-3.2),text="(-6,-5,-3)",box=0, opacity=0,color=color.cyan, visible=0)
kzzzzz=label(pos=(-3,-3,-2.2),text="(-3,-3,-2)",box=0,opacity=0,color=color.cyan, visible=0)
kzzzzzz=label(pos=(-6,-5,-2.2),text="(-6,-5,-2)",box=0,opacity=0,color=color.cyan, visible=0)
kzzzzzzz=label(pos=(-6,-3,-2.2),text="(-6,-3,-2)",box=0,opacity=0,color=color.cyan, visible=0)
kzzzzzzzz=label(pos=(-3,-5,-2.2),text="(-3,-5,-2)",box=0,opacity=0,color=color.cyan, visible=0)
kzzzzzzzzz=points(pos=[(-1,-1,-1),(-3,-3,-3), (-3,-5,-3), (-6,-3,-3),(-3,-3,-2),(-6,-5,-2),(-6,-3,-2),(-3,-5,-2),(-6,-5,-3)],size=6, color=color.cyan, visible=0)
kzzzzzzzzzz=label(pos=(-1,-1.5,-1),text="(-1,-1,-1) TOCKA SIMETRIJE",box=0,opacity=0,color=color.red, visible=0)

#U) Ortogonalna projekcija na os x
kvadaru=cylinder(pos=(1,0,0), axis=(3,0,0), radius = 0.06, color=color.blue, visible=0)
ku=points(pos=[(1,0,0), (4,0,0)],size=6, color=color.cyan, visible=0)
kuu=label(pos=(4,0,0.2),text="(4,0,0)",box=0,opacity=0,color=color.cyan, visible=0)
kuuu=label(pos=(1,0,0.2),text="(1,0,0)",box=0,opacity=0,color=color.cyan, visible=0)

#I) Ortogonalna projekcija na os y
kvadari=cylinder(pos=(0,1,0), axis=(0,2,0), radius = 0.06, color=color.blue, visible=0)
ki=points(pos=[(0,1,0), (0,3,0)],size=6, color=color.cyan, visible=0)
kii=label(pos=(0,1,0.2),text="(0,1,0)",box=0,opacity=0,color=color.cyan, visible=0)
kiii=label(pos=(0,3,0.2),text="(0,3,0)",box=0,opacity=0,color=color.cyan, visible=0)

#O) Ortogonalna projekcija na os z
kvadaro=cylinder(pos=(0,0,0), axis=(0,0,1), radius = 0.06, color=color.blue, visible=0)
ko=points(pos=[(0,0,1),(0,0,0)],size=6, color=color.cyan, visible=0)
koo=label(pos=(0,0,1.2),text="(0,0,1)",box=0,opacity=0,color=color.cyan, visible=0)
kooo=label(pos=(0,0,0.2),text="(0,0,0)",box=0,opacity=0,color=color.cyan, visible=0)

#P) Ortogonalna projekcija na os xy-ravninu
kvadarp = convex(pos=[(1,1,0),(4,3,0),(4,1,0),(1,3,0)], color=color.blue, visible=0)
kp=label(pos=(1,1,0.2),text="(1,1,0)",box=0,opacity=0,color=color.cyan, visible=0)
kpp=label(pos=(1,3,0.2),text="(1,3,0)",box=0,opacity=0,color=color.cyan, visible=0)
kppp=label(pos=(4,1,0.2),text="(4,1,0)",box=0,opacity=0,color=color.cyan, visible=0)
kpppp=label(pos=(4,3,0.2),text="(4,3,0)",box=0, opacity=0,color=color.cyan, visible=0)
kppppp=points(pos=[(1,1,0),(4,3,0),(4,1,0),(1,3,0)],size=6, color=color.cyan, visible=0)

#A) Ortogonalna projekcija na os xz-ravninu
kvadara = convex(pos=[(1,0,1), (4,0,1),(1,0,0),(4,0,0)], color=color.blue, visible=0)
ka=label(pos=(1,0,1.2),text="(1,0,1)",box=0,opacity=0,color=color.cyan, visible=0)
kaa=label(pos=(4,0,1.2),text="(4,0,1)",box=0,opacity=0,color=color.cyan, visible=0)
kaaa=label(pos=(1,0,0.2),text="(1,0,0)",box=0,opacity=0,color=color.cyan, visible=0)
kaaaa=label(pos=(4,0,0.2),text="(4,0,0)",box=0, opacity=0,color=color.cyan, visible=0)
kaaaaa=points(pos=[(1,0,1), (4,0,1),(1,0,0),(4,0,0)],size=6, color=color.cyan, visible=0)

#S) Ortogonalna projekcija na os yz-ravninu
kvadars = convex(pos=[(0,1,1), (0,3,1),(0,1,0),(0,3,0)], color=color.blue, visible=0)
ks=label(pos=(0,1,1.2),text="(0,1,1)",box=0,osacity=0,color=color.cyan, visible=0)
kss=label(pos=(0,3,1.2),text="(0,3,1)",box=0,osacity=0,color=color.cyan, visible=0)
ksss=label(pos=(0,1,0.2),text="(0,1,0)",box=0,osacity=0,color=color.cyan, visible=0)
kssss=label(pos=(0,3,0.2),text="(0,3,0)",box=0, osacity=0,color=color.cyan, visible=0)
ksssss=points(pos=[(0,1,1), (0,3,1),(0,1,0),(0,3,0)],size=6, color=color.cyan, visible=0)

#D) Smicanje (uzduzne deformacije)
kvadard = convex(pos=[(4.46, 4.46, 4.46), (7.93,6.46,7.93), (7.46,9.66,9.66),(2.73,2.73,3.46),(9.19,9.92,12.12),(5.73,7.93,8.66),(6.2,4.73,6.93),(10.93,11.66,13.12)], color=color.blue, visible=0)
kd=label(pos=(4.46, 4.46, 4.46),text="(4.46, 4.46, 4.46)",box=0,opacity=0,color=color.cyan, visible=0)
kdd=label(pos=(7.93,6.46,7.93),text="(7.93,6.46,7.93)",box=0,opacity=0,color=color.cyan, visible=0)
kddd=label(pos=(7.46,9.66,9.66),text="(7.46,9.66,9.66)",box=0,opacity=0,color=color.cyan, visible=0)
kdddd=label(pos=(2.73,2.73,3.46),text="(-6,-5,-3)",box=0, opacity=0,color=color.cyan, visible=0)
kddddd=label(pos=(9.19,9.92,12.12),text="(-3,-3,-2)",box=0,opacity=0,color=color.cyan, visible=0)
kdddddd=label(pos=(5.73,7.93,8.66),text="(-6,-5,-2)",box=0,opacity=0,color=color.cyan, visible=0)
kddddddd=label(pos=(6.2,4.73,6.93),text="(-6,-3,-2)",box=0,opacity=0,color=color.cyan, visible=0)
kdddddddd=label(pos=(10.93,11.66,13.12),text="(10.93,11.66,13.12)",box=0,opacity=0,color=color.cyan, visible=0)
kddddddddd=points(pos=[(4.46, 4.46, 4.46), (7.93,6.46,7.93), (7.46,9.66,9.66),(2.73,2.73,3.46),(9.19,9.92,12.12),(5.73,7.93,8.66),(6.2,4.73,6.93),(10.93,11.66,13.12)],size=6, color=color.cyan, visible=0)
kdddddddddd=label(pos=(-1,-1,2),text="alfa = 60\nbeta = 60\ngama = 60",box=0, opacity=0,color=color.yellow, visible=0)

#help
pomoc1 = label(pos=(-8,3.3,0), text = '1) Translacija za vektor v = (-3, -2, 1)', box=0, opacity=0, visible=0)
pomoc2 = label(pos=(-8,3,0), text = '2) Rotacija oko osi x za 180 stupnjeva', box=0, opacity=0, visible=0)
pomoc3 = label(pos=(-8,2.7,0), text = '3) Rotacija oko osi y za 180 stupnjeva', box=0, opacity=0, visible=0)
pomoc4 = label(pos=(-8,2.4,0), text = '4) Rotacija oko osi z za 180 stupnjeva', box=0, opacity=0, visible=0)
pomoc5 = label(pos=(-8,2.1,0), text = '5) Homotetija za faktor k=-2 sa centrom u ishodistu', box=0, opacity=0, visible=0)
pomoc6 = label(pos=(-8,1.8,0), text = '6) Rotacija oko proizvoljnog pravca', box=0, opacity=0, visible=0)
pomoc7 = label(pos=(-8,1.5,0), text = '7) Homotetija za faktor k=-2 sa centrom u tocki (-2,-2,-2)', box=0, opacity=0, visible=0)
pomoc8 = label(pos=(-8,1.2,0), text = '8) Zrcaljenje s obzirom na xy-ravninu', box=0, opacity=0, visible=0)
pomoc9 = label(pos=(-8,0.9,0), text = '9) Zrcaljenje s obzirom na xz-ravninu', box=0, opacity=0, visible=0)
pomoc0 = label(pos=(-8,0.6,0), text = '0) Zrcaljenje s obzirom na yz-ravninu', box=0, opacity=0, visible=0)
pomocq = label(pos=(-8,0.3,0), text = 'Q) Zrcaljenje s obzirom na os x', box=0, opacity=0, visible=0)
pomocw = label(pos=(-8,0,0), text = 'W) Zrcaljenje s obzirom na os y', box=0, opacity=0, visible=0)
pomoce = label(pos=(-8,-0.3,0), text = 'E) Zrcaljenje s obzirom na os z', box=0, opacity=0, visible=0)
pomocr = label(pos=(-8,-0.6,0), text = 'R) Rastezanje duz koordinatnih osi sa faktorima = 1.5', box=0, opacity=0, visible=0)
pomoct = label(pos=(-8,-0.9,0), text = 'T) Centralna simetrija sa centrom u ishodistu', box=0, opacity=0, visible=0)
pomocz = label(pos=(-8,-1.2,0), text = 'Z) Centralna simetrija sa centrom u tocku (-1, -1, -1)', box=0, opacity=0, visible=0)
pomocu = label(pos=(-8,-1.5,0), text = 'U) Ortogonalna projekcija na os x', box=0, opacity=0, visible=0)
pomoci = label(pos=(-8,-1.8,0), text = 'I) Ortogonalna projekcija na os y', box=0, opacity=0, visible=0)
pomoco = label(pos=(-8,-2.1,0), text = 'O) Ortogonalna projekcija na os z', box=0, opacity=0, visible=0)
pomocp = label(pos=(-8,-2.4,0), text = 'P) Ortogonalna projekcija na xy-ravninu', box=0, opacity=0, visible=0)
pomoca = label(pos=(-8,-2.7,0), text = 'A) Ortogonalna projekcija na xz-ravninu', box=0, opacity=0, visible=0)
pomocs = label(pos=(-8,-3,0), text = 'S) Ortogonalna projekcija na yz-ravninu', box=0, opacity=0, visible=0)
pomocd = label(pos=(-8,-3.3,0), text = 'D) Smicanje (uzduzne deformacije)', box=0, opacity=0, visible=0)

#vidljivost
while 1:
    rate(10)
    if scene.kb.keys:
        s = scene.kb.getkey()
        if s == '1':
            if kvadar1.visible == 1:
                k1.visible=0
                k11.visible=0
                k111.visible=0
                k1111.visible=0
                k11111.visible=0
                k111111.visible=0
                k1111111.visible=0
                k11111111.visible=0
                k111111111.visible=0
                k1111111111.visible=0
                kvadar1.visible = 0
            else:
                kvadar1.visible = 1
                k1.visible=1
                k11.visible=1
                k111.visible=1
                k1111.visible=1
                k11111.visible=1
                k111111.visible=1
                k1111111.visible=1
                k11111111.visible=1
                k111111111.visible=1
                k1111111111.visible=1
        if s == '2' or s == 'q':
            if kvadar2.visible == 1:
                k2.visible=0
                k22.visible=0
                k222.visible=0
                k2222.visible=0
                k22222.visible=0
                k222222.visible=0
                k2222222.visible=0
                k22222222.visible=0
                k222222222.visible=0
                kvadar2.visible = 0
            else:
                kvadar2.visible = 1
                k2.visible=1
                k22.visible=1
                k222.visible=1
                k2222.visible=1
                k22222.visible=1
                k222222.visible=1
                k2222222.visible=1
                k22222222.visible=1
                k222222222.visible=1
        if s == '3' or s == 'w':
            if kvadar3.visible == 1:
                k3.visible=0
                k33.visible=0
                k333.visible=0
                k3333.visible=0
                k33333.visible=0
                k333333.visible=0
                k3333333.visible=0
                k33333333.visible=0
                k333333333.visible=0
                kvadar3.visible = 0
            else:
                kvadar3.visible = 1
                k3.visible=1
                k33.visible=1
                k333.visible=1
                k3333.visible=1
                k33333.visible=1
                k333333.visible=1
                k3333333.visible=1
                k33333333.visible=1
                k333333333.visible=1
        if s == '4' or s == 'e':
            if kvadar4.visible == 1:
                k4.visible=0
                k44.visible=0
                k444.visible=0
                k4444.visible=0
                k44444.visible=0
                k444444.visible=0
                k4444444.visible=0
                k44444444.visible=0
                k444444444.visible=0
                kvadar4.visible = 0
            else:
                kvadar4.visible = 1
                k4.visible=1
                k44.visible=1
                k444.visible=1
                k4444.visible=1
                k44444.visible=1
                k444444.visible=1
                k4444444.visible=1
                k44444444.visible=1
                k444444444.visible=1
        if s == '5':
            if kvadar5.visible == 1:
                k5.visible=0
                k55.visible=0
                k555.visible=0
                k5555.visible=0
                k55555.visible=0
                k555555.visible=0
                k5555555.visible=0
                k55555555.visible=0
                k555555555.visible=0
                kvadar5.visible = 0
            else:
                kvadar5.visible = 1
                k5.visible=1
                k55.visible=1
                k555.visible=1
                k5555.visible=1
                k55555.visible=1
                k555555.visible=1
                k5555555.visible=1
                k55555555.visible=1
                k555555555.visible=1
        if s == '6':
            if kvadar6.visible == 1:
                k6.visible=0
                k66.visible=0
                k666.visible=0
                k6666.visible=0
                k66666.visible=0
                k666666.visible=0
                k6666666.visible=0
                k66666666.visible=0
                k666666666.visible=0
                k6666666666.visible=0
                kvadar6.visible = 0
            else:
                kvadar6.visible = 1
                k66.visible=1
                k666.visible=1
                k6666.visible=1
                k66666.visible=1
                k666666.visible=1
                k6666666.visible=1
                k66666666.visible=1
                k666666666.visible=1
                k6666666666.visible=1
        if s == '7':
            if kvadar7.visible == 1:
                k7.visible=0
                k77.visible=0
                k777.visible=0
                k7777.visible=0
                k77777.visible=0
                k777777.visible=0
                k7777777.visible=0
                k77777777.visible=0
                k777777777.visible=0
                k7777777777.visible=0
                kvadar7.visible = 0
            else:
                kvadar7.visible = 1
                k7.visible=1
                k77.visible=1
                k777.visible=1
                k7777.visible=1
                k77777.visible=1
                k777777.visible=1
                k7777777.visible=1
                k77777777.visible=1
                k777777777.visible=1
                k7777777777.visible=1
        if s == '8':
            if kvadar8.visible == 1:
                k8.visible=0
                k88.visible=0
                k888.visible=0
                k8888.visible=0
                k88888.visible=0
                k888888.visible=0
                k8888888.visible=0
                k88888888.visible=0
                k888888888.visible=0
                kvadar8.visible = 0
            else:
                kvadar8.visible = 1
                k8.visible=1
                k88.visible=1
                k888.visible=1
                k8888.visible=1
                k88888.visible=1
                k888888.visible=1
                k8888888.visible=1
                k88888888.visible=1
                k888888888.visible=1
        if s == '9':
            if kvadar9.visible == 1:
                k9.visible=0
                k99.visible=0
                k999.visible=0
                k9999.visible=0
                k99999.visible=0
                k999999.visible=0
                k9999999.visible=0
                k99999999.visible=0
                k999999999.visible=0
                kvadar9.visible = 0
            else:
                kvadar9.visible = 1
                k9.visible=1
                k99.visible=1
                k999.visible=1
                k9999.visible=1
                k99999.visible=1
                k999999.visible=1
                k9999999.visible=1
                k99999999.visible=1
                k999999999.visible=1
        if s == '0':
            if kvadar0.visible == 1:
                k0.visible=0
                k00.visible=0
                k000.visible=0
                k0000.visible=0
                k00000.visible=0
                k000000.visible=0
                k0000000.visible=0
                k00000000.visible=0
                k000000000.visible=0
                kvadar0.visible = 0
            else:
                kvadar0.visible = 1
                k0.visible=1
                k00.visible=1
                k000.visible=1
                k0000.visible=1
                k00000.visible=1
                k000000.visible=1
                k0000000.visible=1
                k00000000.visible=1
                k000000000.visible=1
        if s == 't':
            if kvadart.visible == 1:
                kt.visible=0
                ktt.visible=0
                kttt.visible=0
                ktttt.visible=0
                kttttt.visible=0
                ktttttt.visible=0
                kttttttt.visible=0
                ktttttttt.visible=0
                kttttttttt.visible=0
                kvadart.visible = 0
            else:
                kvadart.visible = 1
                kt.visible=1
                ktt.visible=1
                kttt.visible=1
                ktttt.visible=1
                kttttt.visible=1
                ktttttt.visible=1
                kttttttt.visible=1
                ktttttttt.visible=1
                kttttttttt.visible=1
        if s == 'r':
            if kvadarr.visible == 1:
                kr.visible=0
                krr.visible=0
                krrr.visible=0
                krrrr.visible=0
                krrrrr.visible=0
                krrrrrr.visible=0
                krrrrrrr.visible=0
                krrrrrrrr.visible=0
                krrrrrrrrr.visible=0
                krrrrrrrrrr.visible=0
                kvadarr.visible = 0
            else:
                kvadarr.visible = 1
                kr.visible=1
                krr.visible=1
                krrr.visible=1
                krrrr.visible=1
                krrrrr.visible=1
                krrrrrr.visible=1
                krrrrrrr.visible=1
                krrrrrrrr.visible=1
                krrrrrrrrr.visible=1
                krrrrrrrrrr.visible=1
        if s == 'u':
            if kvadaru.visible == 1:
                ku.visible=0
                kuu.visible=0
                kuuu.visible=0
                kvadaru.visible = 0
            else:
                kvadaru.visible = 1
                ku.visible=1
                kuu.visible=1
                kuuu.visible=1
        if s == 'z':
            if kvadarz.visible == 1:
                kz.visible=0
                kzz.visible=0
                kzzz.visible=0
                kzzzz.visible=0
                kzzzzz.visible=0
                kzzzzzz.visible=0
                kzzzzzzz.visible=0
                kzzzzzzzz.visible=0
                kzzzzzzzzz.visible=0
                kzzzzzzzzzz.visible=0
                kvadarz.visible = 0
            else:
                kvadarz.visible = 1
                kz.visible=1
                kzz.visible=1
                kzzz.visible=1
                kzzzz.visible=1
                kzzzzz.visible=1
                kzzzzzz.visible=1
                kzzzzzzz.visible=1
                kzzzzzzzz.visible=1
                kzzzzzzzzz.visible=1
                kzzzzzzzzzz.visible=1

        if s == 'i':
            if kvadari.visible == 1:
                ki.visible=0
                kii.visible=0
                kiii.visible=0
                kvadari.visible = 0
            else:
                kvadari.visible = 1
                ki.visible=1
                kii.visible=1
                kiii.visible=1
        if s == 'o':
            if kvadaro.visible == 1:
                ko.visible=0
                koo.visible=0
                kooo.visible=0
                kvadaro.visible = 0
            else:
                kvadaro.visible = 1
                ko.visible=1
                koo.visible=1
                kooo.visible=1
        if s == 'p':
            if kvadarp.visible == 1:
                kp.visible=0
                kpp.visible=0
                kppp.visible=0
                kpppp.visible=0
                kppppp.visible=0
                kvadarp.visible = 0
            else:
                kvadarp.visible = 1
                kp.visible=1
                kpp.visible=1
                kppp.visible=1
                kpppp.visible=1
                kppppp.visible=1
        if s == 'a':
            if kvadara.visible == 1:
                ka.visible=0
                kaa.visible=0
                kaaa.visible=0
                kaaaa.visible=0
                kaaaaa.visible=0
                kvadara.visible = 0
            else:
                kvadara.visible = 1
                ka.visible=1
                kaa.visible=1
                kaaa.visible=1
                kaaaa.visible=1
                kaaaaa.visible=1
        if s == 's':
            if kvadars.visible == 1:
                ks.visible=0
                kss.visible=0
                ksss.visible=0
                kssss.visible=0
                ksssss.visible=0
                kvadars.visible = 0
            else:
                kvadars.visible = 1
                ks.visible=1
                kss.visible=1
                ksss.visible=1
                kssss.visible=1
                ksssss.visible=1
        if s == 'd':
            if kvadard.visible == 1:
                kd.visible=0
                kdd.visible=0
                kddd.visible=0
                kdddd.visible=0
                kddddd.visible=0
                kdddddd.visible=0
                kddddddd.visible=0
                kdddddddd.visible=0
                kddddddddd.visible=0
                kdddddddddd.visible=0
                kvadard.visible = 0
            else:
                kvadard.visible = 1
                kd.visible=1
                kdd.visible=1
                kddd.visible=1
                kdddd.visible=1
                kddddd.visible=1
                kdddddd.visible=1
                kddddddd.visible=1
                kdddddddd.visible=1
                kddddddddd.visible=1
                kdddddddddd.visible=1
        if s == 'f1':
            pomoc1.visible = 1
            pomoc2.visible = 1
            pomoc3.visible = 1
            pomoc4.visible = 1
            pomoc5.visible = 1
            pomoc6.visible = 1
            pomoc7.visible = 1
            pomoc8.visible = 1
            pomoc9.visible = 1
            pomoc0.visible = 1            
            pomocq.visible = 1
            pomocw.visible = 1
            pomoce.visible = 1
            pomocr.visible = 1
            pomoct.visible = 1
            pomocz.visible = 1
            pomocu.visible = 1
            pomoci.visible = 1
            pomoco.visible = 1
            pomocp.visible = 1
            pomoca.visible = 1
            pomocs.visible = 1
            pomocd.visible = 1
        if s == 'f2':
            pomoc1.visible = 0
            pomoc2.visible = 0
            pomoc3.visible = 0
            pomoc4.visible = 0
            pomoc5.visible = 0
            pomoc6.visible = 0
            pomoc7.visible = 0
            pomoc8.visible = 0
            pomoc9.visible = 0
            pomoc0.visible = 0           
            pomocq.visible = 0
            pomocw.visible = 0
            pomoce.visible = 0
            pomocr.visible = 0
            pomoct.visible = 0
            pomocz.visible = 0
            pomocu.visible = 0
            pomoci.visible = 0
            pomoco.visible = 0
            pomocp.visible = 0
            pomoca.visible = 0
            pomocs.visible = 0
            pomocd.visible = 0