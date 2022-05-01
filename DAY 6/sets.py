# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
n_values = set(list(map(int,input().split())))
m = int(input())
m_values = set(list(map(int,input().split())))
val = sorted((n_values.difference(m_values)).union((m_values.difference(n_values))))

for each in val:
    print(each)