export const Header = () => {
  return (
    <header className="bg-white shadow-sm border-b border-gray-200">
      <div className="container mx-auto px-6 py-6">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-4">
            <div className="w-12 h-12 bg-anthropic-orange rounded-xl flex items-center justify-center shadow-md">
              <span className="text-white font-bold text-lg">NL</span>
            </div>
            <div>
              <h1 className="text-2xl font-bold text-gradient">
                Nederland 2029
              </h1>
              <p className="text-gray-600 text-sm">
                Jouw gids voor de Tweede Kamerverkiezingen
              </p>
            </div>
          </div>
          
          <div className="hidden md:flex items-center space-x-6">
            <nav className="flex space-x-6">
              <a 
                href="#partijen" 
                className="text-gray-600 hover:text-anthropic-orange font-medium transition-colors duration-200"
              >
                Partijen
              </a>
              <a 
                href="#over" 
                className="text-gray-600 hover:text-anthropic-orange font-medium transition-colors duration-200"
              >
                Over
              </a>
            </nav>
          </div>
        </div>
      </div>
    </header>
  )
}