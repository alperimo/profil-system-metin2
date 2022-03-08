import localegame
import gameInfo
import uiProfil

	BUTTON_NAME_LIST = ( 
	
		"Profil",#40k-localeInfo
	
	)
	
	def __init__(self):
		self.PROFIL = uiProfil.ProfilWindow()
		self.zaman2 = 0
			
		self.buttonDict["Profil"].SAFE_SetEvent(self.__OnProfilGoster)
		
	def Open(self):
		if name in gameInfo.PROFIL_LIST:
			gameInfo.PROFIL_LIST.remove(name)
		self.PAKET = 0
		
	def RefreshButton(self):
		if player.IsPartyMember(self.vid):
			#[...]#
		else:
			#[...]#
			
			if(self.zaman2 < app.GetTime()):
				self.zaman2 = 0
				if chr.GetNameByVID(self.vid) in gameInfo.PROFIL_LIST:
					self.__ShowButton("Profil")
				else:
					self.__HideButton("Profil")
			else:
				self.__HideButton("Profil")
		
	def __OnProfilGoster(self):
		if not (self.zaman2 < app.GetTime()):
			chat.AppendChat(chat.CHAT_TYPE_INFO, localegame.OYUN_PROFIL_SURE)
			return
		#if self.PROFIL.IsShow():
		if gameInfo.PROFIL_ISHOW == 1:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localegame.PROFIL_BAKIYORSUN)
			return
		self.zaman2 = app.GetTime() + 10
		gameInfo.PROFIL_EKRANI = 1
		gameInfo.PROFIL_NAME = chr.GetNameByVID(self.vid)
		gameInfo.PROFIL_TARGET = 1
		gameInfo.PROFIL_AC = 1
		
	def OnUpdate(self):
		if gameInfo.TARGET == 1:
			gameInfo.TARGET = 0
			self.PAKET = 1
		
		if self.isShowButton:
					
			if (self.vid != 0):				
				if self.PAKET == 0:
					gameInfo.PYTHONISLEM = "profil_kontrol#"+str(self.vid)+"#"+str(chr.GetNameByVID(self.vid))+"#"
					event.QuestButtonClick(gameInfo.PYTHONTOLUA)
					self.PAKET = 1
		