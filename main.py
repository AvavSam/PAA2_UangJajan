class Student:
    def __init__(self, name, allowance):
        self.name = name
        self.allowance = allowance

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i].allowance <= right[j].allowance:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

if __name__ == "__main__":
    students = [
        Student("Abi", 50000),
        Student("Avav", 30000),
        Student("Qhiran", 75000),
        Student("Marsya", 45000),
        Student("Puput", 25000)
    ]

    sorted_students = merge_sort(students)

    print("Daftar Uang Jajan Mahasiswa (Terurut):")
    print("=====================================")
    for student in sorted_students:
        print(f"Nama: {student.name}, Uang Jajan: Rp{student.allowance:,}")
