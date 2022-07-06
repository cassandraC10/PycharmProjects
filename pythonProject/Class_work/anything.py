print("********************************************************************************************")
print("STUDENT\t" "        SUB1\t" "   SUB2\t" "       TOT\t" "        AVG\t" "           POSITION")
print("*******************************************************************************************")
print()

student_name = "Noah"
sub1_score = 23
sub2_score = 12
tot = 35
avg = 23.5
pos = 1

student_name2 = "babe"
Ssub_score = 12
Ssub2_score = 20
Stot = 32
Savg = 16.0
Spos = 2


all1 = [student_name, sub1_score,
        sub2_score, tot,
        avg, pos]

for number in all1:
    print(number, end='\t\t\t')
print()


all2 = [student_name2, Ssub_score,
        Ssub2_score, Stot,
        Savg, Spos]

for number in all2:
    print(number, end='\t\t\t')

# import statistics
# # student_1 = range()
# sub_1 = 23
# sub_2 = 12
# all_subject = (sub_1, sub_2)
# avg = print(statistics.mean(all_subject))


# for number in range(0, 6):
#     print('{0:6d}\t {1:7d}\t {2:3d}'.format(x, x * x, x * x * x))
