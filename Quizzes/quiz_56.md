# Quiz 56
## Python code
```python
def to_bin(n):
    if n == 0:
        return '0'
    result = ''
    while n > 0:
        result = str(n % 2) + result
        n = n // 2
    return result

def secret_handshake(n):
    n = to_bin(n)
    result = []
    for i in range(len(n)):
        if n[-1] == '1':
            if i == 0:
                result.append('wink')
            elif i == 1:
                result.append('double blink')
            elif i == 2:
                result.append('close your eyes')
            elif i == 3:
                result.append('jump')
            else:
                result = result[::-1]
        n = n[:-1]
    return result

print(f"secret handshake for num 3: {', '.join(secret_handshake(3))}") # ['wink', 'double blink']
print(f"secret handshake for num 19: {', '.join(secret_handshake(19))}") # ['double blink', 'wink']
print(f"secret handshake for num 31: {', '.join(secret_handshake(31))}") # ['jump', 'close your eyes', 'double blink', 'wink']
print(f"secret handshake for num 8: {', '.join(secret_handshake(8))}") # ['jump']
print(f"secret handshake for num 16: {', '.join(secret_handshake(16))}") # []
```

## Output
![](/Assets/q56.png)