import json

def JsonSelctor(domain):
    # Your mapping of dropdown values to file names
    domain_file_map = {
        "Machine Learning": "machine_learning.json",
        "Java Full Stack": "java_full_stack.json",
        "Python Backend": "python_backend.json",
        "Data Science": "data_science.json",
        "C/C++ Systems": "c_cpp_systems.json",
        "DevOps & Cloud": "devops_cloud.json",
        "Frontend Development": "frontend_development.json",
        "LLM & Generative AI": "llm_generative_ai.json",
        "MLOps Engineering": "mlops_engineering.json",
        "Advanced Computer Vision": "computer_vision_advanced.json",
        "Natural Language Processing": "natural_language_processing.json",
        "Edge AI & TinyML": "edge_ai_tinyml.json",
        "Reinforcement Learning": "reinforcement_learning.json",
        "AI Trust, Safety & Ethics": "ai_trust_safety_ethics.json"
    }

    # Clean up the string just in case there are trailing spaces from the selectbox
    domain = domain.strip() if domain else None
    json_file_path = domain_file_map.get(domain)

    if json_file_path:
        try:
            with open(json_file_path, 'r') as file:
                domain_data = json.load(file)
                # CRITICAL ADDITION: Return the data so the main app can use it
                return domain_data 
        except FileNotFoundError:
            print(f"Error: Could not find {json_file_path} in the directory.")
            return None
    else:
        print("Error: Domain not found in the mapping.")
        return None
        
      
def ScoreCalculator(resume_chunks, domain_data):
    """
    Takes the chunked resume text and the loaded JSON dictionary to calculate the ATS score.
    """
    if not domain_data or not resume_chunks:
        return None

    # Join the chunks back together into one lowercase string for easy keyword matching
    resume_text = " ".join(resume_chunks).lower()

    keywords_dict = domain_data.get("keywords", {})
    thresholds = domain_data.get("scoring_thresholds", {})

    total_score = 0
    matched_skills = []

    for keyword, attributes in keywords_dict.items():
        if keyword.lower() in resume_text:
            weight = attributes.get("weight", 0)
            total_score += weight
            matched_skills.append({
                "keyword": keyword,
                "weight": weight,
                "category": attributes.get("category", "general")
            })

    candidate_tier = "Needs Improvement" 
    
    for tier, range_values in thresholds.items():
        if range_values.get("min", 0) <= total_score <= range_values.get("max", 100):
            candidate_tier = tier.capitalize()
            break
            
    if total_score > thresholds.get("expert", {}).get("max", 100):
        candidate_tier = "Expert+"

    return {
        "domain_analyzed": domain_data.get("domain", "Unknown"),
        "total_score": total_score,
        "tier": candidate_tier,
        "matched_count": len(matched_skills),
        "matched_skills": matched_skills
    }