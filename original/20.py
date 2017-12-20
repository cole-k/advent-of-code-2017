from collections import Counter
import sys

class Particle:

    def __init__(self, p):
        self.pos, self.vel, self.acc = p

particles = []
p_list = []
for line in sys.stdin:
    line = line.rstrip().replace('<', '(')
    line = line.replace('>', ')')
    line = line.replace('=', '')
    line = line.replace('p', '').replace('v', '').replace('a', '')
    particles.append(Particle(eval(line)))
    p_list.append(eval(line))

def increment(tup, by):
    return tup[0] + by[0], tup[1] + by[1], tup[2] + by[2]

def iteration(particles):
    for p in particles:
        p.vel = increment(p.vel, p.acc)
        p.pos = increment(p.pos, p.vel)
    return particles

def remove_collisions(particles):
    locs = Counter(map(lambda x: x[0], particles))
    return [p for p in particles if locs[p[0]] == 1]

def dist_to_zero(particle):
    return sum(map(abs,particle))

min_particle = min(p_list, key=lambda x: tuple(map(dist_to_zero, reversed(x))))
print(p_list.index(min_particle))

iters = 1000
counter = 0
prev_len = len(particles)
while counter < iters: 
    num_at_pos = Counter(map(lambda x: x.pos, particles))
    particles = [p for p in particles if num_at_pos[p.pos] == 1]
    particles = iteration(particles)
    if prev_len == len(particles):
        counter += 1
    else:
        prev_len = len(particles)
        counter = 0
print(len(particles))
