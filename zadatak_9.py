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

#Kocka sa duljinom brida 1 sa jednim vrhom u ishodistu
kvadar1 = convex(pos=[(1,1,1), (1,1,0), (1,0,1),(1,0,0),(0,1,1),(0,1,0),(0,0,1),(0,0,0)], color=color.red)
k1=label(pos=(1,1,1.2),text="(1,1,1)",box=0,opacity=0,color=color.yellow)
k11=label(pos=(1,1,0.2),text="(1,1,0)",box=0,opacity=0,color=color.yellow)
k111=label(pos=(1,0,1.2),text="(1,0,1)",box=0,opacity=0,color=color.yellow)
k1111=label(pos=(1,0,0.2),text="(1,0,0)",box=0, opacity=0,color=color.yellow)
k11111=label(pos=(0,1,1.2),text="(0,1,1)",box=0,opacity=0,color=color.yellow)
k111111=label(pos=(0,1,0.2),text="(0,1,0)",box=0,opacity=0,color=color.yellow)
k1111111=label(pos=(0,0,1.2),text="(0,0,1)",box=0,opacity=0,color=color.yellow)
k11111111=label(pos=(0,0,0.2),text="(0,0,0)",box=0,opacity=0,color=color.yellow)
k111111111=points(pos=[(1,1,1), (1,1,0), (1,0,1),(1,0,0),(0,1,1),(0,1,0),(0,0,1),(0,0,0)],size=6, color=color.yellow)
k1111111111=label(pos=(-3, 0.5, 0),text="Kocka sa duljinom brida 1\nsa jednim vrhom u ishodistu",box=0,opacity=0,color=color.yellow, visible=1)

c1=cylinder(pos=(2,2,1), axis=(2.5,0,0), radius = 0.05, color=color.blue)
c11=cone(pos=(4.5,2,1), axis=(0.5,0,0), radius =0.1, color=color.cyan)
c111=cylinder(pos=(2,2,1), axis=(0,1.5,0), radius = 0.05, color=color.blue)
c1111=cone(pos=(2,3.5,1), axis=(0,.5,0), radius =0.1, color=color.cyan)
c11111=cylinder(pos=(2,2,1), axis=(0,0,0.5), radius = 0.05, color=color.blue)
c111111=cone(pos=(2,2,1.5), axis=(0,0,0.5), radius =0.1, color=color.cyan)
c1111111=sphere(pos=vector(2,2,1),radius=0.1, color=color.cyan)
c11111111=label(pos=(4, 3, 0),text="Vektor koji razapinje kvadar\nv = (3,2,1) sa pocetkom u tocki (2,2,1)",box=0,opacity=0,color=color.yellow, visible=1)
#1. transformacija
kvadar2 = convex(pos=[(3,2,1), (3,2,0), (3,0,1),(3,0,0),(0,2,1),(0,2,0),(0,0,1),(0,0,0)], color=color.red, visible=0)
k2=label(pos=(3,2,1.2),text="(3,2,1)",box=0,opacity=0,color=color.yellow, visible=0)
k22=label(pos=(3,2,0.2),text="(3,2,0)",box=0,opacity=0,color=color.yellow, visible=0)
k222=label(pos=(3,0,1.2),text="(3,0,1)",box=0,opacity=0,color=color.yellow, visible=0)
k2222=label(pos=(3,0,0.2),text="(3,0,0)",box=0, opacity=0,color=color.yellow, visible=0)
k22222=label(pos=(0,2,1.2),text="(0,2,1)",box=0,opacity=0,color=color.yellow, visible=0)
k222222=label(pos=(0,2,0.2),text="(0,2,0)",box=0,opacity=0,color=color.yellow, visible=0)
k2222222=label(pos=(0,0,1.2),text="(0,0,1)",box=0,opacity=0,color=color.yellow, visible=0)
k22222222=label(pos=(0,0,0.2),text="(0,0,0)",box=0,opacity=0,color=color.yellow, visible=0)
k222222222=points(pos=[(3,2,1), (3,2,0), (3,0,1),(3,0,0),(0,2,1),(0,2,0),(0,0,1),(0,0,0)],size=6, color=color.yellow, visible=0)
k2222222222=label(pos=(-3, 0.5, 0),text="1. transformacija:\nRastezanje duz koordinatnih osi\nkx=3\nky=2\nkz=1",box=0,opacity=0,color=color.yellow, visible=0)

#2. transformacija
kvadar3 = convex(pos=[(5,4,2), (5,4,1), (5,2,2),(5,2,1),(2,4,2),(2,4,1),(2,2,2),(2,2,1)], color=color.yellow, visible=0)
k3=label(pos=(5,4,2.2),text="(5,4,2)",box=0,opacity=0,color=color.cyan, visible=0)
k33=label(pos=(5,4,1.2),text="(5,4,1)",box=0,opacity=0,color=color.cyan, visible=0)
k333=label(pos=(5,2,2.2),text="(5,2,2)",box=0,opacity=0,color=color.cyan, visible=0)
k3333=label(pos=(5,2,1.2),text="(5,2,1)",box=0, opacity=0,color=color.cyan, visible=0)
k33333=label(pos=(2,4,2.2),text="(2,4,2)",box=0,opacity=0,color=color.cyan, visible=0)
k333333=label(pos=(2,4,1.2),text="(2,4,1)",box=0,opacity=0,color=color.cyan, visible=0)
k3333333=label(pos=(2,2,2.2),text="(2,2,2)",box=0,opacity=0,color=color.cyan, visible=0)
k33333333=label(pos=(2,2,1.2),text="(2,2,1)",box=0,opacity=0,color=color.cyan, visible=0)
k333333333=points(pos=[(5,4,2), (5,4,1), (5,2,2),(5,2,1),(2,4,2),(2,4,1),(2,2,2),(2,2,1)],size=6, color=color.cyan, visible=0)
k3333333333=label(pos=(3, 6, 0),text="2. transformacija:\nTranslacija za vektor v\nv = (2, 2, 1)",box=0,opacity=0,color=color.yellow, visible=0)

#Rotacija za 30 stupnjeva
kvadar4 = convex(pos=[(5,2.46,3.73), (5,2.96,2.86), (5,0.73,2.73),(5,1.23,1.86),(2, 2.45, 3.73),(2, 2.96, 2.86),(2, 0.73, 2.73),(2, 1.23, 1.86)], color=color.blue, visible=0)
k4=label(pos=(5,2.46,3.93),text="(5,2.46,3.73)",box=0,opacity=0,color=color.yellow, visible=0)
k44=label(pos=(5,2.96,3.06),text="(5,2.96,2.86)",box=0,opacity=0,color=color.yellow, visible=0)
k444=label(pos=(5,0.73,2.93),text="(5,0.73,2.73)",box=0,opacity=0,color=color.yellow, visible=0)
k4444=label(pos=(5,1.23,2.06),text="(5,1.23,1.86)",box=0, opacity=0,color=color.yellow, visible=0)
k44444=label(pos=(2, 2.45, 3.93),text="(2, 2.45, 3.73)",box=0,opacity=0,color=color.yellow, visible=0)
k444444=label(pos=(2, 2.96, 3.06),text="(2, 2.96, 2.86)",box=0,opacity=0,color=color.yellow, visible=0)
k4444444=label(pos=(2, 0.73, 2.93),text="(2, 0.73, 2.73)",box=0,opacity=0,color=color.yellow, visible=0)
k44444444=label(pos=(2, 1.23, 2.06),text="(2, 1.23, 1.86)",box=0,opacity=0,color=color.yellow, visible=0)
k444444444=points(pos=[(5,2.46,3.73), (5,2.96,2.86), (5,0.73,2.73),(5,1.23,1.86),(2, 2.45, 3.73),(2, 2.96, 2.86),(2, 0.73, 2.73),(2, 1.23, 1.86)],size=6, color=color.cyan, visible=0)
k4444444444=label(pos=(3, 6, 0),text="Rotacija za 30 stupnjeva",box=0,opacity=0,color=color.yellow, visible=0)
#help
pomoc1 = label(pos=(-4,6.3,0), text = 'Na pocetku je prikazana kocka sa bridom duzine 1\n1) Prikazuje prvu transformaciju\n2) Prikazuje drugu transformaciju\n3) Prikazuje rotaciju za 30 stupnjeva\n4) Ponovno postavljanje prikaza na pocetnu kocku\nMORATE ici od 1 do 3 kako bi se tranformacije \npravilno prikazale!\nTek nakon sto ste prosli kroz sve 3 tranformacije \nopcija 4 radi sto treba', box=0, opacity=0, visible=0)

#vidljivost
while 1:
    rate(10)
    if scene.kb.keys:
        s = scene.kb.getkey()
        if s == '1':
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
                c11111111.visible=0
                
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
                k2222222222.visible=1
                
        if s == '2':
                k2.visible=0
                k22.visible=0
                k222.visible=0
                k2222.visible=0
                k22222.visible=0
                k222222.visible=0
                k2222222.visible=0
                k22222222.visible=0
                k222222222.visible=0
                k2222222222.visible=0
                
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
                k3333333333.visible=1
                
        if s == '3':
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
                k4444444444.visible=1
                
                c1.visible=0
                c11.visible=0
                c111.visible=0
                c1111.visible=0
                c11111.visible=0
                c111111.visible=0
                c1111111.visible=0
                c11111111.visible=0
                
                k3.visible=0
                k33.visible=0
                k333.visible=0
                k3333.visible=0
                k33333.visible=0
                k333333.visible=0
                k3333333.visible=0
                k33333333.visible=0
                k333333333.visible=0
                k3333333333.visible=0
                kvadar2.visible = 0
        if s == '4':
                kvadar4.visible = 0
                k4.visible=0
                k44.visible=0
                k444.visible=0
                k4444.visible=0
                k44444.visible=0
                k444444.visible=0
                k4444444.visible=0
                k44444444.visible=0
                k444444444.visible=0
                k4444444444.visible=0
                kvadar3.visible = 0
                
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
                kvadar1.visible = 1
                c1.visible=1
                c11.visible=1
                c111.visible=1
                c1111.visible=1
                c11111.visible=1
                c111111.visible=1
                c1111111.visible=1
                c11111111.visible=1                        
        if s == 'f1':
            pomoc1.visible = 1  
        if s == 'f2':
            pomoc1.visible = 0
            
           