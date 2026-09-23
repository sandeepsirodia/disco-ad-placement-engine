import { Badge } from "@/components/ui/badge"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import type { PersonaMatch } from "@/lib/api"

export function PersonaCards({ personas }: { personas: PersonaMatch[] }) {
  return (
    <div className="grid gap-3 sm:grid-cols-2">
      {personas.map((persona) => (
        <Card key={persona.persona_id}>
          <CardHeader className="flex flex-row items-start justify-between gap-2 space-y-0">
            <CardTitle className="text-base">{persona.name}</CardTitle>
            <Badge
              variant={persona.fit_label === "strong" ? "default" : "secondary"}
              className="tabular-nums whitespace-nowrap"
              aria-label={`Fit ${persona.fit_label}, score ${persona.fit_score.toFixed(0)} out of 100`}
            >
              {persona.fit_label} · {persona.fit_score.toFixed(0)}
            </Badge>
          </CardHeader>
          <CardContent>
            <p className="text-sm text-muted-foreground">{persona.reasoning}</p>
          </CardContent>
        </Card>
      ))}
    </div>
  )
}
