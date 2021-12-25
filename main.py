from pyobjs import Object
import json

if __name__ == '__main__':
    '''w = Object(r=9, s=6, t=5)
    
    l = Object(b={'x': 1, 'y': w, 'z': 8}, c=Object(r=9, s=6, t=5), a=[1,2,{'j': 99, 'k': 104}, Object(q=1, w=2, e=3)])

    print(l.items())

    #attrs_obj = Object(**{k:v for k, v in l.__dict__.items() if isinstance(v, dict)})
    print(l)
    #print(l.b.x, l.b.z, 
    #l.b.y.r, l.b.y.s, l.b.y.t, l.c.r, l.c.s, l.c.t, l.a, l.a[2].j, l.a[2].k, l.a[3].q , l.a[3].w , l.a[3].e )
    '''
    w = Object(r=9, s=6, t=5)
    l = Object(b={'x': 1, 'y': w, 'z': 8}, 
                c=Object(r=9, s=6, t=5))

    l.a = [1,2,
                [({'j': 99, 'k': [{'x':[{'a':1}, {'a':2}]}]})], 
                (1,2),
                set(['a', 'b', 'c']),
                Object(q=1, w=2, e=3)
                ]

    l.w = [1,2,3]
    
    #l.a[2][0].j = 1000
    #print(l.a[2][0].k[0].x[1].a)
    del l.a[2][0].k[0].x[1]
    print(set({'j': 99, 'k': [{'x':[{'a':1}, {'a':2}]}]}))
    print(l)