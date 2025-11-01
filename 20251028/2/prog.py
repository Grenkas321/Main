class Triangle:
    def __init__(self, a, b, c):
        self.a = tuple(a)
        self.b = tuple(b)
        self.c = tuple(c)
    
    def __abs__(self):
        x1, y1 = self.a
        x2, y2 = self.b
        x3, y3 = self.c
        area = 0.5 * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
        return area
    
    def __bool__(self):
        return abs(self) > 1e-10
    
    def __lt__(self, other):
        return abs(self) < abs(other)
    
    def _point_in_triangle(self, point, triangle):
        p = point
        a, b, c = triangle.a, triangle.b, triangle.c
        
        v0 = (c[0]-a[0], c[1]-a[1])
        v1 = (b[0]-a[0], b[1]-a[1])
        v2 = (p[0]-a[0], p[1]-a[1])
        
        dot00 = v0[0]*v0[0] + v0[1]*v0[1]
        dot01 = v0[0]*v1[0] + v0[1]*v1[1]
        dot02 = v0[0]*v2[0] + v0[1]*v2[1]
        dot11 = v1[0]*v1[0] + v1[1]*v1[1]
        dot12 = v1[0]*v2[0] + v1[1]*v2[1]
        
        inv_denom = 1 / (dot00*dot11 - dot01*dot01) if (dot00*dot11 - dot01*dot01) != 0 else 0
        u = (dot11*dot02 - dot01*dot12) * inv_denom
        v = (dot00*dot12 - dot01*dot02) * inv_denom
        
        return (u >= -1e-10) and (v >= -1e-10) and (u + v <= 1 + 1e-10)
    
    def __contains__(self, other):
        if not bool(other):
            return True
        if not bool(self):
            return False
        
        return (self._point_in_triangle(other.a, self) and 
                self._point_in_triangle(other.b, self) and 
                self._point_in_triangle(other.c, self))
    
    def _segments_intersect(self, p1, p2, p3, p4):
        def orientation(p, q, r):
            val = (q[1]-p[1])*(r[0]-q[0]) - (q[0]-p[0])*(r[1]-q[1])
            if abs(val) < 1e-10: return 0
            return 1 if val > 0 else 2
        
        def on_segment(p, q, r):
            return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and 
                    min(p[1], r[1]) <= q[1] <= max(p[1], r[1]))
        
        o1 = orientation(p1, p2, p3)
        o2 = orientation(p1, p2, p4)
        o3 = orientation(p3, p4, p1)
        o4 = orientation(p3, p4, p2)
        
        if o1 != o2 and o3 != o4:
            return True
        
        if o1 == 0 and on_segment(p1, p3, p2): return True
        if o2 == 0 and on_segment(p1, p4, p2): return True
        if o3 == 0 and on_segment(p3, p1, p4): return True
        if o4 == 0 and on_segment(p3, p2, p4): return True
        
        return False
    
    def __and__(self, other):
        if not bool(self) or not bool(other):
            return False
        
        sides1 = [(self.a, self.b), (self.b, self.c), (self.c, self.a)]
        sides2 = [(other.a, other.b), (other.b, other.c), (other.c, other.a)]
        
        for s1 in sides1:
            for s2 in sides2:
                if self._segments_intersect(s1[0], s1[1], s2[0], s2[1]):
                    return True
        
        if self in other or other in self:
            return True
        
        return False

import sys
exec(sys.stdin.read())