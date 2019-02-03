import random


class clustering_networks:


    def __init__(self):
        pass


    @classmethod
    def particle_initilization(self):                   #function to initialize the particles
        no_of_particles=random.randint(0,100) #Ramdomly creates particles in the range 0,100
        particles=[]

        for i in range(no_of_particles):
            id=i                                        #creates a id of the particles
            x_cordinate=random.randint(0,100)           #creates the x cordinate of the particle in the range 0-100 units
            y_cordinate=random.randint(0,100)           #creates the y cordinate of the particles in the range 0-100 units
            #print(x_cordinate,y_cordinate)
            no_of_neighbour=random.randint(0,10)        #randomly generates the number of neighbour a ith particle can have
            neighbor_temporary_list=[]
            for i in range(no_of_neighbour):
                temp=random.randint(0,no_of_particles)
                neighbor_temporary_list.append(temp)
            particles.append([id,x_cordinate, y_cordinate,neighbor_temporary_list])  # append the position of particles in a list named particle and its neighbour
            self.print_particles(self,particles)

        #print(particles)

    def print_particles(self,particles):


        #Printing individual particles
        for each in particles:
            print("ID : {} X-Cordinate and Y-Cordinate : {} {} and neighbour : {}".format(each[0],each[1],each[2],each[3]))



obj1=clustering_networks()
for i in range(1):
    obj1.particle_initilization()

