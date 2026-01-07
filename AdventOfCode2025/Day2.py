from math import floor


test_input="""11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

real_input="""385350926-385403705,48047-60838,6328350434-6328506208,638913-698668,850292-870981,656-1074,742552-796850,4457-6851,138-206,4644076-4851885,3298025-3353031,8594410816-8594543341,396-498,1558-2274,888446-916096,12101205-12154422,2323146444-2323289192,37-57,101-137,46550018-46679958,79-96,317592-341913,495310-629360,33246-46690,14711-22848,1-17,2850-4167,3723700171-3723785996,190169-242137,272559-298768,275-365,7697-11193,61-78,75373-110112,425397-451337,9796507-9899607,991845-1013464,77531934-77616074"""
def read_input():
    ranges=[]
    for x in real_input.split(","):
        x=x.split("-")
        ranges+=range(int(x[0]),int(x[1])+1)
    return [str(x) for x in  ranges]

def part1():
    ranges=read_input()
    value=0
    for id in ranges:
        length=len(id)

        if length%2==0:
            begin=id[:length//2]
            end= id[length//2:]
            if begin==end:
                value+=int(id)
    print(value)

def part2():
    ranges = read_input()
    value = 0
    for id in ranges:
        length = len(id)

        # if length % 2 == 0:
        #     begin = id[:length // 2]
        #     end = id[length // 2:]
        #     if begin == end:
        #         print(id)
        #         value += int(id)
        # else:
        for part in range(1,length//2+1):
            sub_string=id.replace(id[:part],"")
            if sub_string=="":
                value+=int(id)
                break
    print(value)
# part1()
part2()
# part 1 test=1227775554
# part 2 test =4174379265