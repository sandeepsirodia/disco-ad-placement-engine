import { useState } from "react"

import { AdvertiserForm } from "@/components/AdvertiserForm"
import { CampaignConfigView } from "@/components/CampaignConfigView"
import { CampaignProgress } from "@/components/CampaignProgress"
import { CreativeGrid } from "@/components/CreativeGrid"
import { PersonaCards } from "@/components/PersonaCards"
import { PublisherList } from "@/components/PublisherList"
import { ViabilityBanner } from "@/components/ViabilityBanner"
import { type CampaignConfig, createCampaign } from "@/lib/api"

function Section({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <section className="flex flex-col gap-3">
      <h2 className="text-lg font-semibold">{title}</h2>
      {children}
    </section>
  )
}

export default function App() {
  const [campaign, setCampaign] = useState<CampaignConfig | null>(null)
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  async function handleSubmit(description: string, budget: number, flightDays: number) {
    setIsLoading(true)
    setError(null)
    try {
      const result = await createCampaign(description, budget, flightDays)
      setCampaign(result)
    } catch (e) {
      setError(e instanceof Error ? e.message : "Something went wrong.")
      setCampaign(null)
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="mx-auto flex max-w-3xl flex-col gap-8 px-4 py-10">
      <header className="flex flex-col gap-1">
        <h1 className="text-2xl font-bold">Ad Placement Engine</h1>
        <p className="text-sm text-muted-foreground">
          Describe an advertiser. Get ranked publishers, persona-tuned creative, and a draft campaign config —
          every number traceable.
        </p>
      </header>

      <AdvertiserForm onSubmit={handleSubmit} isLoading={isLoading} />

      {error && (
        <div className="rounded-md border border-destructive/30 bg-destructive/10 px-4 py-3 text-sm text-destructive">
          {error}
        </div>
      )}

      {isLoading && <CampaignProgress />}

      {campaign && !isLoading && (
        <div className="flex flex-col gap-10">
          <ViabilityBanner viability={campaign.viability} confidence={campaign.advertiser.confidence} />

          <Section
            title={
              campaign.viability.status === "no_match"
                ? "Publisher ranking (reference only)"
                : "Recommended publishers"
            }
          >
            <PublisherList recommended={campaign.publishers} excluded={campaign.excluded_publishers} />
          </Section>

          <Section title="Shopper personas">
            <PersonaCards personas={campaign.personas} />
          </Section>

          <Section
            title={
              campaign.viability.status === "no_match" ? "Ad creative (not recommended to run)" : "Ad creative"
            }
          >
            <CreativeGrid creatives={campaign.creatives} personas={campaign.personas} />
          </Section>

          <Section title="Campaign config">
            <CampaignConfigView config={campaign} />
          </Section>
        </div>
      )}
    </div>
  )
}
