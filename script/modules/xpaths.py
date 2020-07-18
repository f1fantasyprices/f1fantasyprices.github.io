

def get_xpaths():
    
    xpaths = {

    #username
        "username" : "txtLogin",
        "password" : "txtPassword",

        "sign_in_btn" : "#loginform > div:nth-child(4) > button:nth-child(2)",

        "swap_driver_1" : "player-slot__header",
        "manage" : """.//span[text()='Manage']""",
        "next_1" : """.//div[text()='Next'] """,
        "done" :   """.//div[text()='Done'] """,

        "accept_cookie" : """.//a[text()='I Accept']""",

        "x" : "/html/body/div[9]/div/div/aside/header/button/div[2]",

        "expose_list" : """/html/body/main/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/header/div[1]/button[2]/div[1]""",


        """driver_card""": """lineup-picker__card__body""",
    }
    return xpaths



def get_driver_colors():


    driver_colors = {
        "V. Bottas": "#06fcf8",
        "L. Hamilton": "#06fcf8",
        "S. Vettel": "#f30004",
        "C. Leclerc": "#f30004",
        "C. Sainz": "#ff9102",
        "L. Norris": "#ff9102",
        "D. Ricciardo": "#fee703",
        "E. Ocon": "#fee703",
        "R. Grosjean": "#ebcf76",
        "K. Magnussen": "#ebcf76",
        "N. Latifi": "#091617",
        "G. Russell": "#091617",
        "M. Verstappen": "#022fa2",
        "A. Albon": "#022fa2",
        "A. Giovinazzi": "#860101",
        "K. Räikkönen": "#860101",
        "D. Kvyat": "#3c86fd",
        "P. Gasly": "#3c86fd",
        "S. Perez": "#ef7fbb",
        "L. Stroll": "#ef7fbb",
    }
    return driver_colors



def get_team_colors():
    team_colors = {
        "Mercedes": "#06fcf8",
        "Ferrari": "#f30004",
        "McLaren": "#ff9102",
        "Renault": "#fee703",
        "Haas": "#ebcf76",
        "Williams": "#091617",
        "Red Bull": "#022fa2",
        "Alfa Romeo": "#860101",
        "AlphaTauri": "#3c86fd",
        "Racing Point": "#ef7fbb",
    }

    return team_colors

def get_abrreviated_names():


    abb = {
        "V. Bottas": "VB",
        "L. Hamilton": "LH",
        "S. Vettel": "SV",
        "C. Leclerc": "CL",
        "C. Sainz": "CS",
        "L. Norris": "LN",
        "D. Ricciardo": "DR",
        "E. Ocon": "EO",
        "R. Grosjean": "RG",
        "K. Magnussen": "KM",
        "N. Latifi": "NL",
        "G. Russell": "GR",
        "M. Verstappen": "MV",
        "A. Albon": "AA",
        "A. Giovinazzi": "AG",
        "K. Räikkönen": "KR",
        "D. Kvyat": "DK",
        "P. Gasly": "PG",
        "S. Perez": "SP",
        "L. Stroll": "LS",
    }
    return abb