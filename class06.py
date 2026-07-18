# Common Validation function!

def validation_input_None(input_usr):
	if not input_usr.strip():
		print("Input tidak boleh kosong!\n")
		return None

	if input_usr.lower() == "exit":
		return "exit"
	
	return input_usr.strip()

def validation_input_str(input_usr):
	check_input = validation_input_None(input_usr)

	if check_input is None:
		return None

	if check_input.isdigit():
		print("Input harus berupa String\n")
		return None

	if check_input == "exit":
		return "exit"

	return check_input

def validation_input_int(input_usr):
	check_input = validation_input_None(input_usr)

	if check_input is None:
		return None

	if check_input == "exit":
		return "exit"

	if not check_input.isdigit():
		print("Input harus berupa Integer\n")
		return None

	return int(check_input)


# All Class

class Student:
	def __init__(self, name, student_id):
		self.name = name
		self.student_id = student_id
		self.scores : []

	def add_score(self, score):
		self.scores.append(score)

	def average_score(self):
		if not self.scores:
			return 0
		return sum(self.scores) / len(self.scores)

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
		print(f"Nama  : {self.name}")
		print(f"ID    : {self.student_id}")
		print(f"Nilai : {self.scores}")
		print(f"Rata  : {self.average_score()}") 
		print(f"Grade : {self.get_grade()}") 
		print("========================")


class StudentManager:
	students = [] # Berisi objek Students, buat dalam bentuk list of dict

	def add_student(self):
		print("\n=== Add Student ===")
		print("*Ketik 'EXIT' untuk Keluar\n")
		
		while True:
			name = validation_input_str(input("Tambahkan Nama Siswa/i: "))
			if name is None: continue
			if name == "exit": return

			break

		while True:	
			ID = self.input_ID()
			if ID == "exit": return

			twin_id = self.find_student(ID)
			if twin_id is not None: 
				print("Siswa dengan ID tersebut telah tersedia\n")
				continue

			break

		StudentManager.students.append({ID : name}) # Perbaiki disini!
		print("\nBerhasil menambah Siswa/i")
		
	def find_student(self, ID): # Perbaiki disini!
		if item.student_id == ID:
				return item
		return None

	def input_ID(self):
		while True:
			ID = validation_input_None(input("Masukkan ID Siswa/i: "))
			if ID is None: continue

			return ID

	def check_list_student(self):
		if not StudentManager.students:
			return None

		return StudentManager.students

	def add_student_score(self):
		print("\n=== Add Student Score ===")
		print("*Ketik 'EXIT' untuk Keluar\n")
		
		students_list = self.check_list_student()
		if students_list is None: 
			print("Belum ada data dalam list Student")
			return

		while True:
			ID = self.input_ID()
			if ID == "exit": return

			student = self.find_student(ID) 
			
			if student is None:
				print("Siswa/i tidak tersedia!\n")
				continue

			break
		
		while True:
			Nilai = validation_input_int(input("Masukkan Nilai: "))
			if Nilai is None: continue
			if Nilai == "exit": return

			if Nilai <= 0 or Nilai > 100:
				print("Nilai diluar batas\n")
				continue

			break
		
		student.add_score(Nilai)
		print("\nBerhasil menambah Nilai Siswa/i")

	def show_all_students(self):
		print("\n=== Show all students ===")
		
		students_list = self.check_list_student()
		if students_list is None:
			print("\nBelum ada data dalam list Student")
			return

		for item in students_list:
			item.display()

	def search_student(self):
		print("\n=== Search Student ===")
		print("*Ketik 'EXIT' untuk Keluar\n")

		students_list = self.check_list_student()
		if students_list is None:
			print("Belum ada data dalam list Student")
			return

		while True:
			ID = self.input_ID()
			if ID == "exit": return
			
			student = self.find_student(ID)

			if student is None:
				print("Siswa/i tidak tersedia!\n")
				continue
			
			break
		
		student.display()

	def delete_student(self):
		print("\n=== Delete Student ===")
		print("*Ketik 'EXIT' untuk Keluar\n")
		
		students_list = self.check_list_student()
		if students_list is None:
			print("Belum ada data dalam list Student")
			return

		while True:
			ID = self.input_ID()
			if ID == "exit": return

			student = self.find_student(ID)

			if student is None:
				print("Siswa/i tidak tersedia!\n")
				continue

			break

		students_list.remove(student)	
		print("\nBerhasil menghapus Siswa/i")

# CLI Menu

SM = StudentManager()
while True:
	menu = ("Tambah Mahasiswa", "Tambah Nilai", "Cari Mahasiswa",
		"Tampilkan Semua", "Hapus Mahasiswa", "Keluar")

	print("\n======== MENU ========\n")
	for Nomor, Nama_menu in enumerate(menu, start=1):
		print(f"{Nomor}. {Nama_menu}")

	pilih_menu = validation_input_int(input("\nPilih Nomor MENU: "))
	if pilih_menu is None: continue

	match pilih_menu:
		case 1:
			SM.add_student()
		case 2:
			SM.add_student_score()
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



	



