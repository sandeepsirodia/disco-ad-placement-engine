import type { components } from "@/types/api"

export type CampaignConfig = components["schemas"]["CampaignConfig"]
export type PublisherRecommendation = components["schemas"]["PublisherRecommendation"]
export type ExcludedPublisher = components["schemas"]["ExcludedPublisher"]
export type PersonaMatch = components["schemas"]["PersonaMatch"]
export type Creative = components["schemas"]["Creative"]
export type Viability = components["schemas"]["Viability"]

export async function createCampaign(
  businessDescription: string,
  totalBudgetUsd: number,
  flightDays: number,
): Promise<CampaignConfig> {
  const res = await fetch("/api/campaign", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      business_description: businessDescription,
      total_budget_usd: totalBudgetUsd,
      flight_days: flightDays,
    }),
  })

  if (!res.ok) {
    const body = await res.json().catch(() => null)
    throw new Error(body?.detail ? String(body.detail) : `Request failed (${res.status})`)
  }

  return res.json()
}
