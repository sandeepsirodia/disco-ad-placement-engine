import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion"
import { Card, CardContent } from "@/components/ui/card"
import { Separator } from "@/components/ui/separator"
import type { CampaignConfig } from "@/lib/api"

function Field({ label, value }: { label: string; value: string }) {
  return (
    <div className="flex flex-col gap-0.5">
      <span className="text-xs uppercase tracking-wide text-muted-foreground">{label}</span>
      <span className="text-sm font-medium tabular-nums">{value}</span>
    </div>
  )
}

export function CampaignConfigView({ config }: { config: CampaignConfig }) {
  const { targeting, budget, bid_strategy } = config

  return (
    <Card>
      <CardContent className="flex flex-col gap-4 pt-6">
        <div className="grid grid-cols-2 gap-4 sm:grid-cols-4">
          <Field
            label="Age range"
            value={targeting.age_range ? `${targeting.age_range[0]}–${targeting.age_range[1]}` : "Broad"}
          />
          <Field label="Gender lean" value={targeting.gender_lean ?? "None"} />
          <Field label="Geos" value={targeting.geos.join(", ") || "—"} />
          <Field label="Income tiers" value={targeting.income_tiers.join(", ") || "—"} />
        </div>
        <Separator />
        <div className="grid grid-cols-2 gap-4 sm:grid-cols-4">
          <Field label="Total budget" value={`$${budget.total_usd.toLocaleString()}`} />
          <Field label="Daily budget" value={`$${budget.daily_usd.toLocaleString()}`} />
          <Field label="Flight" value={`${budget.flight_days} days`} />
          <Field label="Bid strategy" value={bid_strategy.model} />
        </div>
        <p className="text-sm text-muted-foreground">{bid_strategy.rationale}</p>

        <Accordion type="single" collapsible>
          <AccordionItem value="raw" className="border-none">
            <AccordionTrigger className="text-xs">View raw campaign config (JSON)</AccordionTrigger>
            <AccordionContent>
              <pre className="max-h-96 overflow-auto rounded-md bg-muted p-3 text-xs">
                {JSON.stringify(config, null, 2)}
              </pre>
            </AccordionContent>
          </AccordionItem>
        </Accordion>
      </CardContent>
    </Card>
  )
}
