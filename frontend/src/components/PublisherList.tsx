import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion"
import { Badge } from "@/components/ui/badge"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Progress } from "@/components/ui/progress"
import type { ExcludedPublisher, PublisherRecommendation } from "@/lib/api"

const BREAKDOWN_LABELS: Record<string, string> = {
  category_fit: "Category fit",
  price_fit: "Price fit",
  audience_fit: "Audience fit",
  tone_fit: "Tone fit",
}

function ScoreBreakdown({ breakdown }: { breakdown: Record<string, number> }) {
  return (
    <div className="flex flex-col gap-2">
      {Object.entries(breakdown).map(([key, value]) => (
        <div key={key} className="grid grid-cols-[100px_1fr_36px] items-center gap-2 text-xs">
          <span className="text-muted-foreground">{BREAKDOWN_LABELS[key] ?? key}</span>
          <Progress value={value} className="h-1.5" />
          <span className="text-right tabular-nums text-muted-foreground">{value.toFixed(0)}</span>
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
    <div className="flex flex-col gap-4">
      <div className="grid gap-3 sm:grid-cols-2">
        {recommended.map((pub) => (
          <Card key={pub.publisher_id}>
            <CardHeader className="flex flex-row items-start justify-between gap-2 space-y-0">
              <CardTitle className="text-base">{pub.name}</CardTitle>
              <Badge
                variant="secondary"
                className="tabular-nums"
                aria-label={`Match score ${pub.match_score.toFixed(0)} out of 100`}
              >
                {pub.match_score.toFixed(0)}
              </Badge>
            </CardHeader>
            <CardContent className="flex flex-col gap-3">
              <p className="text-sm text-muted-foreground">{pub.reasoning}</p>
              <div className="flex flex-wrap items-center gap-x-3 gap-y-1 text-xs text-muted-foreground">
                <span className={pub.budget_allocation_usd === 0 ? "text-destructive" : undefined}>
                  {pub.budget_allocation_usd === 0
                    ? "no spend allocated"
                    : `$${pub.budget_allocation_usd.toLocaleString()} (${pub.budget_allocation_pct.toFixed(0)}%)`}
                </span>
                <span>·</span>
                <span>
                  {pub.suggested_bid_model} ${pub.suggested_bid_range[0]}&ndash;${pub.suggested_bid_range[1]}
                </span>
                <span>·</span>
                <span title="Share of this publisher's monthly impressions this spend would consume">
                  {(pub.monthly_impressions / 1_000_000).toFixed(1)}M/mo reach, using{" "}
                  {pub.inventory_share_pct.toFixed(1)}%
                </span>
              </div>
              <Accordion type="single" collapsible>
                <AccordionItem value="breakdown" className="border-none">
                  <AccordionTrigger className="py-1 text-xs">Score breakdown</AccordionTrigger>
                  <AccordionContent>
                    <ScoreBreakdown breakdown={pub.breakdown} />
                  </AccordionContent>
                </AccordionItem>
              </Accordion>
            </CardContent>
          </Card>
        ))}
      </div>

      {excluded.length > 0 && (
        <Accordion type="single" collapsible>
          <AccordionItem value="excluded">
            <AccordionTrigger className="text-sm">
              {excluded.length} publisher{excluded.length === 1 ? "" : "s"} excluded
            </AccordionTrigger>
            <AccordionContent>
              <ul className="flex flex-col gap-2">
                {excluded.map((pub) => (
                  <li key={pub.publisher_id} className="flex items-start justify-between gap-3 text-sm">
                    <span className="font-medium">{pub.name}</span>
                    <span className="text-right text-muted-foreground">{pub.reason}</span>
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
