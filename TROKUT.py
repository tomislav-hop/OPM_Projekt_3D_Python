from visual import*

scene = display(title='F1 - Prikazi pomoc || F2 - Sakrij pomoc', width=900, height=900)

#koordinatni sustav
curve(pos=[(-10,0,0),(10,0,0)],radius = 0.05, color=color.white)
curve(pos=[(0,-10,0),(0,10,0)],radius = 0.05, color=color.white)
curve(pos=[(0,0,-10),(0,0,10)],radius = 0.05, color=color.white)

#tocke
for x in range(1,10):
    sphere(pos=(x,0,0),radius=0.06, color=color.red)
    sphere(pos=(0,x,0),radius=0.06, color=color.red)
    sphere(pos=(0,0,x),radius=0.06, color=color.red)
    sphere(pos=(-x,0,0),radius=0.06, color=color.red)
    sphere(pos=(0,-x,0),radius=0.06, color=color.red)
    sphere(pos=(0,0,-x),radius=0.06, color=color.red)

#oznake tocaka
label(pos=(10.3,0,0), text = 'X',box = 0,height=30,color=color.red)
label(pos=(1,0,-0.3),text="1",opacity=0,box=0,height=20 ,color=color.red)

label(pos=(0,10.3,0), text = 'Y',box = 0,height=30,color=color.red)
label(pos=(0,1,-0.3),text="1",opacity=0,box=0,height=20 ,color=color.red)

label(pos=(0,0,10.3), text = 'Z',box = 0,height=30,color=color.red)
label(pos=(0,-0.3,1),text="1",opacity=0,box=0,height=20 ,color=color.red)

#trokuti
convex(pos=[(1,1,1), (4,1,3), (3,3,2)], color=color.green)
label(pos=(1,1,1.5), text="(1,1,1)",box=0,opacity=0, color=color.yellow)
label(pos=(4,1,3.5), text="(4,1,3)",box=0,opacity=0, color=color.yellow)
label(pos=(3,3,2.5), text="(3,3,2)",box=0,opacity=0, color=color.yellow)
points(pos=[(1,1,1), (4,1,3), (3,3,2)], size=6, color=color.yellow)

#1) Translacija za vektor v
trokut1 = convex(pos=[(-2,-1,2), (1,-1,4), (0,1,3)], color=color.blue, visible=0)
t1 = label(pos=(-2,-1,2.2), text="(-2,-1,2)",box=0,opacity=0, color=color.cyan, visible=0)
t11 = label(pos=(1,-1,4.2), text="(1,-1,4)",box=0,opacity=0, color=color.cyan, visible=0)
t111 = label(pos=(0,1,3.2), text="(0,1,3)",box=0,opacity=0, color=color.cyan, visible=0)
t1111 = points(pos=[(-2,-1,2), (1,-1,4), (0,1,3)],size=6, color=color.cyan, visible=0)
t11111=label(pos=(-2, -2, 2),text="Translacija za vektor v = (-3, -2, 1)",box=0,opacity=0,color=color.red, visible=0)

#2) Rotacija oko osi x za 180 stupnjeva
#Q) Zrcaljenje s obzirom na os x
trokut2 = convex(pos=[(1,-1,-1), (4,-1,-3), (3,-3,-2)], color=color.blue, visible=0)
t2 = label(pos=(1,-1,-1.5), text="(1,-1,-1)",box=0,opacity=0, color=color.cyan, visible=0)
t22 = label(pos=(4,-1,-3.5), text="(4,-1,-3)",box=0,opacity=0, color=color.cyan, visible=0)
t222 = label(pos=(3,-3,-2.5), text="(3,-3,-2)",box=0,opacity=0, color=color.cyan, visible=0)
t2222 = points(pos=[(1,-1,-1), (4,-1,-3), (3,-3,-2)],size=6, color=color.cyan, visible=0)

#3) Rotacija oko osi y za 180 stupnjeva
#W) Zrcaljenje s obzirom na os y
trokut3 = convex(pos=[(-1,1,-1), (-4,1,-3), (-3,3,-2)], color=color.blue, visible=0)
t3 = label(pos=(-1,1,-1.5), text="(-1,1,-1)",box=0,opacity=0, color=color.cyan, visible=0)
t33 = label(pos=(-4,1,-3.5), text="(-4,1,-3)",box=0,opacity=0, color=color.cyan, visible=0)
t333 = label(pos=(-3,3,-2.5), text="(-3,3,-2)",box=0,opacity=0, color=color.cyan, visible=0)
t3333 = points(pos=[(-1,1,-1), (-4,1,-3), (-3,3,-2)],size=6, color=color.cyan, visible=0)

#4) Rotacija oko osi z za 180 stupnjeva
#E) Zrcaljenje s obzirom na os z
trokut4 = convex(pos=[(-1,-1,1), (-4,-1,3), (-3,-3,2)], color=color.blue, visible=0)
t4 = label(pos=(-1,-1,1.5), text="(-1,-1,1)",box=0,opacity=0, color=color.cyan, visible=0)
t44 = label(pos=(-4,-1,3.5), text="(-4,-1,3)",box=0,opacity=0, color=color.cyan, visible=0)
t444 = label(pos=(-3,-3,2.5), text="(-3,-3,2)",box=0,opacity=0, color=color.cyan, visible=0)
t4444 = points(pos=[(-1,-1,1), (-4,-1,3), (-3,-3,2)],size=6, color=color.cyan, visible=0)

#5) Homotetija za faktor k=-2 sa centrom u ishodistu
trokut5 = convex(pos=[(-2,-2,-2), (-8,-2,-6), (-6,-6,-4)], color=color.blue, visible=0)
t5 = label(pos=(-2,-2,-2.2), text="(-2,-2,-2)",box=0,opacity=0, color=color.cyan, visible=0)
t55 = label(pos=(-8,-2,-6.2), text="(-8,-2,-6)",box=0,opacity=0, color=color.cyan, visible=0)
t555 = label(pos=(-6,-6,-4.2), text="(-6,-6,-4)",box=0,opacity=0, color=color.cyan, visible=0)
t5555 = points(pos=[(-2,-2,-2), (-8,-2,-6), (-6,-6,-4)],size=6, color=color.cyan, visible=0)

#6) Rotacija oko proizvoljnog pravca
trokut6 = convex(pos=[(1,1,1), (1.33, 4.33, 2.33), (2.33, 2.33, 3.33)], color=color.blue, visible=0)
t6 = label(pos=(1,1,1), text="(1,1,1)",box=0,opacity=0, color=color.cyan, visible=0)
t66 = label(pos=(1.33, 4.33, 2.33), text="(1.33, 4.33, 2.33)",box=0,opacity=0, color=color.cyan, visible=0)
t666 = label(pos=(2.33, 2.33, 3.33), text="(2.33, 2.33, 3.33)",box=0,opacity=0, color=color.cyan, visible=0)
t6666 = points(pos=[(1,1,1), (1.33, 4.33, 2.33), (2.33, 2.33, 3.33)],size=6, color=color.cyan, visible=0)
t66666=label(pos=(-1,-1,2),text="v = i+j+k\nkut = 180",box=0, opacity=0,color=color.yellow, visible=0)


#7) Homotetija za faktor k=-1 sa centrom u tocki ( -2, -2, -2)
trokut7 = convex(pos=[(-8,-8,-8), (-14,-8,-12), (-12,-12,-10)], color=color.blue, visible=0)
t7 = label(pos=(-8,-8,-8.2), text="(-8,-8,-8)",box=0,opacity=0, color=color.cyan, visible=0)
t77 = label(pos=(-14,-8,-12.2), text="(-14,-8,-12)",box=0,opacity=0, color=color.cyan, visible=0)
t777 = label(pos=(-12,-12,-10.2), text="(-12,-12,-10)",box=0,opacity=0, color=color.cyan, visible=0)
t7777 = points(pos=[(-8,-8,-8), (-14,-8,-12), (-12,-12,-10), ( -2, -2, -2)],size=6, color=color.cyan, visible=0)
t77777 = label(pos=(-2,-2,-2), text="(-2,-2,-2)",box=0,opacity=0, color=color.cyan, visible=0)

#8) Zrcaljenje s obzirom na xy-ravninu
trokut8 = convex(pos=[(1,1,-1), (4,1,-3), (3,3,-2)], color=color.blue, visible=0)
t8 = label(pos=(1,1,-1.5), text="(1,1,-1)",box=0,opacity=0, color=color.cyan, visible=0)
t88 = label(pos=(4,1,-3.5), text="(4,1,-3)",box=0,opacity=0, color=color.cyan, visible=0)
t888 = label(pos=(3,3,-2.5), text="(3,3,-2)",box=0,opacity=0, color=color.cyan, visible=0)
t8888 = points(pos=[(1,1,-1), (4,1,-3), (3,3,-2)],size=6, color=color.cyan, visible=0)

#9) Zrcaljenje s obzirom na xz-ravninu
trokut9 = convex(pos=[(1,-1,1), (4,-1,3), (3,-3,2)], color=color.blue, visible=0)
t9 = label(pos=(1,-1,1.5), text="(1,-1,1)",box=0,opacity=0, color=color.cyan, visible=0)
t99 = label(pos=(4,-1,3.5), text="(4,-1,3)",box=0,opacity=0, color=color.cyan, visible=0)
t999 = label(pos=(3,-3,2.5), text="(3,-3,2)",box=0,opacity=0, color=color.cyan, visible=0)
t9999 = points(pos=[(1,-1,1), (4,-1,3), (3,-3,2)],size=6, color=color.cyan, visible=0)

#0) Zrcaljenje s obzirom na yz-ravninu
trokut0 = convex(pos=[(-1,1,1), (-4,1,3), (-3,3,2)], color=color.blue, visible=0)
t0 = label(pos=(-1,1,1.5), text="(-1,1,1)",box=0,opacity=0, color=color.cyan, visible=0)
t00 = label(pos=(-4,1,3.5), text="(-4,1,3)",box=0,opacity=0, color=color.cyan, visible=0)
t000 = label(pos=(-3,3,2.5), text="(-3,3,2)",box=0,opacity=0, color=color.cyan, visible=0)
t0000 = points(pos=[(-1,1,1), (-4,1,3), (-3,3,2)],size=6, color=color.cyan, visible=0)

#R) Rastezanje duz koordinatnih osi sa faktorima=1.5
trokutr = convex(pos=[(1.5,1.5,1.5), (6,1.5,4.5), (4.5,4.5,3)], color=color.blue, visible=0)
tr = label(pos=(1.5,1.5,2), text="(1.5,1.5,1.5)",box=0,opacity=0, color=color.cyan, visible=0)
trr = label(pos=(6,1.5,5), text="(6,1.5,4.5)",box=0,opacity=0, color=color.cyan, visible=0)
trrr = label(pos=(4.5,4.5,3.5), text="(4.5,4.5,3)",box=0,opacity=0, color=color.cyan, visible=0)
trrrr = points(pos=[(1.5,1.5,1.5), (6,1.5,4.5), (4.5,4.5,3)],size=6, color=color.cyan, visible=0)
trrrrr = label(pos=(-1,-1,2),text="Faktori=1.5",box=0,opacity=0,color=color.red, visible=0)

#T) Centralna simetrija sa centrom u ishodistu
trokutt = convex(pos=[(-1,-1,-1), (-4,-1,-3), (-3,-3,-2)], color=color.blue, visible=0)
tt = label(pos=(-1,-1,-1.5), text="(-1,-1,-1)",box=0,opacity=0, color=color.cyan, visible=0)
ttt = label(pos=(-4,-1,-3.5), text="(-4,-1,-3)",box=0,opacity=0, color=color.cyan, visible=0)
tttt = label(pos=(-3,-3,-2.5), text="(-3,-3,-2)",box=0,opacity=0, color=color.cyan, visible=0)
ttttt = points(pos=[(-1,-1,-1), (-4,-1,-3), (-3,-3,-2)],size=6, color=color.cyan, visible=0)

#Z) Centralna simetrija sa centrom u tocku ( , , )
trokutz = convex(pos=[(-1,-1,-1), (-4,-1,-3), (-3,-3,-2)], color=color.blue, visible=0)
tz = label(pos=(-1,-1,-1.5), text="(-1,-1,-1)",box=0,opacity=0, color=color.cyan, visible=0)
tzz = label(pos=(-4,-1,-3.5), text="(-4,-1,-3)",box=0,opacity=0, color=color.cyan, visible=0)
tzzz = label(pos=(-3,-3,-2.5), text="(-3,-3,-2)",box=0,opacity=0, color=color.cyan, visible=0)
tzzzz = points(pos=[(3,0,2),(4,-1,4), (4,-1,3), (1,-3,1)],size=6, color=color.cyan, visible=0)
tzzzzz=label(pos=(3,0.5,2),text="(3,0,2) TOCKA SIMETRIJE",box=0,opacity=0,color=color.red, visible=0)

#U) Ortogonalna projekcija na os x
trokutu=cylinder(pos=(1,0,0), axis=(3,0,0), radius = 0.06, color=color.blue, visible=0)
tu = label(pos=(1,0,0), text="(1,0,0)",box=0,opacity=0, color=color.cyan, visible=0)
tuu = label(pos=(4,0,0), text="(4,0,0)",box=0,opacity=0, color=color.cyan, visible=0)
tuuu = points(pos=[(1,0,0), (4,0,0)],size=6, color=color.cyan, visible=0)

#I) Ortogonalna projekcija na os y
trokuti=cylinder(pos=(0,1,0), axis=(0,2,0), radius = 0.06, color=color.blue, visible=0)
ti = label(pos=(0,1,0), text="(0,1,0)",box=0,opacity=0, color=color.cyan, visible=0)
tii = label(pos=(0,3,0), text="(0,3,0)",box=0,opacity=0, color=color.cyan, visible=0)
tiii = points(pos=[(0,1,0), (0,3,0)],size=6, color=color.cyan, visible=0)

#O) Ortogonalna projekcija na os z
trokuto=cylinder(pos=(0,0,1), axis=(0,0,2), radius = 0.06, color=color.blue, visible=0)
to = label(pos=(0,0,1), text="(0,0,1)",box=0,opacity=0, color=color.cyan, visible=0)
too = label(pos=(0,0,3), text="(0,0,3)",box=0,opacity=0, color=color.cyan, visible=0)
tooo = points(pos=[(0,0,3), (0,0,1)],size=6, color=color.cyan, visible=0)

#P) Ortogonalna projekcija na os xy-ravninu
trokutp = convex(pos=[(1,1,0), (4,1,0), (3,3,0)], color=color.blue, visible=0)
tp = label(pos=(1,1,0), text="(1,1,0)",box=0,opacity=0, color=color.cyan, visible=0)
tpp = label(pos=(4,1,0), text="(4,1,0)",box=0,opacity=0, color=color.cyan, visible=0)
tppp = label(pos=(3,3,0), text="(3,3,0)",box=0,opacity=0, color=color.cyan, visible=0)
tpppp = points(pos=[(1,1,0), (4,1,0), (3,3,0)],size=6, color=color.cyan, visible=0)

#A) Ortogonalna projekcija na os xz-ravninu
trokuta = convex(pos=[(1,0,1), (4,0,3), (3,0,2)], color=color.blue, visible=0)
ta = label(pos=(1,0,1), text="(1,0,1)",box=0,opacity=0, color=color.cyan, visible=0)
taa = label(pos=(4,0,3), text="(4,0,3)",box=0,opacity=0, color=color.cyan, visible=0)
taaa = label(pos=(3,0,2), text="(3,0,2)",box=0,opacity=0, color=color.cyan, visible=0)
taaaa = points(pos=[(1,0,1), (4,0,3), (3,0,2)],size=6, color=color.cyan, visible=0)

#S) Ortogonalna projekcija na os yz-ravninu
trokuts = convex(pos=[(0,1,1), (0,1,3), (0,3,2)], color=color.blue, visible=0)
ts = label(pos=(0,1,1), text="(0,1,1)",box=0,opacity=0, color=color.cyan, visible=0)
tss = label(pos=(0,1,3), text="(0,1,3)",box=0,opacity=0, color=color.cyan, visible=0)
tsss = label(pos=(0,3,2), text="(0,3,2)",box=0,opacity=0, color=color.cyan, visible=0)
tssss = points(pos=[(0,1,1), (0,1,3), (0,3,2)],size=6, color=color.cyan, visible=0)

#D) Smicanje (uzduzne deformacije)
trokutd = convex(pos=[(4.46, 4.46, 4.46), (10.93, 13.13, 11.66), (11.66, 11.66, 12.39)], color=color.blue, visible=0)
td = label(pos=(4.46, 4.46, 4.46), text="(4.46, 4.46, 4.46)",box=0,opacity=0, color=color.cyan, visible=0)
tdd = label(pos=(10.93, 13.13, 11.66), text="(10.93, 13.13, 11.66)",box=0,opacity=0, color=color.cyan, visible=0)
tddd = label(pos=(11.66, 11.66, 12.39), text="(11.66, 11.66, 12.39)",box=0,opacity=0, color=color.cyan, visible=0)
tdddd = points(pos=[(4.46, 4.46, 4.46), (10.93, 13.13, 11.66), (11.66, 11.66, 12.39)],size=6, color=color.cyan, visible=0)
tddddd=label(pos=(-1,-1,2),text="alfa = 60\nbeta = 60\ngama = 60",box=0, opacity=0,color=color.yellow, visible=0)

#help
pomoc1 = label(pos=(-8,3.3,0), text = '1) Translacija za vektor v', box=0, opacity=0, visible=0)
pomoc2 = label(pos=(-8,3,0), text = '2) Rotacija oko osi x za 180 stupnjeva', box=0, opacity=0, visible=0)
pomoc3 = label(pos=(-8,2.7,0), text = '3) Rotacija oko osi y za 180 stupnjeva', box=0, opacity=0, visible=0)
pomoc4 = label(pos=(-8,2.4,0), text = '4) Rotacija oko osi z za 180 stupnjeva', box=0, opacity=0, visible=0)
pomoc5 = label(pos=(-8,2.1,0), text = '5) Homotetija za faktor k=-2 sa centrom u ishodistu', box=0, opacity=0, visible=0)
pomoc6 = label(pos=(-8,1.8,0), text = '6) Rotacija oko proizvoljnog pravca', box=0, opacity=0, visible=0)
pomoc7 = label(pos=(-8,1.5,0), text = '7) Homotetija za faktor k=-1 sa centrom u tocki ( -2, -2, -2)', box=0, opacity=0, visible=0)
pomoc8 = label(pos=(-8,1.2,0), text = '8) Zrcaljenje s obzirom na xy-ravninu', box=0, opacity=0, visible=0)
pomoc9 = label(pos=(-8,0.9,0), text = '9) Zrcaljenje s obzirom na xz-ravninu', box=0, opacity=0, visible=0)
pomoc0 = label(pos=(-8,0.6,0), text = '0) Zrcaljenje s obzirom na yz-ravninu', box=0, opacity=0, visible=0)
pomocq = label(pos=(-8,0.3,0), text = 'Q) Zrcaljenje s obzirom na os x', box=0, opacity=0, visible=0)
pomocw = label(pos=(-8,0,0), text = 'W) Zrcaljenje s obzirom na os y', box=0, opacity=0, visible=0)
pomoce = label(pos=(-8,-0.3,0), text = 'E) Zrcaljenje s obzirom na os z', box=0, opacity=0, visible=0)
pomocr = label(pos=(-8,-0.6,0), text = 'R) Rastezanje duz koordinatnih osi sa faktorima=1.5', box=0, opacity=0, visible=0)
pomoct = label(pos=(-8,-0.9,0), text = 'T) Centralna simetrija sa centrom u ishodistu', box=0, opacity=0, visible=0)
pomocz = label(pos=(-8,-1.2,0), text = 'Z) Centralna simetrija sa centrom u tocku ( , , )', box=0, opacity=0, visible=0)
pomocu = label(pos=(-8,-1.5,0), text = 'U) Ortogonalna projekcija na os x', box=0, opacity=0, visible=0)
pomoci = label(pos=(-8,-1.8,0), text = 'I) Ortogonalna projekcija na os y', box=0, opacity=0, visible=0)
pomoco = label(pos=(-8,-2.1,0), text = 'O) Ortogonalna projekcija na os z', box=0, opacity=0, visible=0)
pomocp = label(pos=(-8,-2.4,0), text = 'P) Ortogonalna projekcija na xy-ravninu', box=0, opacity=0, visible=0)
pomoca = label(pos=(-8,-2.7,0), text = 'A) Ortogonalna projekcija na xz-ravninu', box=0, opacity=0, visible=0)
pomocs = label(pos=(-8,-3,0), text = 'S) Ortogonalna projekcija na yz-ravninu', box=0, opacity=0, visible=0)
pomocd = label(pos=(-8,-3.3,0), text = 'D) Smicanje (uzduzne deformacije)', box=0, opacity=0, visible=0)

#vidljivost
while 1:
    if scene.kb.keys:
        s = scene.kb.getkey()
        if s == '1':
            if trokut1.visible == 1:
                t1.visible=0
                t11.visible=0
                t111.visible=0
                t1111.visible=0
                t11111.visible=0
                trokut1.visible = 0
            else:
                trokut1.visible = 1
                t1.visible=1
                t11.visible=1
                t111.visible=1
                t1111.visible=1
                t11111.visible=1
        if s == '2' or s == 'q':
            if trokut2.visible == 1:
                t2.visible=0
                t22.visible=0
                t222.visible=0
                t2222.visible=0
                trokut2.visible = 0
            else:
                trokut2.visible = 1
                t2.visible=1
                t22.visible=1
                t222.visible=1
                t2222.visible=1
        if s == '3' or s == 'w':
            if trokut3.visible == 1:
                t3.visible=0
                t33.visible=0
                t333.visible=0
                t3333.visible=0
                trokut3.visible = 0
            else:
                trokut3.visible = 1
                t3.visible=1
                t33.visible=1
                t333.visible=1
                t3333.visible=1
        if s == 'd':
            if trokutd.visible == 1:
                td.visible=0
                tdd.visible=0
                tddd.visible=0
                tdddd.visible=0
                tddddd.visible=0
                trokutd.visible = 0
            else:
                trokutd.visible = 1
                td.visible=1
                tdd.visible=1
                tddd.visible=1
                tdddd.visible=1
                tddddd.visible=1
        if s == '6':
            if trokut6.visible == 1:
                t6.visible=0
                t66.visible=0
                t666.visible=0
                t6666.visible=0
                t66666.visible=0
                trokut6.visible = 0
            else:
                trokut6.visible = 1
                t6.visible=1
                t66.visible=1
                t666.visible=1
                t6666.visible=1
                t66666.visible=1
        if s == '4' or s == 'e':
            if trokut4.visible == 1:
                t4.visible=0
                t44.visible=0
                t444.visible=0
                t4444.visible=0
                trokut4.visible = 0
            else:
                trokut4.visible = 1
                t4.visible=1
                t44.visible=1
                t444.visible=1
                t4444.visible=1
        if s == '5':
            if trokut5.visible == 1:
                t5.visible=0
                t55.visible=0
                t555.visible=0
                t5555.visible=0
                trokut5.visible = 0
            else:
                trokut5.visible = 1
                t5.visible=1
                t55.visible=1
                t555.visible=1
                t5555.visible=1
        if s == 'r':
            if trokutr.visible == 1:
                tr.visible=0
                trr.visible=0
                trrr.visible=0
                trrrr.visible=0
                trrrrr.visible=0
                trokutr.visible = 0
            else:
                trokutr.visible = 1
                tr.visible=1
                trr.visible=1
                trrr.visible=1
                trrrr.visible=1
                trrrrr.visible=1
        if s == '7':
            if trokut7.visible == 1:
                t7.visible=0
                t77.visible=0
                t777.visible=0
                t7777.visible=0
                t77777.visible=0
                trokut7.visible = 0
            else:
                trokut7.visible = 1
                t7.visible=1
                t77.visible=1
                t777.visible=1
                t7777.visible=1
                t77777.visible=1
        if s == '8':
            if trokut8.visible == 1:
                t8.visible=0
                t88.visible=0
                t888.visible=0
                t8888.visible=0
                trokut8.visible = 0
            else:
                trokut8.visible = 1
                t8.visible=1
                t88.visible=1
                t888.visible=1
                t8888.visible=1
        if s == '9':
            if trokut9.visible == 1:
                t9.visible=0
                t99.visible=0
                t999.visible=0
                t9999.visible=0
                trokut9.visible = 0
            else:
                trokut9.visible = 1
                t9.visible=1
                t99.visible=1
                t999.visible=1
                t9999.visible=1
        if s == '0':
            if trokut0.visible == 1:
                t0.visible=0
                t00.visible=0
                t000.visible=0
                t0000.visible=0
                trokut0.visible = 0
            else:
                trokut0.visible = 1
                t0.visible=1
                t00.visible=1
                t000.visible=1
                t0000.visible=1
        if s == 't':
            if trokutt.visible == 1:
                tt.visible=0
                ttt.visible=0
                tttt.visible=0
                trokutt.visible = 0
            else:
                trokutt.visible = 1
                tt.visible=1
                ttt.visible=1
                tttt.visible=1
        if s == 'z':
            if trokutz.visible == 1:
                tz.visible=0
                tzz.visible=0
                tzzz.visible=0
                tzzzz.visible=0
                tzzzzz.visible=0
                trokutu.visible = 0
            else:
                trokutz.visible = 1
                tz.visible=1
                tzz.visible=1
                tzzz.visible=1
                tzzzz.visible=1
                tzzzzz.visible=1
        if s == 'u':
            if trokutu.visible == 1:
                tu.visible=0
                tuu.visible=0
                tuuu.visible=0
                trokutu.visible = 0
            else:
                trokutu.visible = 1
                tu.visible=1
                tuu.visible=1
                tuuu.visible=1
        if s == 'i':
            if trokuti.visible == 1:
                ti.visible=0
                tii.visible=0
                tiii.visible=0
                trokuti.visible = 0
            else:
                trokuti.visible = 1
                ti.visible=1
                tii.visible=1
                tiii.visible=1
        if s == 'o':
            if trokuto.visible == 1:
                to.visible=0
                too.visible=0
                tooo.visible=0
                trokuto.visible = 0
            else:
                trokuto.visible = 1
                to.visible=1
                too.visible=1
                tooo.visible=1
        if s == 'p':
            if trokutp.visible == 1:
                tp.visible=0
                tpp.visible=0
                tppp.visible=0
                trokutp.visible = 0
            else:
                trokutp.visible = 1
                tp.visible=1
                tpp.visible=1
                tppp.visible=1
        if s == 'a':
            if trokuta.visible == 1:
                ta.visible=0
                taa.visible=0
                taaa.visible=0
                trokuta.visible = 0
            else:
                trokuta.visible = 1
                ta.visible=1
                taa.visible=1
                taaa.visible=1
        if s == 's':
            if trokuts.visible == 1:
                ts.visible=0
                tss.visible=0
                tsss.visible=0
                trokuts.visible = 0
            else:
                trokuts.visible = 1
                ts.visible=1
                tss.visible=1
                tsss.visible=1
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
            
            