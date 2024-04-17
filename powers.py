#!/usr/bin/python3

def square(num):
    sq = num * num
    return sq
  

def cube(num):
    return pow(num,3)
   

def main():
    n = int(input('Enter a number:'))
    seq = 1
    while seq <= n:
       squ = square(seq)
       cub = cube(seq)
       print(f'The number is {seq}, its square is {squ} and its cube is {cub}.')
       seq += 1
       
if __name__ == '__main__':
    main()