"use client";
import { useState } from "react";
import Link from "next/link";
import { ArrowRight, ArrowUpRight, Check } from "lucide-react";

export function LearningPreview() {
  const [temperature, setTemperature] = useState(1);
  const scores = [1, 2, 3];
  const weights = scores.map((score) => Math.exp((score - 3) / temperature));
  const total = weights.reduce((sum, weight) => sum + weight, 0);
  const probabilities = weights.map((weight) => weight / total);
  return (
    <section
      className="public-preview"
      aria-labelledby="preview-title"
      id="how-it-works"
    >
      <div className="public-preview-heading">
        <h2 id="preview-title">A small idea. Made tangible.</h2>
        <span>Try this: softmax turns scores into probabilities.</span>
      </div>
      <div className="public-preview-body">
        <div className="public-preview-control">
          <div className="public-step-label">
            <span>1</span> Change an input
          </div>
          <label htmlFor="preview-temperature">
            Temperature{" "}
            <output htmlFor="preview-temperature">
              {temperature.toFixed(1)}
            </output>
          </label>
          <input
            id="preview-temperature"
            type="range"
            min="0.2"
            max="3"
            step="0.1"
            value={temperature}
            onChange={(event) => setTemperature(Number(event.target.value))}
          />
          <div className="public-range-ends">
            <span>More concentrated</span>
            <span>More even</span>
          </div>
          <p>
            The scores stay at <code>[1, 2, 3]</code>. Move the slider to change
            how much the highest score stands out.
          </p>
        </div>
        <div className="public-preview-implementation">
          <div className="public-step-label">
            <span>2</span> Follow the operation
          </div>
          <pre aria-label="Stable softmax in NumPy">
            <code>
              <span className="preview-code-muted">
                # Shift, exponentiate, normalize
              </span>
              {"\n"}
              <span className="preview-code-name">z</span> = (scores -
              scores.max()) /{" "}
              <span className="preview-code-value">
                {temperature.toFixed(1)}
              </span>
              {"\n"}
              <span className="preview-code-name">weights</span> = np.exp(z)
              {"\n"}
              <span className="preview-code-name">p</span> = weights /
              weights.sum()
            </code>
          </pre>
          <Link href="/problems/stable-softmax/">
            Implement it yourself <ArrowRight size={14} />
          </Link>
        </div>
        <div className="public-preview-result">
          <div className="public-step-label">
            <span>3</span> Inspect the result
          </div>
          <div
            className="public-probabilities"
            role="img"
            aria-label={`Probabilities: ${probabilities.map((probability) => `${(probability * 100).toFixed(1)} percent`).join(", ")}`}
          >
            {probabilities.map((probability, index) => (
              <div className="public-probability" key={index}>
                <span>{scores[index]}</span>
                <div className="public-probability-track">
                  <i style={{ width: `${probability * 100}%` }} />
                </div>
                <output>{(probability * 100).toFixed(1)}%</output>
              </div>
            ))}
          </div>
          <p className="public-probability-sum">
            <Check size={14} /> Probabilities add up to 1
          </p>
        </div>
      </div>
      <div className="public-preview-caption">
        <span>
          {temperature < 1
            ? "Lower temperature puts more weight on the highest score."
            : temperature > 1
              ? "Higher temperature spreads the probability more evenly."
              : "At temperature 1, a score of 3 receives about 67% of the probability."}
        </span>
        <Link href="/explore/">
          Explore the open lab <ArrowUpRight size={14} />
        </Link>
      </div>
    </section>
  );
}
