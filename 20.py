from collections import Counter
import sys

# This would be a good place to use numpy, but I wanted to take an OOP
# approach.

class Coord:
    '''
    A wrapper for a 3-tuple with addition and manhattan distance defined.
    '''
    
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z


    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y, self.z + other.z)


    def __lt__(self, other):
        return (self.x, self.y, self.z) < (other.x, other.y, other.z)
    

    def __gt__(self, other):
        return (self.x, self.y, self.z) > (other.x, other.y, other.z)


    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)


    def __hash__(self):
        return hash((self.x, self.y, self.z))


    def manhattan_distance(self):
        return abs(self.x) + abs(self.y) + abs(self.z)


class Particle:

    def __init__(self, pos, vel, acc):
        self.pos, self.vel, self.acc = pos, vel, acc


    def increment(self):
        '''
        Proceed one time step forward.
        '''
        self.vel += self.acc
        self.pos += self.vel
        return self


    def values(self):
        '''
        Get the coordinates.
        '''
        return self.pos, self.vel, self.acc

def distance_to_zero_comparator(particle):
    '''
    Judge distance to zero based on the Manhattan distance of the acceleration,
    using velocity and position to tie-break.
    '''
    manhattan_dists = list(map(lambda c: c.manhattan_distance(),
                               particle.values()))
    return tuple(reversed(manhattan_dists))


def remove_collisions(particles):
    locs = Counter(map(lambda p: p.pos, particles))
    return [p for p in particles if locs[p.pos] == 1]


def part_one(particles):
    min_particle = min(particles, key=distance_to_zero_comparator)
    return particles.index(min_particle)


def part_two(particles, max_unchanged_iterations=1000):
    '''
    Takes a number of iterations without changing after which the program will
    declare the states unchanging. Default is 1000.
    '''
    # Don't mutate the input.
    particles = particles[:]
    iterations_unchanged = 0
    prev_len = len(particles)
    while iterations_unchanged < max_unchanged_iterations: 
        # A Counter given the number of particles at a position.
        num_at_pos = Counter(map(lambda p: p.pos, particles))
        # Keep only those particles that haven't collided, incrementing them if
        # they are kept.
        particles = [p.increment() for p in particles if num_at_pos[p.pos] == 1]
        # Logic for breaking out of the loop.
        if prev_len == len(particles):
            iterations_unchanged += 1
        else:
            prev_len = len(particles)
            iterations_unchanged = 0
    return len(particles)


# Obviously the use of eval here isn't the best practice. I think it's a pretty
# elegant approach myself, so I'm keeping it.
particles = []
for line in sys.stdin:
    line = line.rstrip().replace('<', '(')
    line = line.replace('>', ')')
    line = line.replace('=', '')
    line = line.replace('p', 'Coord').replace('v', 'Coord').replace('a',
                        'Coord')
    particles.append(Particle(*eval(line)))

print(part_one(particles))
print(part_two(particles))
