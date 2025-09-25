"use client"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Calculator, Menu, Moon, Sun, User } from "lucide-react"
import { useTheme } from "next-themes"

export function Header() {
  const [isMenuOpen, setIsMenuOpen] = useState(false)
  const { theme, setTheme } = useTheme()

  return (
    <header className="border-b bg-card/50 backdrop-blur-sm sticky top-0 z-50">
      <div className="container mx-auto px-4 py-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-2">
            <div className="w-8 h-8 bg-primary rounded-lg flex items-center justify-center">
              <Calculator className="w-5 h-5 text-primary-foreground" />
            </div>
            <h1 className="text-xl font-bold text-foreground">MathMaster</h1>
          </div>

          <nav className="hidden md:flex items-center space-x-6">
            <a href="#topics" className="text-muted-foreground hover:text-foreground transition-colors">
              Temas
            </a>
            <a href="#practice" className="text-muted-foreground hover:text-foreground transition-colors">
              Práctica
            </a>
            <a href="#progress" className="text-muted-foreground hover:text-foreground transition-colors">
              Progreso
            </a>
            <a href="#about" className="text-muted-foreground hover:text-foreground transition-colors">
              Acerca de
            </a>
          </nav>

          <div className="flex items-center space-x-2">
            <Button variant="ghost" size="icon" onClick={() => setTheme(theme === "dark" ? "light" : "dark")}>
              <Sun className="h-4 w-4 rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0" />
              <Moon className="absolute h-4 w-4 rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100" />
            </Button>
            <Button variant="ghost" size="icon">
              <User className="w-4 h-4" />
            </Button>
            <Button variant="ghost" size="icon" className="md:hidden" onClick={() => setIsMenuOpen(!isMenuOpen)}>
              <Menu className="w-4 h-4" />
            </Button>
          </div>
        </div>

        {isMenuOpen && (
          <nav className="md:hidden mt-4 pb-4 border-t pt-4">
            <div className="flex flex-col space-y-2">
              <a href="#topics" className="text-muted-foreground hover:text-foreground transition-colors py-2">
                Temas
              </a>
              <a href="#practice" className="text-muted-foreground hover:text-foreground transition-colors py-2">
                Práctica
              </a>
              <a href="#progress" className="text-muted-foreground hover:text-foreground transition-colors py-2">
                Progreso
              </a>
              <a href="#about" className="text-muted-foreground hover:text-foreground transition-colors py-2">
                Acerca de
              </a>
            </div>
          </nav>
        )}
      </div>
    </header>
  )
}
