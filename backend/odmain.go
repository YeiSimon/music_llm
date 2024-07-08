package main

import (
    "github.com/joho/godotenv"
    "context"
    "fmt"
    "os"
    "log"
    
    "github.com/tmc/langchaingo/llms"
    "github.com/tmc/langchaingo/llms/openai"
)

func main() {
    err := godotenv.Load("config/.env")
    if err != nil {
        log.Fatalf("Error loading .env file: %v", err)
    }
    groqApiKey := os.Getenv("GROQ_API_KEY")
    
    llm, err := openai.New(openai.WithModel("llama3-8b-8192"),
                openai.WithBaseURL("https://api.groq.com/openai/v1"),
                openai.WithToken(groqApiKey),
    )

    if err != nil {
        fmt.Printf("Error creating Groq client: %v\n", err)
        os.Exit(1)
    }

    ctx := context.Background()
    _, err = llms.GenerateFromSinglePrompt(ctx,
        llm,
        "Write a long poem about how golang is a fantastic language.",
        llms.WithTemperature(0.8),
        llms.WithMaxTokens(4096),
        llms.WithStreamingFunc(func(ctx context.Context, chunk []byte) error {
            fmt.Print(string(chunk))
            return nil
        }),
    )
    
    fmt.Println()
    if err != nil {
        log.Fatal(err)
    }
}


