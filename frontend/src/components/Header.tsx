export const Header = () => {
  const scrollToSection = (sectionId: string) => {
    const element = document.getElementById(sectionId)
    if (element) {
      element.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      })
    }
  }

  return (
    <header className="bg-white shadow-sm border-b border-gray-200">
      <div className="container mx-auto px-6 py-6">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-4">
            <img 
              src="/NL25.png" 
              alt="Nederland 2025 Logo" 
              className="w-12 h-12 rounded-xl shadow-md"
            />
            <div>
              <h1 className="text-2xl font-bold text-gradient">
                Nederland 2025
              </h1>
              <p className="text-gray-600 text-sm">
                Jouw gids voor de Tweede Kamerverkiezingen
              </p>
            </div>
          </div>
          
          <div className="hidden md:flex items-center space-x-6">
            <nav className="flex space-x-6">
              <button 
                onClick={() => scrollToSection('partijen')}
                className="text-gray-600 hover:text-anthropic-orange font-medium transition-colors duration-200"
              >
                Partijen
              </button>
              <button 
                onClick={() => scrollToSection('over')}
                className="text-gray-600 hover:text-anthropic-orange font-medium transition-colors duration-200"
              >
                Over
              </button>
            </nav>
          </div>
        </div>
      </div>
    </header>
  )
}