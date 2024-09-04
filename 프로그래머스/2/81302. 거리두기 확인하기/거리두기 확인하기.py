def solution(places):

    offset = [(-1,0),(0,1),(1,0),(0,-1)]
    answer = []

    def is_disconnect(x, y):
        for dx_f, dy_f in offset:
            nx_f = dx_f + x
            ny_f = dy_f + y

            if nx_f < 0 or nx_f > 4 or ny_f < 0 or ny_f > 4:
                continue

            if place[nx_f][ny_f] == "P":
                return False

            elif place[nx_f][ny_f] == "X":
                continue

            for dx_s, dy_s in offset:
                if (dx_f + dx_s == 0) and (dy_f + dy_s == 0):
                    continue

                nx_s = nx_f + dx_s
                ny_s = ny_f + dy_s

                if nx_s < 0 or nx_s > 4 or ny_s < 0 or ny_s > 4:
                    continue

                if place[nx_s][ny_s] == "P":
                    return False

                elif place[nx_s][ny_s] == "X":
                    continue

        return True

    for place in places: # 대기실 1개씩
        check = True

        for x in range(5):
            if not check:
                break
            
            for y in range(5):
                if not check:
                    break
            
                if place[x][y] == 'P': # P가 아니면 넘기기
                    check = is_disconnect(x, y)
                    
        if check:
            answer.append(1)
        else:
            answer.append(0)                

    return answer
