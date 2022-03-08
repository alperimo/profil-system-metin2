import gameInfo
import messenger
import event
import uiProfil

	def __BuildKeyDict(self):
		onPressKeyDict[app.DIK_P]			= lambda state = "PROFIL": self.interface.ToggleProfilWindow(state)

	def __ServerCommand_Build(self):
		serverCommandList={

			## New System Plugin ##
			"PythonToLua"			: self.__PythonToLua, # .python to Quest
			"PythonIslem"			: self.__PythonIslem, # .python to Quest
			"LuaToPython"			: self.__LuaToPython, # Quest to .python
			## END - New System Plugin - END ##

		}

	def OpenQuestWindow(self, skin, idx):
		if gameInfo.INPUT == 1:
			return
		self.interface.OpenQuestWindow(skin, idx)
		
	#[ekle]#
	def OnUpdate(self):
		if gameInfo.PROFIL_AC == 1:
			state = "PROFIL"
			self.interface.ToggleProfilWindow(state)
			gameInfo.PROFIL_AC = 0
		
	def __PythonToLua(self, id):
		gameInfo.PYTHONTOLUA = int(id)

	def __PythonIslem(self, PythonIslem):
		if PythonIslem == "PYTHONISLEM":
			net.SendQuestInputStringPacket(gameInfo.PYTHONISLEM)
		elif PythonIslem == "PROFIL_FACEBOOK":
			net.SendQuestInputStringPacket(str(gameInfo.PROFIL["FACEBOOK"]))
		elif PythonIslem == "PROFIL_WEBSITE":
			net.SendQuestInputStringPacket(str(gameInfo.PROFIL["WEBSITE"]))
		elif PythonIslem == "PROFIL_EPOSTA":
			net.SendQuestInputStringPacket(str(gameInfo.PROFIL["E-POSTA"]))
		elif PythonIslem == "PROFIL_SKYPE":
			net.SendQuestInputStringPacket(str(gameInfo.PROFIL["SKYPE"]))
		elif PythonIslem == "PROFIL_KISISEL":
			net.SendQuestInputStringPacket(str(gameInfo.PROFIL["KISISEL"]))
		elif PythonIslem == "PROFIL_KISISEL2":
			net.SendQuestInputStringPacket(str(gameInfo.PROFIL["KISISEL2"]))
			
	def __LuaToPython(self, LuaToPython):
		if LuaToPython.find("#quest_input#") != -1:
			gameInfo.INPUT = 1
		elif LuaToPython.find("#quest_inputbitir#") != -1:
			gameInfo.INPUT = 0
		elif LuaToPython.find("profil_olustur") != -1:
			gameInfo.PROFIL_DURUM = 1
		
		elif LuaToPython.find("profil|") != -1:
			LuaToPython = LuaToPython.replace("_"," ")
			bol = LuaToPython.split("#")
			gameInfo.PROFIL_NAME = LuaToPython.split("|")[1]
			gameInfo.PROFIL["PAYLASIM"] = int(bol[1])
			gameInfo.PROFIL["CINSIYET"] = str(bol[2])
			gameInfo.PROFIL["YAS"] = str(bol[3])
			gameInfo.PROFIL["IS"] = str(bol[4])
			gameInfo.PROFIL["ISYER"] = str(bol[5])
			gameInfo.PROFIL["SEHIR"] = str(bol[6])
			gameInfo.PROFIL["DOGUM-GUNU"] = str(bol[7])
			gameInfo.PROFIL["BURC"] = str(bol[8])
			gameInfo.PROFIL["FACEBOOK"] = str(bol[9])
			gameInfo.PROFIL["WEBSITE"] = str(bol[10])
			gameInfo.PROFIL["E-POSTA"] = str(bol[11])
			gameInfo.PROFIL["SKYPE"] = str(bol[12])
			gameInfo.PROFIL["KISISEL"] = str(bol[13])
			
		elif LuaToPython.find("profilim|") != -1:
			LuaToPython = LuaToPython.replace("_"," ")
			bol = LuaToPython.split("#")
			gameInfo.PROFIL_NAME = ""
			gameInfo.PROFIL["PAYLASIM"] = int(bol[1])
			gameInfo.PROFIL["CINSIYET"] = str(bol[2])
			gameInfo.PROFIL["YAS"] = str(bol[3])
			gameInfo.PROFIL["IS"] = str(bol[4])
			gameInfo.PROFIL["ISYER"] = str(bol[5])
			gameInfo.PROFIL["SEHIR"] = str(bol[6])
			gameInfo.PROFIL["DOGUM-GUNU"] = str(bol[7])
			gameInfo.PROFIL["BURC"] = str(bol[8])
			gameInfo.PROFIL["FACEBOOK"] = str(bol[9])
			gameInfo.PROFIL["WEBSITE"] = str(bol[10])
			gameInfo.PROFIL["E-POSTA"] = str(bol[11])
			gameInfo.PROFIL["SKYPE"] = str(bol[12])
			gameInfo.PROFIL["KISISEL"] = str(bol[13])
			
		elif LuaToPython.find("#profil_var#") != -1:
			bol = LuaToPython.split("#")
			isim = bol[2]
			if not isim in gameInfo.PROFIL_LIST:
				gameInfo.PROFIL_LIST.append(isim)
			gameInfo.TARGET = 1
		elif LuaToPython.find("profil_var2") != -1:
			bol = LuaToPython.split("#")
			isim = bol[2]
			if not isim in gameInfo.PROFIL_LIST:
				if self.__KONTROL(isim) == TRUE:
					gameInfo.PROFIL_LIST.append(isim)
			gameInfo.TARGET = 1
			
	def __KONTROL(self,gelen):
		if messenger.IsFriendByName(gelen):
			return TRUE
			
		return FALSE