from visual import*

scene = display(title='F1 - Prikazi pomoc || F2 - Sakrij pomoc', width=900, height=900)

scene.lights = [distant_light(direction=(0.22, 0.44, 0.88), color=color.gray(0.8)),
                distant_light(direction=(-0.22,-0.44,-0.88),color=color.gray(0.8)),
                distant_light(direction=(0,0.88,0),color=color.gray(0.6)),
                distant_light(direction=(0,-0.88,0),color=color.gray(0.6))
                ]

#koordinatni sustav
curve(pos=[(-5.5,0,0),(5.5,0,0)],radius = 0.05, color=color.white)
curve(pos=[(0,-5.5,0),(0,5.5,0)],radius = 0.05, color=color.white)
curve(pos=[(0,0,-5.5),(0,0,5.5)],radius = 0.05, color=color.white)

#tocke
for x in range(1,6):
    sphere(pos=vector(x,0,0),radius=0.06, color=color.red)
    sphere(pos=vector(0,x,0),radius=0.06, color=color.red)
    sphere(pos=vector(0,0,x),radius=0.06, color=color.red)
    sphere(pos=vector(-x,0,0),radius=0.06, color=color.red)
    sphere(pos=vector(0,-x,0),radius=0.06, color=color.red)
    sphere(pos=vector(0,0,-x),radius=0.06, color=color.red)

#oznake tocaka
label(pos=(5.8,0,0), text = 'X',box = 0,height=30,color=color.red)
label(pos=(1,0,-0.3),text="1",opacity=0,box=0,height=20 ,color=color.red)

label(pos=(0,5.8,0), text = 'Y',box = 0,height=30,color=color.red)
label(pos=(0,1,-0.3),text="1",opacity=0,box=0,height=20 ,color=color.red)

label(pos=(0,0,5.8), text = 'Z',box = 0,height=30,color=color.red)
label(pos=(0,-0.3,1),text="1",opacity=0,box=0,height=20 ,color=color.red)

#sfere
sphere(pos=(1,0,0),radius=1,color=color.green,opacity=0.7)
label(pos=(1,0,0),text="(1,0,0)",box=0, opacity=0,color=color.blue)
points(pos=[(1,0,0)], size=6, color=color.yellow)

#1) Translacija za vektor v
sfera1=sphere(pos=(-2,-2,1),radius=1,color=color.red,opacity=0.7, visible=0)
s1=label(pos=(-2,-2,1),text="(-2,-2, 1)",box=0, opacity=0,color=color.yellow, visible=0)
s11=points(pos=[(-2,-2,1)], size=6, color=color.blue, visible=0)
s111=label(pos=(-3,-3.2),text="Translacija za vektor v = (-3, -2, 1)",box=0,opacity=0,color=color.cyan, visible=0)

#2) Rotacija oko osi x za 180 stupnjeva
#Q) Zrcaljenje s obzirom na os x
#8) Zrcaljenje s obzirom na xy-ravninu
#9) Zrcaljenje s obzirom na xz-ravninu
sfera2=sphere(pos=(1,0,0),radius=1,color=color.red,opacity=0.7, visible=0)
s2=label(pos=(1,0,0),text="(1,0,0)",box=0, opacity=0,color=color.yellow, visible=0)
s22=points(pos=[(1,0,0)], size=6, color=color.blue, visible=0)

#3) Rotacija oko osi y za 180 stupnjeva
#W) Zrcaljenje s obzirom na os y
#4) Rotacija oko osi z za 180 stupnjeva
#E) Zrcaljenje s obzirom na os z
#0) Zrcaljenje s obzirom na yz-ravninu
#T) Centralna simetrija sa centrom u ishodistu 
sfera3=sphere(pos=(-1,0,0),radius=1,color=color.red,opacity=0.7, visible=0)
s3=label(pos=(-1,0,0),text="(-1,0,0)",box=0, opacity=0,color=color.yellow, visible=0)
s33=points(pos=[(-1,0,0)], size=6, color=color.blue, visible=0)

#5) Homotetija za faktor k=-2 sa centrom u ishodistu
sfera5=sphere(pos=(-2,0,0),radius=1,color=color.red,opacity=0.7, visible=0)
s5=label(pos=(-2,0,0),text="(-2,0,0)",box=0, opacity=0,color=color.yellow, visible=0)
s55=points(pos=[(-2,0,0)], size=6, color=color.blue, visible=0)

#6) Rotacija oko proizvoljnog pravca
sfera6=sphere(pos=(-0.33,0.66,0.66),radius=1,color=color.red,opacity=0.7, visible=0)
s6=label(pos=(-0.33,0.66,0.66),text="(-0.33,0.66,0.66)",box=0, opacity=0,color=color.yellow, visible=0)
s66=points(pos=[(-0.33,0.66,0.66)], size=6, color=color.blue, visible=0)
s666=label(pos=(-1,-1,2),text="v = (1,1,1)\nkut = 180",box=0, opacity=0,color=color.yellow, visible=0)

#7) Homotetija za faktor k=-2 sa centrom u tocki (-2, -2, -2)
sfera7=sphere(pos=(-8,-6,-6),radius=1,color=color.red,opacity=0.7, visible=0)
s7=label(pos=(-8,-6,-6),text="(-8,-6,-6)",box=0, opacity=0,color=color.yellow, visible=0)
s77=points(pos=[(-2,-2,-2), (-8, -6,-6)], size=6, color=color.blue, visible=0)
s777=label(pos=(-2, -2, -2),text="(-2,-2,-2)",box=0,opacity=0,color=color.cyan, visible=0)

#R) Rastezanje duz koordinatnih osi sa faktorima
sferar=ellipsoid(pos=(2, 0,0), length=3, height=3, width=5, color=color.red,opacity=0.7, visible=0)
sr=label(pos=(2,0,0),text="(2,0,0)",box=0, opacity=0,color=color.yellow, visible=0)
srr=points(pos=[(2,0,0)], size=6, color=color.blue, visible=0)
srrr=label(pos=(-1,-1,2),text="kx = 2\nky = 3\nkz = 5",box=0,opacity=0,color=color.red, visible=0)


#Z) Centralna simetrija sa centrom u tocku (1,-2,0)
sferaz=sphere(pos=(1,-4,-0),radius=1,color=color.red,opacity=0.7, visible=0)
sz=label(pos=(1,-4,0),text="(1,-4,0)",box=0, opacity=0,color=color.yellow, visible=0)
szz=points(pos=[(1,0,0),(1,-2,0)], size=6, color=color.blue, visible=0)
szzz=label(pos=(1,-2.5,0),text="(1,-2,0) TOCKA SIMETRIJE",box=0,opacity=0,color=color.cyan, visible=0)

#U) Ortogonalna projekcija na os x
sferau=cylinder(pos=(0,0,0), axis=(2,0,0), radius = 0.06, color=color.blue, visible=0)
su=points(pos=[(0,0,0), (2,0,0)],size=6, color=color.cyan, visible=0)
suu=label(pos=(0,0,0),text="(0,0,0)",box=0,opacity=0,color=color.cyan, visible=0)
suuu=label(pos=(2,0,0),text="(2,0,0)",box=0,opacity=0,color=color.cyan, visible=0)

#I) Ortogonalna projekcija na os y
sferai=cylinder(pos=(0,-1,0), axis=(0,2,0), radius = 0.06, color=color.blue, visible=0)
si=points(pos=[(0,1,0), (0,-1,0)],size=6, color=color.cyan, visible=0)
sii=label(pos=(0,1,0),text="(0,1,0)",box=0,opacity=0,color=color.cyan, visible=0)
siii=label(pos=(0,-1,0),text="(0,-1,0)",box=0,opacity=0,color=color.cyan, visible=0)

#O) Ortogonalna projekcija na os z
sferao=cylinder(pos=(0,0,1), axis=(0,0,-2), radius = 0.06, color=color.blue, visible=0)
so=points(pos=[(0,0,1), (0,0,-1)],size=6, color=color.cyan, visible=0)
soo=label(pos=(0,0,1),text="(0,0,1)",box=0,opacity=0,color=color.cyan, visible=0)
sooo=label(pos=(0,0,-1),text="(0,0,-1)",box=0,opacity=0,color=color.cyan, visible=0)

#P) Ortogonalna projekcija na os xy-ravninu
sferap=ring(pos=(1,0,0), axis=(0,0,1), radius=1, thickness=0.01, color=color.red, visible=0)
sp=ring(pos=(1,0,0), axis=(0,0,1), radius=0.95, thickness=0.05, color=color.red, visible=0)
spp=ring(pos=(1,0,0), axis=(0,0,1), radius=0.90, thickness=0.05, color=color.red, visible=0)
sppp=ring(pos=(1,0,0), axis=(0,0,1), radius=0.85, thickness=0.05, color=color.red, visible=0)
spppp=ring(pos=(1,0,0), axis=(0,0,1), radius=0.80, thickness=0.05, color=color.red, visible=0)
sppppp=ring(pos=(1,0,0), axis=(0,0,1), radius=0.75, thickness=0.05, color=color.red, visible=0)
spppppp=ring(pos=(1,0,0), axis=(0,0,1), radius=0.70, thickness=0.05, color=color.red, visible=0)
sppppppp=ring(pos=(1,0,0), axis=(0,0,1), radius=0.65, thickness=0.05, color=color.red, visible=0)
spppppppp=ring(pos=(1,0,0), axis=(0,0,1), radius=0.60, thickness=0.05, color=color.red, visible=0)
sppppppppp=ring(pos=(1,0,0), axis=(0,0,1), radius=0.55, thickness=0.05, color=color.red, visible=0)
spppppppppp=ring(pos=(1,0,0), axis=(0,0,1), radius=0.50, thickness=0.05, color=color.red, visible=0)
sppppppppppp=ring(pos=(1,0,0), axis=(0,0,1), radius=0.45, thickness=0.05, color=color.red, visible=0)
spppppppppppp=ring(pos=(1,0,0), axis=(0,0,1), radius=0.40, thickness=0.05, color=color.red, visible=0)
sppppppppppppp=ring(pos=(1,0,0), axis=(0,0,1), radius=0.35, thickness=0.05, color=color.red, visible=0)
spppppppppppppp=ring(pos=(1,0,0), axis=(0,0,1), radius=0.30, thickness=0.05, color=color.red, visible=0)
sppppppppppppppp=ring(pos=(1,0,0), axis=(0,0,1), radius=0.25, thickness=0.05, color=color.red, visible=0)
spppppppppppppppp=ring(pos=(1,0,0), axis=(0,0,1), radius=0.20, thickness=0.05, color=color.red, visible=0)
sppppppppppppppppp=ring(pos=(1,0,0), axis=(0,0,1), radius=0.15, thickness=0.05, color=color.red, visible=0)
spppppppppppppppppp=ring(pos=(1,0,0), axis=(0,0,1), radius=0.10, thickness=0.05, color=color.red, visible=0)
sppppppppppppppppppp=ring(pos=(1,0,0), axis=(0,0,1), radius=0.5, thickness=0.05, color=color.red, visible=0)
spppppppppppppppppppp=ring(pos=(1,0,0), axis=(0,0,1), radius=0, thickness=0.05, color=color.red, visible=0)
sppppppppppppppppppppp=label(pos=(1,0,0),text="(1,0,0)",box=0, opacity=0,color=color.cyan, visible=0)
spppppppppppppppppppppp=points(pos=[(1,0,0)], size=6, color=color.cyan, visible=0)

#A) Ortogonalna projekcija na os xz-ravninu
sferaa=ring(pos=(1,0,0), axis=(0,1,0), radius=1, thickness=0.01, color=color.red, visible=0)
sa=ring(pos=(1,0,0), axis=(0,1,0), radius=0.95, thickness=0.05, color=color.red, visible=0)
saa=ring(pos=(1,0,0), axis=(0,1,0), radius=0.90, thickness=0.05, color=color.red, visible=0)
saaa=ring(pos=(1,0,0), axis=(0,1,0), radius=0.85, thickness=0.05, color=color.red, visible=0)
saaaa=ring(pos=(1,0,0), axis=(0,1,0), radius=0.80, thickness=0.05, color=color.red, visible=0)
saaaaa=ring(pos=(1,0,0), axis=(0,1,0), radius=0.75, thickness=0.05, color=color.red, visible=0)
saaaaaa=ring(pos=(1,0,0), axis=(0,1,0), radius=0.70, thickness=0.05, color=color.red, visible=0)
saaaaaaa=ring(pos=(1,0,0), axis=(0,1,0), radius=0.65, thickness=0.05, color=color.red, visible=0)
saaaaaaaa=ring(pos=(1,0,0), axis=(0,1,0), radius=0.60, thickness=0.05, color=color.red, visible=0)
saaaaaaaaa=ring(pos=(1,0,0), axis=(0,1,0), radius=0.55, thickness=0.05, color=color.red, visible=0)
saaaaaaaaaa=ring(pos=(1,0,0), axis=(0,1,0), radius=0.50, thickness=0.05, color=color.red, visible=0)
saaaaaaaaaaa=ring(pos=(1,0,0), axis=(0,1,0), radius=0.45, thickness=0.05, color=color.red, visible=0)
saaaaaaaaaaaa=ring(pos=(1,0,0), axis=(0,1,0), radius=0.40, thickness=0.05, color=color.red, visible=0)
saaaaaaaaaaaaa=ring(pos=(1,0,0), axis=(0,1,0), radius=0.35, thickness=0.05, color=color.red, visible=0)
saaaaaaaaaaaaaa=ring(pos=(1,0,0), axis=(0,1,0), radius=0.30, thickness=0.05, color=color.red, visible=0)
saaaaaaaaaaaaaaa=ring(pos=(1,0,0), axis=(0,1,0), radius=0.25, thickness=0.05, color=color.red, visible=0)
saaaaaaaaaaaaaaaa=ring(pos=(1,0,0), axis=(0,1,0), radius=0.20, thickness=0.05, color=color.red, visible=0)
saaaaaaaaaaaaaaaaa=ring(pos=(1,0,0), axis=(0,1,0), radius=0.15, thickness=0.05, color=color.red, visible=0)
saaaaaaaaaaaaaaaaaa=ring(pos=(1,0,0), axis=(0,1,0), radius=0.10, thickness=0.05, color=color.red, visible=0)
saaaaaaaaaaaaaaaaaaa=ring(pos=(1,0,0), axis=(0,1,0), radius=0.5, thickness=0.05, color=color.red, visible=0)
saaaaaaaaaaaaaaaaaaaa=ring(pos=(1,0,0), axis=(0,1,0), radius=0, thickness=0.05, color=color.red, visible=0)
saaaaaaaaaaaaaaaaaaaaa=label(pos=(1,0,0),text="(1,0,0)",box=0, opacity=0,color=color.cyan, visible=0)
saaaaaaaaaaaaaaaaaaaaaa=points(pos=[(1,0,0)], size=6, color=color.cyan, visible=0)

#S) Ortogonalna projekcija na os yz-ravninu
sferas=ring(pos=(0,0,0), axis=(1,0,0), radius=1, thickness=0.01, color=color.red, visible=0)
ss=ring(pos=(0,0,0), axis=(1,0,0), radius=0.95, thickness=0.05, color=color.red, visible=0)
sss=ring(pos=(0,0,0), axis=(1,0,0), radius=0.90, thickness=0.05, color=color.red, visible=0)
ssss=ring(pos=(0,0,0), axis=(1,0,0), radius=0.85, thickness=0.05, color=color.red, visible=0)
sssss=ring(pos=(0,0,0), axis=(1,0,0), radius=0.80, thickness=0.05, color=color.red, visible=0)
ssssss=ring(pos=(0,0,0), axis=(1,0,0), radius=0.75, thickness=0.05, color=color.red, visible=0)
sssssss=ring(pos=(0,0,0), axis=(1,0,0), radius=0.70, thickness=0.05, color=color.red, visible=0)
ssssssss=ring(pos=(0,0,0), axis=(1,0,0), radius=0.65, thickness=0.05, color=color.red, visible=0)
sssssssss=ring(pos=(0,0,0), axis=(1,0,0), radius=0.60, thickness=0.05, color=color.red, visible=0)
ssssssssss=ring(pos=(0,0,0), axis=(1,0,0), radius=0.55, thickness=0.05, color=color.red, visible=0)
sssssssssss=ring(pos=(0,0,0), axis=(1,0,0), radius=0.50, thickness=0.05, color=color.red, visible=0)
ssssssssssss=ring(pos=(0,0,0), axis=(1,0,0), radius=0.45, thickness=0.05, color=color.red, visible=0)
sssssssssssss=ring(pos=(0,0,0), axis=(1,0,0), radius=0.40, thickness=0.05, color=color.red, visible=0)
ssssssssssssss=ring(pos=(0,0,0), axis=(1,0,0), radius=0.35, thickness=0.05, color=color.red, visible=0)
sssssssssssssss=ring(pos=(0,0,0), axis=(1,0,0), radius=0.30, thickness=0.05, color=color.red, visible=0)
ssssssssssssssss=ring(pos=(0,0,0), axis=(1,0,0), radius=0.25, thickness=0.05, color=color.red, visible=0)
sssssssssssssssss=ring(pos=(0,0,0), axis=(1,0,0), radius=0.20, thickness=0.05, color=color.red, visible=0)
ssssssssssssssssss=ring(pos=(0,0,0), axis=(1,0,0), radius=0.15, thickness=0.05, color=color.red, visible=0)
sssssssssssssssssss=ring(pos=(0,0,0), axis=(1,0,0), radius=0.10, thickness=0.05, color=color.red, visible=0)
ssssssssssssssssssss=ring(pos=(0,0,0), axis=(1,0,0), radius=0.5, thickness=0.05, color=color.red, visible=0)
sssssssssssssssssssss=ring(pos=(0,0,0), axis=(1,0,0), radius=0, thickness=0.05, color=color.red, visible=0)
ssssssssssssssssssssss=label(pos=(0,0,0),text="(0,0,0)",box=0, osacity=0,color=color.cyan, visible=0)
sssssssssssssssssssssss=points(sos=[(0,0,0)], size=6, color=color.cyan, visible=0)

#D) Smicanje (uzduzne deformacije)
sferad=sphere(pos=(1,1.73,1.73),radius=1,color=color.red,opacity=0.7, visible=0)
sd=label(pos=(1,1.73,1.73),text="(1,1.73,1.73)",box=0, opacity=0,color=color.yellow, visible=0)
sdd=points(pos=[(1,1.73,1.73)], size=6, color=color.blue, visible=0)
sddd=label(pos=(-1,-1,2),text="alfa = 60\nbeta = 60\ngama = 60",box=0, opacity=0,color=color.yellow, visible=0)
sdddd=label(pos=(-3,-3.2),text="Sfera treba biti deformirana!",box=0,opacity=0,color=color.cyan, visible=0)


#help
pomoc1 = label(pos=(-8,3.3,0), text = '1) Translacija za vektor v', box=0, opacity=0, visible=0)
pomoc2 = label(pos=(-8,3,0), text = '2) Rotacija oko osi x za 180 stupnjeva', box=0, opacity=0, visible=0)
pomoc3 = label(pos=(-8,2.7,0), text = '3) Rotacija oko osi y za 180 stupnjeva', box=0, opacity=0, visible=0)
pomoc4 = label(pos=(-8,2.4,0), text = '4) Rotacija oko osi z za 180 stupnjeva', box=0, opacity=0, visible=0)
pomoc5 = label(pos=(-8,2.1,0), text = '5) Homotetija za faktor k sa centrom u ishodistu', box=0, opacity=0, visible=0)
pomoc6 = label(pos=(-8,1.8,0), text = '6) Rotacija oko proizvoljnog pravca', box=0, opacity=0, visible=0)
pomoc7 = label(pos=(-8,1.5,0), text = '7) Homotetija za faktor k=-2 sa centrom u tocki (-2, -2, -2)', box=0, opacity=0, visible=0)
pomoc8 = label(pos=(-8,1.2,0), text = '8) Zrcaljenje s obzirom na xy-ravninu', box=0, opacity=0, visible=0)
pomoc9 = label(pos=(-8,0.9,0), text = '9) Zrcaljenje s obzirom na xz-ravninu', box=0, opacity=0, visible=0)
pomoc0 = label(pos=(-8,0.6,0), text = '0) Zrcaljenje s obzirom na yz-ravninu', box=0, opacity=0, visible=0)
pomocq = label(pos=(-8,0.3,0), text = 'Q) Zrcaljenje s obzirom na os x', box=0, opacity=0, visible=0)
pomocw = label(pos=(-8,0,0), text = 'W) Zrcaljenje s obzirom na os y', box=0, opacity=0, visible=0)
pomoce = label(pos=(-8,-0.3,0), text = 'E) Zrcaljenje s obzirom na os z', box=0, opacity=0, visible=0)
pomocr = label(pos=(-8,-0.6,0), text = 'R) Rastezanje duz koordinatnih osi sa faktorima', box=0, opacity=0, visible=0)
pomoct = label(pos=(-8,-0.9,0), text = 'T) Centralna simetrija sa centrom u ishodistu', box=0, opacity=0, visible=0)
pomocz = label(pos=(-8,-1.2,0), text = 'Z) Centralna simetrija sa centrom u tocku (1, -2, 0)', box=0, opacity=0, visible=0)
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
            if sfera1.visible == 1:
                s1.visible=0
                s11.visible=0
                s111.visible=0
                sfera1.visible = 0
            else:
                sfera1.visible = 1
                s1.visible=1
                s11.visible=1
                s111.visible=1
        if s == '2' or s == 'q' or s == '8' or s == '9':
            if sfera2.visible == 1:
                s2.visible=0
                s22.visible=0
                sfera2.visible = 0
            else:
                sfera2.visible = 1
                s2.visible=1
                s22.visible=1
        if s == '3' or s == 'w' or s == '4' or s == 'e' or s == '0' or s =='t':
            if sfera3.visible == 1:
                s3.visible=0
                s33.visible=0
                sfera3.visible = 0
            else:
                sfera3.visible = 1
                s3.visible=1
                s33.visible=1
        if s == '5':
            if sfera5.visible == 1:
                s5.visible=0
                s55.visible=0
                sfera5.visible = 0
            else:
                sfera5.visible = 1
                s5.visible=1
                s55.visible=1
        if s == '7':
            if sfera7.visible == 1:
                s7.visible=0
                s77.visible=0
                s777.visible=0               
                sfera7.visible = 0
            else:
                sfera7.visible = 1
                s7.visible=1
                s77.visible=1
                s777.visible=1
        if s == 'r':
            if sferar.visible == 1:
                sr.visible=0
                srr.visible=0
                srrr.visible=0                
                sferar.visible = 0
            else:
                sferar.visible = 1
                sr.visible=1
                srr.visible=1
                srrr.visible=1
        if s == 'z':
            if sferaz.visible == 1:
                sz.visible=0
                szz.visible=0
                szzz.visible=0
                sferaz.visible = 0
            else:
                sferaz.visible = 1
                sz.visible=1
                szz.visible=1
                szzz.visible=1
        if s == 'u':
            if sferau.visible == 1:
                su.visible=0
                suu.visible=0
                suuu.visible=0
                sferau.visible = 0
            else:
                sferau.visible = 1
                su.visible=1
                suu.visible=1
                suuu.visible=1
        if s == 'i':
            if sferai.visible == 1:
                si.visible=0
                sii.visible=0
                siii.visible=0
                sferai.visible = 0
            else:
                sferai.visible = 1
                si.visible=1
                sii.visible=1
                siii.visible=1
        if s == 'o':
            if sferao.visible == 1:
                so.visible=0
                soo.visible=0
                sooo.visible=0
                sferao.visible = 0
            else:
                sferao.visible = 1
                so.visible=1
                soo.visible=1
                sooo.visible=1
        if s == 'p':
            if sferap.visible == 1:
                sp.visible=0
                spp.visible=0
                sppp.visible=0
                spppp.visible=0
                sppppp.visible=0
                spppppp.visible=0
                sppppppp.visible=0
                spppppppp.visible=0
                sppppppppp.visible=0
                spppppppppp.visible=0
                sppppppppppp.visible=0
                spppppppppppp.visible=0
                sppppppppppppp.visible=0
                spppppppppppppp.visible=0
                sppppppppppppppp.visible=0
                spppppppppppppppp.visible=0
                sppppppppppppppppp.visible=0
                spppppppppppppppppp.visible=0
                sppppppppppppppppppp.visible=0
                spppppppppppppppppppp.visible=0
                sppppppppppppppppppppp.visible=0
                spppppppppppppppppppppp.visible=0
                sferap.visible = 0
            else:
                sferap.visible = 1
                sp.visible=1
                spp.visible=1
                sppp.visible=1
                spppp.visible=1
                sppppp.visible=1
                spppppp.visible=1
                sppppppp.visible=1
                spppppppp.visible=1
                sppppppppp.visible=1
                spppppppppp.visible=1
                sppppppppppp.visible=1
                spppppppppppp.visible=1
                sppppppppppppp.visible=1
                spppppppppppppp.visible=1
                sppppppppppppppp.visible=1
                spppppppppppppppp.visible=1
                sppppppppppppppppp.visible=1
                spppppppppppppppppp.visible=1
                sppppppppppppppppppp.visible=1
                spppppppppppppppppppp.visible=1
                sppppppppppppppppppppp.visible=1
                spppppppppppppppppppppp.visible=1
        if s == 'a':
            if sferaa.visible == 1:
                sa.visible=0
                saa.visible=0
                saaa.visible=0
                saaaa.visible=0
                saaaaa.visible=0
                saaaaaa.visible=0
                saaaaaaa.visible=0
                saaaaaaaa.visible=0
                saaaaaaaaa.visible=0
                saaaaaaaaaa.visible=0
                saaaaaaaaaaa.visible=0
                saaaaaaaaaaaa.visible=0
                saaaaaaaaaaaaa.visible=0
                saaaaaaaaaaaaaa.visible=0
                saaaaaaaaaaaaaaa.visible=0
                saaaaaaaaaaaaaaaa.visible=0
                saaaaaaaaaaaaaaaaa.visible=0
                saaaaaaaaaaaaaaaaaa.visible=0
                saaaaaaaaaaaaaaaaaaa.visible=0
                saaaaaaaaaaaaaaaaaaaa.visible=0
                saaaaaaaaaaaaaaaaaaaaa.visible=0
                saaaaaaaaaaaaaaaaaaaaaa.visible=0
                sferaa.visible = 0
            else:
                sferaa.visible = 1
                sa.visible=1
                saa.visible=1
                saaa.visible=1
                saaaa.visible=1
                saaaaa.visible=1
                saaaaaa.visible=1
                saaaaaaa.visible=1
                saaaaaaaa.visible=1
                saaaaaaaaa.visible=1
                saaaaaaaaaa.visible=1
                saaaaaaaaaaa.visible=1
                saaaaaaaaaaaa.visible=1
                saaaaaaaaaaaaa.visible=1
                saaaaaaaaaaaaaa.visible=1
                saaaaaaaaaaaaaaa.visible=1
                saaaaaaaaaaaaaaaa.visible=1
                saaaaaaaaaaaaaaaaa.visible=1
                saaaaaaaaaaaaaaaaaa.visible=1
                saaaaaaaaaaaaaaaaaaa.visible=1
                saaaaaaaaaaaaaaaaaaaa.visible=1
                saaaaaaaaaaaaaaaaaaaaa.visible=1
                saaaaaaaaaaaaaaaaaaaaaa.visible=1
        if s == 's':
            if sferas.visible == 1:
                ss.visible=0
                sss.visible=0
                ssss.visible=0
                sssss.visible=0
                ssssss.visible=0
                sssssss.visible=0
                ssssssss.visible=0
                sssssssss.visible=0
                ssssssssss.visible=0
                sssssssssss.visible=0
                ssssssssssss.visible=0
                sssssssssssss.visible=0
                ssssssssssssss.visible=0
                sssssssssssssss.visible=0
                ssssssssssssssss.visible=0
                sssssssssssssssss.visible=0
                ssssssssssssssssss.visible=0
                sssssssssssssssssss.visible=0
                ssssssssssssssssssss.visible=0
                sssssssssssssssssssss.visible=0
                ssssssssssssssssssssss.visible=0
                sssssssssssssssssssssss.visible=0
                sferas.visible = 0
            else:
                sferas.visible = 1
                ss.visible=1
                sss.visible=1
                ssss.visible=1
                sssss.visible=1
                ssssss.visible=1
                sssssss.visible=1
                ssssssss.visible=1
                sssssssss.visible=1
                ssssssssss.visible=1
                sssssssssss.visible=1
                ssssssssssss.visible=1
                sssssssssssss.visible=1
                ssssssssssssss.visible=1
                sssssssssssssss.visible=1
                ssssssssssssssss.visible=1
                sssssssssssssssss.visible=1
                ssssssssssssssssss.visible=1
                sssssssssssssssssss.visible=1
                ssssssssssssssssssss.visible=1
                sssssssssssssssssssss.visible=1
                ssssssssssssssssssssss.visible=1
                sssssssssssssssssssssss.visible=1
        if s == 'd':
            if sferad.visible == 1:
                sd.visible=0
                sdd.visible=0
                sddd.visible=0
                sdddd.visible=0
                sferad.visible = 0
            else:
                sferad.visible = 1
                sd.visible=1
                sdd.visible=1
                sddd.visible=1
                sdddd.visible=1
        if s == '6':
            if sfera6.visible == 1:
                s6.visible=0
                s66.visible=0
                s666.visible=0
                sfera6.visible = 0
            else:
                sfera6.visible = 1
                s6.visible=1
                s66.visible=1
                s666.visible=1
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