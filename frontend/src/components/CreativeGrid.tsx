import { Card, CardContent } from "@/components/ui/card"
import type { Creative, PersonaMatch } from "@/lib/api"

export function CreativeGrid({ creatives, personas }: { creatives: Creative[]; personas: PersonaMatch[] }) {
  const nameByPersonaId = Object.fromEntries(personas.map((p) => [p.persona_id, p.name]))

  return (
    <div className="grid gap-4 sm:grid-cols-2">
      {creatives.map((creative) => (
        <Card key={creative.persona_id}>
          <CardContent className="flex flex-col gap-2.5 p-5">
            <span className="text-[10px] font-medium uppercase tracking-wider text-muted-foreground/70">
              Written for {nameByPersonaId[creative.persona_id] ?? creative.persona_id}
            </span>
            <p className="text-base font-semibold leading-snug text-foreground">{creative.headline}</p>
            <p className="text-sm leading-relaxed text-muted-foreground">{creative.body}</p>
          </CardContent>
        </Card>
      ))}
    </div>
  )
}
