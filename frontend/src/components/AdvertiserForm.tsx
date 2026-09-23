import { useState } from "react"

import { Button } from "@/components/ui/button"
import { Textarea } from "@/components/ui/textarea"

type Props = {
  onSubmit: (description: string, budget: number) => void
  isLoading: boolean
}

const EXAMPLE =
  "We sell premium dog food for senior dogs, targeting owners who care about joint health and longevity. Grain-free, vet-formulated, subscription-based."

export function AdvertiserForm({ onSubmit, isLoading }: Props) {
  const [description, setDescription] = useState("")
  const [budget, setBudget] = useState(5000)

  return (
    <form
      className="flex flex-col gap-3"
      onSubmit={(e) => {
        e.preventDefault()
        if (description.trim()) onSubmit(description.trim(), budget)
      }}
    >
      <label htmlFor="description" className="text-sm font-medium text-foreground">
        Describe your business in a sentence or two
      </label>
      <Textarea
        id="description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        placeholder={EXAMPLE}
        rows={3}
        className="resize-none"
      />
      <div className="flex flex-wrap items-center gap-3">
        <label htmlFor="budget" className="text-sm text-muted-foreground">
          Total budget
        </label>
        <div className="flex items-center gap-1">
          <span className="text-sm text-muted-foreground">$</span>
          <input
            id="budget"
            type="number"
            min={100}
            step={100}
            value={budget}
            onChange={(e) => setBudget(Number(e.target.value))}
            className="w-24 rounded-md border border-input bg-transparent px-2 py-1 text-sm"
          />
        </div>
        <Button type="submit" disabled={isLoading || !description.trim()} className="ml-auto">
          {isLoading ? "Building campaign…" : "Generate campaign"}
        </Button>
      </div>
    </form>
  )
}
