class Environment:
    '''
    Simple class representing the financial market.

    Attributes:
        data: series of prices
        position
        t: timestep of the current position of the agent
        done
        profits
        positions
        position_value: current position of the agent
        history
        history_t

    '''
    def __init__(self, data):
        self.data = data
        self.nS = self.data.shape[0]
        self.nA = 3
        self.reset()
        
    def reset(self):
        self.t = 0
        self.done = False
        self.profits = 0
        self.positions = []
        self.position_value = 0
        self.history = [0 for _ in range()]
        return [self.position_value] + self.history # obs
    
    def step(self, action):
        # Initilize the reward
        reward = 0
        
        # act = 0: stay, 1: buy, 2: sell
        if action == 0: 
            pass
        elif action == 1:
            # Save the price
            self.positions.append(self.data.iloc[self.t, :]['Close'])
        elif action == 2:
            if len(self.positions) == 0:
                reward = -1
            else:
                profits = 0
                for p in self.positions:
                    profits += (self.data.iloc[self.t, :]['Close'] - p)
                reward += profits
                self.profits += profits
                self.positions = []
        
        # Prepare for next step
        self.t += 1
        self.position_value = 0
        for p in self.positions:
            self.position_value += (self.data.iloc[self.t, :]['Close'] - p)
        self.history.pop(0)
        self.history.append(self.data.iloc[self.t, :]['Close'] - self.data.iloc[(self.t-1), :]['Close'])
        
        # Clipping reward
        if reward > 0:
            reward = 1
        elif reward < 0:
            reward = -1
        
        return [self.position_value] + self.history, reward, self.done # obs, reward, done