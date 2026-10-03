import math
cx=cy=100
def P(r,a): return (cx+r*math.cos(math.radians(a)), cy+r*math.sin(math.radians(a)))
# gear
N=12; Ro=96; Rr=82; Ri=70
pts=[]
step=360/N
for i in range(N):
    c=i*step-90
    tw_o=step*0.17; tw_r=step*0.27   # half widths (deg) at tip / root
    pts += [P(Rr,c-tw_r-0),P(Ro,c-tw_o),P(Ro,c+tw_o),P(Rr,c+tw_r)]
d="M"+" L".join(f"{x:.2f},{y:.2f}" for x,y in pts)+" Z"
# chrome
R=65; ri=0.42*R; rw=0.5*R
def tang(a,side):
    # point on outer circle for line parallel to radial angle a, offset by ri
    dx,dy=math.cos(math.radians(a)),math.sin(math.radians(a))
    nx,ny=-dy*side,dx*side
    # line: (cx+nx*ri + t*dx, ...) ; intersect circle R
    t=math.sqrt(R*R-ri*ri)
    return (cx+nx*ri+t*dx, cy+ny*ri+t*dy)
def arc(a,b): return f"A{R},{R} 0 0 1 {{}},{{}}"
# boundaries: radial angles (svg, y down): 30,150,270
# each colour = region between two offset lines, bounded by outer arc
def seg(a0,a1,col):
    # a0->a1 clockwise; start line offset so it tangents inner circle
    s=tang(a0,1); e=tang(a1,1)
    # inner meeting points: lines cross at the centre area; use centre as vertex
    return f'<path fill="{col}" d="M{cx},{cy} L{s[0]:.2f},{s[1]:.2f} A{R},{R} 0 0 1 {e[0]:.2f},{e[1]:.2f} Z"/>'
red=seg(210,330,"#DB4437")      # top
yel=seg(330,90,"#F4C20D")  # lower right
grn=seg(90,210,"#0F9D58")  # lower left
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
  <title>chromedp</title>
  <defs><clipPath id="c"><circle cx="{cx}" cy="{cy}" r="{R}"/></clipPath></defs>
  <path fill="#5B94C9" fill-rule="evenodd" d="{d} M{cx+Ri},{cy} A{Ri},{Ri} 0 1 0 {cx-Ri},{cy} A{Ri},{Ri} 0 1 0 {cx+Ri},{cy} Z"/>
  <g clip-path="url(#c)">{red}{yel}{grn}</g>
  <circle cx="{cx}" cy="{cy}" r="{rw:.1f}" fill="#fff"/>
  <circle cx="{cx}" cy="{cy}" r="{ri:.1f}" fill="#4285F4"/>
</svg>
'''
open("chromedp.svg","w").write(svg)
