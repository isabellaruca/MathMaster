import { Button } from "@/components/ui/button"
import { Card } from "@/components/ui/card"
import { ArrowRight, BookOpen, Target, TrendingUp } from "lucide-react"

export function Hero() {
  return (
    <section className="text-center py-12">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl md:text-6xl font-bold text-balance mb-6">
          Domina las{" "}
          <span className="bg-gradient-to-r from-primary to-accent bg-clip-text text-transparent">matemáticas</span>{" "}
          paso a paso
        </h1>
        <p className="text-xl text-muted-foreground text-balance mb-8 max-w-2xl mx-auto leading-relaxed">
          Desde aritmética básica hasta ecuaciones diferenciales. Una herramienta completa diseñada para acompañarte
          durante toda tu carrera de ingeniería.
        </p>

        <div className="flex flex-col sm:flex-row gap-4 justify-center mb-12">
          <Button size="lg" className="text-lg px-8">
            Comenzar ahora
            <ArrowRight className="ml-2 w-5 h-5" />
          </Button>
          <Button variant="outline" size="lg" className="text-lg px-8 bg-transparent">
            Ver demo
          </Button>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-16">
          <Card className="p-6 text-center hover:shadow-lg transition-shadow">
            <div className="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center mx-auto mb-4">
              <BookOpen className="w-6 h-6 text-primary" />
            </div>
            <h3 className="font-semibold mb-2">Aprende</h3>
            <p className="text-sm text-muted-foreground">Conceptos explicados paso a paso con ejemplos interactivos</p>
          </Card>

          <Card className="p-6 text-center hover:shadow-lg transition-shadow">
            <div className="w-12 h-12 bg-accent/10 rounded-lg flex items-center justify-center mx-auto mb-4">
              <Target className="w-6 h-6 text-accent" />
            </div>
            <h3 className="font-semibold mb-2">Practica</h3>
            <p className="text-sm text-muted-foreground">Ejercicios infinitos con retroalimentación inmediata</p>
          </Card>

          <Card className="p-6 text-center hover:shadow-lg transition-shadow">
            <div className="w-12 h-12 bg-success/10 rounded-lg flex items-center justify-center mx-auto mb-4">
              <TrendingUp className="w-6 h-6 text-success" />
            </div>
            <h3 className="font-semibold mb-2">Progresa</h3>
            <p className="text-sm text-muted-foreground">Seguimiento detallado de tu avance y logros</p>
          </Card>
        </div>
      </div>
    </section>
  )
}
