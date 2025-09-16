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

interface PartyCardProps {
  party: Party
  onClick: () => void
}

export const PartyCard = ({ party, onClick }: PartyCardProps) => {
  return (
    <div 
      className="party-card group"
      onClick={onClick}
    >
      <div className="p-6">
        <div className="flex items-center mb-4">
          <div 
            className="w-14 h-14 rounded-xl flex items-center justify-center text-white font-bold text-lg mr-4 shadow-sm"
            style={{ backgroundColor: party.color }}
          >
            {party.name.substring(0, 2).toUpperCase()}
          </div>
          <div className="flex-1">
            <h3 className="text-xl font-bold text-gray-800 group-hover:text-anthropic-orange transition-colors duration-200">
              {party.name}
            </h3>
          </div>
        </div>
        
        <div className="space-y-4">
          <div>
            <h4 className="text-xs font-semibold text-gray-500 mb-2 uppercase tracking-wide">
              Hoe zij Nederland zien
            </h4>
            <p className="text-gray-700 leading-relaxed line-clamp-3">
              {party.current_vision}
            </p>
          </div>
          
          <div>
            <h4 className="text-xs font-semibold text-gray-500 mb-2 uppercase tracking-wide">
              Hun visie voor de toekomst
            </h4>
            <p className="text-gray-700 leading-relaxed line-clamp-3">
              {party.future_vision}
            </p>
          </div>
        </div>
        
        <div className="flex items-center justify-between mt-6 pt-4 border-t border-gray-100">
          <div className="text-sm text-gray-500">
            {party.key_policies.length} kernstandpunten
          </div>
          <div className="text-anthropic-orange font-medium group-hover:text-orange-600 transition-colors duration-200">
            Lees meer →
          </div>
        </div>
      </div>
    </div>
  )
}