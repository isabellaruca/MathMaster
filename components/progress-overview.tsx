import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Progress } from "@/components/ui/progress"
import { Badge } from "@/components/ui/badge"
import { Trophy, Target, Clock, Flame } from "lucide-react"

export function ProgressOverview() {
  return (
    <Card>
      <CardHeader>
        <CardTitle className="flex items-center space-x-2">
          <Trophy className="w-5 h-5 text-accent" />
          <span>Tu Progreso</span>
        </CardTitle>
      </CardHeader>
      <CardContent className="space-y-6">
        <div className="space-y-2">
          <div className="flex justify-between text-sm">
            <span>Progreso General</span>
            <span className="font-medium">36%</span>
          </div>
          <Progress value={36} className="h-3" />
          <p className="text-xs text-muted-foreground">1 de 4 temas completados</p>
        </div>

        <div className="grid grid-cols-2 gap-4">
          <div className="text-center p-3 bg-muted/50 rounded-lg">
            <div className="flex items-center justify-center space-x-1 mb-1">
              <Target className="w-4 h-4 text-primary" />
              <span className="text-2xl font-bold">42</span>
            </div>
            <p className="text-xs text-muted-foreground">Ejercicios resueltos</p>
          </div>

          <div className="text-center p-3 bg-muted/50 rounded-lg">
            <div className="flex items-center justify-center space-x-1 mb-1">
              <Clock className="w-4 h-4 text-accent" />
              <span className="text-2xl font-bold">5.2</span>
            </div>
            <p className="text-xs text-muted-foreground">Horas de estudio</p>
          </div>
        </div>

        <div className="space-y-3">
          <div className="flex items-center justify-between">
            <span className="text-sm font-medium">Racha actual</span>
            <Badge variant="outline" className="bg-accent/10 text-accent border-accent/20">
              <Flame className="w-3 h-3 mr-1" />7 días
            </Badge>
          </div>

          <div className="space-y-2">
            <h4 className="text-sm font-medium">Logros recientes</h4>
            <div className="space-y-1">
              <Badge variant="secondary" className="w-full justify-start">
                🏆 Primer tema completado
              </Badge>
              <Badge variant="secondary" className="w-full justify-start">
                🎯 10 ejercicios seguidos correctos
              </Badge>
            </div>
          </div>
        </div>
      </CardContent>
    </Card>
  )
}
