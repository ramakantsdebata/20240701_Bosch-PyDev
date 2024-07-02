'''`
x = 10000
y = 10000
y = (y+1)-1

print(id(x), type(x), x)
print(id(y), type(y), y)
`'''
'''
class Test
{
    //int x;
};

//t = Test()
//cout << sizeof(t) << endl;

Test tArr[10];

int arr[10];
cout << arr[4];
cout << *(arr + 4)


'''

x = 10
y = x
print(id(x), id(y), sep='\n')

y = y + 1
print("\n", id(x), id(y), sep='\n')

s1 = "Test"
print(s1, id(s1))
s1 += " Value"
print(s1, id(s1))
