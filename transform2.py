import sys
import os
import time
import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np




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


        #print(cluster_list)

        self.deployment(length,breadth,nodes,cluster_list)





    def sergation_of_nodes_in_cluster(self,length,breadth,nodes,cluster_list,particles):




        for each_partilcle in particles:
            for node_cluster in cluster_list:
                if ((each_partilcle[1][0]>=node_cluster[2][0][0] and each_partilcle[1][0]<node_cluster[2][0][1]) and (each_partilcle[1][1]>=node_cluster[2][1][0] and each_partilcle[1][1]<node_cluster[2][1][1])):
                    node_cluster[1].append(each_partilcle)
                    break




        #print(cluster_list)

        for each in cluster_list:
            print(each[0],each[1],len(each[1])/nodes)

        print(cluster_list)


        self.visualization(length,breadth,cluster_list,particles)





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
            battery=0  #change it later on
            particles.append([id,[x_cordinate,y_cordinate],[battery]])

        print(particles)

        self.sergation_of_nodes_in_cluster(length,breadth,nodes,cluster_list,particles)



    def spiral_deployment(self,length,breadth,nodes,cluster_list):

        listx = []
        particles=[]

        def spiralPrint(m, n):


            k = 0
            l = 0

            ''' k - starting row index 
                m - ending row index 
                l - starting column index 
                n - ending column index 
                i - iterator '''

            while (k < m and l < n):

                # Print the first row from
                # the remaining rows
                for i in range(l, n):
                    particles.append([k, i])
                    #print("({},{})".format(k + 0.5, i + 0.5), end=" ")

                k += 1

                # Print the last column from
                # the remaining columns
                for i in range(k, m):
                    particles.append([i, n - 1])
                    #print("({},{})".format(i + 0.5, n - 1 + 0.5), end=" ")

                n -= 1

                # Print the last row from
                # the remaining rows
                if (k < m):

                    for i in range(n - 1, (l - 1), -1):
                        #print("({},{})".format(m - 1 + 0.5, i + 0.5), end=" ")
                        particles.append([m - 1, i])

                    m -= 1

                # Print the first column from
                # the remaining columns
                if (l < n):
                    for i in range(m - 1, k - 1, -1):
                        #print("({},{})".format(i + 0.5, l + 0.5), end=" ")
                        particles.append([i, l])

                    l += 1



        spiralPrint(length, breadth)
        listx=particles

        print("""ENTER THE TIME INTERVAL IN UNITS""")
        time_interval=int(input())
        time_interval=time_interval/nodes
        node_interval=len(listx)//nodes

        time=0
        id=1
        particles=[]
        battery=0
        for i in range(0,len(listx),node_interval):
            particles.append([id,[listx[i][0],listx[i][1]],[battery],time])
            time+=time_interval
            id+=1

        print(particles)

        self.sergation_of_nodes_in_cluster(length, breadth, nodes, cluster_list, particles)

    def square_deployment(self,length,breadth,nodes,cluster_list):

        print("""ENTER THE TIME INTERVAL IN UNITS""")
        time_interval = int(input())
        time_interval=time_interval/nodes
        no_of_particles = nodes
        particles = []
        timex=0

        breadth_sqr=breadth
        no_of_clusters=len(cluster_list)

        breadth_start=int(breadth_sqr-((breadth_sqr//(no_of_clusters**0.5))//2))
        breadth_incx=int(breadth_sqr//(no_of_clusters**0.5))
        id=0
        flx=0

        while(breadth_start>0):

            y_cordinate=breadth_start
            flx+=1

            temp=[]

            battery=0 #change it later on



            for i in range(0, int(no_of_particles // (no_of_clusters ** 0.5))):
                temp.append(random.randrange(0, length))
            if (flx % 2 != 0):
                temp = sorted(temp)
            else:
                temp = sorted(temp, reverse=True)



            for x_cordinate in temp:

                id += 1
                timex+=time_interval
                particles.append([id, [x_cordinate, y_cordinate], [battery], timex])


            breadth_start = breadth_start - breadth_incx


        print(particles)

        self.sergation_of_nodes_in_cluster(length, breadth, nodes, cluster_list, particles)

    def default_deployment(self,length,breadth,nodes,cluster_list):
        pass







    def visualization(self,length,breadth,cluster_list,particles):


        G=nx.Graph()

        for each in particles:
            G.add_node(each[0],pos=(each[1][0],each[1][1]))


        #pos = nx.get_node_attributes(G, 'pos')

        pos = {}

        for each in particles:
            pos[each[0]] = (each[1][0], each[1][1])


        #nx.draw_networkx_labels(G, pos)
        nx.draw_networkx(G,pos=pos)


        plt.title("CLUSTERING NETWORK'S")
        plt.xlabel('X-AXIS')
        plt.ylabel('Y-AXIS')
        # Limits for the Y  and Yaxis
        incx=(len(cluster_list)**0.5)
        #plt.ylim(0, breadth)
        #plt.xlim(0, length)
        plt.xticks(np.arange(0, length+1, length//incx))
        plt.yticks(np.arange(0, breadth+1, breadth//incx))
        #plt.plot([lambda x: x[1][0] for x in particles],[lambda y: y[1][1] for y in particles[1][1]],'ro')
        plt.grid()
        plt.savefig("WSN_labels.png")
        plt.show()

        for each in cluster_list:
            for i in range(0, len(each[1])-1):
                for j in range(i + 1, len((each[1]))):
                    G.add_edge(each[1][i][0], each[1][j][0])

        #nx.draw(G,pos, with_labels=True)
        nx.draw_networkx(G, pos=pos,with_labels=True)

        plt.xticks(np.arange(0, length + 1, length // incx))
        plt.yticks(np.arange(0, breadth + 1, breadth // incx))
        plt.grid()
        plt.savefig("WSN_CLUSTER.png")
        plt.show()






obj1=wireless_sensor_networks()

