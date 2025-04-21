class block(object):
    ''' assumes blocks are objects that have a mass and x-axis velocity
    models blocks for thier behaviours (collisions) '''
    def __init__(self, mass, velocity):
        assert type(mass) == type(velocity) == float
        self.mass = mass
        self.velocity = velocity
        self.set_state()

    def collide(self, other):
        '''changes the velocities of each block in occurdance with physics'''
        #collision space variables assigned
        P = self.momentum + other.momentum #total momentum
        E = self.energy + other.energy     #total Energy
        M = self.mass + other.mass         #total mass
        mean = P/M                         #mean velocity 

        #assigning self a new velocity
        D = (((P*self.mass)**2 - self.mass*M*(P**2 - 2*other.mass*E))**0.5)/(self.mass*M)
        if self.velocity >= mean:
            self.velocity = mean - D
        else:
            self.velocity = mean + D
        self.set_state()

        #assigning other a new velocity
        other.velocity = (P - self.momentum)/other.mass
        other.set_state()

    def get_velocity(self):
        return self.velocity
    def get_mass(self):
        return self.mass
    def set_velocity(self, velocity):
        self.velocity = velocity
        self.set_state()
    def set_state(self):
        self.momentum = self.mass*self.velocity
        self.energy = (1/2)*self.mass*(self.velocity**2)
        self.principal_value = (self.mass**0.5)*self.velocity

def collision_simulation(mass_factor):
    b1 = block(mass_factor, -1.0)
    b2 = block(1.0, 0.0)
    collision_count = 0
    while not (b1.get_velocity() >= 0 and b2.get_velocity() >= 0 and b1.get_velocity() >= b2.get_velocity()):
        if collision_count%2 == 0:
            b1.collide(b2)
        else:
            b2.set_velocity(-b2.get_velocity())
        collision_count += 1
    return collision_count
        
