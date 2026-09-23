import { Card, CardContent } from "@/components/ui/card"
import type { PersonaMatch } from "@/lib/api"

const LABEL_TONE: Record<string, string> = {
  strong: "text-foreground",
  moderate: "text-muted-foreground",
  weak: "text-muted-foreground/70",
}

export function PersonaCards({ personas }: { personas: PersonaMatch[] }) {
  return (
    <div className="grid gap-4 sm:grid-cols-2">
      {personas.map((persona) => (
        <Card key={persona.persona_id}>
          <CardContent className="flex flex-col gap-3 p-5">
            <div className="flex items-start justify-between gap-4">
              <h3 className="text-base font-semibold leading-tight text-foreground">{persona.name}</h3>
              <div
                className="flex shrink-0 flex-col items-end"
                aria-label={`Fit ${persona.fit_label}, score ${persona.fit_score.toFixed(0)} out of 100`}
              >
                <span className="text-2xl font-semibold leading-none tabular-nums text-foreground">
                  {persona.fit_score.toFixed(0)}
                </span>
                <span
                  className={`text-[10px] font-medium uppercase tracking-wider ${LABEL_TONE[persona.fit_label] ?? "text-muted-foreground/70"}`}
                >
                  {persona.fit_label} fit
                </span>
              </div>
            </div>
            <p className="text-sm leading-relaxed text-muted-foreground">{persona.reasoning}</p>
          </CardContent>
        </Card>
      ))}
    </div>
  )
}
