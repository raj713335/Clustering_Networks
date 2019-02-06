import random
#import networkx as nx
#import matplotlib.pyplot as plt


class clustering_networks:


    #particles = []


    def __init__(self):
        pass


    @classmethod
    def particle_initilization(self):                   #function to initialize the particles
        no_of_particles=random.randint(0,100) #Ramdomly creates particles in the range 0,100
        particles=[]

        for i in range(no_of_particles):
            id=i                                        #creates a id of the particles
            x_cordinate=round(random.random()*100,2)          #creates the x cordinate of the particle in the range 0-100 units
            y_cordinate=round(random.random()*100,2)         #creates the y cordinate of the particles in the range 0-100 units
            #print(x_cordinate,y_cordinate)
            no_of_neighbour=random.randint(0,no_of_particles-1)        #randomly generates the number of neighbour a ith particle can have and its always -1 than no of particles
            neighbor_temporary_list=[]
            for j in range(no_of_neighbour):
                temp=random.randint(0,no_of_particles-1)            #randomly generates the neighbour and its always no_of_particles-1 as randint is inclusive
                if i!=j:                                            #ensures that a particle isnt a neighbour of itself
                    neighbor_temporary_list.append(temp)
            particles.append([id,x_cordinate, y_cordinate,neighbor_temporary_list])  # append the position of particles in a list named particle and its neighbour
        self.print_particles(self,particles)                    #a function call to go to print_particles function defination

        #print(particles)

        self.particles_visualization(self,particles)            #visualization of particles

    def print_particles(self,particles):


        #Printing individual particles
        for each in particles:
            print("ID : {} X-Cordinate and Y-Cordinate : {} {} and neighbour : {}".format(each[0],each[1],each[2],each[3]))


    def particles_visualization(self,particles):
        pass




obj1=clustering_networks()
obj1.particle_initilization()

