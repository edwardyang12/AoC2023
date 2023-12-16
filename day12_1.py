import copy 

input = '''
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
'''

input = input.split("\n")[1:-1]

springs = []
records = []
for i in input:
    s, r = i.split(" ")
    springs.append([x for x in s])
    records.append([int(x) for x in r.split(",")])

# queue to store all potential valid states
# with annotation
# total = 0
# for s, r in zip(springs, records):
#     valid = 0
#     queue = [(s, r, 0, False)] # spring state, records left, position, contiguous damaged # should only contain potentially valid configs
#     while queue:
#         # print(queue)
#         s_inst, r_inst, pos, cont = queue.pop(0)
#         if pos==len(s_inst):
#             if len(r_inst)==0 or (len(r_inst)==1 and r_inst[0]==0): # no records to process, complete
#                 valid += 1
#             continue
#         if s_inst[pos] == "?":
#             # choose . 
#             if cont: # if we are in contiguous state and choose .
#                 if len(r_inst) == 0:
#                     s_inst = copy.deepcopy(s_inst)
#                     s_inst[pos] = "."
#                     queue.append((s_inst, r_inst, pos+1, False))
#                 elif r_inst[0] == 0: # only valid to choose . because if we choose # in this situation then we would break it
#                     s_inst = copy.deepcopy(s_inst)
#                     s_inst[pos] = "."
#                     r_temp = copy.deepcopy(r_inst)
#                     r_temp = r_temp[1:]
#                     queue.append((s_inst, r_temp, pos+1, False))
#             else:
#                 s_inst = copy.deepcopy(s_inst)
#                 s_inst[pos] = "."
#                 r_temp = copy.deepcopy(r_inst)
#                 queue.append((s_inst, r_temp, pos+1, False))

#             # choose # 
#             if cont: # if we are in contiguous state and choose #
#                 if len(r_inst) > 0 and r_inst[0] != 0: # only valid to choose # because if we choose . in this situation then we would break it
#                     s_inst = copy.deepcopy(s_inst)
#                     s_inst[pos] = "#"
#                     r_temp = copy.deepcopy(r_inst)
#                     r_temp[0] = r_temp[0]-1
#                     queue.append((s_inst, r_temp, pos+1, True))
#             else:
#                 if len(r_inst) > 0:
#                     s_inst = copy.deepcopy(s_inst)
#                     s_inst[pos] = "#"
#                     r_temp = copy.deepcopy(r_inst)
#                     r_temp[0] = r_temp[0]-1
#                     queue.append((s_inst, r_temp, pos+1, True))

#         elif s_inst[pos] == ".":
#             if cont: # if continugous has begun already
#                 if len(r_inst) == 0:
#                     s_inst = copy.deepcopy(s_inst)
#                     s_inst[pos] = "."
#                     queue.append((s_inst, r_inst, pos+1, False))
#                 elif r_inst[0] == 0: 
#                     s_inst = copy.deepcopy(s_inst)
#                     s_inst[pos] = "."
#                     r_inst = copy.deepcopy(r_inst)
#                     r_inst = r_inst[1:]
#                     queue.append((s_inst, r_inst, pos+1, False))
#             else:
#                 queue.append((s_inst, r_inst, pos+1, False))
#         else:
#             if len(r_inst) > 0 and r_inst[0] != 0:
#                 r_inst = copy.deepcopy(r_inst)
#                 r_inst[0] = r_inst[0]-1
#                 queue.append((s_inst, r_inst, pos+1, True))
#     total+=valid
# print(total)
    
# without annotation
total = 0
for s, r in zip(springs, records):
    valid = 0
    queue = [(r, 0, False)] # spring state, records left, position, contiguous damaged # should only contain potentially valid configs
    while queue:
        r_inst, pos, cont = queue.pop()
        if pos==len(s):
            if len(r_inst)==0 or (len(r_inst)==1 and r_inst[0]==0): # no records to process, complete
                valid += 1
            continue
        if s[pos] == "?":
            # choose . 
            if cont: # if we are in contiguous state and choose .
                if len(r_inst) == 0:
                    queue.append((r_inst, pos+1, False))
                elif r_inst[0] == 0: # only valid to choose . because if we choose # in this situation then we would break it
                    queue.append((r_inst[1:], pos+1, False))
            else:
                queue.append((r_inst, pos+1, False))

            # choose # 
            if cont: # if we are in contiguous state and choose #
                if len(r_inst) > 0 and r_inst[0] != 0: # only valid to choose # because if we choose . in this situation then we would break it
                    r_temp = copy.deepcopy(r_inst)
                    r_temp[0]-=1
                    pos+=1 
                    while pos< len(s) and s[pos] == "#":
                        pos+=1
                        r_temp[0]-=1
                    queue.append((r_temp, pos, True))
            else:
                if len(r_inst) > 0:
                    r_temp = copy.deepcopy(r_inst)
                    r_temp[0]-=1
                    pos+=1 
                    while pos< len(s) and s[pos] == "#":
                        pos+=1
                        r_temp[0] = r_temp[0]-1
                    queue.append((r_temp, pos, True))

        elif s[pos] == ".":
            if cont: # if continugous has begun already
                if len(r_inst) == 0:
                    queue.append((r_inst, pos+1, False))
                elif r_inst[0] == 0: 
                    queue.append((r_inst[1:], pos+1, False))
            else:
                queue.append((r_inst, pos+1, False))
        else:
            if len(r_inst) > 0 and r_inst[0] != 0:
                r_inst = copy.deepcopy(r_inst)
                pos+=1
                r_inst[0]-=1
                while pos< len(s) and s[pos] == "#":
                    pos+=1
                    r_inst[0]-=1
                queue.append((r_inst, pos, True))
    total+=valid

print(total)