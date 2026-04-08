from keyword_search import keyword_search
from semantic_search import semantic_search

def hybrid_search(df, query):
    # Run both searches
    kw_results = keyword_search(df, query)
    sem_results = semantic_search(df, query)

    # Copy semantic results
    combined = sem_results.copy()

    # Add keyword score (1 if present, else 0)
    combined["keyword_score"] = combined["name"].isin(kw_results["name"]).astype(int)

    # Final score
    combined["final_score"] = (
        0.7 * combined["semantic_score"] +
        0.3 * combined["keyword_score"]
    )

    return combined.sort_values(by="final_score", ascending=False)