import type { Viability } from "@/lib/api"

// Semantic status tokens, not raw palette classes: the three campaign states
// are one scale, so they read from one layer and both themes stay in sync.
const STYLES: Record<Viability["status"], string> = {
  ok: "border-success/30 bg-success/10",
  weak: "border-warning/40 bg-warning/10",
  no_match: "border-destructive/40 bg-destructive/10",
}

export function ViabilityBanner({ viability, confidence }: { viability: Viability; confidence: number }) {
  // A confident read of an off-market advertiser and a vague description both
  // land here, so show the confidence number alongside - they need different
  // fixes and the user can't tell them apart from the headline alone.
  return (
    <div className={`rounded-md border px-4 py-3 ${STYLES[viability.status]}`}>
      <div className="flex flex-wrap items-baseline justify-between gap-2">
        <p className="font-semibold">{viability.headline}</p>
        <span className="text-xs tabular-nums text-muted-foreground">
          read confidence {(confidence * 100).toFixed(0)}%
        </span>
      </div>
      <p className="mt-1 text-sm text-muted-foreground">{viability.detail}</p>
    </div>
  )
}
