# Validation function!

# Kalau pakai

# All Class

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
		avg_score = self.average_score()
		if 90 <= avg_score <= 100:
			return "A"
		elif 80 <= avg_score <= 89:
			return "B"
		elif 70 <= avg_score <= 79:
			return "C"
		elif 60 <= avg_score <= 69:
			return "D"
		else:
			return "E"

	def display(self):
		print("\n========================")
		print(f"Nama  : {self.student["name"]}")
		print(f"ID    : {self.student["student_id"]}")
		print(f"Nilai : {self.student["scores"]}")
		print(f"Rata  : {self.average_score()}") 
		print(f"Grade : {self.get_grade()}") 
		print("========================")


class StudentManager:
	students = [] # Berisi objek Students

	def add_student(self):
		name = input("Tambahkan Nama Siswa/i: ")
		ID = input("Buat ID Siswa/i: ")

		StudentManager.students.append(Student(name, ID))
		print("\nBerhasil menambah Siswa/i")
		
	def find_student(self, ID): 
		for item in StudentManager.students:
			if item.student["student_id"] == ID:
				return item
		return None

	def add_student_score(self):
		student = self.find_student(input("Masukkan Id Siswa/i: ")) 
		
		if student is None:
			print("Siswa/i tidak tersedia!")
			return

		student.add_score(int(input("Masukkan nilai: ")))
		print("\nBerhasil menambah Nilai Siswa/i")

	def show_all_students(self):
		for item in StudentManager.students:
			item.display()

	def search_student(self):
		student = self.find_student(input("Masukkan Id Siswa/i: "))

		if student is None:
			print("Siswa/i tidak tersedia!")
			return
		
		student.display()	

	def delete_student(self):
		student = self.find_student(input("Masukkan Id Siswa/i: "))

		if student is None:
			print("Siswa/i tidak tersedia!")
			return

		StudentManager.students.remove(student)	
		print("\nBerhasil menambah Siswa/i")

while True:
	menu = ("Tambah Mahasiswa", "Tambah Nilai", "Cari Mahasiswa",
		"Tampilkan Semua", "Hapus Mahasiswa", "Keluar")

	print("\n======== MENU ========\n")
	for Nomor, Nama_menu in enumerate(menu, start=1):
		print(f"{Nomor}. {Nama_menu}")

	pilih_menu = int(input("Pilih Nomor Menu: ")) # Buat dalam fungsi validasi

	SM = StudentManager()
	match pilih_menu:
		case 1:
			SM.add_student()
		case 2:
			SM.add_score()
		case 3:
			SM.search_student()
		case 4:
			SM.show_all_students()
		case 5:
			SM.delete_student()
		case 6:
			break
		case _:
			print("Menu tidak tersedia")



	



