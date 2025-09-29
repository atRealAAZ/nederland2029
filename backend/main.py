# ruff: noqa: E501
from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="Nederland 2029 API",
    description="API for Dutch election decision app",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Party(BaseModel):
    id: int
    name: str
    color: str
    logo_url: str
    current_vision: str
    future_vision: str
    key_policies: List[str]
    website_url: str


PARTIES_2025 = [
    Party(
        id=1,
        name="PVV",
        color="#F39200",
        logo_url="/logos/pvv.png",
        current_vision=(
            "Nederland is te veel veranderd door massa-immigratie. "
            "Onze cultuur en identiteit staan onder druk. "
            "De EU bepaalt te veel over ons eigen land. "
            "Asielzoekers krijgen voorrang boven Nederlanders."
        ),
        future_vision=(
            "Een Nederland voor Nederlanders, waar onze cultuur "
            "en tradities centraal staan. Minder EU, meer nationale "
            "soevereiniteit. Streng immigratie- en asielbeleid. Nederland eerst."
        ),
        key_policies=[
            "Stop massa-immigratie en asielinstroom",
            "Nederland uit de EU",
            "Beschermen Nederlandse cultuur en identiteit",
            "Meer politie en veiligheid op straat",
            "Lagere energierekening voor gewone Nederlanders"
        ],
        website_url="https://www.pvv.nl"
    ),
    Party(
        id=2,
        name="GroenLinks-PvdA",
        color="#DC143C",
        logo_url="/logos/glpvda.png",
        current_vision="Nederland is te ongelijk geworden. Grote bedrijven en rijken profiteren, terwijl gewone mensen achteruitgaan. De klimaatcrisis vraagt urgente actie. Publieke voorzieningen worden wegbezuinigd.",
        future_vision="Een eerlijk Nederland waar iedereen mee telt. Sociale zekerheid, goede publieke voorzieningen, en een groene economie die werkt voor iedereen. Klimaatrechtvaardigheid en solidariteit.",
        key_policies=[
            "Hogere belastingen voor rijken en bedrijven",
            "Massale investeringen in groene energie",
            "Sterke publieke sector en sociale zekerheid",
            "Mensenrechten en internationale solidariteit",
            "Betaalbare woningen voor iedereen"
        ],
        website_url="https://www.groenlinks.nl"
    ),
    Party(
        id=3,
        name="VVD",
        color="#0A4D8C",
        logo_url="/logos/vvd.png",
        current_vision="Nederland staat er economisch goed voor, maar we moeten onze concurrentiepositie behouden. We zien kansen in innovatie en ondernemerschap, maar bureaucratie houdt ons tegen. Koopkracht moet beschermd worden.",
        future_vision="Een Nederland waar ondernemers vrijelijk kunnen innoveren, waar de overheid efficiënt werkt, en waar iedereen kansen krijgt om te groeien. Minder regels, meer ruimte voor initiatief.",
        key_policies=[
            "Lagere belastingen voor bedrijven en ondernemers",
            "Vermindering van bureaucratie en regelgeving",
            "Investeren in onderwijs en innovatie",
            "Sterke defensie en internationale samenwerking",
            "Effectieve immigratie- en integratiebeleid"
        ],
        website_url="https://www.vvd.nl"
    ),
    Party(
        id=4,
        name="NSC",
        color="#00A0A0",
        logo_url="/logos/nsc.png",
        current_vision="Nederland heeft goede fundamenten maar de politiek is verdeeld en weinig daadkrachtig. We hebben bestuurlijke vernieuwing nodig om de grote uitdagingen aan te pakken.",
        future_vision="Een Nederland met een betrouwbare overheid die zich richt op de hoofdzaken: veiligheid, welvaart en welzijn. Pragmatisch bestuur zonder ideologische verdeeldheid.",
        key_policies=[
            "Bestuurlijke vernieuwing en effectief overheidsbeleid",
            "Beheersbare migratie en goede integratie",
            "Investeren in onderwijs en zorg",
            "Klimaatbeleid dat betaalbaar en realistisch is",
            "Versterken van de rechtsstaat"
        ],
        website_url="https://www.nieuwsociaalcontract.nl"
    ),
    Party(
        id=5,
        name="D66",
        color="#E7007E",
        logo_url="/logos/d66.png",
        current_vision="Nederland heeft veel kansen maar wordt geremd door verouderde structuren. We moeten moderner, democratischer en Europeeser worden. Ongelijkheid neemt toe.",
        future_vision="Een progressief, open Nederland dat voorop loopt in Europa. Meer directe democratie, gelijke kansen voor iedereen, en ambitieus klimaatbeleid. Innovatie en inclusiviteit.",
        key_policies=[
            "Democratische vernieuwing en referenda",
            "Ambitieus klimaat- en duurzaamheidsbeleid",
            "Investeren in onderwijs en wetenschap",
            "Pro-Europese koers en internationale samenwerking",
            "Gelijke rechten en kansen voor iedereen"
        ],
        website_url="https://www.d66.nl"
    ),
    Party(
        id=6,
        name="BBB",
        color="#89C442",
        logo_url="/logos/bbb.png",
        current_vision="Het platteland en de boeren worden over het hoofd gezien. Beleid wordt gemaakt in de Randstad zonder oog voor de gevolgen voor het landelijke gebied. Boeren worden onterecht weggezet als vervuilers.",
        future_vision="Een Nederland waar stad en platteland in balans zijn. Respect voor boeren en de agrarische sector. Beleid dat rekening houdt met alle regio's, niet alleen de grote steden.",
        key_policies=[
            "Beschermen van de agrarische sector",
            "Meer aandacht voor het platteland",
            "Realistische stikstofaanpak",
            "Burgers centraal in plaats van bureaucratie",
            "Betaalbare energie en mobiliteit"
        ],
        website_url="https://www.boerburgerbeweging.nl"
    ),
    Party(
        id=7,
        name="CDA",
        color="#00A74A",
        logo_url="/logos/cda.png",
        current_vision="Nederland heeft sterke fundamenten maar we moeten meer investeren in samenhang en solidariteit. Te veel individualisering bedreigt onze sociale cohesie. Gemeenschappen hebben versterking nodig.",
        future_vision="Een samenleving gebaseerd op christelijke waarden: naastenliefde, verantwoordelijkheid en rentmeesterschap. Sterke gemeenschappen en duurzame ontwikkeling voor toekomstige generaties.",
        key_policies=[
            "Investeren in gezin en gemeenschap",
            "Duurzame landbouw en klimaatbeleid",
            "Behoud van christelijke waarden in beleid",
            "Sterke sociale zekerheid met eigen verantwoordelijkheid",
            "Zorg voor kwetsbare groepen"
        ],
        website_url="https://www.cda.nl"
    ),
    Party(
        id=8,
        name="SP",
        color="#FF0000",
        logo_url="/logos/sp.png",
        current_vision="Nederland wordt steeds ongelijker. Gewone mensen kunnen nauwelijks rondkomen terwijl rijken en bedrijven steeds rijker worden. De publieke sector wordt kapot bezuinigd.",
        future_vision="Een Nederland voor gewone mensen. Goede zorg, onderwijs en huizen voor iedereen. Bedrijven moeten bijdragen aan de samenleving in plaats van alleen winst maken.",
        key_policies=[
            "Hogere minimumloon en betere arbeidsrechten",
            "Nationalisatie van cruciale sectoren",
            "Stoppen met bezuinigingen op zorg en onderwijs",
            "Maximuminkomen en vermogensbelasting",
            "Betaalbare woningen voor iedereen"
        ],
        website_url="https://www.sp.nl"
    ),
    Party(
        id=9,
        name="DENK",
        color="#00A859",
        logo_url="/logos/denk.png",
        current_vision="Nederland heeft een probleem met discriminatie en ongelijke behandeling. Migranten en minderheden worden achtergesteld. Er is te weinig aandacht voor diversiteit en inclusie.",
        future_vision="Een Nederland waar iedereen gelijke kansen krijgt, ongeacht afkomst. Een inclusieve samenleving die diversiteit omarmt en discriminatie actief bestrijdt.",
        key_policies=[
            "Bestrijding van discriminatie en racisme",
            "Gelijke kansen voor alle Nederlanders",
            "Erkenning van de multiculturele samenleving",
            "Investeren in achterstandswijken",
            "Internationale verbindingen en diplomatie"
        ],
        website_url="https://www.bewegingdenk.nl"
    ),
    Party(
        id=10,
        name="Partij voor de Dieren",
        color="#006C2B",
        logo_url="/logos/pvdd.png",
        current_vision="Nederland behandelt dieren slecht en vernietigt de natuur voor korte termijn economische winst. De bio-industrie en intensieve landbouw veroorzaken enorme dierenleed en milieuproblemen.",
        future_vision="Een Nederland waar dieren, natuur en milieu centraal staan. Een plantaardige economie die duurzaam is voor mens, dier en planeet. Respect voor alle levende wezens.",
        key_policies=[
            "Dierenrechten in de Grondwet",
            "Stoppen met de bio-industrie",
            "Bescherming van natuur en biodiversiteit",
            "Transitie naar plantaardige economie",
            "Stoppen met dierproeven"
        ],
        website_url="https://www.partijvoordedieren.nl"
    ),
    Party(
        id=11,
        name="FVD",
        color="#722896",
        logo_url="/logos/fvd.png",
        current_vision="Nederland wordt geregeerd door globalistische elites die de Nederlandse soevereiniteit ondermijnen. Corona-maatregelen hebben onze vrijheden aangetast. De EU dicteert ons beleid.",
        future_vision="Een vrij en soeverein Nederland waar burgers zelf kunnen beslissen. Directe democratie, nationale soevereiniteit en het behoud van Nederlandse waarden en tradities.",
        key_policies=[
            "Nederland uit de EU",
            "Directe democratie en referenda",
            "Behoud van Nederlandse soevereiniteit",
            "Stoppen met klimaatbeleid",
            "Geen lockdowns of verplichte vaccinaties"
        ],
        website_url="https://www.fvd.nl"
    ),
    Party(
        id=12,
        name="SGP",
        color="#0066CC",
        logo_url="/logos/sgp.png",
        current_vision="Nederland verliest zijn christelijke wortels en morele kompas. Seculiere ideologieën ondermijnen de Bijbelse normen en waarden die ons land groot hebben gemaakt. Familie en gezag staan onder druk.",
        future_vision="Een Nederland dat wordt geregeerd volgens Gods woord, waar Bijbelse normen en waarden leidend zijn. Respect voor gezag, sterke christelijke gezinnen en een samenleving gebaseerd op Gereformeerde beginselen.",
        key_policies=[
            "Handhaving van christelijke normen en waarden",
            "Bescherming van het gezin en huwelijk",
            "Zondag als rustdag beschermen",
            "Christelijk onderwijs en opvoeding",
            "Respect voor Gods schepping"
        ],
        website_url="https://www.sgp.nl"
    ),
    Party(
        id=13,
        name="ChristenUnie",
        color="#007CBA",
        logo_url="/logos/cu.png",
        current_vision="Nederland heeft veel goeds maar we verliezen onze morele kompas. Familie en gemeenschap staan onder druk. We moeten meer oog hebben voor kwetsbare mensen en toekomstige generaties.",
        future_vision="Een Nederland gebaseerd op Bijbelse waarden: rechtvaardigheid, rentmeesterschap en naastenliefde. Bescherming van het leven, sterke families en duurzame samenleving.",
        key_policies=[
            "Bescherming van het leven van wieg tot graf",
            "Sterke gezinnen en gemeenschappen",
            "Rentmeesterschap van de schepping",
            "Zorg voor de zwakkeren in de samenleving",
            "Eerlijk delen van welvaart"
        ],
        website_url="https://www.christenunie.nl"
    ),
    Party(
        id=14,
        name="Volt",
        color="#502379",
        logo_url="/logos/volt.png",
        current_vision="Nederland kampt met versnipperde politiek en korte termijn denken. We missen een Europese visie en ambitieuze plannen voor de toekomst. Oude partijen bieden geen antwoord op moderne uitdagingen.",
        future_vision="Een progressief Nederland dat voorop loopt in Europa. Ambitieus klimaatbeleid, digitale innovatie, Europese integratie en pragmatische oplossingen voor complexe problemen van de 21e eeuw.",
        key_policies=[
            "Europese federatie en integratie",
            "Ambitieus klimaat- en energiebeleid",
            "Digitalisering en innovatie",
            "Evidence-based beleid en lange termijn denken",
            "Gelijke kansen en inclusiviteit"
        ],
        website_url="https://www.volteuropa.org/nl"
    ),
    Party(
        id=15,
        name="JA21",
        color="#2E8B57",
        logo_url="/logos/ja21.png",
        current_vision="Nederland heeft goede kanten maar wordt belemmerd door linkse ideologie en inefficiënte overheidsbestuur. We moeten terug naar gezond verstand en realisme in het beleid.",
        future_vision="Een Nederland gebaseerd op conservatief realisme: sterke rechtsstaat, effectief bestuur, behoud van tradities en waarden, en pragmatisch beleid zonder ideologische dogma's.",
        key_policies=[
            "Conservatief realisme in het beleid",
            "Effectieve immigratie en integratie",
            "Sterke rechtsstaat en veiligheid",
            "Realistische klimaataanpak",
            "Behoud van Nederlandse cultuur"
        ],
        website_url="https://www.ja21.nl"
    )
]


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Nederland 2029 API", "status": "running"}


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "healthy"}


@app.get("/api/parties", response_model=List[Party])
async def get_parties() -> List[Party]:
    return PARTIES_2025


@app.get("/api/parties/{party_id}", response_model=Party)
async def get_party(party_id: int) -> Party:
    party = next((p for p in PARTIES_2025 if p.id == party_id), None)
    if party is None:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Party not found")
    return party