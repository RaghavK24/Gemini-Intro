
definitions= [
    {
        "name": "final_answer",
        "description": "Responds to the user with the final result of the task or question",
        "parameters": {
            "type": "object",
            "properties": {
                "message": {
                    "type": "string",
                    "description": "The response message"
                }
            },
            "required": ["message"]
        }
    },
    {
        "name": "send_message_linkedin",
        "description": "User wants to send a message to someone through LinkedIn.",
        "parameters": {
            "type": "object",
            "properties": {
                "To": {
                    "type": "string",
                    "description": "The person or people that the user wants to send a message to."
                },
                "body": {
                    "type": "string",
                    "description": "The contents of the message that the user wants to send on LinkedIn."
                }
            }
        }
    },
    {
        "name": "post_linkedin",
        "description": "User wants to post something to their social media account on LinkedIn. Please make sure that you have all the parameters before you proceed",
        "parameters": {
            "type": "object",
            "properties": {
                "body": {
                    "type": "string",
                    "description": "The contents of the post that the user wants to put on LinkedIn."
                }
            }
        }
    },
    {
        "name": "send_message_facebook",
        "description": "User wants to send a message to someone through Facebook.",
        "parameters": {
            "type": "object",
            "properties": {
                "to": {
                    "type": "string",
                    "description": "The person or people that the user wants to send a message to."
                },
                "body": {
                    "type": "string",
                    "description": "The contents of the message that the user wants to send on Facebook."
                }
            }
        }
    },
    {
        "name": "post_facebook",
        "description": "User wants to post something to their social media account on Facebook.",
        "parameters": {
            "type": "object",
            "properties": {
                "body": {
                    "type": "string",
                    "description": "The contents of the post that the user wants to put on Facebook."
                }
            }
        }
    },
    {
        "name": "send_email_outlook",
        "description": "User wants to send an email over their Outlook account to someone or multiple people.",
        "parameters": {
            "type": "object",
            "properties": {
                "to": {
                    "type": "string",
                    "description": "The email address to send the email to or list of email addresses to send to."
                },
                "subject": {
                    "type": "string",
                    "description": "The subject of the email."
                },
                "body": {
                    "type": "string",
                    "description": "The actual message of the email that the user wants to send."
                }
            }
        }
    },
    {
        "name": "send_email_gmail",
        "description": "User wants to send an email over their Gmail account to someone or multiple people. Please make sure that you have all the parameters before you proceed",
        "parameters": {
            "type": "object",
            "properties": {
                "to": {
                    "type": "string",
                    "description": "The email address to send the email to or list of email addresses to send to."
                },
                "subject": {
                    "type": "string",
                    "description": "The subject of the email."
                },
                "body": {
                    "type": "string",
                    "description": "The actual message of the email that the user wants to send."
                }
            }
        }
    },
    # {
    #     "name": "generate_random_password",
    #     "description": "Generates a random password with specified length and complexity.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "length": {
    #                 "type": "integer",
    #                 "description": "The length of the password to be generated."
    #             },
    #             "complexity": {
    #                 "type": "string",
    #                 "enum": ["low", "medium", "high"],
    #                 "description": "The complexity level of the password (low, medium, high)."
    #             }
    #         },
    #         "required": ["length", "complexity"]
    #     }
    # },
    # {
    #     "name": "fetch_weather_forecast",
    #     "description": "Fetches the weather forecast for a specific location.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "location": {
    #                 "type": "string",
    #                 "description": "The location for which the weather forecast is requested."
    #             }
    #         },
    #         "required": ["location"]
    #     }
    # },
    # {
    #     "name": "calculate_fibonacci_sequence",
    #     "description": "Calculates the Fibonacci sequence up to a specified number of terms.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "terms": {
    #                 "type": "integer",
    #                 "description": "The number of terms in the Fibonacci sequence to be calculated."
    #             }
    #         },
    #         "required": ["terms"]
    #     }
    # },
    # {
    #     "name": "search_wikipedia",
    #     "description": "Searches Wikipedia for information on a given topic.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "topic": {
    #                 "type": "string",
    #                 "description": "The topic to search for on Wikipedia."
    #             }
    #         },
    #         "required": ["topic"]
    #     }
    # },
    # {
    #     "name": "analyze_sentiment",
    #     "description": "Analyzes the sentiment of a given text.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "text": {
    #                 "type": "string",
    #                 "description": "The text whose sentiment needs to be analyzed."
    #             }
    #         },
    #         "required": ["text"]
    #     }
    # },
    # {
    #     "name": "calculate_distance",
    #     "description": "Calculates the distance between two geographical coordinates.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "latitude1": {
    #                 "type": "number",
    #                 "description": "The latitude of the first location."
    #             },
    #             "longitude1": {
    #                 "type": "number",
    #                 "description": "The longitude of the first location."
    #             },
    #             "latitude2": {
    #                 "type": "number",
    #                 "description": "The latitude of the second location."
    #             },
    #             "longitude2": {
    #                 "type": "number",
    #                 "description": "The longitude of the second location."
    #             }
    #         },
    #         "required": ["latitude1", "longitude1", "latitude2", "longitude2"]
    #     }
    # },
    # {
    #     "name": "translate_text",
    #     "description": "Translates text from one language to another.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "text": {
    #                 "type": "string",
    #                 "description": "The text to be translated."
    #             },
    #             "source_language": {
    #                 "type": "string",
    #                 "description": "The source language of the text."
    #             },
    #             "target_language": {
    #                 "type": "string",
    #                 "description": "The target language for the translation."
    #             }
    #         },
    #         "required": ["text", "source_language", "target_language"]
    #     }
    # },
    # {
    #     "name": "analyze_image",
    #     "description": "Analyzes the content of an image and returns relevant information.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "image_url": {
    #                 "type": "string",
    #                 "description": "The URL of the image to be analyzed."
    #             }
    #         },
    #         "required": ["image_url"]
    #     }
    # },
    # {
    #     "name": "search_images",
    #     "description": "Searches for images based on the user's query.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "query": {
    #                 "type": "string",
    #                 "description": "The search query for images."
    #             },
    #             "max_results": {
    #                 "type": "integer",
    #                 "description": "Maximum number of results to return."
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "calculate_distance",
    #     "description": "Calculates the distance between two geographical points.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "latitude1": {
    #                 "type": "number",
    #                 "description": "Latitude of the first point."
    #             },
    #             "longitude1": {
    #                 "type": "number",
    #                 "description": "Longitude of the first point."
    #             },
    #             "latitude2": {
    #                 "type": "number",
    #                 "description": "Latitude of the second point."
    #             },
    #             "longitude2": {
    #                 "type": "number",
    #                 "description": "Longitude of the second point."
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "generate_invoice",
    #     "description": "Generates an invoice for a customer's purchase.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "customer_name": {
    #                 "type": "string",
    #                 "description": "Name of the customer."
    #             },
    #             "items": {
    #                 "type": "array",
    #                 "items": {
    #                     "type": "object",
    #                     "properties": {
    #                         "product": {
    #                             "type": "string",
    #                             "description": "Name of the product."
    #                         },
    #                         "quantity": {
    #                             "type": "integer",
    #                             "description": "Quantity of the product."
    #                         },
    #                         "price": {
    #                             "type": "number",
    #                             "description": "Price per unit of the product."
    #                         }
    #                     }
    #                 }
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "analyze_sentiment",
    #     "description": "Analyzes the sentiment of a piece of text.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "text": {
    #                 "type": "string",
    #                 "description": "The text to analyze sentiment."
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "convert_currency",
    #     "description": "Converts the amount from one currency to another.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "amount": {
    #                 "type": "number",
    #                 "description": "The amount to convert."
    #             },
    #             "from_currency": {
    #                 "type": "string",
    #                 "description": "The currency to convert from."
    #             },
    #             "to_currency": {
    #                 "type": "string",
    #                 "description": "The currency to convert to."
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "generate_password",
    #     "description": "Generates a random password of specified length.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "length": {
    #                 "type": "integer",
    #                 "description": "Length of the password to generate."
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "create_todo",
    #     "description": "Creates a new item in the user's todo list.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "task": {
    #                 "type": "string",
    #                 "description": "The task to add to the todo list."
    #             },
    #             "due_date": {
    #                 "type": "string",
    #                 "description": "The due date of the task."
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "analyze_image",
    #     "description": "Analyzes the content of an image using computer vision techniques.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "image_url": {
    #                 "type": "string",
    #                 "description": "URL of the image to analyze."
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "generate_report",
    #     "description": "Generates a report based on the provided data.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "data": {
    #                 "type": "array",
    #                 "items": {
    #                     "type": "object",
    #                     "description": "Data to include in the report."
    #                 }
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "update_profile",
    #     "description": "Updates the user's profile with the provided information.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "name": {
    #                 "type": "string",
    #                 "description": "The user's name."
    #             },
    #             "email": {
    #                 "type": "string",
    #                 "description": "The user's email address."
    #             },
    #             "bio": {
    #                 "type": "string",
    #                 "description": "A short biography of the user."
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "fetch_weather",
    #     "description": "Fetches the current weather information for a specified location.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "location": {
    #                 "type": "string",
    #                 "description": "The location for which weather information is requested."
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "analyze_audio",
    #     "description": "Analyzes audio content for various attributes such as speech recognition, emotion detection, etc.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "audio_url": {
    #                 "type": "string",
    #                 "description": "URL of the audio content to analyze."
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "translate_text",
    #     "description": "Translates text from one language to another.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "text": {
    #                 "type": "string",
    #                 "description": "The text to translate."
    #             },
    #             "source_language": {
    #                 "type": "string",
    #                 "description": "The language of the source text."
    #             },
    #             "target_language": {
    #                 "type": "string",
    #                 "description": "The language to which the text should be translated."
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "generate_recommendations",
    #     "description": "Generates personalized recommendations for products, services, or content.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "user_id": {
    #                 "type": "string",
    #                 "description": "Identifier of the user for whom recommendations are being generated."
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "schedule_meeting",
    #     "description": "Schedules a meeting or appointment on the user's calendar.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "title": {
    #                 "type": "string",
    #                 "description": "Title or subject of the meeting."
    #             },
    #             "start_time": {
    #                 "type": "string",
    #                 "description": "Start time of the meeting."
    #             },
    #             "end_time": {
    #                 "type": "string",
    #                 "description": "End time of the meeting."
    #             },
    #             "attendees": {
    #                 "type": "array",
    #                 "items": {
    #                     "type": "string",
    #                     "description": "Email addresses of the meeting attendees."
    #                 }
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "analyze_code",
    #     "description": "Analyzes code for syntax errors, code quality issues, and security vulnerabilities.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "code_snippet": {
    #                 "type": "string",
    #                 "description": "The code snippet to analyze."
    #             },
    #             "language": {
    #                 "type": "string",
    #                 "description": "The programming language of the code snippet."
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "generate_quiz",
    #     "description": "Generates a quiz with random questions based on specified criteria.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "topic": {
    #                 "type": "string",
    #                 "description": "The topic of the quiz."
    #             },
    #             "difficulty_level": {
    #                 "type": "string",
    #                 "description": "The difficulty level of the questions."
    #             },
    #             "num_questions": {
    #                 "type": "integer",
    #                 "description": "The number of questions in the quiz."
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "analyze_network_traffic",
    #     "description": "Analyzes network traffic for anomalies, security threats, and performance issues.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "traffic_data": {
    #                 "type": "string",
    #                 "description": "Raw data or logs of network traffic to analyze."
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "recommend_music",
    #     "description": "Recommends music tracks or playlists based on user preferences and listening history.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "user_id": {
    #                 "type": "string",
    #                 "description": "Identifier of the user for whom music recommendations are being generated."
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "analyze_health_data",
    #     "description": "Analyzes health data such as heart rate, activity level, and sleep patterns.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "data": {
    #                 "type": "array",
    #                 "items": {
    #                     "type": "object",
    #                     "description": "Health data records."
    #                 }
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "analyze_customer_feedback",
    #     "description": "Analyzes customer feedback to extract insights and identify areas for improvement.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "feedback_text": {
    #                 "type": "string",
    #                 "description": "The text of the customer feedback."
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "generate_poetry",
    #     "description": "Generates poetry based on specified themes or prompts.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "theme": {
    #                 "type": "string",
    #                 "description": "The theme or topic for the poetry generation."
    #             },
    #             "num_lines": {
    #                 "type": "integer",
    #                 "description": "The number of lines in the poem."
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "detect_object",
    #     "description": "Detects objects and their attributes in images or videos.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "image_url": {
    #                 "type": "string",
    #                 "description": "URL of the image containing the object to detect."
    #             },
    #             "object_type": {
    #                 "type": "string",
    #                 "description": "Type of object to detect (e.g., person, car, cat)."
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "generate_meme",
    #     "description": "Generates memes by combining images and text in a humorous way.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "image_url": {
    #                 "type": "string",
    #                 "description": "URL of the base image for the meme."
    #             },
    #             "text": {
    #                 "type": "string",
    #                 "description": "Text to overlay on the image."
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "analyze_financial_data",
    #     "description": "Analyzes financial data to identify trends, anomalies, and investment opportunities.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "data": {
    #                 "type": "array",
    #                 "items": {
    #                     "type": "object",
    #                     "description": "Financial data records."
    #                 }
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "recommend_books",
    #     "description": "Recommends books based on user preferences, reading history, and genre preferences.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "user_id": {
    #                 "type": "string",
    #                 "description": "Identifier of the user for whom book recommendations are being generated."
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "generate_sudoku",
    #     "description": "Generates Sudoku puzzles with varying levels of difficulty.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "difficulty_level": {
    #                 "type": "string",
    #                 "description": "The difficulty level of the Sudoku puzzle (easy, medium, hard)."
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "analyze_employee_performance",
    #     "description": "Analyzes employee performance metrics to evaluate productivity and identify areas for improvement.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "performance_data": {
    #                 "type": "array",
    #                 "items": {
    #                     "type": "object",
    #                     "description": "Employee performance records."
    #                 }
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "generate_quote",
    #     "description": "Generates motivational or inspirational quotes to uplift users.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "category": {
    #                 "type": "string",
    #                 "description": "The category or theme of the quote (e.g., success, happiness)."
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "analyze_social_media_sentiment",
    #     "description": "Analyzes sentiment and trends on social media platforms to understand public opinion.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "platform": {
    #                 "type": "string",
    #                 "description": "The social media platform to analyze (e.g., Twitter, Facebook)."
    #             },
    #             "query": {
    #                 "type": "string",
    #                 "description": "The search query or topic to analyze."
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "generate_recipe",
    #     "description": "Generates recipes based on specified ingredients or dietary preferences.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "ingredients": {
    #                 "type": "array",
    #                 "items": {
    #                     "type": "string",
    #                     "description": "List of ingredients available."
    #                 }
    #             },
    #             "dietary_preferences": {
    #                 "type": "array",
    #                 "items": {
    #                     "type": "string",
    #                     "description": "Dietary preferences or restrictions (e.g., vegetarian, gluten-free)."
    #                 }
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "analyze_customer_demographics",
    #     "description": "Analyzes customer demographics to identify target markets and tailor marketing strategies.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "demographic_data": {
    #                 "type": "array",
    #                 "items": {
    #                     "type": "object",
    #                     "description": "Customer demographic information."
    #                 }
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "generate_horoscope",
    #     "description": "Generates horoscope predictions based on astrological signs.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "sign": {
    #                 "type": "string",
    #                 "description": "The astrological sign for which to generate the horoscope."
    #             },
    #             "date": {
    #                 "type": "string",
    #                 "description": "The date for which to generate the horoscope (optional)."
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "analyze_market_trends",
    #     "description": "Analyzes market trends and economic indicators to forecast future trends and make investment decisions.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "market_data": {
    #                 "type": "array",
    #                 "items": {
    #                     "type": "object",
    #                     "description": "Market data records."
    #                 }
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "generate_presentation",
    #     "description": "Generates presentations or slideshows based on specified content and templates.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "content": {
    #                 "type": "array",
    #                 "items": {
    #                     "type": "string",
    #                     "description": "Content to include in the presentation."
    #                 }
    #             },
    #             "template": {
    #                 "type": "string",
    #                 "description": "The template or theme for the presentation."
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "analyze_website_traffic",
    #     "description": "Analyzes website traffic data to assess user engagement, performance, and identify areas for improvement.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "traffic_data": {
    #                 "type": "array",
    #                 "items": {
    #                     "type": "object",
    #                     "description": "Website traffic data records."
    #                 }
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "generate_movie_recommendations",
    #     "description": "Generates movie recommendations based on user preferences, genre, and ratings.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "user_id": {
    #                 "type": "string",
    #                 "description": "Identifier of the user for whom movie recommendations are being generated."
    #             },
    #             "genre": {
    #                 "type": "string",
    #                 "description": "Preferred movie genre."
    #             }
    #         }
    #     }
    # },
    # {
    #     "name": "analyze_environmental_data",
    #     "description": "Analyzes environmental data such as air quality, temperature, and pollution levels.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "data": {
    #                 "type": "array",
    #                 "items": {
    #                     "type": "object",
    #                     "description": "Environmental data records."
    #                 }
    #             }
    #         }
    #     }
    # }
]