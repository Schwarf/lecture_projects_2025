from tasks import add

result = add.delay(4, 4)

print(result.get(timeout=10))  # Should print 8