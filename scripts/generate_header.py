from PIL import Image,ImageDraw,ImageFont
from pathlib import Path
import random
W,H,F=1200,270,120
rng=random.Random(9090)
font='/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf'
normal=ImageFont.truetype(font,17)
small=ImageFont.truetype(font,13)
# Index zero is truly transparent. Tails remain readable over light and dark themes.
colors=[(0,0,0),(8,70,47),(9,94,61),(7,121,76),(3,145,87),(0,168,99),(0,189,116),(31,210,139),(93,233,173),(53,214,148)]
palette=[v for rgb in colors for v in rgb]+[0]*(768-3*len(colors))
chars='01ABCDEFabcdef{}[]<>/;:=+*0123456789'
tokens=['if()','</>','{ }','=>','let','def','git','0xF','for','try','int','&&']
streams=[]
for i,x in enumerate(range(14,W-12,28)):
 length=rng.randint(6,12)
 streams.append((x,length,rng.random(),rng.choice([1,1,1,2]),[rng.choice(chars) for _ in range(length)],rng.choice(tokens),i))
frames=[]
for f in range(F):
 im=Image.new('P',(W,H),0);im.putpalette(palette);d=ImageDraw.Draw(im)
 for x,n,offset,cycles,letters,token,i in streams:
  period=H+n*21+35
  head=((offset+f/F*cycles)%1)*period-18
  for j in range(n):
   y=round(head-j*21)
   if y<-20 or y>H:continue
   level=9 if j==0 else max(1,8-int(j*7/n))
   text=letters[j]
   ft=normal
   if i%3==0 and j==3:text=token;ft=small
   d.text((x,y),text,font=ft,fill=level,anchor='mt')
 frames.append(im)
p=Path(__file__).resolve().parents[1] / 'assets' / 'code-rain.gif'
frames[0].save(p,save_all=True,append_images=frames[1:],duration=50,loop=0,transparency=0,background=0,disposal=2,optimize=False)
print(p.stat().st_size,'bytes')
