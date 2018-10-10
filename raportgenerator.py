from fpdf import FPDF
import requests

def generate_raport(name, rank, icon_id, server, lvl):
    icon = requests.get("http://ddragon.leagueoflegends.com/cdn/6.24.1/img/profileicon/{}.png".format(icon_id))
    if icon.status_code == 200:
        with open("src/temporary/icon.png", 'wb') as f:
            f.write(icon.content)

    pdf = FPDF()
    pdf.set_author("Marcin Binkowski")
    pdf.add_page()
    pdf.set_font("arial", size=50)
    pdf.cell(0, 20, txt="GraphsLeague",  ln=2, align="C")
    pdf.set_font("arial", size=30)
    pdf.image("src/temporary/icon.png", w=30)
    pdf.cell(0, 15, txt="{}".format(name), ln=2, align="L")
    pdf.set_font("arial", size=16)
    pdf.cell(0, 8, txt="server: {}".format(server), ln=1, align="L")
    pdf.cell(0, 8, txt="level: {}".format(lvl), ln=1, align="L")


    pdf.output("{}_raport.pdf".format(name))

if __name__ == "__main__":
    generate_raport("binq661", "gold", 588, "eune", "90")