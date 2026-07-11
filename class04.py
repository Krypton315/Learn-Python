# Common Validation function!

def validation_input_None(input_usr):
	if not input_usr.strip():
		print("Input tidak boleh kosong!\n")
		return None
	
	return input_usr.strip()

def validation_input_str(input_usr):
	check_input = validation_input_None(input_usr)

	if check_input is None:
		return None

	if input_usr.isdigit() 
		print("Input harus berupa String\n")
		return None

	return check_input

def validation_input_int(input_usr):
	check_input = validation_input_None(input_usr)

	if check_input is None:
		return None

	if not check_input.isdigit():
		print("Input harus berupa Integer\n")
		return None

	return int(check_input)


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
		print("\n=== Add Student ===")
		print("*Ketik EXIT untuk Keluar\n")
		
		while True:
			name = validation_input_str(input("Tambahkan Nama Siswa/i: "))
			if name is None: continue
			if name.lower() == "exit": return

			break

		while True:
			ID = validation_input_None(input("Buat ID Siswa/i: "))
			if ID is None: continue
			if ID.lower() == "exit": return

			twin_id = self.find_student(ID)
			if twin_id is not None: continue

			break

		StudentManager.students.append(Student(name, ID))
		print("\nBerhasil menambah Siswa/i")
		
	
	def find_student(self, ID):
		for item in StudentManager.students:
			if item.student["student_id"] == ID:
				return item
		return None

	def add_student_score(self):
		print("\n=== Add Student Score ===")
		print("*Ketik EXIT untuk Keluar\n")
		
		while True:
			ID = validation_input_None(input("Masukkan ID Siswa/i: "))
			if ID is None: continue
			if ID.lower() == "exit": return

			break

		student = self.find_student(ID) 
		
		if student is None:
			print("Siswa/i tidak tersedia!")
			return
		
		while True:
			Nilai = validation_input_int(input("Masukkan Nilai: "))
			if Nilai is None: continue
			if Nilai.lower() == "exit": return

			if Nilai <= 0 or Nilai > 100:
				print("Nilai diluar batas\n")
				continue

			break
		
		student.add_score(Nilai)
		print("\nBerhasil menambah Nilai Siswa/i")

	def show_all_students(self):
		for item in StudentManager.students:
			item.display()

	def search_student(self):
		print("\n=== Search Student ===")
		print("*Ketik 'EXIT' untuk Keluar\n")

		while True:
			ID = validation_input_None(input("Masukkan ID Siswa/i: "))
			if ID is None: continue
			if ID.lower() == "exit": return

			break
		
		student = self.find_student(ID)

		if student is None:
			print("Siswa/i tidak tersedia!")
			return
		
		student.display()	

	def delete_student(self):
		print("\n=== Delete Student ===")
		print("*Ketik 'EXIT' untuk Keluar\n")
		
		while True:
			ID = validation_input_None(input("Masukkan ID Siswa/i: "))
			if ID is None: continue
			if ID.lower() == "exit": return

			break

		student = self.find_student(ID)

		if student is None:
			print("Siswa/i tidak tersedia!")
			return

		StudentManager.students.remove(student)	
		print("\nBerhasil menambah Siswa/i")

# CLI Menu

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



	



