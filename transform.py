import random
import networkx as nx
import matplotlib.pyplot as plt

class wireless_sensor_networks:


    def __init__(self):
        self.user_input()




    def user_input(self):
        print("ENTER THE DIMENSION OF THE FIELD AS (Length Breadth [as Int]) : ")
        length,breadth=list(map(int,input().split(" ")))
        print("ENTER THE NUMBER OF NODES THAT IS NEEDED TO BE DEPLOYED [as INT] :")
        nodes=int(input())
        print(length,breadth,nodes)



        self.cluster_creation(length,breadth,nodes)








    def cluster_creation(self,length,breadth,nodes):
        print("""ENTER TYPE OF CLUSTER CREATION:
                 1. AREA WISE CLUSTER CREATION
                 2. DEFAULT (NOT KNOWS AS OF NOW) :""")

        cluster_option=int(input())


        if cluster_option==1:
            self.cluster_area_wise(length,breadth,nodes)
        elif cluster_option==2:
            pass

        else:
            pass


    def cluster_area_wise(self,length,breadth,nodes):
        print("ENTER THE NUMBER OF CLUSTERS YOU WANT TO CREATE :")
        number_of_clusters=int(input()) #can be changed to user input later on

        x=length//(number_of_clusters**0.5)
        y=breadth//(number_of_clusters**0.5)

        cluster_list=[]
        cluster_count=1

        x=int(x)
        y=int(y)
        print(length,breadth,x,y)

        #THE CLUSTERING ASSIGNMENT CAUSES ERROR DURING UNEVEN LENGTH AND BREADTH ASSIGNMENT

        for x_axis in range(0,length,x):
            for y_axis in range(0,breadth,y):
                cluster_number="CLUSTER "+str(cluster_count)
                cluster_count+=1
                cluster_list.append([cluster_number,[],[[x_axis,x_axis+x],[y_axis,y_axis+y]]])


        print(cluster_list)

        self.deployment(length,breadth,nodes,cluster_list)





    def sergation_of_nodes_in_cluster(self,cluster_list,particles,length,breadth):




        for each_partilcle in particles:
            for node_cluster in cluster_list:
                if ((each_partilcle[1][0]>=node_cluster[2][0][0] and each_partilcle[1][0]<node_cluster[2][0][1]) and (each_partilcle[1][1]>=node_cluster[2][1][0] and each_partilcle[1][1]<node_cluster[2][1][1])):
                    node_cluster[1].append(each_partilcle)
                    break




        print(cluster_list)

        for each in cluster_list:
            print(each[0],each[1])

        print(cluster_list)


        self.visualization(cluster_list,particles,length,breadth)





    def deployment(self,length,breadth,nodes,cluster_list):
        print("""CHOOSE A DEPLOYMENT TYPE AS OPTIONS -
                 1. RANDOM DEPLOYMENT
                 2. SPIRAL DEPPLYMENT
                 3. SQUARE DEPLYMENT
                 4. DEFAULT DEPLOYMENT""")
        deployment_option=int(input())

        print(deployment_option)

        if deployment_option==1:
            self.random_deployment(length,breadth,nodes,cluster_list)
        elif deployment_option==2:
            self.spiral_deployment(length,breadth,nodes,cluster_list)
        elif deployment_option==3:
            self.square_deployment(length,breadth,nodes,cluster_list)
        else:
            self.default_deployment(length,breadth,nodes,cluster_list)


    def random_deployment(self,length,breadth,nodes,cluster_list):
        no_of_particles = nodes
        particles = []

        for i in range(no_of_particles):
            id = i+1  # creates a id of the particles
            x_cordinate = round(random.randrange(0,length),2)+round(random.random(),2)# creates the x cordinate of the particle in the range 0-100 units
            y_cordinate = round(random.randrange(0,breadth),2)+round(random.random(),2)  # creates the y cordinate of the particles in the range 0-100 units
            # print(x_cordinate,y_cordinate)
            particles.append([id,[x_cordinate,y_cordinate]])

        print(particles)

        self.sergation_of_nodes_in_cluster(cluster_list,particles,length,breadth)



    def spiral_deployment(self,length,breadth,nodes,cluster_list):
        pass
    def square_deployment(self,length,breadth,nodes,cluster_list):
        pass
    def default_deployment(self,length,breadth,nodes,cluster_list):
        pass







    def visualization(self,cluster_list,particles,length,breadth):
        G=nx.Graph()

        for each in particles:
            G.add_node(each[0],pos=(each[1][0],each[1][1]))

        for each in cluster_list:
            for i in range(0,len(each[1])):
                for j in range(i+1,len((each[1]))-1):
                    G.add_edge(each[1][i][0],each[1][j][0])

        pos = nx.get_node_attributes(G, 'pos')
        # nx.draw_networkx_labels(G, pos)


        plt.title("CLUSTERING NETWORK'S")
        plt.xlabel('X-AXIS')
        plt.ylabel('Y-AXIS')
        # Limits for the Y axis
        plt.ylim(0, breadth)

        # Create names
        plt.xlim(0, length)

        nx.draw(G,pos, with_labels=True)

        plt.show()




obj1=wireless_sensor_networks()

