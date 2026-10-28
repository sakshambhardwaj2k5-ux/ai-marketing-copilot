from schemas import CampaignContent
campaign = CampaignContent(
    campaign_name="Fuel Your Foundation",
    key_marketing_message="Make plant-based protein part of your routine.",
    primary_ad_copy="Discover a plant-based option for your fitness journey.",
    social_posts=["Post one", "Post two", "Post three"],
    primary_cta="Learn more",
    influencer_brief="Introduce the product to your fitness audience.",
    hashtags=[
        "#Fitness",
        "#PlantBased",
        "#Nutrition",
        "#Training",
        "#FitnessJourney"
    ]
)
print(campaign)
print(campaign.model_dump_json(indent=4))