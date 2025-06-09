import heapq as hq

offset = {
    "N" : (-1, 0),
    "E" : (0, 1),
    "S" : (1, 0),
    "W" : (0, -1)
}

road_cost = {
    "straight" : 100,
    "corner" : 500
}

answer = 0

def solution(board):
    
    size = len(board)
    
    board = [[float('inf') if j == 0 else 1 for j in i] for i in board]
    
    board[0][0] = 0
    
    pos_hq = [(0, 0, 0, "start")]
    
    while pos_hq:
        now_cost, x, y, pre_d = hq.heappop(pos_hq)
        
        for now_d, d_pos in offset.items():
            dx, dy = d_pos
            
            nx, ny = x+dx, y+dy
            
            if nx < 0 or nx == size or ny < 0 or ny == size or board[nx][ny] == 1:
                continue
            
            next_cost = now_cost + road_cost["straight"] + (road_cost["corner"] if not pre_d == now_d and not pre_d == "start" else 0)
            
            # 직선 도로가 코너 도로보다 싸지는 현상 보정
            # 코너일 때, 추가로 드는 금액 만큼은 보류하여 힙큐에 넣도록 설정
            if next_cost > board[nx][ny] + road_cost["corner"]:
                continue
            elif next_cost < board[nx][ny]:
                board[nx][ny] = next_cost
            hq.heappush(pos_hq, (next_cost, nx, ny, now_d))
    
    return board[-1][-1]