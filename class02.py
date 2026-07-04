class Student:
	def __init__(self, name, student_id):
		self.student = {
		"name" : name,
		"student_id" : student_id,
		"scores" : []
		}
	
	def add_score(self, score):
		self.student["scores"].append(score)

	def average_score(self):
		if not self.student["scores"]:
			return 0
		return sum(self.student["scores"]) / len(self.student["scores"])

	def get_grade(self):
		average_score = average_score()
		if 90 <= average_score <= 100:
			return "A"
		elif 80 <= average_score <= 89:
			return "B"
		elif 70 <= average_score <= 79:
			return "C"
		elif 60 <= average_score <= 69:
			return "D"
		else:
			return "E"

	def display(self):
		print("\n========================")
		print(f"Nama  : {self.student["name"]}")
		print(f"ID    : {self.student["student_id"]}")
		print(f"Nilai : {self.student["scores"]}")
		print(f"Rata  : {Student().average_score()}") #Perbaiki Disini!
		print(f"Grade : {Student().get_grade()}") #Perbaiki Disini!
		print("========================")

class StudentManager:
	def __init__(self):
		self.__students = []

	def add_student(self):
		Name = input("Masukkan Nama Siswa/i: ")
		Id = input("Buat ID Siswa/i: ")
		
		self.__students.append(Student(Name, Id))
		print("Berhasil menambah Siswa/i")

	def find_student(self):
		Id = input("Masukkan ID Siswa/i: ")
		
		for item in self.__students:
			if item.student["student_id"] == Id:
				return item.display()
		return None

	def add_student_score(self):
		Id = input("Masukkan Id: ")
		Nilai = input("Masukkan nilai: ")
		
		for item in self.__students:
			if item.student["student_id"] == Id:
				item.add_score(Nilai)
				print("Berhasil menambah Nilai Siswa/i")
		print("Siswa/i tidak tersedia")

	def show_all_students(self):
		for item in self.__students:
			item.display()

while True:
	s1 = StudentManager()
	s1.add_student()
	s1.find_student()
	s1.add_student_score()
	s1.show_all_students()





