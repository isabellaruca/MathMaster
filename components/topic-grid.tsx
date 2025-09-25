"use client"

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { Progress } from "@/components/ui/progress"
import { Calculator, Hash, Divide, Zap, BookOpen, Play, CheckCircle, Clock } from "lucide-react"

const topics = [
  {
    id: 1,
    title: "Conjuntos Numéricos",
    description: "Números reales, propiedades de operaciones, teorema fundamental de la aritmética",
    icon: Hash,
    progress: 85,
    status: "completed",
    exercises: 24,
    timeEstimate: "2-3 horas",
  },
  {
    id: 2,
    title: "Números Primos",
    description: "MCM, MCD, criterios de divisibilidad y factorización",
    icon: Calculator,
    progress: 60,
    status: "in-progress",
    exercises: 18,
    timeEstimate: "1-2 horas",
  },
  {
    id: 3,
    title: "Fraccionarios",
    description: "Operaciones con fracciones, simplificación y conversiones",
    icon: Divide,
    progress: 0,
    status: "locked",
    exercises: 20,
    timeEstimate: "2 horas",
  },
  {
    id: 4,
    title: "Potenciación y Radicación",
    description: "Leyes de exponentes, raíces y operaciones con radicales",
    icon: Zap,
    progress: 0,
    status: "locked",
    exercises: 22,
    timeEstimate: "2-3 horas",
  },
]

export function TopicGrid() {
  return (
    <section id="topics">
      <div className="flex items-center justify-between mb-6">
        <h2 className="text-2xl font-bold">Temas de Estudio</h2>
        <Badge variant="secondary">4 temas disponibles</Badge>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {topics.map((topic) => {
          const Icon = topic.icon
          const isLocked = topic.status === "locked"
          const isCompleted = topic.status === "completed"
          const isInProgress = topic.status === "in-progress"

          return (
            <Card
              key={topic.id}
              className={`transition-all hover:shadow-lg ${isLocked ? "opacity-60" : "hover:scale-[1.02]"}`}
            >
              <CardHeader>
                <div className="flex items-start justify-between">
                  <div className="flex items-center space-x-3">
                    <div
                      className={`w-10 h-10 rounded-lg flex items-center justify-center ${
                        isCompleted ? "bg-success/10" : isInProgress ? "bg-primary/10" : "bg-muted"
                      }`}
                    >
                      <Icon
                        className={`w-5 h-5 ${
                          isCompleted ? "text-success" : isInProgress ? "text-primary" : "text-muted-foreground"
                        }`}
                      />
                    </div>
                    <div>
                      <CardTitle className="text-lg">{topic.title}</CardTitle>
                      <div className="flex items-center space-x-2 mt-1">
                        {isCompleted && (
                          <Badge variant="default" className="bg-success text-success-foreground">
                            <CheckCircle className="w-3 h-3 mr-1" />
                            Completado
                          </Badge>
                        )}
                        {isInProgress && (
                          <Badge variant="default">
                            <Play className="w-3 h-3 mr-1" />
                            En progreso
                          </Badge>
                        )}
                        {isLocked && <Badge variant="secondary">Bloqueado</Badge>}
                      </div>
                    </div>
                  </div>
                </div>
                <CardDescription className="text-sm leading-relaxed">{topic.description}</CardDescription>
              </CardHeader>

              <CardContent>
                <div className="space-y-4">
                  <div className="flex items-center justify-between text-sm text-muted-foreground">
                    <div className="flex items-center space-x-1">
                      <BookOpen className="w-4 h-4" />
                      <span>{topic.exercises} ejercicios</span>
                    </div>
                    <div className="flex items-center space-x-1">
                      <Clock className="w-4 h-4" />
                      <span>{topic.timeEstimate}</span>
                    </div>
                  </div>

                  {!isLocked && (
                    <div className="space-y-2">
                      <div className="flex justify-between text-sm">
                        <span>Progreso</span>
                        <span>{topic.progress}%</span>
                      </div>
                      <Progress value={topic.progress} className="h-2" />
                    </div>
                  )}

                  <div className="flex space-x-2">
                    <Button className="flex-1" disabled={isLocked} variant={isCompleted ? "outline" : "default"}>
                      {isCompleted ? "Revisar" : isInProgress ? "Continuar" : "Comenzar"}
                    </Button>
                    {!isLocked && (
                      <Button variant="outline" size="icon">
                        <Play className="w-4 h-4" />
                      </Button>
                    )}
                  </div>
                </div>
              </CardContent>
            </Card>
          )
        })}
      </div>
    </section>
  )
}
