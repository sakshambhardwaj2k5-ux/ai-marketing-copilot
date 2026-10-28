from pydantic import BaseModel, Field, field_validator
class CampaignRequest(BaseModel):
    product: str = Field(min_length=1)
    audience: str
    goal: str 
    platform: str
    tone: str 
    product_description: str

class CampaignContent(BaseModel):
    campaign_name: str
    key_marketing_message: str
    primary_ad_copy: str
    social_posts: list[str] = Field(min_length=3, max_length=3)
    primary_cta: str
    influencer_brief: str
    hashtags: list[str] = Field(min_length=5, max_length=5)
    assumptions: list[str] = Field(default_factory=list)

    @field_validator("hashtags")
    @classmethod
    def hashtags_must_start_with_hash(cls, hashtags):
        if any(not tag.startswith("#") for tag in hashtags):
            raise ValueError("Every hashtag must start with '#'")
        return hashtags