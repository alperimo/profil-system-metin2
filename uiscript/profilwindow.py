import uiScriptLocale
import gameInfo

PROFILSYSTEM_PATH = str(gameInfo.CONFIG_YOL)+"profil/"
SMALL_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_00.sub"
MIDDLE_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_01.sub"
LARGE_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_03.sub"

BOARD_WIDTH = 260
BOARD_HEIGHT = 400

SLOT_HEIGHT=16

window = {
	"name" : "ProfilSystem",

	"x" : 24,
	"y" : (SCREEN_HEIGHT - 37 - 361) / 2,

	"style" : ("movable", "float",),

	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,

	"children" :
	(
		{
			"name" : "Board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : BOARD_WIDTH,
			"height" : BOARD_HEIGHT,

			"children" :
			(
				
				
				{
					"name": "ProfilSystem",
					
					"x" : 0+9000,
					"y" : 328,
					
					"width" : 250,
					"height" : 31,
					
					"children" :
					(
						## Tab
						{
							"name" : "Tab_01",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"width" : 250,
							"height" : 31,

							"image" : PROFILSYSTEM_PATH+"arkaplan.tga",
						},
						{
							"name" : "Tab_02",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"width" : 250,
							"height" : 31,

							"image" : PROFILSYSTEM_PATH+"arkaplan.tga",
						},
						{
							"name" : "Tab_03",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"width" : 250,
							"height" : 31,

							"image" : PROFILSYSTEM_PATH+"arkaplan.tga",
						},
						## RadioButton
						{
							"name" : "Tab_Button_01",
							"type" : "radio_button",

							"x" : 6,
							"y" : 5,

							"width" : 75,
							"height" : 27,
						},
						{
							"name" : "Tab_Button_02",
							"type" : "radio_button",

							"x" : 85,
							"y" : 5,

							"width" : 75,
							"height" : 27,
						},
						{
							"name" : "Tab_Button_03",
							"type" : "radio_button",

							"x" : 165,
							"y" : 5,

							"width" : 75,
							"height" : 27,
						},
					),
				},
				
				{
					"name" : "ProfilPage",
					"type" : "window",
					"style" : ("attach",),

					"x" : 0,
					"y" : 2,

					"width" : BOARD_WIDTH,
					"height" : BOARD_HEIGHT,

					"children" :
					(
						{"name" : "Yukleniyor-TEXT", "type" : "text", "x" : 250/2-60, "y" : 304/2-34+45, "text" : "%0 "},
						## arkaplanBASLA ##
						{"name":"ArkaPLAN", "type":"image","x":0,"y":0,"image":str(PROFILSYSTEM_PATH)+"arkaplan.tga", "children":
							(		
								## arkaplanSON ##
								
								## paylasimBASLA ##						
								{"name":"Paylasim-Herkes-Button", "type":"button","x":73,"y":37-5,"default_image":str(PROFILSYSTEM_PATH)+"secilmemis.tga","over_image":str(PROFILSYSTEM_PATH)+"secilmemis.tga","down_image":str(PROFILSYSTEM_PATH)+"secilmemis.tga"},
								{"name":"Paylasim-Arkadaslar-Button", "type":"button","x":170,"y":37-5,"default_image":str(PROFILSYSTEM_PATH)+"secilmemis.tga","over_image":str(PROFILSYSTEM_PATH)+"secilmemis.tga","down_image":str(PROFILSYSTEM_PATH)+"secilmemis.tga"},
								{"name":"Paylasim-Ozel-Button", "type":"button","x":234,"y":37-5,"default_image":str(PROFILSYSTEM_PATH)+"secilmemis.tga","over_image":str(PROFILSYSTEM_PATH)+"secilmemis.tga","down_image":str(PROFILSYSTEM_PATH)+"secilmemis.tga"},
								## paylasimSON ##
								
								## valueBASLA ##
								{"name":"Cinsiyet-Value","type":"editline","x":64,"y":74,"width":92,"height":SLOT_HEIGHT,"r":124,"g":120,"b":117,"text":"M/F","input_limit":1},
								{"name":"Yas-Value","type":"editline","width":92,"height":SLOT_HEIGHT,"r":124,"g":120,"b":117,"text":"","input_limit":2,"x":169,"y":74},
								{"name":"Is-Value","type":"editline","width":92,"height":SLOT_HEIGHT,"r":124,"g":120,"b":117,"text":"","input_limit":12,"x":64,"y":103},
								{"name":"IsYER-Value","type":"editline","width":92,"height":SLOT_HEIGHT,"r":124,"g":120,"b":117,"text":"","input_limit":14,"x":170,"y":103},
								{"name":"Sehir-Value","type":"editline","width":92,"height":SLOT_HEIGHT,"r":124,"g":120,"b":117,"text":"","input_limit":12,"x":64,"y":132},
								{"name":"Ilce-Value","type":"editline","width":92,"height":SLOT_HEIGHT,"r":124,"g":120,"b":117,"text":"","input_limit":14,"x":169+9000,"y":127},#kaldirildi
								{"name":"DogumGunu-Value","type":"editline","width":92,"height":SLOT_HEIGHT,"r":124,"g":120,"b":117,"text":"xx/xx","input_limit":5,"x":169,"y":132},
								{"name":"DogumGunu2-Value","type":"editline","width":92,"height":SLOT_HEIGHT,"r":124,"g":120,"b":117,"text":"","input_limit":2,"x":94+9000,"y":163},#kaldirildi
								{"name":"Burc-Value","type":"editline","width":92,"height":SLOT_HEIGHT,"r":124,"g":120,"b":117,"text":"","input_limit":14,"x":95,"y":131+34},
								## valueSON ##
								
								## sosyalBaglantilarBASLA ##
								{"name":"Facebook-Value","type":"editline","width":92,"height":SLOT_HEIGHT,"text":"","input_limit":27,"x":75,"y":196,"r":124,"g":120,"b":117},
								{"name":"WebSite-Value","type":"editline","width":92,"height":SLOT_HEIGHT,"text":"","input_limit":27,"x":75,"y":220,"r":124,"g":120,"b":117},
								{"name":"Eposta-Value","type":"editline","width":92,"height":SLOT_HEIGHT,"text":"","input_limit":27,"x":75,"y":246,"r":124,"g":120,"b":117},
								{"name":"Skype-Value","type":"editline","width":92,"height":SLOT_HEIGHT,"text":"","input_limit":27,"x":75,"y":271,"r":124,"g":120,"b":117},
								{"name":"Kisisel-Value","type":"editline","width":147,"height":52,"text":"","input_limit":29,"x":75,"y":294,"r":124,"g":120,"b":117},
									## sosyalBaglantilarTEXTBASLA ##
								{"name":"Facebook-TEXT","type":"text","width":92,"height":16,"text":"","input_limit":25,"x":17,"y":3,"r":124,"g":120,"b":117,"all_align":"center"},
								{"name":"WebSite-TEXT","type":"text","width":92,"height":16,"text":"","input_limit":25,"x":17,"y":3+21,"r":124,"g":120,"b":117,"all_align":"center"},
								{"name":"Eposta-TEXT","type":"text","width":92,"height":16,"text":"","input_limit":25,"x":16,"y":3+21+25,"r":124,"g":120,"b":117,"all_align":"center"},
								{"name":"Skype-TEXT","type":"text","width":92,"height":16,"text":"","input_limit":25,"x":16,"y":3+21+21+31,"r":124,"g":120,"b":117,"all_align":"center"},
								{"name":"Kisisel-TEXT","type":"text","width":92,"height":16,"text":"","input_limit":120,"x":15,"y":3+21+21+21+30,"r":124,"g":120,"b":117,"all_align":"center"},
									## sosyalBaglantilarTEXTSON ##
								## sosyalBaglantilarSON ##
								
								## buttonBASLA ##
								{"name":"TamamButton","type":"button","text":"","x":49,"y":361,"default_image":str(PROFILSYSTEM_PATH)+"kaydetbutton.tga","over_image":str(PROFILSYSTEM_PATH)+"kaydetbutton_2.tga","down_image":str(PROFILSYSTEM_PATH)+"kaydetbutton_3.tga"},
								{"name":"DuzenleButton","type":"button","text":"","x":49,"y":361,"default_image":str(PROFILSYSTEM_PATH)+"duzenlebutton.tga","over_image":str(PROFILSYSTEM_PATH)+"duzenlebutton_2.tga","down_image":str(PROFILSYSTEM_PATH)+"duzenlebutton_3.tga"},
								{"name":"IptalButton","type":"button","text":"","x":44+90,"y":361,"default_image":str(PROFILSYSTEM_PATH)+"iptalbutton.tga","over_image":str(PROFILSYSTEM_PATH)+"iptalbutton_2.tga","down_image":str(PROFILSYSTEM_PATH)+"iptalbutton_3.tga"},
								## buttonSON ##
								
								## textBASLA ##				

								{"name":"Cinsiyet-TEXT", "type":"text","width":92,"height":16,"text":"E/K","input_limit":14,"x":-47,"y":-119,"r":124,"g":120,"b":117,"all_align":"center"},
								{"name":"Yas-TEXT","type":"text","width":92,"height":16,"text":"","input_limit":14,"x":59,"y":-119,"r":124,"g":120,"b":117,"all_align":"center"},
								{"name":"Is-TEXT","type":"text","width":92,"height":16,"text":"","input_limit":14,"x":-48+12,"y":-116+26,"r":124,"g":120,"b":117,"all_align":"center"},
								{"name":"IsYER-TEXT","type":"text","width":92,"height":16,"text":"","input_limit":14,"x":-48+9+109,"y":-116+26,"r":124,"g":120,"b":117,"all_align":"center"},
								{"name":"Sehir-TEXT","type":"text","width":92,"height":16,"text":"","input_limit":14,"x":-48+12,"y":-116+26+28,"r":124,"g":120,"b":117,"all_align":"center"},
								{"name":"Ilce-TEXT","type":"text","width":92,"height":16,"text":"","input_limit":14,"x":0,"y":0,"r":124,"g":120,"b":117},#kaldirildi
								{"name":"DogumGunu-TEXT","type":"text","width":92,"height":16,"text":"xx/xx/xxxx","input_limit":14,"x":-48+9+108,"y":-116+26+28,"r":124,"g":120,"b":117,"all_align":"center"},
								{"name":"DogumGunu2-TEXT","type":"text","width":92,"height":16,"text":"xx/xx/xxxx","input_limit":14,"x":0,"y":0,"r":124,"g":120,"b":117},#kaldirildi
								{"name":"Burc-TEXT","type":"text","width":92,"height":16,"text":"","input_limit":14,"x":5,"y":-28,"all_align":"center","r":124,"g":120,"b":117,"all_align":"center"},
								
								
								## textSON ##
							),
						
						},

					),
				},
				
				{
					"name" : "Titlebar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 7,

					"width" : BOARD_WIDTH-15,
					"color" : "red",

					"children" :
					(
						{ "name":"TitleNameProfil", "type":"text", "x":0, "y":-1, "text":"Profil", "all_align":"center","fontsize":"LARGE"},
						#{ "name":"TitleNameProfil", "type":"text", "x":0, "y":-1, "text":"Profil", "all_align":"center","fontsize":"LARGE","r":124,"g":120,"b":117 },
						{ "name":"TitleNameEfsun", "type":"text", "x":0, "y":-1, "text":"Efsun Tablosu", "all_align":"center" },
						{ "name":"TitleNameXXX", "type":"text", "x":0, "y":-1, "text":"Efsun Tablosu", "all_align":"center" },
					),
				},
				
				{
					"name" : "EfsunPage",
					"type" : "window",
					"style" : ("attach",),

					"x" : 0,
					"y" : 24,

					"width" : 250,
					"height" : 304,

					"children" :
					(
						{
							"name":"Critical", "type":"window", "x":10, "y":25+23*0, "width":200, "height":20,
							"children" :
							(
								{ "name":"Text", "type":"text", "x":10, "y":3, "text":"Kritik Vuruþ Þansý", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"left" },
								{ "name":"Slot", "type":"image", "x":180, "y":0, "image":SMALL_VALUE_FILE },
								{ "name":"Critical_Value", "type":"text", "x":200, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							),
						},
						{
							"name":"Penetrate", "type":"window", "x":10, "y":25+23*1, "width":200, "height":20,
							"children" :
							(
								{ "name":"Text", "type":"text", "x":10, "y":3, "text":"Delici Vuruþ Þansý", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"left" },
								{ "name":"Slot", "type":"image", "x":180, "y":0, "image":SMALL_VALUE_FILE },
								{ "name":"Penetrate_Value", "type":"text", "x":200, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							),
						},
						{
							"name":"Human", "type":"window", "x":10, "y":25+23*2, "width":200, "height":20,
							"children" :
							(
								{ "name":"Text", "type":"text", "x":10, "y":3, "text":"Yarý Ýnsan Bonusu", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"left" },
								{ "name":"Slot", "type":"image", "x":180, "y":0, "image":SMALL_VALUE_FILE },
								{ "name":"Human_Value", "type":"text", "x":200, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							),
						},
						{
							"name":"Sword", "type":"window", "x":10, "y":25+23*3, "width":200, "height":20,
							"children" :
							(
								{ "name":"Text", "type":"text", "x":10, "y":3, "text":"Kýlýç Savunmasý", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"left" },
								{ "name":"Slot", "type":"image", "x":180, "y":0, "image":SMALL_VALUE_FILE },
								{ "name":"Sword_Value", "type":"text", "x":200, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							),
						},
						{
							"name":"TwoHand", "type":"window", "x":10, "y":25+23*4, "width":200, "height":20,
							"children" :
							(
								{ "name":"Text", "type":"text", "x":10, "y":3, "text":"Çift-El Savunmasý", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"left" },
								{ "name":"Slot", "type":"image", "x":180, "y":0, "image":SMALL_VALUE_FILE },
								{ "name":"TwoHand_Value", "type":"text", "x":200, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							),
						},
						{
							"name":"Fan", "type":"window", "x":10, "y":25+23*5, "width":200, "height":20,
							"children" :
							(
								{ "name":"Text", "type":"text", "x":10, "y":3, "text":"Yelpaze Savunmasý", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"left" },
								{ "name":"Slot", "type":"image", "x":180, "y":0, "image":SMALL_VALUE_FILE },
								{ "name":"Fan_Value", "type":"text", "x":200, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							),
						},
						{
							"name":"Bell", "type":"window", "x":10, "y":25+23*6, "width":200, "height":20,
							"children" :
							(
								{ "name":"Text", "type":"text", "x":10, "y":3, "text":"Çan Savunmasý", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"left" },
								{ "name":"Slot", "type":"image", "x":180, "y":0, "image":SMALL_VALUE_FILE },
								{ "name":"Bell_Value", "type":"text", "x":200, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							),
						},
						{
							"name":"Dagger", "type":"window", "x":10, "y":25+23*7, "width":200, "height":20,
							"children" :
							(
								{ "name":"Text", "type":"text", "x":10, "y":3, "text":"Býçak Savunmasý", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"left" },
								{ "name":"Slot", "type":"image", "x":180, "y":0, "image":SMALL_VALUE_FILE },
								{ "name":"Dagger_Value", "type":"text", "x":200, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							),
						},
						{
							"name":"Bow", "type":"window", "x":10, "y":25+23*8, "width":200, "height":20,
							"children" :
							(
								{ "name":"Text", "type":"text", "x":10, "y":3, "text":"Ok Savunmasý", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"left" },
								{ "name":"Slot", "type":"image", "x":180, "y":0, "image":SMALL_VALUE_FILE },
								{ "name":"Bow_Value", "type":"text", "x":200, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							),
						},
						{
							"name":"Magic", "type":"window", "x":10, "y":25+23*9, "width":200, "height":20,
							"children" :
							(
								{ "name":"Text", "type":"text", "x":10, "y":3, "text":"Büyü Savunmasý", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"left" },
								{ "name":"Slot", "type":"image", "x":180, "y":0, "image":SMALL_VALUE_FILE },
								{ "name":"Magic_Value", "type":"text", "x":200, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							),
						},
						{
							"name":"Stun", "type":"window", "x":10, "y":25+23*10, "width":200, "height":20,
							"children" :
							(
								{ "name":"Text", "type":"text", "x":10, "y":3, "text":"Sersemletme Þansý", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"left" },
								{ "name":"Slot", "type":"image", "x":180, "y":0, "image":SMALL_VALUE_FILE },
								{ "name":"Stun_Value", "type":"text", "x":200, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							),
						},	
					),
				},
				
				{
					"name" : "xxxPage",
					"type" : "window",
					"style" : ("attach",),

					"x" : 0,
					"y" : 24,

					"width" : 250,
					"height" : 304,

					"children" :
					(
					
						#...#
					
					),
				},

			),
		},
	),
}