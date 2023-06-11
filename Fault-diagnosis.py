from pyknow import *

fault_list = []
fault_list_symptoms = []
fault_map = {}
d_desc_map = {}
d_solutions_map = {}

def preprocess():
	global fault_list,fault_list_symptoms,fault_map,d_desc_map,d_solutions_map
	fault = open("Fault-diagnosis/faults.txt")
	fault_t = fault.read()
	fault_list = fault_t.split("\n")
	fault.close()
	for fault in fault_list:
		fault_s_file = open("Fault-diagnosis/Fault-symptoms/" + fault + ".txt")
		fault_s_data = fault_s_file.read()
		s_list = fault_s_data.split("\n")
		fault_list_symptoms.append(s_list)
		fault_map[str(s_list)] = fault
  		
		fault_s_file.close()
		fault_s_file = open("Fault-diagnosis/Fault-descriptions/" + fault + ".txt")
		fault_s_data = fault_s_file.read()
		d_desc_map[fault] = fault_s_data
		fault_s_file.close()
		fault_s_file = open("Fault-diagnosis/Fault-solutions/" + fault + ".txt")
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
		print("The most probable fault that you have is %s\n" %(id_fault))
		print("A short description of the fault is given below :\n")
		print(fault_details+"\n")
		print("The common medications and procedures suggested by other real doctors are: \n")
		print(solutions+"\n")

# @my_decorator is just a way of saying just_some_function = my_decorator(just_some_function)
#def identify_fault(headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness,low_body_temp ,fever,sunken_eyes):
class Greetings(KnowledgeEngine):
	@DefFacts()
	def _initial_action(self):
		print("")
		print("Hi! I am Dr.Yar, I am here to help you make your health better.")
		print("For that you'll have to answer a few questions about your conditions")
		print("Do you feel any of the following symptoms:")
		print("")
		yield Fact(action="find_fault")


	@Rule(Fact(action='find_fault'), NOT(Fact(headache=W())),salience = 1)
	def symptom_0(self):
		self.declare(Fact(headache=input("headache: ")))

	@Rule(Fact(action='find_fault'), NOT(Fact(back_pain=W())),salience = 1)
	def symptom_1(self):
		self.declare(Fact(back_pain=input("back pain: ")))

	@Rule(Fact(action='find_fault'), NOT(Fact(chest_pain=W())),salience = 1)
	def symptom_2(self):
		self.declare(Fact(chest_pain=input("chest pain: ")))

	@Rule(Fact(action='find_fault'), NOT(Fact(cough=W())),salience = 1)
	def symptom_3(self):
		self.declare(Fact(cough=input("cough: ")))

	@Rule(Fact(action='find_fault'), NOT(Fact(fainting=W())),salience = 1)
	def symptom_4(self):
		self.declare(Fact(fainting=input("fainting: ")))

	@Rule(Fact(action='find_fault'), NOT(Fact(fatigue=W())),salience = 1)
	def symptom_5(self):
		self.declare(Fact(fatigue=input("fatigue: ")))
	 
	@Rule(Fact(action='find_fault'), NOT(Fact(sunken_eyes=W())),salience = 1)
	def symptom_6(self):
		self.declare(Fact(sunken_eyes=input("sunken eyes: ")))
	
	@Rule(Fact(action='find_fault'), NOT(Fact(low_body_temp=W())),salience = 1)
	def symptom_7(self):
		self.declare(Fact(low_body_temp=input("low body temperature: ")))
	
	@Rule(Fact(action='find_fault'), NOT(Fact(restlessness=W())),salience = 1)
	def symptom_8(self):
		self.declare(Fact(restlessness=input("restlessness: ")))
	
	@Rule(Fact(action='find_fault'), NOT(Fact(sore_throat=W())),salience = 1)
	def symptom_9(self):
		self.declare(Fact(sore_throat=input("sore throat: ")))
	
	@Rule(Fact(action='find_fault'), NOT(Fact(fever=W())),salience = 1)
	def symptom_10(self):
		self.declare(Fact(fever=input("fever: ")))

	@Rule(Fact(action='find_fault'), NOT(Fact(nausea=W())),salience = 1)
	def symptom_11(self):
		self.declare(Fact(nausea=input("Nausea: ")))

	@Rule(Fact(action='find_fault'), NOT(Fact(blurred_vision=W())),salience = 1)
	def symptom_12(self):
		self.declare(Fact(blurred_vision=input("blurred_vision: ")))

	@Rule(Fact(action='find_fault'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def fault_0(self):
		self.declare(Fact(fault="Jaundice"))

	@Rule(Fact(action='find_fault'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="yes"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def fault_1(self):
		self.declare(Fact(fault="Alzheimers"))

	@Rule(Fact(action='find_fault'),Fact(headache="no"),Fact(back_pain="yes"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def fault_2(self):
		self.declare(Fact(fault="Arthritis"))

	@Rule(Fact(action='find_fault'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def fault_3(self):
		self.declare(Fact(fault="Tuberculosis"))

	@Rule(Fact(action='find_fault'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="yes"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def fault_4(self):
		self.declare(Fact(fault="Asthma"))

	@Rule(Fact(action='find_fault'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="yes"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def fault_5(self):
		self.declare(Fact(fault="Sinusitis"))

	@Rule(Fact(action='find_fault'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def fault_6(self):
		self.declare(Fact(fault="Epilepsy"))

	@Rule(Fact(action='find_fault'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def fault_7(self):
		self.declare(Fact(fault="Heart fault"))

	@Rule(Fact(action='find_fault'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="yes"))
	def fault_8(self):
		self.declare(Fact(fault="Diabetes"))

	@Rule(Fact(action='find_fault'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="yes"))
	def fault_9(self):
		self.declare(Fact(fault="Glaucoma"))

	@Rule(Fact(action='find_fault'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def fault_10(self):
		self.declare(Fact(fault="Hyperthyroidism"))

	@Rule(Fact(action='find_fault'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def fault_11(self):
		self.declare(Fact(fault="Heat Stroke"))

	@Rule(Fact(action='find_fault'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="yes"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="yes"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def fault_12(self):
		self.declare(Fact(fault="Hypothermia"))

	@Rule(Fact(action='find_fault'),Fact(fault=MATCH.fault),salience = -998)
	def fault(self, fault):
		print("")
		id_fault = fault
		fault_details = get_details(id_fault)
		solutions = get_solutions(id_fault)
		print("")
		print("The most probable fault that you have is %s\n" %(id_fault))
		print("A short description of the fault is given below :\n")
		print(fault_details+"\n")
		print("The common medications and procedures suggested by other real doctors are: \n")
		print(solutions+"\n")

	@Rule(Fact(action='find_fault'),
		  Fact(headache=MATCH.headache),
		  Fact(back_pain=MATCH.back_pain),
		  Fact(chest_pain=MATCH.chest_pain),
		  Fact(cough=MATCH.cough),
		  Fact(fainting=MATCH.fainting),
		  Fact(sore_throat=MATCH.sore_throat),
		  Fact(fatigue=MATCH.fatigue),
		  Fact(low_body_temp=MATCH.low_body_temp),
		  Fact(restlessness=MATCH.restlessness),
		  Fact(fever=MATCH.fever),
		  Fact(sunken_eyes=MATCH.sunken_eyes),
		  Fact(nausea=MATCH.nausea),
		  Fact(blurred_vision=MATCH.blurred_vision),NOT(Fact(fault=MATCH.fault)),salience = -999)

	def not_matched(self,headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness,low_body_temp ,fever ,sunken_eyes ,nausea ,blurred_vision):
		print("\nDid not find any fault that matches your exact symptoms")
		lis = [headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness,low_body_temp ,fever ,sunken_eyes ,nausea ,blurred_vision]
		max_count = 0
		max_fault = ""
		for key,val in fault_map.items():
			count = 0
			temp_list = eval(key)
			for j in range(0,len(lis)):
				if(temp_list[j] == lis[j] and lis[j] == "yes"):
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
		print("Would you like to diagnose some other symptoms?")
		if input() == "no":
			exit()
		#print(engine.facts)