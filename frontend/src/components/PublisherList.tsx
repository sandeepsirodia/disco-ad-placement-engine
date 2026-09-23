import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion"
import { Card, CardContent } from "@/components/ui/card"
import { Progress } from "@/components/ui/progress"
import { Separator } from "@/components/ui/separator"
import type { ExcludedPublisher, PublisherRecommendation } from "@/lib/api"

const BREAKDOWN_LABELS: Record<string, string> = {
  category_fit: "Category fit",
  price_fit: "Price fit",
  audience_fit: "Audience fit",
  tone_fit: "Tone fit",
}

/** Tiny uppercase label above a value - the label recedes on colour, the value
 *  carries weight. Hierarchy from weight + colour rather than size, so the
 *  numbers stay legible instead of shrinking. */
function Metric({ label, value, muted = false }: { label: string; value: string; muted?: boolean }) {
  return (
    <div className="flex flex-col gap-0.5">
      <span className="text-[10px] font-medium uppercase tracking-wider text-muted-foreground/70">{label}</span>
      <span
        className={`whitespace-nowrap text-sm tabular-nums ${muted ? "font-normal text-muted-foreground" : "font-medium text-foreground"}`}
      >
        {value}
      </span>
    </div>
  )
}

function ScoreBreakdown({ breakdown }: { breakdown: Record<string, number> }) {
  return (
    <div className="flex flex-col gap-2 pt-1">
      {Object.entries(breakdown).map(([key, value]) => (
        <div key={key} className="grid grid-cols-[92px_1fr_32px] items-center gap-3 text-xs">
          <span className="text-muted-foreground">{BREAKDOWN_LABELS[key] ?? key}</span>
          <Progress value={value} className="h-1" />
          <span className="text-right font-medium tabular-nums text-foreground">{value.toFixed(0)}</span>
        </div>
      ))}
    </div>
  )
}

export function PublisherList({
  recommended,
  excluded,
}: {
  recommended: PublisherRecommendation[]
  excluded: ExcludedPublisher[]
}) {
  return (
    <div className="flex flex-col gap-5">
      <div className="grid gap-4 sm:grid-cols-2">
        {recommended.map((pub, i) => {
          const unfunded = pub.budget_allocation_usd === 0
          return (
            <Card key={pub.publisher_id} className="overflow-hidden">
              <CardContent className="flex flex-col gap-4 p-5">
                {/* Anchor row: the score is the point of this card, so it gets
                    the largest, heaviest treatment on the page. */}
                <div className="flex items-start justify-between gap-4">
                  <div className="flex min-w-0 flex-col gap-0.5">
                    <span className="text-[10px] font-medium uppercase tracking-wider text-muted-foreground/70">
                      Rank {i + 1}
                    </span>
                    <h3 className="truncate text-base font-semibold leading-tight text-foreground">{pub.name}</h3>
                  </div>
                  <div
                    className="flex shrink-0 flex-col items-end"
                    aria-label={`Match score ${pub.match_score.toFixed(0)} out of 100`}
                  >
                    <span className="text-2xl font-semibold leading-none tabular-nums text-foreground">
                      {pub.match_score.toFixed(0)}
                    </span>
                    <span className="text-[10px] font-medium uppercase tracking-wider text-muted-foreground/70">
                      match
                    </span>
                  </div>
                </div>

                <p className="text-sm leading-relaxed text-muted-foreground">{pub.reasoning}</p>

                <Separator />

                <div className="grid grid-cols-3 gap-4">
                  <Metric
                    label="Budget"
                    muted={unfunded}
                    value={
                      unfunded
                        ? "Not funded"
                        : `$${pub.budget_allocation_usd.toLocaleString()} · ${pub.budget_allocation_pct.toFixed(0)}%`
                    }
                  />
                  <Metric
                    label={`Bid (${pub.suggested_bid_model})`}
                    // Second "$" dropped: the range wrapped to two lines at
                    // card width, and the unit is already established.
                    value={`$${pub.suggested_bid_range[0]}–${pub.suggested_bid_range[1]}`}
                  />
                  <Metric
                    label="Inventory used"
                    value={`${pub.inventory_share_pct.toFixed(1)}% of ${(pub.monthly_impressions / 1_000_000).toFixed(1)}M`}
                  />
                </div>

                <Accordion type="single" collapsible>
                  <AccordionItem value="breakdown" className="border-none">
                    <AccordionTrigger className="py-0 text-xs text-muted-foreground hover:text-foreground">
                      Score breakdown
                    </AccordionTrigger>
                    <AccordionContent className="pb-0">
                      <ScoreBreakdown breakdown={pub.breakdown} />
                    </AccordionContent>
                  </AccordionItem>
                </Accordion>
              </CardContent>
            </Card>
          )
        })}
      </div>

      {excluded.length > 0 && (
        <Accordion type="single" collapsible>
          <AccordionItem value="excluded">
            <AccordionTrigger className="text-sm">
              {excluded.length} publisher{excluded.length === 1 ? "" : "s"} excluded
            </AccordionTrigger>
            <AccordionContent>
              <ul className="flex flex-col divide-y">
                {excluded.map((pub) => (
                  <li key={pub.publisher_id} className="grid grid-cols-[130px_40px_1fr] items-start gap-3 py-2.5">
                    <span className="truncate text-sm font-medium text-foreground">{pub.name}</span>
                    <span className="text-right text-sm tabular-nums text-muted-foreground">
                      {pub.score.toFixed(0)}
                    </span>
                    <span className="text-sm leading-relaxed text-muted-foreground">{pub.reason}</span>
                  </li>
                ))}
              </ul>
            </AccordionContent>
          </AccordionItem>
        </Accordion>
      )}
    </div>
  )
}
