# Create and write some lines to a file
f = open("demo.txt", "w+")
f.write("Line 1\nLine 2\nLine 3\nLine 4\nLine 5\n")
f.flush()  # Flush the buffer
print("Flush done.")

print("File descriptor number:", f.fileno())  # fileno
print("Is file connected to terminal (isatty)?", f.isatty())  # isatty usually False

f.seek(0)  # Move to start

print("\nRead full content:")
print(f.read())  # read all

f.seek(0)
print("\nRead 10 characters:")
print(f.read(10))  # read with size

f.seek(0)
print("\nRead one line:")
print(f.readline())  # readline

f.seek(0)
print("\nRead one line with size limit:")
print(f.readline(5))  # readline with size

f.seek(0)
print("\nRead all lines into a list:")
print(f.readlines())  # readlines

f.seek(0)
print("\nRead lines with hint (might limit memory usage):")
print(f.readlines(15))  # readlines with hint

f.seek(0)
print("\nCurrent file position:", f.tell())  # tell

f.seek(10, 0)  # Move to offset 10 from start
print("File position after seek:", f.tell())

f.truncate(20)  # Truncate the file to 20 bytes
print("File truncated to 20 bytes.")

f.seek(0)
print("\nFile content after truncate:")
print(f.read())

f.close()
print("\nFile closed.")

# Write and writelines
f = open("demo2.txt", "w")
f.write("This is a single line.\n")  # write

lines = ["Line A\n", "Line B\n", "Line C\n"]
f.writelines(lines)  # writelines
f.close()
print("\nWrite and writelines done.")

# Bonus: file.__next__() only works with iterators (Python 2), use next() in Python 3
f = open("demo2.txt", "r")
print("\nUsing next() to read lines one by one:")
print(next(f).strip())
print(next(f).strip())
f.close()
