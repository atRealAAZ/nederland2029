import { useState, useEffect } from 'react'
import { PartyCard } from './components/PartyCard'
import { Header } from './components/Header'
import { PartyModal } from './components/PartyModal'

interface Party {
  id: number
  name: string
  color: string
  logo_url: string
  current_vision: string
  future_vision: string
  key_policies: string[]
  website_url: string
}

function App() {
  const [parties, setParties] = useState<Party[]>([])
  const [selectedParty, setSelectedParty] = useState<Party | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    fetchParties()
  }, [])

  const fetchParties = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/parties')
      if (!response.ok) {
        throw new Error('Failed to fetch parties')
      }
      const data = await response.json()
      setParties(data)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Unknown error')
    } finally {
      setLoading(false)
    }
  }

  const openPartyModal = (party: Party) => {
    setSelectedParty(party)
  }

  const closePartyModal = () => {
    setSelectedParty(null)
  }

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <div className="w-16 h-16 mx-auto mb-6 bg-anthropic-orange rounded-full animate-spin flex items-center justify-center">
            <span className="text-white font-bold text-lg">NL</span>
          </div>
          <div className="text-2xl font-semibold text-gray-700 mb-2">
            Laden van partijen...
          </div>
          <div className="text-gray-500">
            Een moment geduld terwijl we de partijinformatie ophalen
          </div>
        </div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center max-w-md mx-auto p-8">
          <div className="w-20 h-20 mx-auto mb-6 bg-red-500 rounded-full flex items-center justify-center">
            <svg className="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.732-.833-2.5 0L4.268 15.5c-.77.833.192 2.5 1.732 2.5z" />
            </svg>
          </div>
          <div className="text-2xl font-bold text-gray-800 mb-4">
            Er is een fout opgetreden
          </div>
          <div className="text-gray-600 mb-8 leading-relaxed">{error}</div>
          <button 
            onClick={fetchParties}
            className="btn-primary"
          >
            Opnieuw proberen
          </button>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <Header />
      
      <main className="container mx-auto px-6 py-16">
        <div className="text-center mb-16 animate-fade-in">
          <div className="inline-block mb-6">
            <div className="inline-flex items-center px-4 py-2 bg-white border border-gray-200 rounded-full text-sm font-medium text-gray-600 shadow-sm">
              <div className="w-2 h-2 bg-anthropic-orange rounded-full mr-2"></div>
              Tweede Kamerverkiezingen 2025
            </div>
          </div>
          
          <h2 className="text-4xl md:text-5xl font-bold text-gray-800 mb-6 leading-tight">
            Ontdek de Visie van
            <span className="block text-gradient mt-2">Politieke Partijen</span>
          </h2>
          
          <p className="text-xl text-gray-600 max-w-3xl mx-auto leading-relaxed mb-8">
            Elke partij heeft een unieke kijk op hoe Nederland er nu uitziet en waar we naartoe moeten. 
            Ontdek hun verhaal en vind de partij die bij jouw visie past.
          </p>
          
          <div className="flex flex-wrap items-center justify-center gap-6 text-sm text-gray-500">
            <div className="flex items-center">
              <div className="w-2 h-2 bg-green-500 rounded-full mr-2"></div>
              Volledig anoniem
            </div>
            <div className="flex items-center">
              <div className="w-2 h-2 bg-blue-500 rounded-full mr-2"></div>
              Onafhankelijk platform
            </div>
            <div className="flex items-center">
              <div className="w-2 h-2 bg-purple-500 rounded-full mr-2"></div>
              Actuele informatie
            </div>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-6xl mx-auto">
          {parties.map((party, index) => (
            <div 
              key={party.id}
              className="animate-slide-up"
              style={{ animationDelay: `${index * 0.1}s` }}
            >
              <PartyCard 
                party={party} 
                onClick={() => openPartyModal(party)}
              />
            </div>
          ))}
        </div>
      </main>

      {selectedParty && (
        <PartyModal 
          party={selectedParty} 
          onClose={closePartyModal}
        />
      )}
    </div>
  )
}

export default App
