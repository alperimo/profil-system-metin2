import gameInfo

	
		{ 
			"name":"ProfilButton", 
			"type":"button", 
			"x" : 68+9000,
			"y" : SCREEN_HEIGHT-240,
			"default_image" : str(gameInfo.CONFIG_YOL)+"profil/profilbutton.tga",
			"over_image" : str(gameInfo.CONFIG_YOL)+"profil/profilbutton_2.tga",
			"down_image" : str(gameInfo.CONFIG_YOL)+"profil/profilbutton_3.tga",

			"children" : 
			(
				{ 
					"name":"ProfilButtonLabel", 
					"type":"text", 
					"x": 16, 
					"y": 40, 
					"text":"Profil", 
					"r":1.0, "g":1.0, "b":1.0, "a":1.0, 
					"text_horizontal_align":"center" 
				},
			),
		},