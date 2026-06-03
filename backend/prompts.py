
caption_prompt = """
Analyze this image.

Generate four outputs.

1. Formal Caption
- Professional
- Objective
- 2-3 sentences

2. Casual Caption
- Friendly
- Conversational

3. SEO Caption
- 15-25 words
- Keyword rich

4. Alt Text
- WCAG compliant
- Under 125 characters

Return JSON format only:

{
  "formal":"",
  "casual":"",
  "seo":"",
  "alt_text":""
}
"""
