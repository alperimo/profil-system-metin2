import uiProfil
import gameInfo
import systemSetting

			self.gameButtonDict={
				"PROFIL" : self.GetChild("ProfilButton"),
			}
			
			self.gameButtonDict["PROFIL"].SetEvent(ui.__mem_func__(self.__OnClickProfilGOSTER))
			
	#new
	def __OnClickProfilGOSTER(self):
		gameInfo.PROFIL_AC = 1
		
	#new
	def OnUpdate(self):
		if gameInfo.PROFIL_DURUM==0:
			self.gameButtonDict["PROFIL"].Hide()
		
	#change
	def CheckGameButton(self):
	
		statusPlusButton=self.gameButtonDict["STATUS"]
		skillPlusButton=self.gameButtonDict["SKILL"]
		helpButton=self.gameButtonDict["HELP"]
		profilButton=self.gameButtonDict["PROFIL"]

		if self.__IsSkillStat():
			skillPlusButton.Show()
		else:
			skillPlusButton.Hide()

		if 0 == player.GetPlayTime():
			helpButton.Show()
			helpButton.SetPosition(68, systemSetting.GetHeight()-170)
			if gameInfo.PROFIL_DURUM == 1:
				profilButton.SetPosition(68, systemSetting.GetHeight()-240)
				profilButton.Show()
			else:
				profilButton.Hide()
		else:
			if gameInfo.PROFIL_DURUM == 1:
				profilButton.SetPosition(68, systemSetting.GetHeight()-170)
				profilButton.Show()
			else:
				profilButton.Hide()
			helpButton.Hide()
			
		if player.GetStatus(player.STAT) > 0:
			statusPlusButton.Show()
		else:
			statusPlusButton.Hide()
			if 0 == player.GetPlayTime():
				helpButton.Show()
				helpButton.SetPosition(68, systemSetting.GetHeight()-100)
				if gameInfo.PROFIL_DURUM == 1:
					profilButton.SetPosition(68, systemSetting.GetHeight()-170)
					profilButton.Show()
				else:
					profilButton.Hide()
			else:
				helpButton.Hide()
				if gameInfo.PROFIL_DURUM == 1:
					profilButton.SetPosition(68, systemSetting.GetHeight()-100)
					profilButton.Show()
				else:
					profilButton.Hide()