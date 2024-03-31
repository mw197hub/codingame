# https://www.codingame.com/ide/puzzle/six-degrees-of-kevin-bacon

import sys,math


def bfs_shortest_path(graph, start, goal):
    explored = []
    queue = [[start]]
    if start == goal:
        return [goal]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path
            explored.append(node)

    return "So sorry, but a connecting path doesn't exist :("

actor="Elvis Presley";movieList=['Change of Habit: Elvis Presley, Mary Tyler Moore, Barbara McNair, Jane Elliot, Ed Asner', 'JFK: Kevin Costner, Kevin Bacon, Tommy Lee Jones, Laurie Metcalf, Gary Oldman, Ed Asner', 'Sleepers: Kevin Bacon, Jason Patric, Brad Pitt, Robert De Niro, Dustin Hoffman']
actor="Anusha Viswanathan";movieList=['The Air I Breathe: Brendan Fraser, Sarah Michelle Gellar, Andy Garcia, Kevin Bacon', 'Diner: Steve Guttenberg, Mickey Rourke, Kevin Bacon, Daniel Stern', 'The Bengali Night: Hugh Grant, Shabana Azmi, Supriya Pathak, John Hurt, Soumitra Chatterjee, Utpal Dutt', 'Murder in the First: Christian Slater, Kevin Bacon, Gary Oldman, Embeth Davidtz', 'Change of Habit: Elvis Presley, Mary Tyler Moore, Barbara McNair, Jane Elliot, Ed Asner', 'Mission Dugga Dugga: Anusha Viswanathan, Rahul Dev Bose, Kheyali Dastidar, Priyanka Bhattacharjee', 'The Two Companions: Priyanka Bhattacharjee, Aishi Roy, ', 'Criminal Law: Gary Oldman, Kevin Bacon, Tess Harper, Karen Young', 'Beauty Shop: Queen Latifah, Alicia Silverstone, Kevin Bacon, Djimon Hounsou', 'My One and Only: Renée Zellweger, Logan Lerman, Kevin Bacon, Chris Noth', 'Path O Prasad: Utpal Dutt, Soumitra Chatterjee, Ruma Guha Thakurta, Satya Bandopadhyay, Kheyali Dastidar', 'Where the Truth Lies: Kevin Bacon, Colin Firth, Alison Lohman, David Hayman', 'Tremors: Kevin Bacon, Fred Ward, Finn Carter, Michael Gross', 'Hollow Man: Kevin Bacon, Elisabeth Shue, Josh Brolin, Kim Dickens', 'Mr. 3000: Bernie Mac, Angela Bassett, Brian J. White, Chris Noth, Tony Lee Gratz', 'Taking Chance: Kevin Bacon, Tom Aldredge, Nicholas Art, Blanche Baker', 'Cop Car: Kevin Bacon, James Freedson-Jackson, Hays Wellford, Shea Whigham', 'Stir of Echoes: Kevin Bacon, Zachary David Cope, Kathryn Erbe, Illeana Douglas', 'Sleepers: Kevin Bacon, Jason Patric, Brad Pitt, Robert De Niro, Dustin Hoffman', 'Chatrapathi: Chatrapathi Sekhar, Prabhas, Bhanupriya, Shafi, Pradeep Ram Singh Rawat, L. B. Sriram', 'The Big Picture: Kevin Bacon, Jennifer Jason Leigh, Emily Longstreth, J.T. Walsh', "Jayne Mansfield's Car: Kevin Bacon, Tippi Hedren, Shawnee Smith, Ray Stevenson, John Hurt", 'Friday the 13th: Betsy Palmer, Adrienne King, Jeannine Taylor, Robbi Morgan, Kevin Bacon, Tom Savini', 'R.I.P.D: Ryan Reynolds, Jeff Bridges, Mary-Louise Parker, Kevin Bacon', 'Balto: Kevin Bacon, Bob Hoskins, Bridget Fonda, Jim Cummings', 'Wasted: David Kopriva, Alex Wilder, A.J. Laird, Oliver Grant, Natalie Matthai, Michael Oilar', 'The Woodsman: Kevin Bacon, Kyra Sedgwick, Yasiin Bey, David Alan Grier', 'RRR: N.T. Rama Rao Jr., Ram Charan, Olivia Morris, Ray Stevenson, Alison Doody, Chatrapathi Sekhar', 'Crazy, Stupid, Love.: Steve Carell, Ryan Gosling, Julianne Moore, Emma Stone, Kevin Bacon', 'Apollo 13: Tom Hanks, Bill Paxton, Kevin Bacon, Gary Sinise', 'The Notebook: Rachel McAdams, Ryan Gosling, James Garner, Gena Rowlands', 'Flatliners: Kiefer Sutherland, Kevin Bacon, Julia Roberts, William Baldwin', 'Clueless: Alicia Silverstone, Stacey Dash, Brittany Murphy, Paul Rudd', 'Chained to a Cowboy: Monty Kane, Tyree Jensen, Tony Lee Gratz, Michael Oilar', 'Grindhouse: Kurt Russell, Zoë Bell, Rosario Dawson, Vanessa Ferlito, Sydney Tamiia Poitier, Tracie Thoms, Rose McGowan, Mary Elizabeth Winstead, Tom Savini', 'Picture Perfect: Jennifer Aniston, Jay Mohr, Kevin Bacon, Olympia Dukakis', 'Frost/Nixon: Frank Langella, Michael Sheen, Kevin Bacon, Sam Rockwell', 'Swiss Army Man: Paul Dano, Daniel Radcliffe, Mary Elizabeth Winstead, Antonia Ribero, Shane Carruth', 'Slice: Asha Coy, Francis Faye, David Kopriva, Barrett Lione-Seaton', 'Wild Things: Kevin Bacon, Neve Campbell, Matt Dillon, Denise Richards']

####

suche="Kevin Bacon"
graph={}

for movie in movieList:
    m1List=movie.split(":")
    m2List = m1List[1].split(",")
    mList=[]
    for m in m2List:
        mList.append(m.strip())
    for m in mList:
        rList =mList[:]
        rList.remove(m)        
        if m in graph:
            graph[m]= graph[m]+rList
        else:
            graph[m]=rList

print(graph['Ed Asner'])

ergList = bfs_shortest_path(graph, actor, suche)
print(len(ergList)-1)
