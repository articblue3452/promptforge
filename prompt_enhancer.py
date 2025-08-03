import subprocess

def enhance_prompt(user_prompt):
    # Instruction prompt
    system_prompt = f"""
You are a prompt enhancer.
Rewrite the following into ONE vivid, emotionally rich, cinematic sentence.
Add sensory details, mood, and energy — no list, no bullets. Only one enhanced line.

Prompt: "{user_prompt}"
"""

    # Run ollama with llama3
    try:
        result = subprocess.run(
            ["ollama", "run", "llama3"],
            input=system_prompt.encode(),
            capture_output=True,
            timeout=60
        )

        response = result.stdout.decode().strip()
        error = result.stderr.decode().strip()

        if error:
            print("⚠️ Error:", error)

        # Filter meaningful output
        lines = response.splitlines()
        enhanced = ""
        for line in lines:
            line = line.strip()
            if line and not line.lower().startswith("prompt:"):
                enhanced = line
                break

        return enhanced

    except subprocess.TimeoutExpired:
        return "❌ Timed out. Try again."

if __name__ == "__main__":
    user_prompt = input("Enter base prompt: ")
    enhanced = enhance_prompt(user_prompt)
    print("\n💡 Enhanced Prompt:\n", enhanced if enhanced else "❌ No response received.")
