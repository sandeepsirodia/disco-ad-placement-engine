import { useEffect, useState } from "react"

import { Progress } from "@/components/ui/progress"

// The pipeline's real stages (backend/app/pipeline.py). Offsets are where each
// one typically starts within a ~25s run, measured across the 15 eval
// advertisers - not a live feed, so the copy says "typically" rather than
// claiming to know where the request actually is.
const STAGES = [
  { at: 0, label: "Reading your description" },
  { at: 6, label: "Scoring 20 publishers and 10 personas" },
  { at: 10, label: "Writing reasoning and ad creative" },
  { at: 22, label: "Assembling the campaign" },
] as const

const EXPECTED_SECONDS = 25

export function CampaignProgress() {
  const [elapsed, setElapsed] = useState(0)

  useEffect(() => {
    const started = Date.now()
    const id = setInterval(() => setElapsed((Date.now() - started) / 1000), 250)
    return () => clearInterval(id)
  }, [])

  const activeIndex = STAGES.reduce((acc, stage, i) => (elapsed >= stage.at ? i : acc), 0)
  // Ease toward 95% rather than hitting 100 before the response lands - a bar
  // that sits full while the user still waits is worse than no bar.
  const percent = Math.min(95, (elapsed / EXPECTED_SECONDS) * 95)

  return (
    <div className="flex flex-col gap-3 rounded-lg border p-4" role="status" aria-live="polite">
      <div className="flex items-baseline justify-between gap-3">
        <p className="text-sm font-medium">{STAGES[activeIndex].label}…</p>
        <span className="text-xs tabular-nums text-muted-foreground">
          {elapsed.toFixed(0)}s elapsed · typically ~{EXPECTED_SECONDS}s
        </span>
      </div>

      <Progress value={percent} className="h-1.5" />

      <ol className="flex flex-col gap-1.5">
        {STAGES.map((stage, i) => (
          <li
            key={stage.label}
            className={`flex items-center gap-2 text-xs ${
              i < activeIndex
                ? "text-muted-foreground line-through decoration-muted-foreground/40"
                : i === activeIndex
                  ? "text-foreground"
                  : "text-muted-foreground/60"
            }`}
          >
            <span
              aria-hidden
              className={`size-1.5 rounded-full ${
                i <= activeIndex ? "bg-foreground" : "bg-muted-foreground/30"
              }`}
            />
            {stage.label}
          </li>
        ))}
      </ol>
    </div>
  )
}
