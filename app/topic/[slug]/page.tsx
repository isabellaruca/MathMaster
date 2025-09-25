"use client"

import { useState } from "react"
import { useParams } from "next/navigation"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Badge } from "@/components/ui/badge"
import { Progress } from "@/components/ui/progress"
import { ArrowLeft, CheckCircle, XCircle, RefreshCw, Lightbulb, Target, Clock } from "lucide-react"
import Link from "next/link"

// Simulación de datos de ejercicios
const topicData = {
  "conjuntos-numericos": {
    title: "Conjuntos Numéricos",
    description: "Números reales, propiedades de operaciones, teorema fundamental de la aritmética",
    exercises: [
      {
        id: "cn_1001",
        question: "Clasifica el número -5 según los conjuntos numéricos (N, Z, Q, I, R)",
        type: "multiple-choice",
        options: ["Natural", "Entero", "Racional", "Irracional", "Real"],
        correctAnswer: ["Entero", "Racional", "Real"],
        explanation: "-5 es un número entero (Z), racional (Q) y real (R), pero no natural (N) ni irracional (I).",
      },
      {
        id: "cn_1002",
        question: "Aplica la propiedad distributiva: 3(4 + 7) = ?",
        type: "input",
        correctAnswer: "33",
        explanation: "3(4 + 7) = 3×4 + 3×7 = 12 + 21 = 33",
      },
    ],
  },
  "numeros-primos": {
    title: "Números Primos",
    description: "MCM, MCD, criterios de divisibilidad y factorización",
    exercises: [
      {
        id: "np_1001",
        question: "¿Es 17 un número primo?",
        type: "boolean",
        correctAnswer: true,
        explanation: "17 es primo porque solo es divisible por 1 y por sí mismo.",
      },
      {
        id: "np_1002",
        question: "Calcula el MCD de 24 y 36",
        type: "input",
        correctAnswer: "12",
        explanation: "MCD(24, 36) = 12",
      },
    ],
  },
}

export default function TopicPage() {
  const params = useParams()
  const slug = params.slug as string
  const [currentExercise, setCurrentExercise] = useState(0)
  const [userAnswer, setUserAnswer] = useState("")
  const [selectedOptions, setSelectedOptions] = useState<string[]>([])
  const [showResult, setShowResult] = useState(false)
  const [isCorrect, setIsCorrect] = useState(false)
  const [score, setScore] = useState(0)
  const [attempts, setAttempts] = useState(0)

  const topic = topicData[slug as keyof typeof topicData]

  if (!topic) {
    return (
      <div className="container mx-auto px-4 py-8">
        <div className="text-center">
          <h1 className="text-2xl font-bold mb-4">Tema no encontrado</h1>
          <Link href="/">
            <Button>Volver al inicio</Button>
          </Link>
        </div>
      </div>
    )
  }

  const exercise = topic.exercises[currentExercise]
  const progress = ((currentExercise + 1) / topic.exercises.length) * 100

  const handleSubmit = () => {
    setAttempts(attempts + 1)
    let correct = false

    if (exercise.type === "input") {
      correct = userAnswer.trim() === exercise.correctAnswer
    } else if (exercise.type === "boolean") {
      correct = (userAnswer === "true") === exercise.correctAnswer
    } else if (exercise.type === "multiple-choice") {
      const correctSet = new Set(exercise.correctAnswer)
      const userSet = new Set(selectedOptions)
      correct = correctSet.size === userSet.size && [...correctSet].every((x) => userSet.has(x))
    }

    setIsCorrect(correct)
    setShowResult(true)

    if (correct) {
      setScore(score + 1)
    }
  }

  const nextExercise = () => {
    if (currentExercise < topic.exercises.length - 1) {
      setCurrentExercise(currentExercise + 1)
      resetExercise()
    }
  }

  const resetExercise = () => {
    setUserAnswer("")
    setSelectedOptions([])
    setShowResult(false)
    setIsCorrect(false)
  }

  const handleOptionToggle = (option: string) => {
    setSelectedOptions((prev) => (prev.includes(option) ? prev.filter((o) => o !== option) : [...prev, option]))
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <div className="flex items-center justify-between mb-8">
          <Link href="/">
            <Button variant="ghost" size="sm">
              <ArrowLeft className="w-4 h-4 mr-2" />
              Volver
            </Button>
          </Link>
          <div className="text-center">
            <h1 className="text-2xl font-bold">{topic.title}</h1>
            <p className="text-muted-foreground">{topic.description}</p>
          </div>
          <div className="text-right">
            <Badge variant="outline">
              {currentExercise + 1} de {topic.exercises.length}
            </Badge>
          </div>
        </div>

        {/* Progress */}
        <div className="mb-8">
          <div className="flex justify-between text-sm mb-2">
            <span>Progreso del tema</span>
            <span>{Math.round(progress)}%</span>
          </div>
          <Progress value={progress} className="h-2" />
        </div>

        {/* Exercise Card */}
        <Card className="mb-8">
          <CardHeader>
            <div className="flex items-center justify-between">
              <CardTitle className="flex items-center space-x-2">
                <Target className="w-5 h-5 text-primary" />
                <span>Ejercicio {currentExercise + 1}</span>
              </CardTitle>
              <div className="flex items-center space-x-2 text-sm text-muted-foreground">
                <Clock className="w-4 h-4" />
                <span>2-3 min</span>
              </div>
            </div>
            <CardDescription className="text-lg font-medium text-foreground">{exercise.question}</CardDescription>
          </CardHeader>

          <CardContent className="space-y-6">
            {/* Answer Input */}
            {exercise.type === "input" && (
              <div className="space-y-2">
                <label className="text-sm font-medium">Tu respuesta:</label>
                <Input
                  value={userAnswer}
                  onChange={(e) => setUserAnswer(e.target.value)}
                  placeholder="Escribe tu respuesta aquí..."
                  disabled={showResult}
                  className="text-lg"
                />
              </div>
            )}

            {exercise.type === "boolean" && (
              <div className="space-y-3">
                <label className="text-sm font-medium">Selecciona tu respuesta:</label>
                <div className="flex space-x-4">
                  <Button
                    variant={userAnswer === "true" ? "default" : "outline"}
                    onClick={() => setUserAnswer("true")}
                    disabled={showResult}
                  >
                    Verdadero
                  </Button>
                  <Button
                    variant={userAnswer === "false" ? "default" : "outline"}
                    onClick={() => setUserAnswer("false")}
                    disabled={showResult}
                  >
                    Falso
                  </Button>
                </div>
              </div>
            )}

            {exercise.type === "multiple-choice" && (
              <div className="space-y-3">
                <label className="text-sm font-medium">Selecciona todas las opciones correctas:</label>
                <div className="grid grid-cols-2 gap-3">
                  {exercise.options?.map((option) => (
                    <Button
                      key={option}
                      variant={selectedOptions.includes(option) ? "default" : "outline"}
                      onClick={() => handleOptionToggle(option)}
                      disabled={showResult}
                      className="justify-start"
                    >
                      {option}
                    </Button>
                  ))}
                </div>
              </div>
            )}

            {/* Result */}
            {showResult && (
              <div
                className={`p-4 rounded-lg border ${
                  isCorrect
                    ? "bg-success/10 border-success/20 text-success"
                    : "bg-destructive/10 border-destructive/20 text-destructive"
                }`}
              >
                <div className="flex items-center space-x-2 mb-2">
                  {isCorrect ? <CheckCircle className="w-5 h-5" /> : <XCircle className="w-5 h-5" />}
                  <span className="font-medium">{isCorrect ? "¡Correcto!" : "Incorrecto"}</span>
                </div>
                <div className="flex items-start space-x-2">
                  <Lightbulb className="w-4 h-4 mt-0.5 flex-shrink-0" />
                  <p className="text-sm">{exercise.explanation}</p>
                </div>
              </div>
            )}

            {/* Actions */}
            <div className="flex justify-between">
              <Button variant="outline" onClick={resetExercise} disabled={!showResult}>
                <RefreshCw className="w-4 h-4 mr-2" />
                Reintentar
              </Button>

              {!showResult ? (
                <Button
                  onClick={handleSubmit}
                  disabled={
                    (exercise.type === "input" && !userAnswer.trim()) ||
                    (exercise.type === "boolean" && !userAnswer) ||
                    (exercise.type === "multiple-choice" && selectedOptions.length === 0)
                  }
                >
                  Verificar respuesta
                </Button>
              ) : (
                <Button onClick={nextExercise} disabled={currentExercise >= topic.exercises.length - 1}>
                  Siguiente ejercicio
                </Button>
              )}
            </div>
          </CardContent>
        </Card>

        {/* Stats */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <Card className="text-center p-4">
            <div className="text-2xl font-bold text-primary">{score}</div>
            <div className="text-sm text-muted-foreground">Correctas</div>
          </Card>
          <Card className="text-center p-4">
            <div className="text-2xl font-bold text-accent">{attempts}</div>
            <div className="text-sm text-muted-foreground">Intentos</div>
          </Card>
          <Card className="text-center p-4">
            <div className="text-2xl font-bold text-success">
              {attempts > 0 ? Math.round((score / attempts) * 100) : 0}%
            </div>
            <div className="text-sm text-muted-foreground">Precisión</div>
          </Card>
        </div>
      </div>
    </div>
  )
}
