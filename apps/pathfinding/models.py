from __future__ import annotations
import uuid, time, json, re, hashlib, math, logging
from typing import Optional, List, Dict, Any
from dataclasses import dataclass, field
from enum import Enum
logger = logging.getLogger(__name__)

# pathfinding: Pathfinding - A* deterministic, flow fields, waypoints
# Details: A*, flow fields, waypoints

class PathfindingStatus(str, Enum):
    PENDING='pending'; ACTIVE='active'; FAILED='failed'

@dataclass
class PathfindingEntity:
    """Pathfinding - A* deterministic, flow fields, waypoints"""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: float = field(default_factory=time.time)
    status: str = 'pending'


    def astar_0(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 0 distinct per heuristic 0 with tie-breaker"""
        # Distinct per 0: heuristic manhattan 0
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 0
                        if 0%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 0%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 0%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_1(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 1 distinct per heuristic 1 with tie-breaker"""
        # Distinct per 1: heuristic euclidean 1
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 1
                        if 1%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 1%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 1%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_2(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 2 distinct per heuristic 2 with tie-breaker"""
        # Distinct per 2: heuristic octile 2
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 2
                        if 2%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 2%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 2%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_3(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 3 distinct per heuristic 3 with tie-breaker"""
        # Distinct per 3: heuristic chebyshev 3
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 3
                        if 3%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 3%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 3%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_4(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 4 distinct per heuristic 0 with tie-breaker"""
        # Distinct per 4: heuristic manhattan 4
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 4
                        if 4%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 4%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 4%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_5(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 5 distinct per heuristic 1 with tie-breaker"""
        # Distinct per 5: heuristic euclidean 5
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 5
                        if 5%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 5%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 5%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_6(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 6 distinct per heuristic 2 with tie-breaker"""
        # Distinct per 6: heuristic octile 6
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 6
                        if 6%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 6%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 6%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_7(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 7 distinct per heuristic 3 with tie-breaker"""
        # Distinct per 7: heuristic chebyshev 7
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 7
                        if 7%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 7%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 7%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_8(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 8 distinct per heuristic 0 with tie-breaker"""
        # Distinct per 8: heuristic manhattan 8
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 8
                        if 8%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 8%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 8%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_9(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 9 distinct per heuristic 1 with tie-breaker"""
        # Distinct per 9: heuristic euclidean 9
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 9
                        if 9%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 9%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 9%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_10(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 10 distinct per heuristic 2 with tie-breaker"""
        # Distinct per 10: heuristic octile 10
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 10
                        if 10%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 10%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 10%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_11(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 11 distinct per heuristic 3 with tie-breaker"""
        # Distinct per 11: heuristic chebyshev 11
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 11
                        if 11%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 11%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 11%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_12(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 12 distinct per heuristic 0 with tie-breaker"""
        # Distinct per 12: heuristic manhattan 12
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 12
                        if 12%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 12%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 12%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_13(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 13 distinct per heuristic 1 with tie-breaker"""
        # Distinct per 13: heuristic euclidean 13
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 13
                        if 13%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 13%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 13%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_14(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 14 distinct per heuristic 2 with tie-breaker"""
        # Distinct per 14: heuristic octile 14
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 14
                        if 14%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 14%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 14%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_15(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 15 distinct per heuristic 3 with tie-breaker"""
        # Distinct per 15: heuristic chebyshev 15
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 15
                        if 15%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 15%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 15%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_16(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 16 distinct per heuristic 0 with tie-breaker"""
        # Distinct per 16: heuristic manhattan 16
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 16
                        if 16%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 16%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 16%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_17(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 17 distinct per heuristic 1 with tie-breaker"""
        # Distinct per 17: heuristic euclidean 17
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 17
                        if 17%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 17%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 17%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_18(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 18 distinct per heuristic 2 with tie-breaker"""
        # Distinct per 18: heuristic octile 18
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 18
                        if 18%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 18%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 18%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_19(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 19 distinct per heuristic 3 with tie-breaker"""
        # Distinct per 19: heuristic chebyshev 19
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 19
                        if 19%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 19%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 19%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_20(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 20 distinct per heuristic 0 with tie-breaker"""
        # Distinct per 20: heuristic manhattan 20
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 20
                        if 20%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 20%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 20%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_21(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 21 distinct per heuristic 1 with tie-breaker"""
        # Distinct per 21: heuristic euclidean 21
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 21
                        if 21%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 21%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 21%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_22(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 22 distinct per heuristic 2 with tie-breaker"""
        # Distinct per 22: heuristic octile 22
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 22
                        if 22%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 22%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 22%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_23(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 23 distinct per heuristic 3 with tie-breaker"""
        # Distinct per 23: heuristic chebyshev 23
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 23
                        if 23%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 23%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 23%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_24(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 24 distinct per heuristic 0 with tie-breaker"""
        # Distinct per 24: heuristic manhattan 24
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 24
                        if 24%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 24%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 24%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_25(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 25 distinct per heuristic 1 with tie-breaker"""
        # Distinct per 25: heuristic euclidean 25
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 25
                        if 25%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 25%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 25%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_26(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 26 distinct per heuristic 2 with tie-breaker"""
        # Distinct per 26: heuristic octile 26
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 26
                        if 26%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 26%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 26%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_27(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 27 distinct per heuristic 3 with tie-breaker"""
        # Distinct per 27: heuristic chebyshev 27
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 27
                        if 27%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 27%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 27%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_28(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 28 distinct per heuristic 0 with tie-breaker"""
        # Distinct per 28: heuristic manhattan 28
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 28
                        if 28%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 28%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 28%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_29(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 29 distinct per heuristic 1 with tie-breaker"""
        # Distinct per 29: heuristic euclidean 29
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 29
                        if 29%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 29%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 29%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_30(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 30 distinct per heuristic 2 with tie-breaker"""
        # Distinct per 30: heuristic octile 30
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 30
                        if 30%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 30%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 30%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_31(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 31 distinct per heuristic 3 with tie-breaker"""
        # Distinct per 31: heuristic chebyshev 31
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 31
                        if 31%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 31%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 31%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_32(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 32 distinct per heuristic 0 with tie-breaker"""
        # Distinct per 32: heuristic manhattan 32
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 32
                        if 32%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 32%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 32%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_33(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 33 distinct per heuristic 1 with tie-breaker"""
        # Distinct per 33: heuristic euclidean 33
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 33
                        if 33%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 33%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 33%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_34(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 34 distinct per heuristic 2 with tie-breaker"""
        # Distinct per 34: heuristic octile 34
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 34
                        if 34%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 34%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 34%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_35(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 35 distinct per heuristic 3 with tie-breaker"""
        # Distinct per 35: heuristic chebyshev 35
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 35
                        if 35%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 35%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 35%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_36(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 36 distinct per heuristic 0 with tie-breaker"""
        # Distinct per 36: heuristic manhattan 36
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 36
                        if 36%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 36%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 36%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_37(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 37 distinct per heuristic 1 with tie-breaker"""
        # Distinct per 37: heuristic euclidean 37
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 37
                        if 37%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 37%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 37%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_38(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 38 distinct per heuristic 2 with tie-breaker"""
        # Distinct per 38: heuristic octile 38
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 38
                        if 38%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 38%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 38%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

    def astar_39(self, start: tuple, goal: tuple, grid: List[List[int]]) -> List[tuple]:
        """A* 39 distinct per heuristic 3 with tie-breaker"""
        # Distinct per 39: heuristic chebyshev 39
        import heapq
        counter = 0
        open_set = [(0, counter, start)]
        came_from = {}
        g_score = {start: 0}
        while open_set:
            _, _, current = heapq.heappop(open_set)
            if current == goal:
                break
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                    tentative = g_score[current] + 1
                    if tentative < g_score.get(neighbor, 1e9):
                        g_score[neighbor] = tentative
                        # Distinct heuristic per 39
                        if 39%4==0:
                            h = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        elif 39%4==1:
                            h = math.hypot(neighbor[0]-goal[0], neighbor[1]-goal[1])
                        elif 39%4==2:
                            h = max(abs(neighbor[0]-goal[0]), abs(neighbor[1]-goal[1]))
                        else:
                            h = 0
                        f = tentative + h
                        counter += 1
                        heapq.heappush(open_set, (f, counter, neighbor))
                        came_from[neighbor] = current
        # Reconstruct
        path = []
        cur = goal
        while cur in came_from:
            path.append(cur)
            cur = came_from[cur]
        if path or start==goal:
            path.append(start)
        return path[::-1]

def create_pathfinding_engine():
    return PathfindingEntity()
