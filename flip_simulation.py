import random

class coin(object):
    
    ''' assumes coins are objects which have a state(heads or tails), name, and value
    models the coin for its behaviors (flips)'''
    
    count = 0
    
    def __init__(self, name, value, state):
        
        assert state in (0,1)
        assert type(name) == str
        assert type(value) == float
        
        self.name = name
        self.value = value
        self.state = state
        
        self.ID = coin.count + 1
        coin.count += 1
        
    def __str__(self):
        if self.state == 1:
            return "Heads"
        else:
            return "Tails"
        
    def flip(self, bias_for_heads = 0.5):
        
        '''assumes bais foor heads is a value between 0 and 1
        flips coin (changes its state based on bias)'''
        
        assert 0 <= bias_for_heads <= 1
        if random.random() < bias_for_heads:
            self.state = 1
        else:
            self.state = 0
        
    def get_ID(self):
        return self.ID
    
    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_state(self):
        return self.state

    def set_state(self, new_state):
        self.state = new_state
    
    def get_all(self):
        return self.__dict__   #Evil

def flip_simulation(n_flips = 1000000, bias = 0.5):
    
    ''' assumes n_flips is the number of times a certain coin with a bias(bias) towards heads is flipped
    returns probability of getting heads based on the result of n_flips'''
    
    assert n_flips > 0
    a = coin("dime",0.1, 1)
    n_heads = 0.0
    for i in range(n_flips):
        a.flip(bias)
        n_heads += a.get_state()
    return n_heads/n_flips
        
        
        
