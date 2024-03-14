ms = 0
s = 0
m = 0
h = 0
d = 0
w = 0
mm = 0
y = 0
while True:
    print(f"\r {ms, s, m, h, d, w, mm, y}", end="")
    ms += 1
    if ms == 100:
        s += 1
        ms = 0
        if s == 60:
            m += 1
            s = 0
            if m == 60:
                h += 1
                m = 0
                if h == 24:
                    d += 1
                    h = 0
                    if d == 7:
                        w += 1
                        d = 0
                        if w == 4:
                            mm += 1
                            w = 0
                            if mm == 52:
                                y += 1
                                mm = 0
                                if ms < 2:
                                    print(f"\r {ms, s, m, h, d, w, mm, y}", end="")
