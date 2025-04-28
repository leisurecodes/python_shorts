import requests
import json
import sys

def get_meaning(word, url):
    url = f"{url}/api/v2/entries/en/{word}"

    try:
        # api request with timeout
        response = requests.get(url, timeout=10)

        # check success of response
        if response.status_code == 200:
            data = response.json()
            meanings = data[0]['meanings']

            print(f"\nDefinition for '{word}': \n")
            for meaning in meanings:
                part_of_speech = meaning['partOfSpeech']
                definitions = meaning['definitions']
                print(f"Part of Speech: {part_of_speech}")

                for i, definition in \
                enumerate(definitions, 1):
                    print(
                        f"    {i}. {definition['definition']}"
                    )

                    # display example
                    if 'example' in definition \
                    and definition['example']:
                        print(
                            f"    Example: " \
                            f"\"{definition['example']}\""
                        )
                    
                    # display synonym
                    if 'synonyms' in definition \
                    and definition['synonyms']:
                        synonyms = ', '.join(definition[
                            'synonyms'
                        ][:3])
                        if synonyms:
                            print(
                                f"    Synonyms: {synonyms}"
                            )
                print()
            return True
            
        elif response.status_code == 404:
            print(f"\nWord '{word}' not found. " \
                  "Please check spelling.")
            return False
        else:
            print(f"\nAPI Error: Status code " \
                  f"{response.status_code}")
            return False
    
    except requests.exceptions.Timeout:
        print("\nRequest time out. " \
              "Please check internet connection.")
        return False
    
    except requests.exceptions.ConnectionError:
        print("\nConnection failed: " \
              "Please check internet connection.")
        return False
    
    except json.JSONDecodeError:
        print("\nError parsing API response.")
        return False
    
    except KeyError as e:
        print(f"\nUnexpected API response error: {e}")
        return False

    except Exception as e:
        print(f"\nUnexpected error : {e}")
        return False

def main():
    try:
        url = "https://api.dictionaryapi.dev"
        if len(sys.argv) > 1:
            word = sys.argv[1].strip().lower()
        else:
            word = input(
                "Enter a word to search: "
            ).strip().lower()

        # input validation
        if not word:
            print("Enter a valid word. ")
            return
        
        if not word.isalpha():
            print("Enter valid word letters only.")
            return
        
        get_meaning(word, url)
    except KeyboardInterrupt:
        print("\nOperation stopped by user.")
    except Exception as e:
        print(f"\nUnexpected error occurred: {e}")

if __name__ == "__main__":
    main()