import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Calculator, BookOpen, PenTool, BarChart3, Zap, HelpCircle } from "lucide-react"

export function QuickActions() {
  return (
    <Card>
      <CardHeader>
        <CardTitle className="flex items-center space-x-2">
          <Zap className="w-5 h-5 text-primary" />
          <span>Acciones Rápidas</span>
        </CardTitle>
      </CardHeader>
      <CardContent className="space-y-3">
        <Button variant="outline" className="w-full justify-start bg-transparent">
          <Calculator className="w-4 h-4 mr-2" />
          Calculadora avanzada
        </Button>

        <Button variant="outline" className="w-full justify-start bg-transparent">
          <PenTool className="w-4 h-4 mr-2" />
          Práctica rápida
        </Button>

        <Button variant="outline" className="w-full justify-start bg-transparent">
          <BookOpen className="w-4 h-4 mr-2" />
          Formulario matemático
        </Button>

        <Button variant="outline" className="w-full justify-start bg-transparent">
          <BarChart3 className="w-4 h-4 mr-2" />
          Estadísticas detalladas
        </Button>

        <Button variant="outline" className="w-full justify-start bg-transparent">
          <HelpCircle className="w-4 h-4 mr-2" />
          Ayuda y tutoriales
        </Button>
      </CardContent>
    </Card>
  )
}
