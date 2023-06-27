import openai
import sys
import os
import json
import concurrent.futures

openai.api_key = '<OPENAI-KEY>'

def generate_response(obj, field):
    # Prepare the full prompt for each field
    full_prompt = f"if field 'description' paraphrase. If field 'name' paraphrase and simplify: '{obj[field]}'"

    # Generate text using the GPT-3 API
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=full_prompt,
        max_tokens=100
    )

    # Return the updated text
    return field, response.choices[0].text.strip()

def chat_gpt(input_file, output_file):
    # Read and load JSON from the input file
    with open(input_file, 'r') as file:
        data = json.load(file)

    # Create a ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Iterate over each object in the JSON array
        for obj in data:
            futures = {executor.submit(generate_response, obj, field): (obj, field) for field in ['description', 'name']}
            
            for future in concurrent.futures.as_completed(futures):
                obj, field = futures[future]
                try:
                    field, text = future.result()
                except Exception as exc:
                    print(f"Generated an exception: {exc}")
                else:
                    # Update the field with the paraphrased and simplified text
                    obj[field] = text
                    print(f"Updated field '{field}' with: {text}")

    # Write the updated JSON array to the output file
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)  # Indentation set to 4 spaces

    print(f"{output_file} file successfully generated")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("--> Usage: python3 script.py '<input-filename>' '<output-filename>'")
        print("==> Output: output file with the updated JSON data")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    chat_gpt(input_filename, output_filename)
