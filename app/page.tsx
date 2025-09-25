import { Header } from "@/components/header"
import { Hero } from "@/components/hero"
import { TopicGrid } from "@/components/topic-grid"
import { ProgressOverview } from "@/components/progress-overview"
import { QuickActions } from "@/components/quick-actions"

export default function HomePage() {
  return (
    <div className="min-h-screen bg-background">
      <Header />
      <main className="container mx-auto px-4 py-8">
        <Hero />
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 mt-12">
          <div className="lg:col-span-2">
            <TopicGrid />
          </div>
          <div className="space-y-6">
            <ProgressOverview />
            <QuickActions />
          </div>
        </div>
      </main>
    </div>
  )
}
