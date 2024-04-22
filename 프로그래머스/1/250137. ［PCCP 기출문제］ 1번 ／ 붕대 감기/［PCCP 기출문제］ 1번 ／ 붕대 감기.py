from collections import deque

def solution(bandage, health, attacks):
    answer = 0
    t, x, y = bandage
    c, r = health, 0
    attacks = deque(attacks)

    for i in range(1, 1001):
        attack_time, damage = attacks[0]
        if attack_time == i:
            c -= damage
            r = 0
            if c <= 0:
                return -1
            if attacks:
                attacks.popleft()
                if not attacks:
                    return c
        else:
            r += 1
            if c + x > health:
                c = health
            else:
                c += x
            if r == t:
                r = 0
                if c + y > health:
                    c = health
                else:
                    c += y
        print(i, c, r)

    return c