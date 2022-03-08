--[[

TR: Tüm özel sistemler, fonksiyonlar, methodlar, ve yol...
TRL : All Special Systems, funcs, method and the way to...

Geliþtirici : .. Fatihbab34™ ..
Paketler ; LuaToPython, PythonToLua, PythonIslem
Fonksiyonlar ; "split('#blabla#blabla#', '#'), systems.getinput('PythonIslem'), io funcs(open, remove, write, read, readline, readlines), table forms, pc.getqf(), pc.setqf()"

--]]

quest systems begin
	state start begin

		function getinput(gelen)
			local input1 = "#quest_input#"
			local input0 = "#quest_inputbitir#"
			cmdchat("LuaToPython "..input1)
			local al = input(cmdchat("PythonIslem "..gelen))
			cmdchat("LuaToPython "..input0)
			return al
		end

		function split(command_, ne)
			return systems.split_(command_,ne)
		end
		
		function split_(string_,delimiter)
			local result = { }
			local from  = 1
			local delim_from, delim_to = string.find( string_, delimiter, from  )
			while delim_from do
				table.insert( result, string.sub( string_, from , delim_from-1 ) )
				from  = delim_to + 1
				delim_from, delim_to = string.find( string_, delimiter, from  )
			end
			table.insert( result, string.sub( string_, from  ) )
			return result
		end

		when login begin
			cmdchat("PythonToLua "..q.getcurrentquestindex())
			if pc.getqf("profil") == 0 then
				cmdchat("LuaToPython #profil_olustur#")
			end
		end

		when button begin
			local gelen = systems.getinput("PYTHONISLEM")
			if gelen == "profilim#" then
				local ac = io.open('/usr/game/share/locale/turkey/quest/systems/profil/'..pc.get_name()..'.cfg', 'r')
				local text = ""
				if ac then
					for i in ac:lines() do
						text = text..i
					end
					cmdchat("LuaToPython profilim|benim|#"..text)
				end
			end
			
			if string.find(gelen, "pv#") then
				gelen = string.gsub(gelen,' ','_')
				local bol = systems.split(gelen, "#")
				--chat(string.len(gelen))
				local FACEBOOK = systems.getinput("PROFIL_FACEBOOK")
				local WEBSITE = systems.getinput("PROFIL_WEBSITE")
				local EPOSTA = systems.getinput("PROFIL_EPOSTA")
				local SKYPE = systems.getinput("PROFIL_SKYPE")
				local KISISEL = systems.getinput("PROFIL_KISISEL")
				local KISISEL2 = ""
				KISISEL = string.gsub(KISISEL,' ','_')
				if string.len(KISISEL) >= 54 then
					local KISISEL2 = systems.getinput("PROFIL_KISISEL2")
					KISISEL2 = string.gsub(KISISEL2,' ','_')
				end
				local ac_kontrol = io.open('/usr/game/share/locale/turkey/quest/systems/profil/'..pc.get_name()..'.cfg', 'r')
				if ac_kontrol then
					os.remove('/usr/game/share/locale/turkey/quest/systems/profil/'..pc.get_name()..'.cfg')
				end
				
				local ac = io.open('/usr/game/share/locale/turkey/quest/systems/profil/'..pc.get_name()..'.cfg', 'a+')
				if bol[3] == "M" then
					ac:write(bol[2].."#Male".."#"..bol[4].."#"..bol[5].."#"..bol[6].."#"..bol[7].."#"..bol[8].."#"..bol[9].."#\\n")
				elseif bol[3] == "F" then
					ac:write(bol[2].."#Female".."#"..bol[4].."#"..bol[5].."#"..bol[6].."#"..bol[7].."#"..bol[8].."#"..bol[9].."#\\n")
				else
					ac:write(bol[2].."#"..bol[3].."#"..bol[4].."#"..bol[5].."#"..bol[6].."#"..bol[7].."#"..bol[8].."#"..bol[9].."#\\n")
				end
				ac:write(FACEBOOK.."#\\n")
				ac:write(WEBSITE.."#\\n")
				ac:write(EPOSTA.."#\\n")
				ac:write(SKYPE.."#\\n")
				if KISISEL2 != "" then
					ac:write(KISISEL..KISISEL2.."\\n")
				else
					ac:write(KISISEL.."\\n")
				end
				ac:close()
				pc.setqf("profil", 1)
			end
			
			if string.find(gelen, "profil_ara#") then
				local bol2 = systems.split(gelen, "#")
				local isim = bol2[2]
				local ac = io.open('/usr/game/share/locale/turkey/quest/systems/profil/'..isim..'.cfg', 'r')
				local text = ""
				local tek = 0
				if ac then
					for i in ac:lines() do
						local bol = systems.split(i, "#")
						if tek == 0 then
							if tonumber(bol[1]) == 3 then
								return
							elseif tonumber(bol[1]) == 1 then
								text = text..i
							elseif tonumber(bol[1]) == 2 then -- Sadece Arkadaþlar!
								text = text..i
							end
							tek = 1
						else
							text = text..i
						end
					end
					cmdchat("LuaToPython profil|"..isim.."|#"..text)
				else
					syschat('Bu kiþi profilini engellemiþ.')
				end
				
			end
			
			if gelen == "profiliptaledildi#" then
				pc.getqf("profil", 2)
				local ac = io.open('/usr/game/share/locale/turkey/quest/systems/profil/'..pc.get_name()..'.cfg', 'r')
				if ac then
					os.remove('/usr/game/share/locale/turkey/quest/systems/profil/'..pc.get_name()..'.cfg')
				end
			end
			
			if string.find(gelen, "profil_kontrol#") then
				
				local isim = systems.split(gelen, "#")[3]
				
				local ac = io.open('/usr/game/share/locale/turkey/quest/systems/profil/'..isim..'.cfg', 'r')
				if ac then
					local kontrol = 0
					for i in ac:lines() do
						local bol = systems.split(i, "#")
						local tek = 0
						if tek == 0 then
							if tonumber(bol[1]) == 3 then
								return
							elseif tonumber(bol[1]) == 1 then
								kontrol = 1
							elseif tonumber(bol[1]) == 2 then -- Sadece Arkadaþlar!
								kontrol = 2
							end
							tek = 1
						end
					end
					if kontrol == 1 then
						cmdchat("LuaToPython #profil_var#"..isim)
						return
					elseif kontrol == 2 then
						cmdchat("LuaToPython #profil_var2#"..isim)
						return
					end
				end

			end

		end
	end
end