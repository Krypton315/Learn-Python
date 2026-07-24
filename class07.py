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
		print("Input harus berupa String!\n")
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
		print("Input harus berupa Integer!\n")
		return None

	return int(check_input)


# All Class

class Student:
	def __init__(self, name, student_id):
		self.name = name
		self.student_id = student_id
		self.scores = []

	def add_score(self, score):
		self.scores.append(int(score))

	def average_score(self):
		if not self.scores:
			return 0
		return sum(self.scores) / len(self.scores)

	def get_grade(self):
		avg_score = self.average_score()
		if 90 <= avg_score <= 100:
			return "A"
		elif 80 <= avg_score:
			return "B"
		elif 70 <= avg_score:
			return "C"
		elif 60 <= avg_score:
			return "D"
		else:
			return "E"

	def display(self):
		print("\n--------------------------\n")
		print(f"Nama  : {self.name}")
		print(f"ID    : {self.student_id}")
		
		print("\nNilai :")
		for Nilai in self.scores:
			print(Nilai)

		print(f"\nRata-rata  : {self.average_score()}") 
		print(f"Grade      : {self.get_grade()}") 
		print("\n--------------------------")


class StudentManager:
	def __init__(self):
		self.__students = []

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
				print("Siswa dengan ID tersebut telah tersedia!\n")
				continue

			break

		self.__students.append(Student(name, ID))
		
		print("\n-----------------------")
		print("\nTambah Mahasiswa\n")
		print(f"Nama :\n{name}\n")
		print(f"ID : \n{ID}\n")
		print("Berhasil ditambahkan.")
		print("\n-----------------------")

	def find_student(self, ID):
		for item in self.__students:
			if item.student_id == ID:
				return item

		print("Siswa/i tidak tersedia!\n")
		return None

	def input_ID(self):
		while True:
			ID = validation_input_None(input("Masukkan ID Siswa/i: "))
			if ID is None: continue

			return ID

	def check_list_student(self):
		if not self.__students:
			print("- Belum ada data dalam list Student")
			return None

		return self.__students

	def add_student_score(self):
		print("\n=== Add Student Score ===")
		print("*Ketik 'EXIT' untuk Keluar\n")
		
		students_list = self.check_list_student()
		
		if students_list is None: return

		while True:
			ID = self.input_ID()
			if ID == "exit": return

			student = self.find_student(ID) 
			
			if student is None: continue

			break
		
		while True:
			Nilai = validation_input_int(input("Masukkan Nilai: "))
			if Nilai is None: continue
			if Nilai == "exit": return

			if Nilai < 0 or Nilai > 100:
				print("Nilai diluar batas\n")
				continue

			break
		
		student.add_score(Nilai)
		
		print("\n-----------------------")
		print("\nTambah Nilai\n")
		print(f"ID :\n{ID}\n")
		print(f"Nilai :\n{Nilai}\n")
		print("Berhasil ditambahkan.")
		print("\n-----------------------")

	def show_all_students(self):
		print("\n=== Show all students ===")
		
		students_list = self.check_list_student()
		if students_list is None: return

		for item in students_list:
			item.display()

	def search_student(self):
		print("\n=== Search Student ===")
		print("*Ketik 'EXIT' untuk Keluar\n")

		students_list = self.check_list_student()
		if students_list is None: return

		while True:
			ID = self.input_ID()
			if ID == "exit": return
			
			student = self.find_student(ID)

			if student is None: continue
			
			break
		
		student.display()

	def delete_student(self):
		print("\n=== Delete Student ===")
		print("*Ketik 'EXIT' untuk Keluar\n")
		
		students_list = self.check_list_student()
		if students_list is None: return

		while True:
			ID = self.input_ID()
			if ID == "exit": return

			student = self.find_student(ID)

			if student is None: continue

			break

		students_list.remove(student)	
		
		print("\n-----------------------")
		print("\nHapus Siswa/i\n")
		print(f"Nama :\n{student.name}\n")
		print(f"ID :\n{student.student_id}\n")
		print("Berhasil dihapus.")
		print("\n-----------------------")

# CLI Menu

SM = StudentManager()

menu = ("Tambah Mahasiswa", "Tambah Nilai", "Cari Mahasiswa",
		"Tampilkan Semua", "Hapus Mahasiswa", "Keluar")

while True:
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
			print("Menu tidak tersedia!")