from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
from PIL import Image, ImageTk
import math


class RiskMatrix(tk.Tk):

    def __init__(self, root):
        self.root = root
        self.root.title("GeoPolitics Position")
        label1 = Label(self.root)
        label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="nsa.png")
        label1.configure(image=self.img)
        self.root.geometry('1366x768')
        self.root.state('zoomed')
        self.create_gui()
        
        

        

    def create_gui(self):
        self.create_matrix_frame()
        self.create_combobox_rating1()
        self.create_main_label()
        self.create_combobox_rating2()
        self.display_result()
        self.create_result_frame()
        self.create_menu()
        
        

    def abs_move(self, maincanvas, _object, new_x, new_y, speed=10):
        # Get the current object position
        x, y, *_ = self.bbox(_object)
        # Move the object
        self.move(_object, new_x-x, new_y-y)
    # Monkey patch the `abs_move` method
    Canvas.abs_move = abs_move

    s1 = -1
    dl = -1
    def display_result(self, *args, **kwargs):
        self.resultlist = []

        
        
        global rating_selected4, rating_selected5, rating_selected6, rating_selected7,rating_selected8, rating_selected9
        global treatyDict, intervene_to_governmentDict, diplomaticpressureDict, militaryaidDict,economicaidDict, tradepolicyDict
        global combo_treaty,combo_intervene_to_government, combo_diplomaticpressure, combo_militaryaid, combo_economicaid,combo_tradepolicy
        
        global canvas
        global chesspiece
        global sl
        global dl
        
        nationalsecurityDict_x = {'3': 395, '2': 265, '1': 155, '0': 155}
        diplomacyDict_y = {'3': 80, '2': 205, '1': 350, '0': 350}
        sl = -1
        dl = -1
        
        
        
        
        if self.combo_aidtoinsurgents.get() and self.combo_interveneforrebels.get() and self.combo_destabilize.get() and combo_treaty.get() and combo_intervene_to_government.get() and combo_diplomaticpressure.get() and combo_militaryaid.get() and combo_economicaid.get() and combo_tradepolicy.get()!= '':
            total =(aid_to_insurgentsDict[self.combo_aidtoinsurgents.get()]),(intervene_to_rebelsDict[self.combo_interveneforrebels.get()]), (destabilizeDict[self.combo_destabilize.get()]),(treatyDict[combo_treaty.get()]),(intervene_to_governmentDict[combo_intervene_to_government.get()]),(diplomaticpressureDict[combo_diplomaticpressure.get()]),(militaryaidDict[combo_militaryaid.get()]),(economicaidDict[combo_economicaid.get()]),(tradepolicyDict[combo_tradepolicy.get()])
            self.resultlist.append(total)
            print(total)
            print(type(total))
            L = list(total)
            print(L)
            print(type(L))
            firstthree = L[0:3]
            csum = sum(firstthree)
            print(csum)
            lastsix = L[3:9]
            print(lastsix)
            lsum = sum(lastsix)
            print(lsum)
            securitylevel = (csum*3)/15
            diplomacylevel = (lsum*3)/30
            sl= round(securitylevel, None)
            dl= round(diplomacylevel, None)
            print(securitylevel)
            print(diplomacylevel)
            print(sl)
            print(dl)
            
            
            
         
    
        
        
        
         #self.result1.configure(text="Risk score : " + str(sl))'''

        if sl == 0 and dl == 0:
            self.maincanvas.abs_move(self.maincanvas, self.chesspiece, 140, 330)
        elif sl == 0 and dl == 1:
            self.maincanvas.abs_move(self.maincanvas, self.chesspiece, 140, 330)
        elif sl == 0 and dl == 2:
            self.maincanvas.abs_move(self.maincanvas, self.chesspiece, 140, 185)
        elif sl == 0 and dl == 3:
            self.maincanvas.abs_move(self.maincanvas, self.chesspiece, 140, 60)
        elif sl == 1 and dl == 0:
            self.maincanvas.abs_move(self.maincanvas, self.chesspiece, 140, 330)
        elif sl == 1 and dl == 1:
            self.maincanvas.abs_move(self.maincanvas, self.chesspiece, 140, 330)
        elif sl == 1 and dl == 2:
            self.maincanvas.abs_move(self.maincanvas, self.chesspiece, 140,185)
        elif sl == 1 and dl == 3:
            self.maincanvas.abs_move(self.maincanvas, self.chesspiece, 140, 60)
        elif sl == 2 and dl == 0:
            self.maincanvas.abs_move(self.maincanvas, self.chesspiece, 240, 330)
        elif sl == 2 and dl == 1:
            self.maincanvas.abs_move(self.maincanvas, self.chesspiece, 240, 330)
        elif sl == 2 and dl == 2:
            self.maincanvas.abs_move(self.maincanvas, self.chesspiece, 240, 185)
        elif sl == 2 and dl == 3:
            self.maincanvas.abs_move(self.maincanvas, self.chesspiece, 240, 60)
        elif sl == 3 and dl == 0:
            self.maincanvas.abs_move(self.maincanvas, self.chesspiece, 340, 330)
        elif sl == 3 and dl == 1:
            self.maincanvas.abs_move(self.maincanvas, self.chesspiece, 340, 330)
        elif sl == 3 and dl == 2:
            self.maincanvas.abs_move(self.maincanvas, self.chesspiece, 340, 185)
        elif sl == 3 and dl == 3:
            self.maincanvas.abs_move(self.maincanvas, self.chesspiece, 340, 60)
        else:
            self.maincanvas.abs_move(self.maincanvas, self.chesspiece, 40, 405)
        

        
        

        
    def create_result_frame(self):
        resultframe = LabelFrame(self.root, text='Result', fg='white', bg="#142F55", font=('Franklin Gothic Heavy', 12))
        resultframe.place(relx=0.38, rely=0.75, width = 270, height=150)
        ratebtn = Button(resultframe, text="Rate", height = 2, width = 15, command=self.display_result).place(relx=0.4, rely= 0.46)
       

    def create_main_label(self):
        labelname = Label(self.root, fg='white', bg="#091A36", text='GeoPolitics Rating',font=('Franklin Gothic Heavy', 24))
        labelname.place(relx=0.02, rely=0.06)
                          
    
    

    def create_matrix_frame(self):
        global chesspiece
        global grade
        self.matrixframe = LabelFrame(self.root, text = "Risk Matrix", font=('Franklin Gothic Heavy', 12))
        self.matrixframe.place(relx=0.60, rely = 0.12, width = 510, height = 580)
        self.maincanvas = Canvas(self.matrixframe, width = 500, height = 510, background="#FFFFFF")
        self.maincanvas.place(relx=0, rely=0)
        self.maincanvas.bind("<Button-1>", self.on_button_pressed)
                       
        self.img2 = PhotoImage(file="Matrix BOP2.png")
        self.item1= self.maincanvas.create_image(0,0,image=self.img2, anchor ="nw")
        self.risklevel = ImageTk.PhotoImage(file="king5.png")
        self.chesspiece= self.maincanvas.create_image(50,465,image=self.risklevel)
          
    

    def on_button_pressed(self, event):
       start_x = self.maincanvas.canvasx(event.x)
       start_y = self.maincanvas.canvasy(event.y)
       print("start_x, start_y =", start_x, start_y)

    def create_menu(self):
        self.menubar = Menu(self.root)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Exit", command=root.destroy)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About...", command=self.aboutrating)
        self.helpmenu.add_command(label="National Security rating Guideline ", command=self.aboutsecurityrating)
        self.helpmenu.add_command(label="Diplomacy rating Guideline..", command=self.aboutdiplomacyrating)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        self.root.config(menu=self.menubar)
    
        
    def aboutrating(self):
        self.filewin = Toplevel(self.root)
        self.filewin.config(background = 'white')
        self.text = Label(self.filewin, font = "Times 14" , justify = LEFT, text = "About Geopolitical Prestige Rating \n"
                                                                                                                             "\n"
                                                                                                                             "Geopolitical rating is based on the Balance of power game which is adopted by pentagon's simulations system. The tool was used during cold war period, \n"
                                                                                                                             "in order to device state foreign policy and training of state department staffs. \n"
                                                                                                                             "The goal in geopolitical rating is to understand a country's geopolitical prestige through diplomacy effectiveness and national security effectiveness.\n"
                                                                                                                             "The concept of geopolitical prestige is a country wants to be popular with the countries that count the most. In the world of geopolitics, countries that count are \n"
                                                                                                                             "the countries that are powerful in military might and economically dominant in the world. These countries are categorized under two tiers.Tier One countries are \n"
                                                                                                                             "United States, China, Japan, United Kingdom and EU (including Israel). These countries control 65% of the world economy. The next Tier Two countries \n"
                                                                                                                             "control 20% of the world economy and they are Brazil, Russia, India, Canada, Australia, Mexico, South Korea, Indonesia, Turkey and Saudi Arabia. \n"
                                                                                                                             "Thus, a country that accumulate lots of powerful friends from tier one and tier two countries, will be able to ostracize and weaken its enemies through \n"
                                                                                                                            "military alliance and economic cooperation with powerful nations.The nations of the world are sovereign states; they do whatever they choose to do- Your country's \n"
                                                                                                                            "ability to influence the course of events is directly related to its prestige. Short of direct conquest or the exercise of naked military power,prestige \n"
                                                                                                                            "closest a country can get to true international power position.\n"
                                                                                                                            "After the rating, if the black king chesspiece lands on Green Area, it means the country has a Geopolitical prestige in the world.\n"
                                                                                                                            "if it lands on yellow area, it means the country finds itself in an intermediate vulnerable geopolitical situations. Finally, if it lands on \n"
                                                                                                                            "Red area, the country is found in geopolitically risky position. The likelihood of the country getting into crisis is higher")
          
        self.text.grid(row=0, column=0)

    def aboutsecurityrating(self):
        self.filewin = Toplevel(self.root)
        self.frame = tk.Frame(self.filewin).pack()
        self.scrollbar=ttk.Scrollbar(self.filewin)
        self.scrollbar.pack(side = RIGHT, fill= Y)
        self.text = Label(self.filewin, font = "Times 13" , justify = LEFT, text = "National security rating guideline \n"
                                                                                                                             "\n"                          
                                                                                                                             "The goal in National security effectiveness is to defend offense strategy of an  enemy state. A powerful country will try to topple the country \n"
                                                                                                                             "to be rated through various offensive strategy.\n"
                                                                                                                             "\n"
                                                                                                                              "offensive strategy tactic 1 : Aid to insurrgents:\n"
                                                                                                                              "There are three types of insurgents: terrorists, guerrillas, and rebels. A powerful and stable government has none of these. Terrorists are the weakest form of \n"
                                                                                                                              "insurgents. If the terrorists are successful and grow in power, they become guerrillas and initiate a guerrilla war. If the guerrillas grow in power, they start a civil war\n"
                                                                                                                              "Then they are called rebels. Once enemy have identified a likely candidate for subversion, they have two weapons: Aid to Insurgents and Intervene for Rebels. \n"
                                                                                                                             " The amount of aid a enemy state can ship depends on the level of insurgency (terrorist level, guerrilas level and rebel level). When the level of aid is higher, \n"
                                                                                                                             "the powerful the insurgents will be. This means the regime (the country to be rated) will be affected badly.\n"
                                                                                                                              "\n"
                                                                                                                              "offensive strategy tactic 2 : Intervene for insurrgents:\n"
                                                                                                                              "A superpower can only ship weapons to a country through contiguous allies in which it has stationed troops. For example, it must have troops\n"
                                                                                                                              "in Honduras, El Salvador, or Costa Rica to ship weapons to the contras in Nicaragua. The amount of weapons that can be shipped is dependent \n"
                                                                                                                              "on the number of troops so stationed. However, a superpower can always leak a small amount of weaponry into any country since in world borders \n"
                                                                                                                              "aren't airtight. The most sincere form of assistance is direct intervention. This means that enemy state is sending part of its own army into that country to \n"
                                                                                                                              "help the rebels overthrow the government. Enemy state are limited in much the same way as with military aid to insurgencies. An enemy state must have \n"
                                                                                                                               "troops in a contiguous country before it can send troops to intervene for the rebels in a civil war; the number of troops that can intervene is always \n"
                                                                                                                               "a determinant factor in affecting the government to be toppled. The higher the troops, the higher will be the risk.\n"
                                                                                                                               "\n"
                                                                                                                               "offensive strategy tactic 3 : Destablization:\n"
                                                                                                                               "An alternative channel of geopolitical interaction is the subversion and destabilization of foreign governments.  Here enemy state tries to replace the \n"
                                                                                                                               "the unwanted government with a more friendly one through the less violent avenue of the coup d'etat. This is a more subtle, less direct approach requiring \n"
                                                                                                                               "a greater degree of finesse. The central concept is the coup d'etat. This is a change of government initiated by political factors rather than military ones. \n"
                                                                                                                               "Rebels must use military power to win a revolution, but a coup can overthrow a government only if the political climate is ripe for it- The most important \n"
                                                                                                                               "element of the political climate is the performance of the economy. If the economy performs well, the political climate is favorable for the existing \n"
                                                                                                                               "government. But if the economy performs poorly, discontent rises and the government is vulnerable to a coup. Modifying this is the political control \n"
                                                                                                                               "exerted by the government. Some states, such as the Russia and cuba, exercise such thorough control over their citizens that there is little or no chance \n"
                                                                                                                               "of a true coup d'etat. A changing of the guard, perhaps, but not a policy-changing coup. Totalitarian governments with sufficiently strong political control can \n"
                                                                                                                               "survive with economic performance that would topple other governments. If a government is shaky, it can be toppled (hence bringing about a coup d'etat) \n"
                                                                                                                               "with the judicious use of Destabilization. You destabilize a government by sending in the spies to encourage dissidents, fund the opposition, incite riots,\n"
                                                                                                                               "and create other domestic political mayhem. If the government is already weak, this might be enough to push it over the edge. If the government is strong, \n"
                                                                                                                               "the efforts of foreign powers will accomplish nothing.")                                    
                          
        self.text.pack()
        
    def aboutdiplomacyrating(self):
        self.filewin = Toplevel(self.root)
        self.scrollbar=ttk.Scrollbar(self.filewin)
        self.c = Canvas(self.filewin, background = 'white', yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command = self.c.yview)
        self.scrollbar.pack(side = RIGHT, fill= Y)
        self.elframe = Frame(self.c)
        self.c.pack(side = LEFT, fill = BOTH, expand = True)
        self.c.create_window(0,0, window=self.elframe, anchor='nw')
        self.text = Label(self.elframe, wraplength=1900, font = "Times 13" , justify = LEFT, text = "Diplomacy effectiveness rating guideline \n"
                                                                                                                             "\n"                          
                                                                                                                             "The goal in Diplomacy effectiveness is to attaract strong allies from tier 1 and tier 2 countries. If the country to be rated is successful in this endeavour, \n"
                                                                                                                             "then it will be able to shield itself using defensive strategy of its allied states. Here the allies protect the rated country from insurgents using various \n"
                                                                                                                             "defensive strategies.\n"
                                                                                                                             "\n"
                                                                                                                              "defensive strategy tactic 1 : Intervene for government:\n"
                                                                                                                              "the number of troops that can intervene is always a determinat factor in keeping in power a favored government by the allies. \n"
                                                                                                                              "Here Nations are even more sensitive about allowing a foreign power to send troops onto its soil. Furthermore strong allies face \n"
                                                                                                                              "limitation of resources because If they really want to send some troops to one country, they may be forced to pull some out of another. \n"
                                                                                                                              "\n"
                                                                                                                               "defensive strategy tactic 2 : Military Aid:\n"
                                                                                                                               "This option allows a powerful country to provide weapons (but not soldiers) to a friendly government, It will boost the military power of the government, \n"
                                                                                                                               "making it better able to withstand internal insurgencies and external military pressure. When the level of aid is higher the more powerful will be the government.\n"
                                                                                                                               "The more powerful the government is the more difficult it will be for insurgents. Every government in the world knows that help from foreign powers always\n"
                                                                                                                               "seems to come with sticky strings attached. Most governments are understandably reluctant to accept an unseemly amount of aid from foreign power.\n"
                                                                                                                               "This reluctance is directly related to the degree of enmity between the two nations. Thus, some countries would not accept generous offer of military assistance \n"
                                                                                                                               "they would undoubtedly suspect some fiendish infidel subterfuge. On the other hand, some countries has already cast thier lot with \n"
                                                                                                                               "foreign powers and would have no reservations about accepting scads of military aid. Here military aid will alleviate the budget restriction \n"
                                                                                                                               "of the receiving nation. This will help the receiving nation to divert it's budget to other economic activies so that the can alleviate political pressures. \n"
                                                                                                                               "\n"
                                                                                                                                "defensive strategy tactic 3 : Economic Aid:\n"
                                                                                                                               "Foreign powers can protect a friendly regime from coups by assisting its economy. This is done with economic aid, a direct transfer of money from \n"
                                                                                                                               "foreign powers economy to the recipient's. Foreign power GDP will be reduced with the secondary effect of reducing the amount of money available \n"
                                                                                                                               "for military expenditures. The recipent's economy will be boosted; this will increase public satisfaction with the regime. Thus, economic aid reduces \n"
                                                                                                                               "a country's vulnerability to coups d’etat. Of course, the magnitude of the effect is dependent on the wealth of the recipient. If foreign powers dump \n"
                                                                                                                               "4 billion dollars on poverty-stricken country, that amounts have significant impact on the recipent GDP; the effect on the recipent will be electric. \n"
                                                                                                                               "Basking in their immense wealth, their discontent with the government will completely vanish. However, a wealthier country is much harder to buy off. \n"
                                                                                                                               "Four billion dollars is but a drop in the bucket for such a country. Thus, it is very difficult to save a wealthy nation with economic assistance. \n"
                                                                                                                                "\n"
                                                                                                                                "defensive strategy tactic 4 : Diplomatic Pressure:\n"
                                                                                                                               "These  tactic introduces a geopolitical weapon named finlandization. The term comes from the postwar experience of Finland. Finland had been an ally \n"
                                                                                                                               "of Nazi Germany against the USSR; when the war ended, Finland was not invaded by the Soviets only because they were too busy with bigger fish. \n"
                                                                                                                               "Yet, Finland did not get off scot-free, None of the Western powers were willing to stand up for a Nazi ally. Finlandization can occur to any nation that \n"
                                                                                                                               "perceives itself to be in a hopeless diplomatic and military position- If a foreign power is hostile and possesses the power to crush the victim, and \n"
                                                                                                                               "external support is inadequate to protect the victim, then the victim Finlandizes; it adjusts its diplomatic position to make itself less hostile and more \n"
                                                                                                                               "friendly to the dangerous foreign power. To encourage or discourage Finlandization among the nations of the world. superpoweres have two weapons \n"
                                                                                                                               "to help them: Diplomatic Pressure and Treaties. Pressure is an attempt to intimidate a country with words and provocative actions. A simple diplomatic \n"
                                                                                                                               "note expressing grave concern can be interpreted as a very weak form of pressure. At the opposite extreme we have the full-scale diplomatic offensive, \n"
                                                                                                                               "including an array of actions such as holding naval maneuvers off the coast of the victim, making speeches about the evil ways of the victim, or ostentatiously \n"
                                                                                                                               "consulting with declared enemies of the victim. All of these actions serve to make a victim acutely aware of the disparity in strength between the two nations.\n"
                                                                                                                               "If the victim feels sufficiently insecure, it will Finlandize to the superpower applying diplomatic pressure. Obviously, the more pressure is applied, the greater \n"
                                                                                                                               "the likelihood that the victim will indeed Finlandize. When a country Finlandizes to a superpower, a news message will be created describing how \n"
                                                                                                                               "the leader of the Finlandizing country praises the Superpower that is the object of the policy. Although the word Finlandize does not appear, \n"
                                                                                                                               "you should have no trouble interpreting the headline. Moreover, pressure can induce the victim to increase its military spending as a form of self-defense. \n"
                                                                                                                               "This in turn forces the government to cut into consumer spending, an act that will increase public dissatisfaction with the regime and could lead to a coup d'etat  \n"
                                                                                                                               "or change of government. Thus, pressure can sometimes cause a coup d'etat. Unlike most other options, pressure is not an ongoing process, \n"
                                                                                                                               "it is a one-time action that automatically terminates after one year.\n"
                                                                                                                               "\n"
                                                                                                                                "defensive strategy tactic 5 : Treaties:\n"
                                                                                                                               "The antidote for pressure is a treaty. If a powerful country fear that a client of its may Finlandize to another enemy state, it can bolster that client's will \n"
                                                                                                                               "to resist in several ways. it can send military aid to increase its military power, or it can station troops in that country to help defend it. By increasing \n"
                                                                                                                               "its defensive military strength, the powerful country can shore up the flagging confidence of the country to be rated. A treaty implies a degree of \n"
                                                                                                                               "commitment by powerfull ally to the regime with which they sign. Powerful countries are, to a greater or lesser degree, guaranteeing the security of \n"
                                                                                                                               "the country with which they sign the treaty and the degree of commitment is related to the type of treaty. A treaty establishing diplomatic relations \n"
                                                                                                                               "between your two countries committment is very little. In contrast, a nuclear defense treaty is an absolute commitment that  a powerful ally will take \n"
                                                                                                                               "all measures possible, including the initiation of a nuclear holocaust, to protect the signatory. \n"
                                                                                                                               "\n"
                                                                                                                               "defensive strategy tactic 6 : Trade:\n"
                                                                                                                                "There last geopolitical policy option is trade policy. A powerful country may adjust its trade policy toward any country. This policy will have no effect \n"
                                                                                                                                "on the economy of the targeted nation. It will, however, make a diplomatic statement that will affect relations between two countries." )                                    
                          
        self.text.pack()
        self.filewin.update()
        self.c.config(scrollregion=self.c.bbox("all"))
        
    def create_combobox_rating1(self):
        global rating_selected1, rating_selected2, rating_selected3 
        global aid_to_insurgentsDict, intervene_to_rebelsDict, destabilizeDict
        global combo_aidtoinsurgents, combo_interveneforrebels, combo_destabilize
        
        aid_to_insurgentsDict = {'None': 5, 'Up to 20 million': 4, 'up to 100 million': 3, 'Up to 500 million': 2, 'More than 1 billion': 1}
        intervene_to_rebelsDict = {'None': 5, 'up to 1000 troops' :4, 'up to 5000 troops': 3, 'up to 20000 troops': 2,'More than 100 thousands troops':1}
        destabilizeDict = {'None': 5, 'Encourage Dissidents' :4, 'Fund opposition': 3, 'Incite riots': 2,'Provoke assasination or Coup detat':1}
        ratingframe = LabelFrame(self.root, bg="#142F55", fg="white", text = "National Security Effectiveness Rating", font=('Franklin Gothic Heavy', 11))
        ratingframe.place(relx=0.03, rely=0.21, width=390, height= 150)
        aidtoinsurgentslabel =Label(ratingframe, bg= "#142F55", fg='white', text='Financial Aid to Insurgents', font=('Franklin Gothic Heavy', 10)).place(relx=0.04, rely=0.06)
        var_aidtoinsurgents = StringVar()
        self.combo_aidtoinsurgents = ttk.Combobox(ratingframe, values=list(aid_to_insurgentsDict.keys()), justify="center", textvariable=var_aidtoinsurgents)
        self.combo_aidtoinsurgents.bind('<<ComboboxSelected>>', lambda event: rating_selected1.config(text=aid_to_insurgentsDict[var_aidtoinsurgents.get()]))
        self.combo_aidtoinsurgents.set('')
        self.combo_aidtoinsurgents.place(relx=0.53, rely=0.06)
        
        rating_selected1 = StringVar()
        rating_selected1 = Label(ratingframe, text="", bg= "#142F55", fg='white')
        rating_selected1.place(relx=0.95, rely=0.06)
        
        interveneforrebelslabel =Label(ratingframe, bg= "#142F55", fg='white',text='Intervene for Rebels', font=('Franklin Gothic Heavy', 10)).place(relx=0.04, rely=0.3)
        var_interveneforrebels = StringVar()
        self.combo_interveneforrebels = ttk.Combobox(ratingframe, values=list(intervene_to_rebelsDict.keys()), justify="center", textvariable=var_interveneforrebels)
        self.combo_interveneforrebels.bind('<<ComboboxSelected>>', lambda event: rating_selected2.config(text=intervene_to_rebelsDict[var_interveneforrebels.get()]))
        self.combo_interveneforrebels.set('')
        self.combo_interveneforrebels.place(relx=0.53, rely=0.3)
        
        rating_selected2 = StringVar()
        rating_selected2 = Label(ratingframe, text="", bg= "#142F55", fg='white')
        rating_selected2.place(relx=0.95, rely=0.3)
        
        destablizelabel =Label(ratingframe, text='Destabilize', bg= "#142F55", fg='white',font=('Franklin Gothic Heavy', 10)).place(relx=0.04, rely=0.54)
            
        var_destabilize = StringVar()
        self.combo_destabilize = ttk.Combobox(ratingframe, values=list(destabilizeDict.keys()), justify="center", textvariable=var_destabilize)
        self.combo_destabilize.bind('<<ComboboxSelected>>', lambda event: rating_selected3.config(text=destabilizeDict[var_destabilize.get()]))
        self.combo_destabilize.set('')
        self.combo_destabilize.place(relx=0.53, rely=0.54)
        rating_selected3 = StringVar()
        rating_selected3 = Label(ratingframe, text="", bg= "#142F55", fg='white')
        rating_selected3.place(relx=0.95, rely=0.54)
        
        
    def create_combobox_rating2(self):
        global rating_selected4, rating_selected5, rating_selected6, rating_selected7,rating_selected8, rating_selected9
        global treatyDict, intervene_to_governmentDict, diplomaticpressureDict, militaryaidDict,economicaidDict, tradepolicyDict
        global combo_treaty,combo_intervene_to_government, combo_diplomaticpressure, combo_militaryaid, combo_economicaid,combo_tradepolicy

        treatyDict = {'None or diplomatic relations': 1, 'trade relations': 2, 'military base': 3, 'conventinal weapons': 4, 'nuclear deal': 5}
        intervene_to_governmentDict = {'None': 1, 'up to 1000 troops' :2, 'up to 5000 troops': 3, 'up to 20000 troops': 4,'More than 100 thousands troops':5}
        diplomaticpressureDict = {'None or quiet diplomacy': 5, 'public posturing' :4, 'Moderate Pressure': 3, 'Intense pressure': 2,'Offensive diplomacy':1}
        militaryaidDict = {'None': 1, 'Up to 20 million': 2, 'up to 100 million': 3, 'Up to 500 million': 4, 'More than 1 billion': 5}
        economicaidDict = {'None': 1, 'Up to 20 million': 2, 'up to 100 million': 3, 'Up to 500 million': 4, 'More than 1 billion': 5}
        tradepolicyDict = {'Favorable Trade': 5, 'Normal Trade': 4, 'Trade Quota': 3, 'stiff quota': 2, 'Trade or tech emabargo': 1}
        
        ratingframe = LabelFrame(self.root, bg="#142F55", fg="white", text = "Diplomacy Effectiveness Rating", font=('Franklin Gothic Heavy', 11))
        ratingframe.place(relx=0.03, rely=0.51, width=390, height= 250)
        
        treatylabel =Label(ratingframe, text='Treaty', bg= "#142F55", fg='white', font=('Franklin Gothic Heavy', 10)).place(relx=0.04, rely=0.06)
        var_treaty = StringVar()
        combo_treaty = ttk.Combobox(ratingframe, values=list(treatyDict.keys()), justify="center", textvariable=var_treaty)
        combo_treaty.bind('<<ComboboxSelected>>', lambda event: rating_selected4.config(text=treatyDict[var_treaty.get()]))
        combo_treaty.set('')
        combo_treaty.place(relx=0.53, rely=0.06)
        rating_selected4 = StringVar()
        rating_selected4 = Label(ratingframe, text="", bg= "#142F55", fg='white')
        rating_selected4.place(relx=0.95, rely=0.06)

        intervene_to_governmentlabel =Label(ratingframe, bg= "#142F55", fg='white',text='Intervene for Government', font=('Franklin Gothic Heavy', 10)).place(relx=0.04, rely=0.21)
        var_intervene_to_government = StringVar()
        combo_intervene_to_government = ttk.Combobox(ratingframe, values=list(intervene_to_governmentDict.keys()), justify="center", textvariable=var_intervene_to_government)
        combo_intervene_to_government.bind('<<ComboboxSelected>>', lambda event: rating_selected5.config(text=intervene_to_governmentDict[var_intervene_to_government.get()]))
        combo_intervene_to_government.set('')
        combo_intervene_to_government.place(relx=0.53, rely=0.21)
        rating_selected5 = StringVar()
        rating_selected5 = Label(ratingframe, text="", bg= "#142F55", fg='white')
        rating_selected5.place(relx=0.95, rely=0.21)

        militaryaidlabel =Label(ratingframe, text='Military Aid', bg= "#142F55", fg='white',font=('Franklin Gothic Heavy', 10)).place(relx=0.04, rely=0.36)
        var_militaryaid = StringVar()
        combo_militaryaid = ttk.Combobox(ratingframe, values=list(militaryaidDict.keys()), justify="center", textvariable=var_militaryaid)
        combo_militaryaid.bind('<<ComboboxSelected>>', lambda event: rating_selected7.config(text=militaryaidDict[var_militaryaid.get()]))
        combo_militaryaid.set('')
        combo_militaryaid.place(relx=0.53, rely=0.36)
        rating_selected7 = StringVar()
        rating_selected7 = Label(ratingframe, text="", bg= "#142F55", fg='white')
        rating_selected7.place(relx=0.95, rely=0.36)

        economicaidlabel =Label(ratingframe, text='Economic Aid', bg= "#142F55", fg='white',font=('Franklin Gothic Heavy', 10)).place(relx=0.04, rely=0.51)
        var_economicaid = StringVar()
        combo_economicaid = ttk.Combobox(ratingframe, values=list(economicaidDict.keys()), justify="center", textvariable=var_economicaid)
        combo_economicaid.bind('<<ComboboxSelected>>', lambda event: rating_selected8.config(text=economicaidDict[var_economicaid.get()]))
        combo_economicaid.set('')
        combo_economicaid.place(relx=0.53, rely=0.51)
        rating_selected8 = StringVar()
        rating_selected8 = Label(ratingframe, text="", bg= "#142F55", fg='white')
        rating_selected8.place(relx=0.95, rely=0.51)

        diplomaticpressurelabel =Label(ratingframe, text='Diplomatic Pressure', bg= "#142F55", fg='white',font=('Franklin Gothic Heavy', 10)).place(relx=0.04, rely=0.66)
        var_diplomaticpressure = StringVar()
        combo_diplomaticpressure = ttk.Combobox(ratingframe, values=list(diplomaticpressureDict.keys()), justify="center", textvariable=var_diplomaticpressure)
        combo_diplomaticpressure.bind('<<ComboboxSelected>>', lambda event: rating_selected6.config(text=diplomaticpressureDict[var_diplomaticpressure.get()]))
        combo_diplomaticpressure.set('')
        combo_diplomaticpressure.place(relx=0.53, rely=0.66)
        rating_selected6 = StringVar()
        rating_selected6 = Label(ratingframe, text="", bg= "#142F55", fg='white')
        rating_selected6.place(relx=0.95, rely=0.66)

        tradepolicylabel =Label(ratingframe, text='Trade Policy', bg= "#142F55", fg='white',font=('Franklin Gothic Heavy', 10)).place(relx=0.04, rely=0.81)
        var_tradepolicy = StringVar()
        combo_tradepolicy = ttk.Combobox(ratingframe, values=list(tradepolicyDict.keys()), justify="center", textvariable=var_tradepolicy)
        combo_tradepolicy.bind('<<ComboboxSelected>>', lambda event: rating_selected9.config(text=tradepolicyDict[var_tradepolicy.get()]))
        combo_tradepolicy.set('')
        combo_tradepolicy.place(relx=0.53, rely=0.81)
        rating_selected9 = StringVar()
        rating_selected9 = Label(ratingframe, text="", bg= "#142F55", fg='white')
        rating_selected9.place(relx=0.95, rely=0.81)

        
        



















if __name__ == '__main__':
    root = tk.Tk()
    application = RiskMatrix(root)
    root.mainloop()
