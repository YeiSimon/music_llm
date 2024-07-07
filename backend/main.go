package main

import (
    "context"
    "log"
    "time"

    "backend/controllers"
    "backend/dal"
    "backend/routers"
    "backend/services"

    "go.mongodb.org/mongo-driver/mongo"
    "go.mongodb.org/mongo-driver/mongo/options"
)

func main() {
    // Set up MongoDB connection
    ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
    defer cancel()
    clientOptions := options.Client().ApplyURI("mongodb://yehsimon:superstrongpsw@localhost:27017")
    client, err := mongo.Connect(ctx, clientOptions)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Disconnect(ctx)

    // Initialize DALs
    userDAL := dal.NewUserDAL(client, "your_db_name", "Users")
    conversationDAL := dal.NewConversationDAL(client, "your_db_name", "Conversations")
    messageDAL := dal.NewMessageDAL(client, "your_db_name", "Messages")

    // Initialize Services
    userService := services.NewUserService(userDAL)
    conversationService := services.NewConversationService(conversationDAL)
    messageService := services.NewMessageService(messageDAL)

    // Initialize Controllers
    userController := controllers.NewUserController(userService)
    conversationController := controllers.NewConversationController(conversationService)
    messageController := controllers.NewMessageController(messageService)

    // Set up Router
    r := routers.SetupRouter(userController, conversationController, messageController)
    
    r.Run() // listen and serve on 0.0.0.0:8080
}
