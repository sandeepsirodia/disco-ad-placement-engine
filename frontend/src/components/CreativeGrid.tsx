import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import type { Creative, PersonaMatch } from "@/lib/api"

export function CreativeGrid({ creatives, personas }: { creatives: Creative[]; personas: PersonaMatch[] }) {
  const nameByPersonaId = Object.fromEntries(personas.map((p) => [p.persona_id, p.name]))

  return (
    <div className="grid gap-3 sm:grid-cols-2">
      {creatives.map((creative) => (
        <Card key={creative.persona_id}>
          <CardHeader>
            <CardTitle className="text-xs font-medium uppercase tracking-wide text-muted-foreground">
              {nameByPersonaId[creative.persona_id] ?? creative.persona_id}
            </CardTitle>
          </CardHeader>
          <CardContent className="flex flex-col gap-1.5">
            <p className="font-semibold leading-snug">{creative.headline}</p>
            <p className="text-sm text-muted-foreground">{creative.body}</p>
          </CardContent>
        </Card>
      ))}
    </div>
  )
}
