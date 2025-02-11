import sys

input = sys.stdin.readline

def list_available_meetingroom_time(schedule: list):
    start = 9
    end = start
    result = []
    while end <= 18:
        if not schedule[end]:
            end += 1
        else:
            if end - start > 0:
                f_start = str(start).rjust(2, "0")
                f_end = str(end).rjust(2, "0")
                result.append((f_start, f_end))
                start = end
            else:
                start += 1
                end += 1
    return result

if __name__ == "__main__":
    n, m = map(int, input().split())
    meetingroom = {}
    for _ in range(n):
        room_name = input().rstrip()
        meetingroom[room_name] = [0 for __ in range(18)] + [1]
    for _ in range(m):
        r, s, t = input().split()
        s, t = int(s), int(t)
        for time in range(s, t):
            meetingroom[r][time] = 1

    for i, mr in enumerate(sorted(meetingroom.keys())):
        result = list_available_meetingroom_time(meetingroom[mr])
        print(f"Room {mr}:")
        # if len(result) == 0:
        if not result:
            print("Not available")
        else:
            print(f"{len(result)} available:")
            for start, end in result:
                print(f"{start}-{end}")
        if i != len(meetingroom) - 1:
            print("-----")