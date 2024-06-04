# Tạo các danh sách để lưu trữ điểm của các bạn
students = []
java_scores = []
english_scores = []
python_scores = []
# Nhập điểm của 5 bạn cho từng môn học
for i in range(5):
    name = input(f"Nhập tên của bạn thứ {i+1}: ")
    java_score = float(input(f"Nhập điểm của {name} cho môn công nghệ Java: "))
    english_score = float(input(f"Nhập điểm của {name} cho môn tiếng Anh chuyên ngành CNPM: "))
    python_score = float(input(f"Nhập điểm của {name} cho môn lập trình ứng dụng Python: "))
    students.append(name)
    java_scores.append(java_score)
    english_scores.append(english_score)
    python_scores.append(python_score)
# Tìm điểm cao nhất và thấp nhất cho từng môn học
max_java_score = max(java_scores)
min_java_score = min(java_scores)
max_english_score = max(english_scores)
min_english_score = min(english_scores)
max_python_score = max(python_scores)
min_python_score = min(python_scores)
# Tìm ra bạn nào có điểm cao nhất và thấp nhất cho từng môn học
java_index_max = java_scores.index(max_java_score)
java_index_min = java_scores.index(min_java_score)
english_index_max = english_scores.index(max_english_score)
english_index_min = english_scores.index(min_english_score)
python_index_max = python_scores.index(max_python_score)
python_index_min = python_scores.index(min_python_score)
# In ra kết quả
print("Kết quả:")
print(f"Điểm cao nhất môn công nghệ Java: {students[java_index_max]} với điểm {max_java_score}")
print(f"Điểm thấp nhất môn công nghệ Java: {students[java_index_min]} với điểm {min_java_score}")
print(f"Điểm cao nhất môn tiếng Anh chuyên ngành CNPM: {students[english_index_max]} với điểm {max_english_score}")
print(f"Điểm thấp nhất môn tiếng Anh chuyên ngành CNPM: {students[english_index_min]} với điểm {min_english_score}")
print(f"Điểm cao nhất môn lập trình ứng dụng Python: {students[python_index_max]} với điểm {max_python_score}")
print(f"Điểm thấp nhất môn lập trình ứng dụng Python: {students[python_index_min]} với điểm {min_python_score}")