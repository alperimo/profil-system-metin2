import app
import event
import net
import player
import item
import os
import ui
import uiToolTip
import mouseModule
import localegame
import uiCommon
import constInfo
import gameInfo
import dbg
import math
import shop
import chat
import snd
from _weakref import proxy

class ProfilWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded = FALSE
		self.TabButtonDict = None
		self.TabImageDict = None
		self.PageDict = None
		self.TitleNameDict = None
		
	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		if gameInfo.PROFIL_DURUM == 1 and gameInfo.PROFIL_TARGET == 0:#kendi profili (olusturma)
			gameInfo.PROFIL_NAME = player.GetName()
			gameInfo.PROFIL_EKRANI = 1
			gameInfo.PROFIL_ISHOW = 1
		elif gameInfo.PROFIL_DURUM == 0 and gameInfo.PROFIL_TARGET == 0: #kendi profili(bakma)
			gameInfo.PROFIL_NAME = ""
			gameInfo.PROFIL_EKRANI = 1
			gameInfo.PROFIL_ISHOW = 1
		elif gameInfo.PROFIL_DURUM == 0 and gameInfo.PROFIL_TARGET == 1:#rakip profili
			gameInfo.PROFIL_EKRANI = 1
			gameInfo.PROFIL_ISHOW = 1
			self.Zaman = app.GetTime()
			self.__profilWithTargetAL()
		elif gameInfo.PROFIL_DURUM == 1 and gameInfo.PROFIL_TARGET == 1:#rakip profili
			gameInfo.PROFIL_EKRANI = 1
			gameInfo.PROFIL_ISHOW = 1
			self.Zaman = app.GetTime()
			self.__profilWithTargetAL()
			
		if FALSE == self.isLoaded:
			self.__LoadScript()

		ui.ScriptWindow.Show(self)
		
	def __LoadScript(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/profilwindow.py")
		except:
			import exception
			exception.Abort("test.__LoadScript.LoadObject")

		try: 
			self.Board = self.GetChild("Board")
			self.Titlebar = self.GetChild("Titlebar")
			self.TamamButton = self.GetChild("TamamButton")
			self.DuzenleButton = self.GetChild("DuzenleButton")
			self.IptalButton = self.GetChild("IptalButton")
			
			## paylasimBASLA ##
			self.Paylasim = {
				"HERKES" : self.GetChild("Paylasim-Herkes-Button"),
				"ARKADASLAR" : self.GetChild("Paylasim-Arkadaslar-Button"),
				"OZEL" : self.GetChild("Paylasim-Ozel-Button"),
			}
			self.Paylasim["HERKES"].Enable()
			self.Paylasim["ARKADASLAR"].Enable()
			self.Paylasim["OZEL"].Enable()
			## paylasimSON ##
			
			## sosyalBaglantilarBASLA ##
			self.SosyalAG = {
				"FACEBOOK" : self.GetChild("Facebook-Value"),
				"WEBSITE" : self.GetChild("WebSite-Value"),
				"E-POSTA" : self.GetChild("Eposta-Value"),
				"SKYPE" : self.GetChild("Skype-Value"),
				"KISISEL" : self.GetChild("Kisisel-Value"),
				
				"FACEBOOK_TEXT" : self.GetChild("Facebook-TEXT"),
				"WEBSITE_TEXT" : self.GetChild("WebSite-TEXT"),
				"E-POSTA_TEXT" : self.GetChild("Eposta-TEXT"),
				"SKYPE_TEXT" : self.GetChild("Skype-TEXT"),
				"KISISEL_TEXT" : self.GetChild("Kisisel-TEXT"),
			}
			## sosyalBaglantilarSON ##
			
			self.Cinsiyet = self.GetChild("Cinsiyet-Value")
			self.Yas = self.GetChild("Yas-Value")
			self.Is = self.GetChild("Is-Value")
			self.IsYER = self.GetChild("IsYER-Value")
			self.Sehir = self.GetChild("Sehir-Value")
			self.Ilce = self.GetChild("Ilce-Value")
			self.DogumGunu = self.GetChild("DogumGunu-Value")
			self.DogumGunu2 = self.GetChild("DogumGunu2-Value")
			self.Burc = self.GetChild("Burc-Value")
			
			self.Cinsiyet_TEXT = self.GetChild("Cinsiyet-TEXT")
			self.Yas_TEXT = self.GetChild("Yas-TEXT")
			self.Is_TEXT = self.GetChild("Is-TEXT")
			self.IsYER_TEXT = self.GetChild("IsYER-TEXT")
			self.Sehir_TEXT = self.GetChild("Sehir-TEXT")
			self.Ilce_TEXT = self.GetChild("Ilce-TEXT")
			self.DogumGunu_TEXT = self.GetChild("DogumGunu-TEXT")
			self.DogumGunu2_TEXT = self.GetChild("DogumGunu2-TEXT")
			self.Burc_TEXT = self.GetChild("Burc-TEXT")
			
			self.Cinsiyet.SetReturnEvent(ui.__mem_func__(self.Yas.SetFocus))
			self.Yas.SetReturnEvent(ui.__mem_func__(self.Is.SetFocus))
			self.Is.SetReturnEvent(ui.__mem_func__(self.IsYER.SetFocus))
			self.IsYER.SetReturnEvent(ui.__mem_func__(self.Sehir.SetFocus))
			self.Sehir.SetReturnEvent(ui.__mem_func__(self.DogumGunu.SetFocus))
			#self.Ilce.SetReturnEvent(ui.__mem_func__(self.DogumGunu.SetFocus))
			self.DogumGunu.SetReturnEvent(ui.__mem_func__(self.Burc.SetFocus))
			#self.DogumGunu2.SetReturnEvent(ui.__mem_func__(self.Burc.SetFocus))
			self.Burc.SetReturnEvent(ui.__mem_func__(self.SosyalAG["FACEBOOK"].SetFocus))
			self.SosyalAG["FACEBOOK"].SetReturnEvent(ui.__mem_func__(self.SosyalAG["WEBSITE"].SetFocus))
			self.SosyalAG["WEBSITE"].SetReturnEvent(ui.__mem_func__(self.SosyalAG["E-POSTA"].SetFocus))
			self.SosyalAG["E-POSTA"].SetReturnEvent(ui.__mem_func__(self.SosyalAG["SKYPE"].SetFocus))
			self.SosyalAG["SKYPE"].SetReturnEvent(ui.__mem_func__(self.SosyalAG["KISISEL"].SetFocus))
			self.SosyalAG["KISISEL"].SetReturnEvent(ui.__mem_func__(self.Cinsiyet.SetFocus))
			
			self.Cinsiyet.SetTabEvent(ui.__mem_func__(self.Yas.SetFocus))
			self.Yas.SetTabEvent(ui.__mem_func__(self.Is.SetFocus))
			self.Is.SetTabEvent(ui.__mem_func__(self.IsYER.SetFocus))
			self.IsYER.SetTabEvent(ui.__mem_func__(self.Sehir.SetFocus))
			self.Sehir.SetTabEvent(ui.__mem_func__(self.DogumGunu.SetFocus))
			#self.Ilce.SetTabEvent(ui.__mem_func__(self.DogumGunu.SetFocus))
			self.DogumGunu.SetTabEvent(ui.__mem_func__(self.Burc.SetFocus))
			#self.DogumGunu2.SetTabEvent(ui.__mem_func__(self.Burc.SetFocus))
			self.Burc.SetTabEvent(ui.__mem_func__(self.SosyalAG["FACEBOOK"].SetFocus))
			self.SosyalAG["FACEBOOK"].SetTabEvent(ui.__mem_func__(self.SosyalAG["WEBSITE"].SetFocus))
			self.SosyalAG["WEBSITE"].SetTabEvent(ui.__mem_func__(self.SosyalAG["E-POSTA"].SetFocus))
			self.SosyalAG["E-POSTA"].SetTabEvent(ui.__mem_func__(self.SosyalAG["SKYPE"].SetFocus))
			self.SosyalAG["SKYPE"].SetTabEvent(ui.__mem_func__(self.SosyalAG["KISISEL"].SetFocus))
			self.SosyalAG["KISISEL"].SetTabEvent(ui.__mem_func__(self.Cinsiyet.SetFocus))
			
			## textKAPAT + valueKAPAT##
			self.sayfaTEMIZLE()
			## textKAPATSON + valueKAPATSON ##

			self.Zaman = 0
			self.Full = 0
			self.Loading = 0
			self.YENILE = 0
			
			self.__BindObject()
			self.__BindEvent()
			
			if gameInfo.PROFIL_DURUM == 0 and gameInfo.PROFIL_NAME == "":#kendi profil(bakma)
				self.Zaman = app.GetTime()
				self.__profilAL()
				
			if gameInfo.PROFIL_DURUM == 1 and gameInfo.PROFIL_NAME == player.GetName():#kendi profil(olusturma)
				self.__ProfilOLUSTUR()
				self.Full = 101
				gameInfo.PROFIL_EKRANI = 0
			
		except:
			import exception
			exception.Abort("test.__LoadScript.BindObject")
			
		self.SetState("PROFIL")
		self.__OnClickPaylasimButton(1)
		
	def __BindObject(self):
		self.TabButtonDict	= {
			"PROFIL"					: self.GetChild("Tab_Button_01"),
			"EFSUN"					: self.GetChild("Tab_Button_02"),
			"BOS"					: self.GetChild("Tab_Button_03"),
		}
			
		self.TabImageDict = {
			"PROFIL"					: self.GetChild("Tab_01"),
			"EFSUN"					: self.GetChild("Tab_02"),
			"BOS"					: self.GetChild("Tab_03"),
		}
	
		self.PageDict = {
			"PROFIL"	: self.GetChild("ProfilPage"),
			"EFSUN"		: self.GetChild("EfsunPage"),
			"BOS"		: self.GetChild("xxxPage"),
		}
		
		self.TitleNameDict = {
			"PROFIL"	: self.GetChild("TitleNameProfil"),
			"EFSUN"		: self.GetChild("TitleNameEfsun"),
			"BOS"		: self.GetChild("TitleNameXXX"),
		}
		
	def __BindEvent(self):
		for (tabKey, tabButton) in self.TabButtonDict.items():
			tabButton.SetEvent(ui.__mem_func__(self.__OnClickTabButton), tabKey)
			
		self.Paylasim["HERKES"].SetEvent(ui.__mem_func__(self.__OnClickPaylasimButton), 1)
		self.Paylasim["ARKADASLAR"].SetEvent(ui.__mem_func__(self.__OnClickPaylasimButton), 2)
		self.Paylasim["OZEL"].SetEvent(ui.__mem_func__(self.__OnClickPaylasimButton), 3)
		
		#self.TamamButton.SetEvent(ui.__mem_func__(self.TamamButton))
		#self.DuzenleButton.SetEvent(ui.__mem_func__(self.DuzenleButton))
		#self.IptalButton.SetEvent(ui.__mem_func__(self.IptalButton))
		self.TamamButton.SetEvent(ui.__mem_func__(self.__TamamButton))
		self.DuzenleButton.SetEvent(ui.__mem_func__(self.__DuzenleButton))
		self.IptalButton.SetEvent(ui.__mem_func__(self.__IptalButton))
		self.Titlebar.SetCloseEvent(ui.__mem_func__(self.Close))
			
	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def Destroy(self):
		self.Hide()
		self.ClearDictionary()
		
	def __TamamButton(self):
		x = gameInfo.PROFIL
		cinsiyet = self.Cinsiyet.GetText()
		yas = self.Yas.GetText()
		is_ = self.Is.GetText()
		isYER = self.IsYER.GetText()
		sehir = self.Sehir.GetText()
		dogumgunu = self.DogumGunu.GetText()
		burc = self.Burc.GetText()
		facebook = self.SosyalAG["FACEBOOK"].GetText()
		website = self.SosyalAG["WEBSITE"].GetText()
		eposta = self.SosyalAG["E-POSTA"].GetText()
		skype = self.SosyalAG["SKYPE"].GetText()
		kisisel = self.SosyalAG["KISISEL"].GetText()
		
		## düzeltmeSTART ##
		if cinsiyet.find("E") != -1:
			cinsiyet = "E"
		else:
			cinsiyet = "K"
		if yas == "":
			yas = "."
		if is_ == "":
			is_ = "."
		if isYER == "":
			isYER = "."
		if sehir == "":
			sehir = "."
		if dogumgunu == "":
			dogumgunu = "."
		if burc == "":
			dogumgunu = "."
		if facebook == "":
			facebook = "."
		if website == "":
			website = "."
		if eposta == "":
			eposta = "."
		if skype == "":
			skype = "."
		if kisisel == "":
			kisisel = "."
		## düzeltmeSON ##
		
		gameInfo.PROFIL["CINSIYET"] = str(cinsiyet)
		gameInfo.PROFIL["YAS"] = str(yas)
		gameInfo.PROFIL["IS"] = str(is_)
		gameInfo.PROFIL["ISYER"] = str(isYER)
		gameInfo.PROFIL["SEHIR"] = str(sehir)
		gameInfo.PROFIL["DOGUM-GUNU"] = str(dogumgunu)
		gameInfo.PROFIL["BURC"] = str(burc)
		gameInfo.PROFIL["FACEBOOK"] = str(facebook)
		gameInfo.PROFIL["WEBSITE"] = str(website)
		gameInfo.PROFIL["E-POSTA"] = str(eposta)
		gameInfo.PROFIL["SKYPE"] = str(skype)
		if len(kisisel) >= 54:
			gameInfo.PROFIL["KISISEL"] = str(kisisel[:54])
			gameInfo.PROFIL["KISISEL2"] = str(kisisel[54:])
		else:
			gameInfo.PROFIL["KISISEL"] = str(kisisel)
		gameInfo.PYTHONISLEM = "pv#"+str(x["PAYLASIM"])+"#"+str(cinsiyet)+"#"+str(yas)+"#"+str(is_)+"#"+str(isYER)+"#"+str(sehir)+"#"+str(dogumgunu)+"#"+str(burc)
		event.QuestButtonClick(gameInfo.PYTHONTOLUA)
		
		self.TamamButton.Hide()
		self.DuzenleButton.Show()
		self.IptalButton.Show()
		
		gameInfo.PROFIL_DURUM = 0
		
		self.__profilGOSTER()
		
	def __DuzenleButton(self):
		
		self.SosyalAG["FACEBOOK_TEXT"].Hide()
		self.SosyalAG["WEBSITE_TEXT"].Hide()
		self.SosyalAG["E-POSTA_TEXT"].Hide()
		self.SosyalAG["SKYPE_TEXT"].Hide()
		self.SosyalAG["KISISEL_TEXT"].Hide()
		self.Cinsiyet_TEXT.Hide()
		self.Yas_TEXT.Hide()
		self.Is_TEXT.Hide()
		self.IsYER_TEXT.Hide()
		self.Sehir_TEXT.Hide()
		self.Ilce_TEXT.Hide()
		self.DogumGunu_TEXT.Hide()
		self.DogumGunu2_TEXT.Hide()
		self.Burc_TEXT.Hide()
		self.DuzenleButton.Hide()
		
		self.SosyalAG["FACEBOOK"].Show()
		self.SosyalAG["WEBSITE"].Show()
		self.SosyalAG["E-POSTA"].Show()
		self.SosyalAG["SKYPE"].Show()
		self.SosyalAG["KISISEL"].Show()
		self.Cinsiyet.Show()
		self.Yas.Show()
		self.Is.Show()
		self.IsYER.Show()
		self.Sehir.Show()
		self.Ilce.Show()
		self.DogumGunu.Show()
		self.DogumGunu2.Show()
		self.Burc.Show()
		self.TamamButton.Show()
		self.IptalButton.Show()
		
		if gameInfo.PROFIL["CINSIYET"] == ".":
			self.Cinsiyet.SetText("")
		else:
			if gameInfo.PROFIL["CINSIYET"]=="Erkek" or gameInfo.PROFIL["CINSIYET"]=="E":
				self.Cinsiyet.SetText("E")
			else:
				self.Cinsiyet.SetText("K")
		
		if gameInfo.PROFIL["YAS"] == ".":
			self.Yas.SetText("")
		else:
			self.Yas.SetText(str(gameInfo.PROFIL["YAS"]))
			
		if gameInfo.PROFIL["IS"] == ".":
			self.Is.SetText("")
		else:
			self.Is.SetText(str(gameInfo.PROFIL["IS"]))
			
		if gameInfo.PROFIL["ISYER"] == ".":
			self.IsYER.SetText("")
		else:
			self.IsYER.SetText(str(gameInfo.PROFIL["ISYER"]))
			
		if gameInfo.PROFIL["SEHIR"] == ".":
			self.Sehir.SetText("")
		else:
			self.Sehir.SetText(str(gameInfo.PROFIL["SEHIR"]))
			
		if gameInfo.PROFIL["ILCE"] == ".":
			self.Ilce.SetText("")
		else:
			self.Ilce.SetText(str(gameInfo.PROFIL["ILCE"]))
			
		if gameInfo.PROFIL["DOGUM-GUNU"] == ".":
			self.DogumGunu.SetText("")
		else:
			self.DogumGunu.SetText(str(gameInfo.PROFIL["DOGUM-GUNU"]))
			
		if gameInfo.PROFIL["DOGUM-GUNU2"] == ".":
			self.DogumGunu2.SetText("")
		else:
			self.DogumGunu2.SetText(str(gameInfo.PROFIL["DOGUM-GUNU2"]))
		
		if gameInfo.PROFIL["BURC"] == ".":
			self.Burc.SetText("")
		else:
			self.Burc.SetText(str(gameInfo.PROFIL["BURC"]))
			
		if gameInfo.PROFIL["FACEBOOK"] == ".":
			self.SosyalAG["FACEBOOK"].SetText("")
		else:
			self.SosyalAG["FACEBOOK"].SetText(str(gameInfo.PROFIL["FACEBOOK"]))
			
		if gameInfo.PROFIL["WEBSITE"] == ".":
			self.SosyalAG["WEBSITE"].SetText("")
		else:
			self.SosyalAG["WEBSITE"].SetText(str(gameInfo.PROFIL["WEBSITE"]))
			
		if gameInfo.PROFIL["E-POSTA"] == ".":
			self.SosyalAG["E-POSTA"].SetText("")
		else:
			self.SosyalAG["E-POSTA"].SetText(str(gameInfo.PROFIL["E-POSTA"]))
			
		if gameInfo.PROFIL["SKYPE"] == ".":
			self.SosyalAG["SKYPE"].SetText("")
		else:
			self.SosyalAG["SKYPE"].SetText(str(gameInfo.PROFIL["SKYPE"]))
		
		if gameInfo.PROFIL["KISISEL"] == ".":
			self.SosyalAG["KISISEL"].SetText("")
		else:
			self.SosyalAG["KISISEL"].SetText(str(gameInfo.PROFIL["KISISEL"]))
			
		self.Paylasim["HERKES"].Enable()
		self.Paylasim["ARKADASLAR"].Enable()
		self.Paylasim["OZEL"].Enable()
			
		#self.profilHAZIRLA_DUZENLE()
		
	def __IptalButton(self):
		iptalProfilQuestion = uiCommon.QuestionDialog2()
		iptalProfilQuestion.SetText1(localegame.PROFIL_TEXT)
		iptalProfilQuestion.SetText2(localegame.PROFIL_KABULEDIYORMUSUN)
		iptalProfilQuestion.SetAcceptEvent(lambda : self.OnSuccessIptalButton(1))
		iptalProfilQuestion.SetCancelEvent(lambda : self.OnSuccessIptalButton(0))
		iptalProfilQuestion.Open()
		self.iptalProfilQuestion = iptalProfilQuestion
		
	def OnSuccessIptalButton(self, gelen):
		if gelen == 1:
			self.Close()
			self.iptalProfilQuestion.Close()
			gameInfo.PYTHONISLEM = "profiliptaledildi#"
			event.QuestButtonClick(gameInfo.PYTHONTOLUA)
		else:
			self.iptalProfilQuestion.Close()
			
	def __profilAL(self):
		gameInfo.PYTHONISLEM = "profilim#"
		event.QuestButtonClick(gameInfo.PYTHONTOLUA)
		
	def __ProfilOLUSTUR(self):
		self.SosyalAG["FACEBOOK_TEXT"].Hide()
		self.SosyalAG["WEBSITE_TEXT"].Hide()
		self.SosyalAG["E-POSTA_TEXT"].Hide()
		self.SosyalAG["SKYPE_TEXT"].Hide()
		self.SosyalAG["KISISEL_TEXT"].Hide()
		self.Cinsiyet_TEXT.Hide()
		self.Yas_TEXT.Hide()
		self.Is_TEXT.Hide()
		self.IsYER_TEXT.Hide()
		self.Sehir_TEXT.Hide()
		self.Ilce_TEXT.Hide()
		self.DogumGunu_TEXT.Hide()
		self.DogumGunu2_TEXT.Hide()
		self.Burc_TEXT.Hide()
		self.DuzenleButton.Hide()
		
		self.Paylasim["HERKES"].Enable()
		self.Paylasim["ARKADASLAR"].Enable()
		self.Paylasim["OZEL"].Enable()
		self.Paylasim["HERKES"].Show()
		self.Paylasim["ARKADASLAR"].Show()
		self.Paylasim["OZEL"].Show()
		
		self.SosyalAG["FACEBOOK"].Show()
		self.SosyalAG["WEBSITE"].Show()
		self.SosyalAG["E-POSTA"].Show()
		self.SosyalAG["SKYPE"].Show()
		self.SosyalAG["KISISEL"].Show()
		self.Cinsiyet.Show()
		self.Yas.Show()
		self.Is.Show()
		self.IsYER.Show()
		self.Sehir.Show()
		self.Ilce.Show()
		self.DogumGunu.Show()
		self.DogumGunu2.Show()
		self.Burc.Show()
		self.TamamButton.Show()
		self.IptalButton.Show()
		
	def __profilWithTargetAL(self):
		gameInfo.PYTHONISLEM = "profil_ara#"+str(gameInfo.PROFIL_NAME)
		event.QuestButtonClick(gameInfo.PYTHONTOLUA)
		
	def profilHAZIRLA_GOSTER(self):
		
		PAYLASIM = gameInfo.PROFIL["PAYLASIM"]
		if PAYLASIM == 1:
			self.Paylasim["HERKES"].SetUpVisual(PROFILSYSTEM_PATH+"secilmis.tga")
			self.Paylasim["HERKES"].SetOverVisual(PROFILSYSTEM_PATH+"secilmis.tga")
			self.Paylasim["HERKES"].SetDownVisual(PROFILSYSTEM_PATH+"secilmis.tga")
			self.Paylasim["HERKES"].Disable()
		elif PAYLASIM == 2:
			self.Paylasim["ARKADASLAR"].SetUpVisual(PROFILSYSTEM_PATH+"secilmis.tga")
			self.Paylasim["ARKADASLAR"].SetOverVisual(PROFILSYSTEM_PATH+"secilmis.tga")
			self.Paylasim["ARKADASLAR"].SetDownVisual(PROFILSYSTEM_PATH+"secilmis.tga")
			self.Paylasim["ARKADASLAR"].Disable()
		elif PAYLASIM == 3:
			self.Paylasim["OZEL"].SetUpVisual(PROFILSYSTEM_PATH+"secilmis.tga")
			self.Paylasim["OZEL"].SetOverVisual(PROFILSYSTEM_PATH+"secilmis.tga")
			self.Paylasim["OZEL"].SetDownVisual(PROFILSYSTEM_PATH+"secilmis.tga")
			self.Paylasim["OZEL"].Disable()
		
		self.Paylasim["HERKES"].Disable()
		self.Paylasim["ARKADASLAR"].Disable()
		self.Paylasim["OZEL"].Disable()
		
		self.SosyalAG["FACEBOOK"].Hide()
		self.SosyalAG["WEBSITE"].Hide()
		self.SosyalAG["E-POSTA"].Hide()
		self.SosyalAG["SKYPE"].Hide()
		self.SosyalAG["KISISEL"].Hide()
		self.Cinsiyet.Hide()
		self.Yas.Hide()
		self.Is.Hide()
		self.IsYER.Hide()
		self.Sehir.Hide()
		self.Ilce.Hide()
		self.DogumGunu.Hide()
		self.DogumGunu2.Hide()
		self.Burc.Hide()
		self.TamamButton.Hide()
		self.IptalButton.Hide()
		
		self.SosyalAG["FACEBOOK_TEXT"].Show()
		self.SosyalAG["WEBSITE_TEXT"].Show()
		self.SosyalAG["E-POSTA_TEXT"].Show()
		self.SosyalAG["SKYPE_TEXT"].Show()
		self.SosyalAG["KISISEL_TEXT"].Show()
		self.Cinsiyet_TEXT.Show()
		self.Yas_TEXT.Show()
		self.Is_TEXT.Show()
		self.IsYER_TEXT.Show()
		self.Sehir_TEXT.Show()
		self.Ilce_TEXT.Show()
		self.DogumGunu_TEXT.Show()
		self.DogumGunu2_TEXT.Show()
		self.Burc_TEXT.Show()
		if gameInfo.PROFIL_NAME == player.GetName():
			self.DuzenleButton.Show()
			self.IptalButton.Show()
		else:
			if gameInfo.PROFIL_TARGET == 0:
				self.DuzenleButton.Show()
				self.IptalButton.Show()
		
	def __profilGOSTER(self):
		self.paylasimTEMIZLE()
		self.profilHAZIRLA_GOSTER()
			
		if gameInfo.PROFIL["CINSIYET"] == ".":
			self.Cinsiyet_TEXT.SetText("...")
		else:
			self.Cinsiyet_TEXT.SetText(str(gameInfo.PROFIL["CINSIYET"]))
		
		if gameInfo.PROFIL["YAS"] == ".":
			self.Yas_TEXT.SetText("...")
		else:
			self.Yas_TEXT.SetText(str(gameInfo.PROFIL["YAS"]))
			
		if gameInfo.PROFIL["IS"] == ".":
			self.Is_TEXT.SetText("...")
		else:
			self.Is_TEXT.SetText(str(gameInfo.PROFIL["IS"]))
			
		if gameInfo.PROFIL["ISYER"] == ".":
			self.IsYER_TEXT.SetText("...")
		else:
			self.IsYER_TEXT.SetText(str(gameInfo.PROFIL["ISYER"]))
			
		if gameInfo.PROFIL["SEHIR"] == ".":
			self.Sehir_TEXT.SetText("...")
		else:
			self.Sehir_TEXT.SetText(str(gameInfo.PROFIL["SEHIR"]))
			
		if gameInfo.PROFIL["ILCE"] == ".":
			self.Ilce_TEXT.SetText("")
		else:
			self.Ilce_TEXT.SetText(str(gameInfo.PROFIL["ILCE"]))
			
		if gameInfo.PROFIL["DOGUM-GUNU"] == ".":
			self.DogumGunu_TEXT.SetText("...")
		else:
			self.DogumGunu_TEXT.SetText(str(gameInfo.PROFIL["DOGUM-GUNU"]))
			
		if gameInfo.PROFIL["DOGUM-GUNU2"] == ".":
			self.DogumGunu2_TEXT.SetText("")
		else:
			self.DogumGunu2_TEXT.SetText(str(gameInfo.PROFIL["DOGUM-GUNU2"]))
		
		if gameInfo.PROFIL["BURC"] == ".":
			self.Burc_TEXT.SetText("...")
		else:
			self.Burc_TEXT.SetText(str(gameInfo.PROFIL["BURC"]))
			
		if gameInfo.PROFIL["FACEBOOK"] == ".":
			self.SosyalAG["FACEBOOK_TEXT"].SetText("...")
		else:
			self.SosyalAG["FACEBOOK_TEXT"].SetText(str(gameInfo.PROFIL["FACEBOOK"]))
			
		if gameInfo.PROFIL["WEBSITE"] == ".":
			self.SosyalAG["WEBSITE_TEXT"].SetText("...")
		else:
			self.SosyalAG["WEBSITE_TEXT"].SetText(str(gameInfo.PROFIL["WEBSITE"]))
			
		if gameInfo.PROFIL["E-POSTA"] == ".":
			self.SosyalAG["E-POSTA_TEXT"].SetText("...")
		else:
			self.SosyalAG["E-POSTA_TEXT"].SetText(str(gameInfo.PROFIL["E-POSTA"]))
			
		if gameInfo.PROFIL["SKYPE"] == ".":
			self.SosyalAG["SKYPE_TEXT"].SetText("...")
		else:
			self.SosyalAG["SKYPE_TEXT"].SetText(str(gameInfo.PROFIL["SKYPE"]))
		
		if gameInfo.PROFIL["KISISEL"] == ".":
			self.SosyalAG["KISISEL_TEXT"].SetText("...")
		else:
			self.SosyalAG["KISISEL_TEXT"].SetText(str(gameInfo.PROFIL["KISISEL"]))
	
	def __OnClickPaylasimButton(self, gelen):
		self.paylasimTEMIZLE()
		if gelen == 1:
			gameInfo.PROFIL["PAYLASIM"] = 1
			self.Paylasim["HERKES"].SetUpVisual(PROFILSYSTEM_PATH+"secilmis.tga")
			self.Paylasim["HERKES"].SetOverVisual(PROFILSYSTEM_PATH+"secilmis.tga")
			self.Paylasim["HERKES"].SetDownVisual(PROFILSYSTEM_PATH+"secilmis.tga")
		elif gelen == 2:
			gameInfo.PROFIL["PAYLASIM"] = 2
			self.Paylasim["ARKADASLAR"].SetUpVisual(PROFILSYSTEM_PATH+"secilmis.tga")
			self.Paylasim["ARKADASLAR"].SetOverVisual(PROFILSYSTEM_PATH+"secilmis.tga")
			self.Paylasim["ARKADASLAR"].SetDownVisual(PROFILSYSTEM_PATH+"secilmis.tga")
		elif gelen == 3:
			gameInfo.PROFIL["PAYLASIM"] = 3
			self.Paylasim["OZEL"].SetUpVisual(PROFILSYSTEM_PATH+"secilmis.tga")
			self.Paylasim["OZEL"].SetOverVisual(PROFILSYSTEM_PATH+"secilmis.tga")
			self.Paylasim["OZEL"].SetDownVisual(PROFILSYSTEM_PATH+"secilmis.tga")
			
	def paylasimTEMIZLE(self):
		self.Paylasim["HERKES"].SetUpVisual(PROFILSYSTEM_PATH+"secilmemis.tga")
		self.Paylasim["HERKES"].SetOverVisual(PROFILSYSTEM_PATH+"secilmemis.tga")
		self.Paylasim["HERKES"].SetDownVisual(PROFILSYSTEM_PATH+"secilmemis.tga")
		self.Paylasim["ARKADASLAR"].SetUpVisual(PROFILSYSTEM_PATH+"secilmemis.tga")
		self.Paylasim["ARKADASLAR"].SetOverVisual(PROFILSYSTEM_PATH+"secilmemis.tga")
		self.Paylasim["ARKADASLAR"].SetDownVisual(PROFILSYSTEM_PATH+"secilmemis.tga")
		self.Paylasim["OZEL"].SetUpVisual(PROFILSYSTEM_PATH+"secilmemis.tga")
		self.Paylasim["OZEL"].SetOverVisual(PROFILSYSTEM_PATH+"secilmemis.tga")
		self.Paylasim["OZEL"].SetDownVisual(PROFILSYSTEM_PATH+"secilmemis.tga")
		
	def sayfaTEMIZLE(self):
		self.SosyalAG["FACEBOOK"].Hide()
		self.SosyalAG["WEBSITE"].Hide()
		self.SosyalAG["E-POSTA"].Hide()
		self.SosyalAG["SKYPE"].Hide()
		self.SosyalAG["KISISEL"].Hide()
		self.SosyalAG["FACEBOOK_TEXT"].Hide()
		self.SosyalAG["WEBSITE_TEXT"].Hide()
		self.SosyalAG["E-POSTA_TEXT"].Hide()
		self.SosyalAG["SKYPE_TEXT"].Hide()
		self.SosyalAG["KISISEL_TEXT"].Hide()
		self.Cinsiyet.Hide()
		self.Yas.Hide()
		self.Is.Hide()
		self.IsYER.Hide()
		self.Sehir.Hide()
		self.Ilce.Hide()
		self.DogumGunu.Hide()
		self.DogumGunu2.Hide()
		self.Burc.Hide()
		self.TamamButton.Hide()
		self.DuzenleButton.Hide()
		self.IptalButton.Hide()
		self.Cinsiyet_TEXT.Hide()
		self.Yas_TEXT.Hide()
		self.Is_TEXT.Hide()
		self.IsYER_TEXT.Hide()
		self.Sehir_TEXT.Hide()
		self.Ilce_TEXT.Hide()
		self.DogumGunu_TEXT.Hide()
		self.DogumGunu2_TEXT.Hide()
		self.Burc_TEXT.Hide()
		
	def __OnClickTabButton(self, stateKey):
		self.SetState(stateKey)
		
	def SetState(self, stateKey):
		
		self.state = stateKey
		if stateKey == "PROFIL":
			if gameInfo.PROFIL_DURUM == 1 and gameInfo.PROFIL_NAME == player.GetName():
				self.GetChild("Yukleniyor-TEXT").Hide()
				self.Zaman = 0
			else:
				self.GetChild("ArkaPLAN").Hide()
				#self.Zaman = app.GetTime()
			
		for (tabKey, tabButton) in self.TabButtonDict.items():
			if stateKey!=tabKey:
				tabButton.SetUp()

		for tabValue in self.TabImageDict.itervalues():
			tabValue.Hide()

		for pageValue in self.PageDict.itervalues():
			pageValue.Hide()

		for titleNameValue in self.TitleNameDict.itervalues():
			titleNameValue.Hide()

		self.TitleNameDict[stateKey].Show()
		self.TabImageDict[stateKey].Show()
		self.PageDict[stateKey].Show()

	def GetState(self):
		return self.state
			
	def Chat(self, text):
		chat.AppendChat(chat.CHAT_TYPE_INFO, "<PROFIL>: "+str(text))
		
	def Close(self):
		gameInfo.PROFIL_NAME = ""
		gameInfo.PROFIL_EKRANI = 0
		gameInfo.PROFIL_ISHOW = 0
		gameInfo.PROFIL_TARGET = 0
		gameInfo.PROFIL["PAYLASIM"] = 1
		gameInfo.PROFIL["CINSIYET"] = ""
		gameInfo.PROFIL["YAS"] = "."
		gameInfo.PROFIL["IS"] = "."
		gameInfo.PROFIL["ISYER"] = "."
		gameInfo.PROFIL["SEHIR"] = "."
		gameInfo.PROFIL["ILCE"] = "."
		gameInfo.PROFIL["DOGUM-GUNU"] = "."
		gameInfo.PROFIL["DOGUM-GUNU2"] = "."
		gameInfo.PROFIL["BURC"] = "."
		gameInfo.PROFIL["FACEBOOK"] = "."
		gameInfo.PROFIL["WEBSITE"] = "."
		gameInfo.PROFIL["E-POSTA"] = "."
		gameInfo.PROFIL["SKYPE"] = "."
		gameInfo.PROFIL["KISISEL"] = "."
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	#def OnPressExitKey(self):
	#	self.Close()
	#	return TRUE
		
	def OnUpdate(self):
	
		if self.Full < 102:
			self.GetChild("Yukleniyor-TEXT").Show()
			self.GetChild("Yukleniyor-TEXT").SetFontName("Tahoma:60")
			self.GetChild("Yukleniyor-TEXT").SetText("%"+str(self.Full))
			self.Full += 1

		if self.Full == 101 and self.Loading == 0:
			self.GetChild("Yukleniyor-TEXT").Hide()
			self.GetChild("ArkaPLAN").Show()
			self.__profilGOSTER()
			self.Full = 103
			self.Loading = 1

		if app.GetTime() < self.Zaman + 2:
			pass
		else:
			if gameInfo.PROFIL_NAME != player.GetName() and self.YENILE==0:
				self.__profilGOSTER()
				self.YENILE=1
				
		#if gameInfo.PROFIL_TARGET == 1:
		#	self.GetChild("Board").SetSize(260,365)
		#	self.SetSize(260,365)
		#	self.GetChild("ArkaPLAN").LoadImage(str(gameInfo.CONFIG_YOL)+"profil/arkaplan_target.tga")
		#else:
		#	self.GetChild("Board").SetSize(260,400)
		#	self.SetSize(260,400)
				
		"""eskiZAMAN = self.timeBALIK
		yeniZAMAN = app.GetTime()
		suanZAMAN = yeniZAMAN - eskiZAMAN
		intSUAN_ZAMAN = int(suanZAMAN)
		if suanZAMAN > gameInfo.BALIK_PENCERE_SURESI:
			if gameInfo.BALIK_VNUM >= 27400 and gameInfo.BALIK_VNUM <= 27590 and not TRUE == shop.IsMainPlayerPrivateShop():
				self.timeBALIK = yeniZAMAN"""
			
		if gameInfo.PROFIL_NAME != "":
			if gameInfo.PROFIL_NAME != player.GetName():
				self.TabButtonDict[self.state].Hide()
				self.TabImageDict[self.state].Hide()
				self.TitleNameDict[self.state].SetText(localegame.PROFIL_TITLE % (str(gameInfo.PROFIL_NAME)))
				self.GetChild("Board").SetSize(260,371)
				self.SetSize(260,371)
				self.GetChild("ArkaPLAN").LoadImage(str(gameInfo.CONFIG_YOL)+"profil/arkaplan_target.tga")
		
ProfilSystemWnd = ProfilWindow()
PROFILSYSTEM_PATH = str(gameInfo.CONFIG_YOL)+"profil/"