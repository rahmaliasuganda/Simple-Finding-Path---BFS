from collections import deque  

def bfs_shortest_path(city_map, start, goal):
    queue = deque([[start]])  
    visited = set()  

    while queue:  
        path = queue.popleft()  
        node = path[-1]  

        if node == goal:  
            return path  

        if node not in visited:  
            visited.add(node)  
            for neighbor in city_map.get(node, []):  
                new_path = list(path)  
                new_path.append(neighbor)  
                queue.append(new_path)  

    return None  


city_map = {
    'Home': ['Mall', 'School'],
    'Mall': ['Gym', 'Hospital'],
    'School': ['Library'],
    'Gym': ['Hospital'],
    'Library': ['Hospital'],
    'Hospital': []
}

start_location = 'Home'  
goal_location = 'Hospital'  
shortest_path = bfs_shortest_path(city_map, start_location, goal_location)

print("Jalur Terpendek:", shortest_path)
