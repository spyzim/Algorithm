# # 연월일 달력

test = int(input())

for i in range(test):
    n = input()
    year = int(n[0:4])
    month = int(n[4:6])
    day = int(n[6:8])

    if((month == 0) or (month > 12) ):
       print(f'#{i+1} {-1}')
    else :
        if((month == 2) and (day == 0 ) or (day > 28)):
            print(f'#{i+1} {-1}')
        elif((day == 0) or (day > 31)):
            print(f'#{i+1} {-1}')
        else:
            if(month < 10):
                if(year<1000):
                    if(day<10):
                        print(f'#{i+1} 0{year}/0{month}/0{day}')
                    else:
                        print(f'#{i+1} 0{year}/0{month}/{day}')
                else:
                    if(day<10):
                        print(f'#{i+1} {year}/0{month}/0{day}')
                    else:
                        print(f'#{i+1} {year}/0{month}/{day}')
            else:
                if(year<1000):
                    if(day<10):
                        print(f'#{i+1} 0{year}/{month}/0{day}')
                    else:
                        print(f'#{i+1} 0{year}/{month}/{day}')
                else:
                    if(day<10):
                        print(f'#{i+1} {year}/{month}/0{day}')
                    else:
                        print(f'#{i+1} {year}/{month}/{day}')
                