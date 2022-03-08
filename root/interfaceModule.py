import uiProfil
import gameInfo

	def __MakeWindows(self):
		#[...]#
		self.ProfilSystemWindow = uiProfil.ProfilSystemWnd
		
	def Close(self):
		#[...]#
		if self.ProfilSystemWindow:
			self.ProfilSystemWindow.Destroy()
			
		del self.ProfilSystemWindow
		
	#[ekle]#
	
	def ToggleProfilWindowStatusPage(self):
		if gameInfo.PROFIL_BUTTON == 0:
			self.ToggleProfilWindow("PROFIL")
	
	def ToggleProfilWindow(self, state):
		if FALSE == player.IsObserverMode():
			if FALSE == self.ProfilSystemWindow.IsShow():
				self.OpenProfilWindowWithState(state)
			else:
				if state == self.ProfilSystemWindow.GetState():
					self.ProfilSystemWindow.Close()
				else:
					self.OpenProfilWindowWithState(state)

	def OpenProfilWindowWithState(self, state):
		if FALSE == player.IsObserverMode():
			self.ProfilSystemWindow.Show()
			self.ProfilSystemWindow.SetTop()
			self.ProfilSystemWindow.SetState(state)