import { useEffect } from 'react'

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

interface PartyModalProps {
  party: Party
  onClose: () => void
}

export const PartyModal = ({ party, onClose }: PartyModalProps) => {
  useEffect(() => {
    const handleEscape = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        onClose()
      }
    }

    document.addEventListener('keydown', handleEscape)
    document.body.style.overflow = 'hidden'

    return () => {
      document.removeEventListener('keydown', handleEscape)
      document.body.style.overflow = 'unset'
    }
  }, [onClose])

  const handleBackdropClick = (e: React.MouseEvent) => {
    if (e.target === e.currentTarget) {
      onClose()
    }
  }

  return (
    <div 
      className="fixed inset-0 bg-black/60 backdrop-blur-sm flex items-center justify-center p-4 z-50 animate-fade-in"
      onClick={handleBackdropClick}
    >
      <div className="bg-white/95 backdrop-blur-lg rounded-3xl max-w-4xl w-full max-h-[90vh] overflow-y-auto animate-slide-up shadow-2xl border border-gray-200/50 scroll-smooth">
        <div className="sticky top-0 bg-white/95 backdrop-blur-lg border-b border-gray-200/50 p-8 rounded-t-3xl z-10">
          <div className="flex items-center justify-between">
            <div className="flex items-center">
              <div className="relative">
                <div 
                  className="w-20 h-20 rounded-2xl flex items-center justify-center text-white font-bold text-2xl mr-6 shadow-lg"
                  style={{ backgroundColor: party.color }}
                >
                  {party.name.substring(0, 2).toUpperCase()}
                </div>
                <div className="absolute -inset-1 opacity-50 blur-sm rounded-2xl" 
                     style={{ backgroundColor: party.color }}></div>
              </div>
              <div>
                <h2 className="text-4xl font-bold text-gray-800 mb-2">
                  {party.name}
                </h2>
                <div className="flex items-center text-gray-600">
                  <div className="w-2 h-2 bg-accent-500 rounded-full mr-2"></div>
                  Nederlandse politieke partij
                </div>
              </div>
            </div>
            <button
              onClick={onClose}
              className="w-12 h-12 rounded-2xl hover:bg-gray-100 flex items-center justify-center transition-all duration-300 group"
            >
              <svg 
                className="w-6 h-6 text-gray-500 group-hover:text-gray-700" 
                fill="none" 
                stroke="currentColor" 
                viewBox="0 0 24 24"
              >
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
        </div>
        
        <div className="p-8 space-y-10">
          <div className="grid md:grid-cols-2 gap-8">
            <div className="space-y-4">
              <div className="flex items-center mb-4">
                <div className="w-3 h-3 bg-accent-400 rounded-full mr-3"></div>
                <h3 className="text-2xl font-bold text-gray-800">
                  Hoe zij Nederland nu zien
                </h3>
              </div>
              <div className="bg-gray-50/80 backdrop-blur-sm rounded-2xl p-6 border border-gray-100">
                <p className="text-gray-700 leading-relaxed text-lg">
                  {party.current_vision}
                </p>
              </div>
            </div>
            
            <div className="space-y-4">
              <div className="flex items-center mb-4">
                <div className="w-3 h-3 bg-accent-500 rounded-full mr-3"></div>
                <h3 className="text-2xl font-bold text-gray-800">
                  Hun visie voor Nederland
                </h3>
              </div>
              <div className="bg-accent-50/80 backdrop-blur-sm rounded-2xl p-6 border border-accent-100">
                <p className="text-gray-700 leading-relaxed text-lg">
                  {party.future_vision}
                </p>
              </div>
            </div>
          </div>
          
          <div>
            <div className="flex items-center mb-6">
              <div className="w-3 h-3 bg-accent-600 rounded-full mr-3"></div>
              <h3 className="text-2xl font-bold text-gray-800">
                Kernstandpunten
              </h3>
            </div>
            <div className="grid gap-4">
              {party.key_policies.map((policy, index) => (
                <div 
                  key={index}
                  className="flex items-start space-x-4 p-6 bg-white/80 backdrop-blur-sm rounded-2xl border border-gray-100 hover:border-gray-200 transition-colors duration-300"
                >
                  <div 
                    className="w-8 h-8 rounded-xl flex items-center justify-center text-white text-sm font-bold flex-shrink-0 shadow-sm"
                    style={{ backgroundColor: party.color }}
                  >
                    {index + 1}
                  </div>
                  <p className="text-gray-700 leading-relaxed text-lg font-medium flex-1">
                    {policy}
                  </p>
                </div>
              ))}
            </div>
          </div>
          
          <div className="flex flex-col md:flex-row items-center justify-between pt-8 border-t border-gray-200 space-y-4 md:space-y-0">
            <div className="text-gray-600 font-medium">
              Meer informatie op hun officiële website
            </div>
            <div className="flex space-x-4">
              <button
                onClick={onClose}
                className="btn-secondary"
              >
                Sluiten
              </button>
              <a
                href={party.website_url}
                target="_blank"
                rel="noopener noreferrer"
                className="btn-primary inline-flex items-center"
              >
                Bezoek website
                <svg 
                  className="w-4 h-4 ml-2" 
                  fill="none" 
                  stroke="currentColor" 
                  viewBox="0 0 24 24"
                >
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                </svg>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}