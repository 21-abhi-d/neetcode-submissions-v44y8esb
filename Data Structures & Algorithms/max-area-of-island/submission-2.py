class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: 
            return 0
        
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()
        visit = set()
        max_area = 0

        def bfs(r, c):
            q.append((r, c))
            visit.add((r, c))
            area = 1 # initialise on first cell
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (nr < 0 or nr >= rows or
                        nc < 0 or nc >= cols or
                        grid[nr][nc] == 0 or
                        (nr, nc) in visit):
                        continue
                    q.append((nr, nc))
                    visit.add((nr, nc))
                    area += 1 # incerement through path
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    curr_area = bfs(r, c)
                    max_area = max(max_area, curr_area)

        return max_area
