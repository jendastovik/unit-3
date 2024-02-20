import requests
import json

url = "https://stablediffusionapi.com/api/v3/text2img"

zip_code = "84044"

payload = json.dumps({
    "key": "X3vIyxxUUNT3Rs9fMhLmUb7MSO70GSjr8HqqwHlyQoJBDYSdOEGiZQvYFVEz",

    "prompt": f"generate image that symbolises region with the zip code {zip} hyperrealistic, full body, detailed clothing, highly detailed, cinematic lighting, stunningly beautiful, intricate, sharp focus, f\/1. 8, 85mm, (centered image composition), (professionally color graded), ((bright soft diffused light)), volumetric fog, trending on instagram, trending on tumblr, HDR 4K, 8K",
    "negative_prompt": " (child:1.5), ((((underage)))), ((((child)))), (((kid))), (((preteen))), (teen:1.5) ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs, disfigured, deformed, body out of frame, bad anatomy, watermark, signature, cut off, low contrast, underexposed, overexposed, bad art, beginner, amateur, distorted face, blurry, draft, grainy",
    "width": "512",
    "safety_checker": None,
    "guidance": "7.5",
    "instant_response": None,
    "height": "512",
    "samples": "1",
    "steps": 20,
    "temp": None,
    "seed": None,
    "webhook": None,
    "track_id": None
})

headers = {
  'Content-Type': 'application/json'
}

# response = requests.request("POST", url, headers=headers, data=payload)

response = {
  "status": "success",
  "generationTime": 1.3200268745422363,
  "id": 12202888,
  "output": [
    "https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/e5cd86d3-7305-47fc-82c1-7d1a3b130fa4-0.png"
  ],
  "meta": {
    "H": 512,
    "W": 512,
    "enable_attention_slicing": "true",
    "file_prefix": "e5cd86d3-7305-47fc-82c1-7d1a3b130fa4",
    "guidance_scale": 7.5,
    "model": "runwayml/stable-diffusion-v1-5",
    "n_samples": 1,
    "negative_prompt": " ((out of frame)), ((extra fingers)), mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), (((tiling))), ((naked)), ((tile)), ((fleshpile)), ((ugly)), (((abstract))), blurry, ((bad anatomy)), ((bad proportions)), ((extra limbs)), cloned face, glitchy, ((extra breasts)), ((double torso)), ((extra arms)), ((extra hands)), ((mangled fingers)), ((missing breasts)), (missing lips), ((ugly face)), ((fat)), ((extra legs))",
    "outdir": "out",
    "prompt": "ultra realistic close up portrait ((beautiful pale cyberpunk female with heavy black eyeliner)) DSLR photography, sharp focus, Unreal Engine 5, Octane Render, Redshift, ((cinematic lighting)), f/1.4, ISO 200, 1/160s, 8K, RAW, unedited, symmetrical balance, in-frame",
    "revision": "fp16",
    "safetychecker": "no",
    "seed": 3499575229,
    "steps": 20,
    "vae": "stabilityai/sd-vae-ft-mse"
  }
}

print(response["output"][0])
# print(response.text)