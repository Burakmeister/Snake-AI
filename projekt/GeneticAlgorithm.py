import numpy as np
from time import sleep

input_neurons = 192
hidden_neurons = 64
output_neurons = 4
agents_num = 1000
the_best_agents_num = 10
loops = 100
sleep_time = 0.1
# def net_init(input_layer, hidden_layer, output_layer):
#     np.random.seed(69)
#     W1 = np.random.randn(hidden_layer, input_layer) * 0.1
#     W2 = np.random.randn(output_layer, hidden_layer) * 0.1
#     params = {"W1": W1, "W2": W2, "eff": 0}
#     return params

def init_layer(number_of_neurons, number_of_inputs_per_neuron):
    synaptic_weights = 2 * np.random.random((number_of_inputs_per_neuron, number_of_neurons)) - 1
    return synaptic_weights

def population_init():
    population = []
    for i in range(agents_num):
        layer_1 = init_layer(64,192)
        layer_2 = init_layer(4, 64)
        layers = {"W1": layer_1,"W2": layer_2,"eff": 0}
        population.append(layers)   # net_init(input_neurons, hidden_neurons, output_neurons)
    return population
    
def selection_model(population):
    population = sorted(population, key=lambda d: d['eff'])
    return population[agents_num-the_best_agents_num:]

    
class GeneticAlgorithm:
    
    def __init__(self):
        self.first_generation_func = population_init
        self.selection_model = selection_model
        self.mutation_probability = 0.1

    def run(self):
        population = self.first_generation_func()
        for p in population:
            step = 0
            ttl = 0
            gameover = False
            while not gameover and ttl<30:
                costam, gameover = player(p, step)
                sleep(sleep_time)
                step+=1
                ttl+=1
        i = 1
        while i<loops:
            
            selected = self.selection_model(population)
            new_population = selected.copy()
            while len(new_population) != agents_num:
                temp = np.random.choice(new_population)
                temp1 = np.random.choice(new_population)
                
                dad = temp['W1'][0:int(hidden_neurons/2)]
                mum = temp1['W1'][int(hidden_neurons/2):]
                dad1 = temp['W2'][0:int(output_neurons/2)]
                mum2 = temp1['W2'][int(output_neurons/2):]
                child = {"W1": np.concatenate((dad,mum), axis=0),"W2": np.concatenate((dad1,mum2),axis=0), "eff": 0}
                
                if np.random.random() <= self.mutation_probability:
                    print("hoho")
                    #child.mutation()                                               #work in progress
                new_population.append(child)
            population = new_population
            the_best_match = max(population, key=lambda d: d['eff'])
            sleep(3)
            print("Generation: {} S: {} fitness: {}".format(i, the_best_match, the_best_match["eff"]))
            sleep(5)
            i += 1
            for p in population:
                step = 0
                ttl = 0
                gameover = False
                while not gameover and ttl<30:
                    costam, gameover = player(p, step)
                    sleep(sleep_time)
                    step+=1
                    ttl+=1


def init_layer(number_of_neurons, number_of_inputs_per_neuron):
    synaptic_weights = 2 * np.random.random((number_of_inputs_per_neuron, number_of_neurons)) - 1
    return synaptic_weights

def get_data(file_name):
    with open(file_name) as f:
        array = []
        points = 0
        for line in f:
            if line[0]=='5':
                f.close()
                return array, points, True
            temp = [float(x) for x in line.split()]
            for x in temp:
                if x == float(0.33):
                    points+=1  
                array.append(x)
    f.close()
    if not array:
        sleep(0.2)
        input, points, gameover = get_data(file_name)
        return input, points,gameover
    else:
        return array, points, False

def write_control(file_name,output,step):
    f = open(file_name, "w")
    if np.max(output) == output[0]:
        f.write("D " + str(step+1))
    elif np.max(output) == output[1]:
        f.write("S " + str(step+1))
    elif np.max(output) == output[2]:
        f.write("A " + str(step+1))
    elif np.max(output) == output[3]:
        f.write("W " + str(step+1))
    f.close()

def sigmoid(x):
    return 1/(1+np.exp(-x))

def relu(x):
    return np.maximum(0,x)

def think(X, layer1, layer2):
    W1 = layer1
    W2 = layer2
    output_1 = relu(np.dot(X, W1))
    output_2 = sigmoid(np.dot(output_1,W2))
    print(output_2)
    return output_2

def calculate_fitness(steps,points):
    fitness = 100 * points + 1 * steps
    return fitness

def player(layers,step):
    input, points, gameover = get_data("data")
    layer1 = layers["W1"]
    layer2 = layers["W2"]
    layers["eff"] = calculate_fitness(step, points)
    print(layers["eff"])
    if gameover:
        f = open("control", "w")
        f.write("0 0")
        f.close()
        return layers, gameover
    output = think(input, layer1, layer2)
    write_control("control", output, step)
    return layers, gameover

def teach_me_senpai():
    ga = GeneticAlgorithm()
    ga.run()

teach_me_senpai()