import sys
import os
import time
import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math




class wireless_sensor_networks:


    def __init__(self):


        file_data = open("inputs.txt", "a")



        print("""PRESS 
1 TO CONTINUE
0 TO EXIT AND SAVE :
                 """)

        file_data.writelines("""PRESS 
1 TO CONTINUE
0 TO EXIT AND SAVE:\n \n""")  #saving inputs in text file




        stc=int(input())
        file_data.writelines(">>> "+ str(stc)+"\n \n")
        if (stc==1):
            self.user_input(file_data)  #updates of the time 10th august 2019
        else:
            file_data.close()

            exit(0)






    def user_input(self,file_data):
        print("ENTER THE DIMENSION OF THE FIELD AS (Length Breadth [as Int]) : ")
        file_data.writelines("ENTER THE DIMENSION OF THE FIELD AS (Length Breadth [as Int]) :\n \n")  #saving file in text file
        length,breadth=list(map(int,input().split(" ")))
        file_data.writelines(">>> " + str(length) +"  "+str(breadth)+ "\n \n")
        print("ENTER THE NUMBER OF NODES THAT IS NEEDED TO BE DEPLOYED [as INT] :")
        file_data.writelines("ENTER THE NUMBER OF NODES THAT IS NEEDED TO BE DEPLOYED [as INT] :\n \n")   #saving file in text file
        nodes=int(input())
        print(length,breadth,nodes)
        file_data.writelines(">>> " + str(nodes) + "\n \n")

        #file_data.close()



        self.cluster_creation(length,breadth,nodes,file_data)








    def cluster_creation(self,length,breadth,nodes,file_data):

        print("""ENTER TYPE OF CLUSTER CREATION:
                 1. AREA WISE CLUSTER CREATION
                 2. DEFAULT (NOT KNOWS AS OF NOW) :""")

        file_data.writelines("""ENTER TYPE OF CLUSTER CREATION:
                 1. AREA WISE CLUSTER CREATION
                 2. DEFAULT (NOT KNOWS AS OF NOW) : \n""")  #saving file in text editor

        cluster_option=int(input())
        file_data.writelines(">>> " + str(cluster_option) + "\n \n")


        if cluster_option==1:
            self.cluster_area_wise(length,breadth,nodes,file_data)
        elif cluster_option==2:
            pass

        else:
            pass


    def cluster_area_wise(self,length,breadth,nodes,file_data):

        print("ENTER THE NUMBER OF CLUSTERS YOU WANT TO CREATE :")

        file_data.writelines("ENTER THE NUMBER OF CLUSTERS YOU WANT TO CREATE : \n ")
        number_of_clusters=int(input()) #can be changed to user input later on

        file_data.writelines(">>> " + str(number_of_clusters) + "\n \n")

        x=length//(number_of_clusters**0.5)
        y=breadth//(number_of_clusters**0.5)

        cluster_list=[]
        cluster_count=1

        x=int(x)
        y=int(y)
        #print(length,breadth,x,y)
        #file_data.writelines(">>> " + str(length)+" " + str(breadth)+" "  + str(x)+" "  +str(y)+ "\n ")

        #THE CLUSTERING ASSIGNMENT CAUSES ERROR DURING UNEVEN LENGTH AND BREADTH ASSIGNMENT

        for x_axis in range(0,length,x):
            for y_axis in range(0,breadth,y):
                cluster_number="CLUSTER "+str(cluster_count)
                cluster_count+=1
                cluster_list.append([cluster_number,[],[[x_axis,x_axis+x],[y_axis,y_axis+y]]])


        #print(cluster_list)

        self.deployment(length,breadth,nodes,cluster_list,file_data)





    def sergation_of_nodes_in_cluster(self,length,breadth,nodes,cluster_list,particles,file_data):




        for each_partilcle in particles:
            for node_cluster in cluster_list:
                if ((each_partilcle[1][0]>=node_cluster[2][0][0] and each_partilcle[1][0]<node_cluster[2][0][1]) and (each_partilcle[1][1]>=node_cluster[2][1][0] and each_partilcle[1][1]<node_cluster[2][1][1])):
                    node_cluster[1].append(each_partilcle)
                    break




        #print(cluster_list)

        for each in cluster_list:
            print(each[0],each[1],len(each[1])/nodes)
            file_data.writelines(">>> " + str(each[0]) +str(each[1])+str(len(each[1])/nodes)+ "\n ")

        print(cluster_list)
        file_data.writelines(">>> " + str(cluster_list)  + "\n ")




        self.visualization(length,breadth,cluster_list,particles,file_data)






    def deployment(self,length,breadth,nodes,cluster_list,file_data):
        print("""CHOOSE A DEPLOYMENT TYPE AS OPTIONS -
                 1. RANDOM DEPLOYMENT
                 2. SPIRAL DEPPLYMENT
                 3. SQUARE DEPLYMENT
                 4. DEFAULT DEPLOYMENT""")

        file_data.writelines("""CHOOSE A DEPLOYMENT TYPE AS OPTIONS -
                 1. RANDOM DEPLOYMENT
                 2. SPIRAL DEPPLYMENT
                 3. SQUARE DEPLYMENT
                 4. DEFAULT DEPLOYMENT \n
                 """)   #sving file in text file
        deployment_option=int(input())

        print(deployment_option)
        file_data.writelines(">>> " + str(deployment_option) + "\n ")

        if deployment_option==1:
            self.random_deployment(length,breadth,nodes,cluster_list,file_data)
        elif deployment_option==2:
            self.spiral_deployment(length,breadth,nodes,cluster_list,file_data)
        elif deployment_option==3:
            self.square_deployment(length,breadth,nodes,cluster_list,file_data)
        else:
            self.default_deployment(length,breadth,nodes,cluster_list,file_data)


    def random_deployment(self,length,breadth,nodes,cluster_list,file_data):
        no_of_particles = nodes
        particles = []

        print("""ENTER THE TIME INTERVAL IN UNITS""")

        file_data.writelines("""ENTER THE TIME INTERVAL IN UNITS \n""")
        time_interval = int(input())
        time_interval = time_interval / nodes

        file_data.writelines(">>> " + str(time_interval)  + "\n ")


        time = 0

        for i in range(no_of_particles):
            id = i+1  # creates a id of the particles
            x_cordinate = round(random.randrange(0,length),2)+round(random.random(),2)# creates the x cordinate of the particle in the range 0-100 units
            y_cordinate = round(random.randrange(0,breadth),2)+round(random.random(),2)  # creates the y cordinate of the particles in the range 0-100 units
            # print(x_cordinate,y_cordinate)
            battery=0  #change it later on
            particles.append([id,[x_cordinate,y_cordinate],[time],[battery]])
            time+=time_interval

        print(particles)
        file_data.writelines(">>> " + str(particles) + "\n ")

        self.sergation_of_nodes_in_cluster(length,breadth,nodes,cluster_list,particles,file_data)



    def spiral_deployment(self,length,breadth,nodes,cluster_list,file_data):

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

        file_data.writelines("""ENTER THE TIME INTERVAL IN UNITS \n""") #saving flie in txt file
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
        file_data.writelines(str(particles)+ " \n")


        self.sergation_of_nodes_in_cluster(length, breadth, nodes, cluster_list,particles, file_data)

    def square_deployment(self,length,breadth,nodes,cluster_list,file_data):

        print("""ENTER THE TIME INTERVAL IN UNITS""")

        file_data.writelines("""ENTER THE TIME INTERVAL IN UNITS \n """) #saving file in txt file
        time_interval = int(input())

        file_data.writelines(">>> " + str(time_interval)  + "\n ")
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
        file_data.writelines(">>> " + str(particles) + "\n ")

        self.sergation_of_nodes_in_cluster(length, breadth, nodes, cluster_list, particles,file_data)

    def default_deployment(self,length,breadth,nodes,cluster_list):
        pass







    def visualization(self,length,breadth,cluster_list,particles,file_data):


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

        self.analyze(cluster_list, file_data)



    def analyze(self,cluster_list,file_data):


        leader_node=[]

        for cluster in cluster_list:
            min_distance=math.inf
            for cluster_value_x in cluster[1]:
                total_distance=0
                for cluster_value_y in cluster[1]:
                    if cluster_value_x[0]!=cluster_value_y[0]:
                        total_distance+=(((cluster_value_x[1][0]-cluster_value_y[1][0])**2)+((cluster_value_x[1][1]-cluster_value_y[1][1])**2)**0.5)
                if total_distance<min_distance:
                    min_distance=total_distance
                    id =cluster_value_x[0]


            for cluster_value_x in cluster[1]:
                if id==cluster_value_x[0]:
                    leader_node.append([cluster[0],cluster_value_x])

        file_data.writelines("THE LEADER NODES IN RESPECTIVE CLUSTERS\n")
        for row in leader_node:
            print(row)
            file_data.writelines(">>>"+str(row)+"\n")

        print(leader_node)





        self.__init__()






if __name__=="__main__":
    obj1=wireless_sensor_networks()

