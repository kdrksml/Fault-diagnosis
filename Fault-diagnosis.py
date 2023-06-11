# -*- coding: utf-8 -*-

from pyknow import *
import os.path
import sys
fault_list = []
fault_list_symptoms = []
fault_map = {}
d_desc_map = {}
d_solutions_map = {}

def preprocess():
	global fault_list,fault_list_symptoms,fault_map,d_desc_map,d_solutions_map
	fault = open("faults.txt", encoding="utf-8")
	fault_t = fault.read()
	fault_list = fault_t.split("\n")
	fault.close()
	for fault in fault_list:
		fault_s_file = open("Fault-symptoms/" + fault + ".txt", encoding="utf-8")
		fault_s_data = fault_s_file.read()
		s_list = fault_s_data.split("\n")
		fault_list_symptoms.append(s_list)
		fault_map[str(s_list)] = fault
  		
		fault_s_file.close()
		fault_s_file = open("Fault-descriptions/" + fault + ".txt",encoding="utf-8")
		fault_s_data = fault_s_file.read()
		d_desc_map[fault] = fault_s_data
		fault_s_file.close()
		fault_s_file = open("Fault-solutions/" + fault + ".txt",encoding="utf-8")
		fault_s_data = fault_s_file.read()
		d_solutions_map[fault] = fault_s_data
  		
		fault_s_file.close()
	


def identify_fault(*arguments):
	symptom_list = []
	for symptom in arguments:
		symptom_list.append(symptom)
	# Handle key error
	return fault_map[str(symptom_list)]

def get_details(fault):
	return d_desc_map[fault]

def get_solutions(fault):
	return d_solutions_map[fault]

def if_not_matched(fault):
		print("")
		id_fault = fault
		fault_details = get_details(id_fault)
		solutions = get_solutions(id_fault)
		print("")
		print("Muhtemel arızanız :  %s\n" %(id_fault))
		print("Arıza hakkında genel bilgi aşağıdadır :\n")
		print(fault_details+"\n")
		print("Bu konuda yapılabilecekler şu şekildedir :  \n")
		print(solutions+"\n")

# @my_decorator is just a way of saying just_some_function = my_decorator(just_some_function)
#def identify_fault(motor, direksiyon, yağ, fren, lastik, pedal, şanzıman, yakıt,egzoz ,ısınma,elektrik):
class Greetings(KnowledgeEngine):
	@DefFacts()
	def _initial_action(self):
		print("")
		print("Merhaba ! , ")
		print("Aracınızda bulunan semptomplara evet veya hayır diyerek uzman sistemimizin çalıştırabilirsiniz")
		print("Araçta aşağıdaki semptomlar var mı")
		print("Var ise evet yok ise hayır yazınız.")
		print
		("")
		yield Fact(action="find_fault")


	@Rule(Fact(action='find_fault'), NOT(Fact(motor=W())),salience = 1)
	def symptom_0(self):
		self.declare(Fact(motor=input("Motor çalıştırıldığında herhangi bir anormal ses duyuluyor mu?: ")))

	@Rule(Fact(action='find_fault'), NOT(Fact(direksiyon=W())),salience = 1)
	def symptom_1(self):
		self.declare(Fact(direksiyon=input("Direksiyonu çevirdiğinizde herhangi bir zorluk yaşıyor musunuz?: ")))

	@Rule(Fact(action='find_fault'), NOT(Fact(yağ=W())),salience = 1)
	def symptom_2(self):
		self.declare(Fact(yağ=input("Motor yağı seviyesi düşüyor veya aşırıya mı çıkıyor?: ")))

	@Rule(Fact(action='find_fault'), NOT(Fact(fren=W())),salience = 1)
	def symptom_3(self):
		self.declare(Fact(fren=input("Fren pedalını bıraktığınızda fren lambaları hala yanıyor mu?: ")))

	@Rule(Fact(action='find_fault'), NOT(Fact(lastik=W())),salience = 1)
	def symptom_4(self):
		self.declare(Fact(lastik=input("Lastiklerde herhangi bir aşınma, çatlaklık veya şişkinlik var mı?: ")))

	@Rule(Fact(action='find_fault'), NOT(Fact(şanzıman=W())),salience = 1)
	def symptom_5(self):
		self.declare(Fact(şanzıman=input("Şanzımanın geçişleri sırasında ani bir sarsıntı hissediliyor mu?: ")))
	 
	@Rule(Fact(action='find_fault'), NOT(Fact(elektrik=W())),salience = 1)
	def symptom_6(self):
		self.declare(Fact(elektrik=input("Aracın elektrik sistemi ile ilgili herhangi bir sorun yaşıyor musunuz? (farlar, sinyal lambaları, radyo vb.): ")))
	
	@Rule(Fact(action='find_fault'), NOT(Fact(egzoz=W())),salience = 1)
	def symptom_7(self):
		self.declare(Fact(egzoz=input("Egzozdan herhangi bir anormal duman çıkıyor mu?: ")))
	
	@Rule(Fact(action='find_fault'), NOT(Fact(yakıt=W())),salience = 1)
	def symptom_8(self):
		self.declare(Fact(yakıt=input("Yakıt tüketimi normalden daha yüksek mi?: ")))
	
	@Rule(Fact(action='find_fault'), NOT(Fact(pedal=W())),salience = 1)
	def symptom_9(self):
		self.declare(Fact(pedal=input(
			"Fren pedalını sertleştirerek basmam gerekiyor mu?: ")))
	
	@Rule(Fact(action='find_fault'), NOT(Fact(ısınma=W())),salience = 1)
	def symptom_10(self):
		self.declare(Fact(ısınma=input("Aracın ısınması normalden daha uzun sürüyor mu? ")))

	@Rule(Fact(action='find_fault'), NOT(Fact(valf=W())),salience = 1)
	def symptom_11(self):
		self.declare(Fact(valf=input(
			"Aracınız çalışırken valf sesleri normalden daha yüksek mi? ")))

	@Rule(Fact(action='find_fault'), NOT(Fact(kesinti=W())),salience = 1)
	def symptom_12(self):
		self.declare(Fact(kesinti=input(
			"Aracınızda hızlanma sırasında ya da seyir halindeyken motor gücünde aniden düşme veya kesintiler yaşıyor musunuz? ")))

	@Rule(Fact(action='find_fault'),Fact(motor="no"),Fact(direksiyon="no"),Fact(yağ="no"),Fact(fren="no"),Fact(lastik="no"),Fact(pedal="no"),Fact(şanzıman="yes"),Fact(yakıt="no"),Fact(egzoz="no"),Fact(ısınma="yes"),Fact(elektrik="no"),Fact(valf="yes"),Fact(kesinti="no"))
	def fault_0(self):
		self.declare(Fact(fault="AküArızaları"))

	@Rule(Fact(action='find_fault'),Fact(motor="no"),Fact(direksiyon="no"),Fact(yağ="no"),Fact(fren="no"),Fact(lastik="no"),Fact(pedal="no"),Fact(şanzıman="no"),Fact(yakıt="yes"),Fact(egzoz="no"),Fact(ısınma="no"),Fact(elektrik="no"),Fact(valf="no"),Fact(kesinti="no"))
	def fault_1(self):
		self.declare(Fact(fault="ElektrikselAriza"))

	@Rule(Fact(action='find_fault'),Fact(motor="no"),Fact(direksiyon="yes"),Fact(yağ="no"),Fact(fren="no"),Fact(lastik="no"),Fact(pedal="no"),Fact(şanzıman="yes"),Fact(yakıt="no"),Fact(egzoz="no"),Fact(ısınma="no"),Fact(elektrik="no"),Fact(valf="no"),Fact(kesinti="no"))
	def fault_2(self):
		self.declare(Fact(fault="Fren_Balata_Arızası"))

	@Rule(Fact(action='find_fault'),Fact(motor="no"),Fact(direksiyon="no"),Fact(yağ="yes"),Fact(fren="yes"),Fact(lastik="no"),Fact(pedal="no"),Fact(şanzıman="no"),Fact(yakıt="no"),Fact(egzoz="no"),Fact(ısınma="yes"),Fact(elektrik="no"),Fact(valf="no"),Fact(kesinti="no"))
	def fault_3(self):
		self.declare(Fact(fault="Rot_Başı_Problemi"))

	@Rule(Fact(action='find_fault'),Fact(motor="no"),Fact(direksiyon="no"),Fact(yağ="yes"),Fact(fren="yes"),Fact(lastik="no"),Fact(pedal="no"),Fact(şanzıman="no"),Fact(yakıt="yes"),Fact(egzoz="no"),Fact(ısınma="no"),Fact(elektrik="no"),Fact(valf="no"),Fact(kesinti="no"))
	def fault_4(self):
		self.declare(Fact(fault="SensörArızaları"))

	@Rule(Fact(action='find_fault'),Fact(motor="yes"),Fact(direksiyon="no"),Fact(yağ="no"),Fact(fren="yes"),Fact(lastik="no"),Fact(pedal="yes"),Fact(şanzıman="no"),Fact(yakıt="no"),Fact(egzoz="no"),Fact(ısınma="yes"),Fact(elektrik="no"),Fact(valf="no"),Fact(kesinti="no"))
	def fault_5(self):
		self.declare(Fact(fault="SigortaProblemleri"))

	@Rule(Fact(action='find_fault'),Fact(motor="no"),Fact(direksiyon="no"),Fact(yağ="no"),Fact(fren="no"),Fact(lastik="no"),Fact(pedal="no"),Fact(şanzıman="yes"),Fact(yakıt="no"),Fact(egzoz="no"),Fact(ısınma="no"),Fact(elektrik="no"),Fact(valf="no"),Fact(kesinti="no"))
	def fault_6(self):
		self.declare(Fact(fault="SogutmaSistemiArizasi"))

	@Rule(Fact(action='find_fault'),Fact(motor="no"),Fact(direksiyon="no"),Fact(yağ="yes"),Fact(fren="no"),Fact(lastik="no"),Fact(pedal="no"),Fact(şanzıman="no"),Fact(yakıt="no"),Fact(egzoz="no"),Fact(ısınma="no"),Fact(elektrik="no"),Fact(valf="yes"),Fact(kesinti="no"))
	def fault_7(self):
		self.declare(Fact(fault="Süspansiyon_Arızası"))

	@Rule(Fact(action='find_fault'),Fact(motor="no"),Fact(direksiyon="no"),Fact(yağ="no"),Fact(fren="no"),Fact(lastik="no"),Fact(pedal="no"),Fact(şanzıman="yes"),Fact(yakıt="no"),Fact(egzoz="no"),Fact(ısınma="no"),Fact(elektrik="no"),Fact(valf="yes"),Fact(kesinti="yes"))
	def fault_8(self):
		self.declare(Fact(fault="ValfArizasi"))

	@Rule(Fact(action='find_fault'),Fact(motor="yes"),Fact(direksiyon="no"),Fact(yağ="no"),Fact(fren="no"),Fact(lastik="no"),Fact(pedal="no"),Fact(şanzıman="no"),Fact(yakıt="no"),Fact(egzoz="no"),Fact(ısınma="no"),Fact(elektrik="no"),Fact(valf="yes"),Fact(kesinti="yes"))
	def fault_9(self):
		self.declare(Fact(fault="YakıtEnjektörlerininTıkanması"))

	@Rule(Fact(action='find_fault'),Fact(motor="no"),Fact(direksiyon="no"),Fact(yağ="no"),Fact(fren="no"),Fact(lastik="no"),Fact(pedal="no"),Fact(şanzıman="yes"),Fact(yakıt="no"),Fact(egzoz="no"),Fact(ısınma="no"),Fact(elektrik="no"),Fact(valf="yes"),Fact(kesinti="no"))
	def fault_10(self):
		self.declare(Fact(fault="YakıtFiltresiArızalari"))

	@Rule(Fact(action='find_fault'),Fact(motor="yes"),Fact(direksiyon="no"),Fact(yağ="no"),Fact(fren="no"),Fact(lastik="no"),Fact(pedal="no"),Fact(şanzıman="no"),Fact(yakıt="no"),Fact(egzoz="no"),Fact(ısınma="yes"),Fact(elektrik="no"),Fact(valf="yes"),Fact(kesinti="no"))
	def fault_11(self):
		self.declare(Fact(fault="YakıtPompasıArızaları"))


	@Rule(Fact(action='find_fault'),Fact(fault=MATCH.fault),salience = -998)
	def fault(self, fault):
		print("")
		id_fault = fault
		fault_details = get_details(id_fault)
		solutions = get_solutions(id_fault)
		print("")
		print("Muhtemel problem : %s\n" %(id_fault))
		print("Arızanın tanımı:  :\n")
		print(fault_details+"\n")
		print("Bu arıza için yapabilecekleriniz: \n")
		print(solutions+"\n")

	@Rule(Fact(action='find_fault'),
		  Fact(motor=MATCH.motor),
		  Fact(direksiyon=MATCH.direksiyon),
		  Fact(yağ=MATCH.yağ),
		  Fact(fren=MATCH.fren),
		  Fact(lastik=MATCH.lastik),
		  Fact(pedal=MATCH.pedal),
		  Fact(şanzıman=MATCH.şanzıman),
		  Fact(egzoz=MATCH.egzoz),
		  Fact(yakıt=MATCH.yakıt),
		  Fact(ısınma=MATCH.ısınma),
		  Fact(elektrik=MATCH.elektrik),
		  Fact(valf=MATCH.valf),
		  Fact(kesinti=MATCH.kesinti),NOT(Fact(fault=MATCH.fault)),salience = -999)

	def not_matched(self,motor, direksiyon, yağ, fren, lastik, pedal, şanzıman, yakıt,egzoz ,ısınma ,elektrik ,valf ,kesinti):
		print("\nDid not find any fault that matches your exact symptoms")
		lis = [motor, direksiyon, yağ, fren, lastik, pedal, şanzıman, yakıt,egzoz ,ısınma ,elektrik ,valf ,kesinti]
		max_count = 0
		max_fault = ""
		for key,val in fault_map.items():
			count = 0
			temp_list = eval(key)
			for j in range(0,len(lis)):
				if(temp_list[j] == lis[j] and lis[j] == "evet"):
					count = count + 1
			if count > max_count:
				max_count = count
				max_fault = val
		if_not_matched(max_fault)


if __name__ == "__main__":
	preprocess()
	engine = Greetings()
	while(1):
		engine.reset()  # Prepare the engine for the execution.
		engine.run()  # Run it!
		print("Başka bir arızayı kontrol etmek ister misiniz?")
		if input() == "hayır":
			exit()
		#print(engine.facts)