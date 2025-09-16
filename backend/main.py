from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
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


SAMPLE_PARTIES = [
    Party(
        id=1,
        name="VVD",
        color="#0A4D8C",
        logo_url="/logos/vvd.png",
        current_vision="Nederland staat er economisch goed voor, maar we moeten onze concurrentiepositie behouden. We zien kansen in innovatie en ondernemerschap, maar bureaucratie houdt ons tegen.",
        future_vision="Een Nederland waar ondernemers vrijelijk kunnen innoveren, waar de overheid efficiënt werkt, en waar iedereen kansen krijgt om te groeien. Minder regels, meer ruimte voor initiatief.",
        key_policies=[
            "Lagere belastingen voor bedrijven en ondernemers",
            "Vermindering van bureaucratie en regelgeving",
            "Investeren in onderwijs en innovatie",
            "Sterke defensie en internationale samenwerking"
        ],
        website_url="https://www.vvd.nl"
    ),
    Party(
        id=2,
        name="PVV",
        color="#F39200",
        logo_url="/logos/pvv.png",
        current_vision="Nederland is te veel veranderd door massa-immigratie. Onze cultuur en identiteit staan onder druk. De EU bepaalt te veel over ons eigen land.",
        future_vision="Een Nederland voor Nederlanders, waar onze cultuur en tradities centraal staan. Minder EU, meer nationale soevereiniteit. Streng immigratie- en asielbeleid.",
        key_policies=[
            "Stop massa-immigratie en asielinstroom",
            "Nederland uit de EU",
            "Beschermen Nederlandse cultuur en identiteit",
            "Meer politie en veiligheid op straat"
        ],
        website_url="https://www.pvv.nl"
    ),
    Party(
        id=3,
        name="CDA",
        color="#00A74A",
        logo_url="/logos/cda.png",
        current_vision="Nederland heeft sterke fundamenten maar we moeten meer investeren in samenhang en solidariteit. Te veel individualisering bedreigt onze sociale cohesie.",
        future_vision="Een samenleving gebaseerd op christelijke waarden: naastenliefde, verantwoordelijkheid en rentmeesterschap. Sterke gemeenschappen en duurzame ontwikkeling.",
        key_policies=[
            "Investeren in gezin en gemeenschap",
            "Duurzame landbouw en klimaatbeleid",
            "Behoud van christelijke waarden in beleid",
            "Sterke sociale zekerheid met eigen verantwoordelijkheid"
        ],
        website_url="https://www.cda.nl"
    ),
    Party(
        id=4,
        name="D66",
        color="#E7007E",
        logo_url="/logos/d66.png",
        current_vision="Nederland heeft veel kansen maar wordt geremd door verouderde structuren. We moeten moderner, democratischer en Europeeser worden.",
        future_vision="Een progressief, open Nederland dat voorop loopt in Europa. Meer directe democratie, gelijke kansen voor iedereen, en ambitieus klimaatbeleid.",
        key_policies=[
            "Democratische vernieuwing en referenda",
            "Ambitieus klimaat- en duurzaamheidsbeleid",
            "Investeren in onderwijs en wetenschap",
            "Pro-Europese koers en internationale samenwerking"
        ],
        website_url="https://www.d66.nl"
    ),
    Party(
        id=5,
        name="GroenLinks-PvdA",
        color="#DC143C",
        logo_url="/logos/glpvda.png",
        current_vision="Nederland is te ongelijk geworden. Grote bedrijven en rijken profiteren, terwijl gewone mensen achteruitgaan. De klimaatcrisis vraagt urgente actie.",
        future_vision="Een eerlijk Nederland waar iedereen mee telt. Sociale zekerheid, goede publieke voorzieningen, en een groene economie die werkt voor iedereen.",
        key_policies=[
            "Hogere belastingen voor rijken en bedrijven",
            "Massale investeringen in groene energie",
            "Sterke publieke sector en sociale zekerheid",
            "Mensenrechten en internationale solidariteit"
        ],
        website_url="https://www.groenlinks.nl"
    )
]


@app.get("/")
async def root():
    return {"message": "Nederland 2029 API", "status": "running"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.get("/api/parties", response_model=List[Party])
async def get_parties():
    return SAMPLE_PARTIES


@app.get("/api/parties/{party_id}", response_model=Party)
async def get_party(party_id: int):
    party = next((p for p in SAMPLE_PARTIES if p.id == party_id), None)
    if party is None:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Party not found")
    return party