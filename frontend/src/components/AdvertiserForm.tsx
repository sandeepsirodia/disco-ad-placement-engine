import { useState } from "react"

import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Textarea } from "@/components/ui/textarea"

type Props = {
  onSubmit: (description: string, budget: number, flightDays: number) => void
  isLoading: boolean
}

const PLACEHOLDER =
  "We sell premium dog food for senior dogs, targeting owners who care about joint health and longevity. Grain-free, vet-formulated, subscription-based."

// Drawn from data/example_advertisers.txt - one clear, one ambiguous, one the
// catalog deliberately can't serve. The landing state otherwise opens on a
// disabled CTA with nothing to click.
const EXAMPLES = [
  {
    label: "Sustainable activewear",
    text: "A sustainable activewear brand for women. Made from recycled ocean plastic. Price point sits between Lululemon and Girlfriend Collective.",
  },
  {
    label: "Cat subscription box",
    text: "A subscription box for new cat owners. First three months of their cat's life. Toys, food samples, a little booklet about what to expect.",
  },
  {
    label: "Vague input",
    text: "We help people feel better.",
  },
  {
    label: "Off-market B2B",
    text: "B2B SaaS for dental practices. We automate their patient recall workflow.",
  },
]

export function AdvertiserForm({ onSubmit, isLoading }: Props) {
  const [description, setDescription] = useState("")
  const [budget, setBudget] = useState(5000)
  const [flightDays, setFlightDays] = useState(14)
  const [touched, setTouched] = useState(false)

  return (
    <form
      className="flex flex-col gap-3"
      onSubmit={(e) => {
        e.preventDefault()
        if (!description.trim()) {
          setTouched(true)
          document.getElementById("description")?.focus()
          return
        }
        onSubmit(description.trim(), budget, flightDays)
      }}
    >
      <label htmlFor="description" className="text-sm font-medium text-foreground">
        Describe your business in a sentence or two
      </label>
      <Textarea
        id="description"
        aria-invalid={touched && !description.trim()}
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        placeholder={PLACEHOLDER}
        rows={3}
        className="resize-none"
      />

      {touched && !description.trim() && (
        <p className="text-xs text-destructive">Add a sentence about your business first.</p>
      )}

      <div className="flex flex-wrap items-center gap-x-4 gap-y-1">
        <span className="text-xs text-muted-foreground/70">Try an example</span>
        {EXAMPLES.map((example) => (
          <button
            key={example.label}
            type="button"
            onClick={() => setDescription(example.text)}
            disabled={isLoading}
            className="rounded-sm text-xs text-muted-foreground underline-offset-4 hover:text-foreground hover:underline focus-visible:outline-none focus-visible:ring-[3px] focus-visible:ring-ring/50 disabled:opacity-50"
          >
            {example.label}
          </button>
        ))}
      </div>

      <div className="flex flex-wrap items-end gap-4">
        <div className="flex flex-col gap-1.5">
          <label htmlFor="budget" className="text-xs text-muted-foreground">
            Total budget ($)
          </label>
          <Input
            id="budget"
            type="number"
            min={100}
            step={100}
            value={budget}
            onChange={(e) => setBudget(Number(e.target.value))}
            className="h-9 w-28"
          />
        </div>
        <div className="flex flex-col gap-1.5">
          <label htmlFor="flight-days" className="text-xs text-muted-foreground">
            Flight (days)
          </label>
          <Input
            id="flight-days"
            type="number"
            min={1}
            max={90}
            value={flightDays}
            onChange={(e) => setFlightDays(Number(e.target.value))}
            className="h-9 w-24"
          />
        </div>
        <Button type="submit" disabled={isLoading} className="ml-auto">
          {isLoading ? "Building campaign…" : "Generate campaign"}
        </Button>
      </div>
    </form>
  )
}
